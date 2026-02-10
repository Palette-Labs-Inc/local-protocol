<?php

declare(strict_types=1);

namespace LocalProtocol\Merchants\Availability;

use LocalProtocol\Core\Attributes\Optional;
use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * A single time interval for a day of the week or a specific date.
 *
 * @phpstan-type IntervalShape = array{
 *   fromHour: int,
 *   fromMinute: int,
 *   toHour: int,
 *   toMinute: int,
 *   date?: string|null,
 *   day?: string|null,
 * }
 */
final class Interval implements BaseModel
{
    /** @use SdkModel<IntervalShape> */
    use SdkModel;

    /**
     * Start hour (0-23).
     */
    #[Required('from_hour')]
    public int $fromHour;

    /**
     * Start minute (0-59).
     */
    #[Required('from_minute')]
    public int $fromMinute;

    /**
     * End hour (0-23).
     */
    #[Required('to_hour')]
    public int $toHour;

    /**
     * End minute (0-59).
     */
    #[Required('to_minute')]
    public int $toMinute;

    /**
     * Calendar date in YYYY-MM-DD.
     */
    #[Optional]
    public ?string $date;

    /**
     * Day of week (e.g., Monday, Tuesday).
     */
    #[Optional]
    public ?string $day;

    /**
     * `new Interval()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * Interval::with(fromHour: ..., fromMinute: ..., toHour: ..., toMinute: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new Interval)
     *   ->withFromHour(...)
     *   ->withFromMinute(...)
     *   ->withToHour(...)
     *   ->withToMinute(...)
     * ```
     */
    public function __construct()
    {
        $this->initialize();
    }

    /**
     * Construct an instance from the required parameters.
     *
     * You must use named parameters to construct any parameters with a default value.
     */
    public static function with(
        int $fromHour,
        int $fromMinute,
        int $toHour,
        int $toMinute,
        ?string $date = null,
        ?string $day = null,
    ): self {
        $self = new self;

        $self['fromHour'] = $fromHour;
        $self['fromMinute'] = $fromMinute;
        $self['toHour'] = $toHour;
        $self['toMinute'] = $toMinute;

        null !== $date && $self['date'] = $date;
        null !== $day && $self['day'] = $day;

        return $self;
    }

    /**
     * Start hour (0-23).
     */
    public function withFromHour(int $fromHour): self
    {
        $self = clone $this;
        $self['fromHour'] = $fromHour;

        return $self;
    }

    /**
     * Start minute (0-59).
     */
    public function withFromMinute(int $fromMinute): self
    {
        $self = clone $this;
        $self['fromMinute'] = $fromMinute;

        return $self;
    }

    /**
     * End hour (0-23).
     */
    public function withToHour(int $toHour): self
    {
        $self = clone $this;
        $self['toHour'] = $toHour;

        return $self;
    }

    /**
     * End minute (0-59).
     */
    public function withToMinute(int $toMinute): self
    {
        $self = clone $this;
        $self['toMinute'] = $toMinute;

        return $self;
    }

    /**
     * Calendar date in YYYY-MM-DD.
     */
    public function withDate(string $date): self
    {
        $self = clone $this;
        $self['date'] = $date;

        return $self;
    }

    /**
     * Day of week (e.g., Monday, Tuesday).
     */
    public function withDay(string $day): self
    {
        $self = clone $this;
        $self['day'] = $day;

        return $self;
    }
}
