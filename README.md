# openapi

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/APIs-guru-python.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

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
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [ap_is](docs/sdks/apis/README.md)

* [get_api](docs/sdks/apis/README.md#get_api) - Retrieve one version of a particular API
* [get_metrics](docs/sdks/apis/README.md#get_metrics) - Get basic metrics
* [get_provider](docs/sdks/apis/README.md#get_provider) - List all APIs for a particular provider
* [get_providers](docs/sdks/apis/README.md#get_providers) - List all providers
* [get_service_api](docs/sdks/apis/README.md#get_service_api) - Retrieve one version of a particular API with a serviceName.
* [get_services](docs/sdks/apis/README.md#get_services) - List all serviceNames for a particular provider
* [list_ap_is](docs/sdks/apis/README.md#list_ap_is) - List all APIs
<!-- End Available Resources and Operations [operations] -->







<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

### Example

```python
import openapi
from openapi.models import errors, operations

s = openapi.Openapi()

req = operations.GetAPIRequest(
    api='2.1.0',
    provider='apis.guru',
)

res = None
try:
    res = s.ap_is.get_api(req)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.api is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->



<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.apis.guru/v2` | None |

#### Example

```python
import openapi
from openapi.models import operations

s = openapi.Openapi(
    server_idx=0,
)

req = operations.GetAPIRequest(
    api='2.1.0',
    provider='apis.guru',
)

res = s.ap_is.get_api(req)

if res.api is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import openapi
from openapi.models import operations

s = openapi.Openapi(
    server_url="https://api.apis.guru/v2",
)

req = operations.GetAPIRequest(
    api='2.1.0',
    provider='apis.guru',
)

res = s.ap_is.get_api(req)

if res.api is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->



<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import openapi
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = openapi.Openapi(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
