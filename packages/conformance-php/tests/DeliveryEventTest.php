<?php

declare(strict_types=1);

namespace Tests;

class DeliveryEventTest extends IntegrationTestBase
{
    public function testDeliveryHasEventFields(): void
    {
        $delivery = $this->createDelivery();
        $this->assertNotEmpty($delivery->event);
        $this->assertNotEmpty($delivery->eventDescription);
        $this->assertNotEmpty($delivery->eventVocabulary);
        $this->assertNotNull($delivery['createdAt']);
        $this->assertNotNull($delivery['updatedAt']);
    }

    public function testDeliveryHasRequestAndQuoteIds(): void
    {
        $delivery = $this->createDelivery();
        $this->assertNotEmpty($delivery->requestID);
        $this->assertNotEmpty($delivery->quoteID);
    }

    public function testInitialEventIsCreated(): void
    {
        $delivery = $this->createDelivery();
        $this->assertSame('created', $delivery->event);
    }

    public function testEventVocabularyIncludesVersion(): void
    {
        $delivery = $this->createDelivery();
        $this->assertStringContainsString('@', $delivery->eventVocabulary);
    }

    public function testEventVocabularyVersionIsDateFormat(): void
    {
        $delivery = $this->createDelivery();
        $parts = explode('@', $delivery->eventVocabulary);
        $this->assertCount(2, $parts);
        $this->assertMatchesRegularExpression('/^\d{4}-\d{2}-\d{2}$/', $parts[1]);
    }

    public function testEventCanTransitionToAssigned(): void
    {
        $delivery = $this->createDelivery();
        $updated = $this->sdk->deliveries->updateEvent(
            $delivery->id,
            'assigned',
            'Courier assigned',
        );
        $this->assertSame('assigned', $updated->event);
    }

    public function testEventCanTransitionToDelivered(): void
    {
        $delivery = $this->createDelivery();
        $updated = $this->sdk->deliveries->updateEvent(
            $delivery->id,
            'delivered',
            'Courier completed dropoff',
        );
        $this->assertSame('delivered', $updated->event);
    }

    public function testEventCanTransitionToCanceled(): void
    {
        $delivery = $this->createDelivery();
        $updated = $this->sdk->deliveries->updateEvent(
            $delivery->id,
            'canceled',
            'Delivery canceled',
        );
        $this->assertSame('canceled', $updated->event);
    }

    public function testFullCourierLifecycle(): void
    {
        $delivery = $this->createDelivery();

        $lifecycle = [
            ['assigned', 'Courier assigned'],
            ['enroute_pickup', 'Courier heading to pickup'],
            ['arrived_pickup', 'Courier at pickup location'],
            ['collected', 'Courier picked up'],
            ['arrived_dropoff', 'Courier at dropoff location'],
            ['delivered', 'Courier completed dropoff'],
        ];

        foreach ($lifecycle as [$event, $description]) {
            $updated = $this->sdk->deliveries->updateEvent(
                $delivery->id,
                $event,
                $description,
            );
            $this->assertSame($event, $updated->event, "Failed to transition to {$event}");
        }

        // Verify final state
        $final = $this->sdk->deliveries->retrieve($delivery->id);
        $this->assertSame('delivered', $final->event);
    }
}
