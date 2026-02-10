<?php

declare(strict_types=1);

namespace LocalProtocol\EventVocabularies;

use LocalProtocol\Core\Attributes\Optional;
use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;
use LocalProtocol\EventVocabularies\EventVocabularyGetResponse\Event;

/**
 * Schema for delivery event vocabularies.
 *
 * @phpstan-import-type EventShape from \LocalProtocol\EventVocabularies\EventVocabularyGetResponse\Event
 *
 * @phpstan-type EventVocabularyGetResponseShape = array{
 *   events: array<string,Event|EventShape>,
 *   name: string,
 *   title: string,
 *   version: string,
 *   description?: string|null,
 *   extends?: list<string>|null,
 *   spec?: string|null,
 * }
 */
final class EventVocabularyGetResponse implements BaseModel
{
    /** @use SdkModel<EventVocabularyGetResponseShape> */
    use SdkModel;

    /**
     * Map of event IDs to event definitions.
     *
     * @var array<string,Event> $events
     */
    #[Required(map: Event::class)]
    public array $events;

    /**
     * Standard identifier in reverse-domain notation.
     */
    #[Required]
    public string $name;

    /**
     * Human-readable title.
     */
    #[Required]
    public string $title;

    /**
     * Version in YYYY-MM-DD format.
     */
    #[Required]
    public string $version;

    /**
     * Human-readable description.
     */
    #[Optional]
    public ?string $description;

    /**
     * Parent standard this extends (optional, max one).
     *
     * @var list<string>|null $extends
     */
    #[Optional(list: 'string')]
    public ?array $extends;

    /**
     * URL to specification document.
     */
    #[Optional]
    public ?string $spec;

    /**
     * `new EventVocabularyGetResponse()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * EventVocabularyGetResponse::with(
     *   events: ..., name: ..., title: ..., version: ...
     * )
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new EventVocabularyGetResponse)
     *   ->withEvents(...)
     *   ->withName(...)
     *   ->withTitle(...)
     *   ->withVersion(...)
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
     * @param array<string,Event|EventShape> $events
     * @param list<string>|null $extends
     */
    public static function with(
        array $events,
        string $name,
        string $title,
        string $version,
        ?string $description = null,
        ?array $extends = null,
        ?string $spec = null,
    ): self {
        $self = new self;

        $self['events'] = $events;
        $self['name'] = $name;
        $self['title'] = $title;
        $self['version'] = $version;

        null !== $description && $self['description'] = $description;
        null !== $extends && $self['extends'] = $extends;
        null !== $spec && $self['spec'] = $spec;

        return $self;
    }

    /**
     * Map of event IDs to event definitions.
     *
     * @param array<string,Event|EventShape> $events
     */
    public function withEvents(array $events): self
    {
        $self = clone $this;
        $self['events'] = $events;

        return $self;
    }

    /**
     * Standard identifier in reverse-domain notation.
     */
    public function withName(string $name): self
    {
        $self = clone $this;
        $self['name'] = $name;

        return $self;
    }

    /**
     * Human-readable title.
     */
    public function withTitle(string $title): self
    {
        $self = clone $this;
        $self['title'] = $title;

        return $self;
    }

    /**
     * Version in YYYY-MM-DD format.
     */
    public function withVersion(string $version): self
    {
        $self = clone $this;
        $self['version'] = $version;

        return $self;
    }

    /**
     * Human-readable description.
     */
    public function withDescription(string $description): self
    {
        $self = clone $this;
        $self['description'] = $description;

        return $self;
    }

    /**
     * Parent standard this extends (optional, max one).
     *
     * @param list<string> $extends
     */
    public function withExtends(array $extends): self
    {
        $self = clone $this;
        $self['extends'] = $extends;

        return $self;
    }

    /**
     * URL to specification document.
     */
    public function withSpec(string $spec): self
    {
        $self = clone $this;
        $self['spec'] = $spec;

        return $self;
    }
}
