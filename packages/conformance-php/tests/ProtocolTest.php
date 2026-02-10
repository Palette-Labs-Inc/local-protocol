<?php

declare(strict_types=1);

namespace Tests;

class ProtocolTest extends IntegrationTestBase
{
    // --- Discovery ---

    public function testWellKnownEndpointExists(): void
    {
        $data = $this->sdk->wellKnown->retrieve();
        $this->assertNotEmpty($data->version);
    }

    public function testHealthCheck(): void
    {
        $data = $this->sdk->healthz->check();
        $this->assertSame('ok', $data->status);
    }

    // --- Request Lifecycle ---

    public function testCreateRequestReturns201(): void
    {
        $req = $this->createRequest();
        $this->assertNotEmpty($req->id);
    }

    public function testGetRequestById(): void
    {
        $created = $this->createRequest();
        $fetched = $this->sdk->requests->retrieve($created->id);
        $this->assertSame($created->id, $fetched->id);
    }

    // --- Quote Lifecycle ---

    public function testCreateQuoteForRequest(): void
    {
        $req = $this->createRequest();
        $quote = $this->createQuote($req->id);
        $this->assertNotEmpty($quote->id);
    }

    public function testListQuotesForRequest(): void
    {
        $req = $this->createRequest();

        for ($i = 0; $i < 3; $i++) {
            $this->createQuote($req->id, price: 1000 + $i * 100);
        }

        $quotes = $this->sdk->requests->quotes->list($req->id);
        $this->assertGreaterThanOrEqual(3, count($quotes));
    }

    // --- Delivery Lifecycle ---

    public function testCreateDelivery(): void
    {
        $delivery = $this->createDelivery();
        $this->assertNotEmpty($delivery->id);
        $this->assertSame('created', $delivery->event);
    }

    public function testGetDeliveryById(): void
    {
        $delivery = $this->createDelivery();
        $fetched = $this->sdk->deliveries->retrieve($delivery->id);
        $this->assertSame($delivery->id, $fetched->id);
        $this->assertSame($delivery->event, $fetched->event);
    }

    public function testListDeliveries(): void
    {
        $delivery = $this->createDelivery();
        $deliveries = $this->sdk->deliveries->list();
        $ids = array_map(fn($d) => $d->id, $deliveries);
        $this->assertContains($delivery->id, $ids);
    }
}
