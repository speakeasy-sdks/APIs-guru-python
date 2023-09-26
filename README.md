# openapi

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/APIs-guru-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import openapi
from openapi.models import operations

s = openapi.Openapi()

req = operations.GetAPIRequest(
    api='2.1.0',
    provider='apis.guru',
)

res = s.ap_is.get_api(req)

if res.api is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [APIs](docs/sdks/apis/README.md)

* [get_api](docs/sdks/apis/README.md#get_api) - Retrieve one version of a particular API
* [get_metrics](docs/sdks/apis/README.md#get_metrics) - Get basic metrics
* [get_provider](docs/sdks/apis/README.md#get_provider) - List all APIs for a particular provider
* [get_providers](docs/sdks/apis/README.md#get_providers) - List all providers
* [get_service_api](docs/sdks/apis/README.md#get_service_api) - Retrieve one version of a particular API with a serviceName.
* [get_services](docs/sdks/apis/README.md#get_services) - List all serviceNames for a particular provider
* [list_ap_is](docs/sdks/apis/README.md#list_ap_is) - List all APIs
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->



<!-- End Dev Containers -->



<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:


<!-- End Pagination -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
