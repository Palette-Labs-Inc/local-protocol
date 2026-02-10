<?php

declare(strict_types=1);

namespace LocalProtocol\Merchants;

use LocalProtocol\Core\Attributes\Optional;
use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;
use LocalProtocol\Merchants\Availability\Interval;

/**
 * Availability schedule for a catalog, category, or item.
 *
 * @phpstan-import-type IntervalShape from \LocalProtocol\Merchants\Availability\Interval
 *
 * @phpstan-type AvailabilityShape = array{
 *   intervals: list<Interval|IntervalShape>, timezone?: string|null
 * }
 */
final class Availability implements BaseModel
{
    /** @use SdkModel<AvailabilityShape> */
    use SdkModel;

    /**
     * Availability intervals (weekly or date-specific).
     *
     * @var list<Interval> $intervals
     */
    #[Required(list: Interval::class)]
    public array $intervals;

    /**
     * IANA timezone. Defaults to merchant timezone when omitted.
     */
    #[Optional]
    public ?string $timezone;

    /**
     * `new Availability()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * Availability::with(intervals: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new Availability)->withIntervals(...)
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
     *
     * @param list<Interval|IntervalShape> $intervals
     */
    public static function with(array $intervals, ?string $timezone = null): self
    {
        $self = new self;

        $self['intervals'] = $intervals;

        null !== $timezone && $self['timezone'] = $timezone;

        return $self;
    }

    /**
     * Availability intervals (weekly or date-specific).
     *
     * @param list<Interval|IntervalShape> $intervals
     */
    public function withIntervals(array $intervals): self
    {
        $self = clone $this;
        $self['intervals'] = $intervals;

        return $self;
    }

    /**
     * IANA timezone. Defaults to merchant timezone when omitted.
     */
    public function withTimezone(string $timezone): self
    {
        $self = clone $this;
        $self['timezone'] = $timezone;

        return $self;
    }
}
