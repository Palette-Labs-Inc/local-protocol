<!-- Start SDK Example Usage [usage] -->
```php
declare(strict_types=1);

require 'vendor/autoload.php';

use LocalProtocol;

$sdk = LocalProtocol\LocalProtocol::builder()->build();



$response = $sdk->discovery->get(

);

if ($response->discoveryResponse !== null) {
    // handle response
}
```
<!-- End SDK Example Usage [usage] -->