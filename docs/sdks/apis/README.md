# APIs
(*ap_is*)

## Overview

Actions relating to APIs in the collection

### Available Operations

* [get_api](#get_api) - Retrieve one version of a particular API
* [get_metrics](#get_metrics) - Get basic metrics
* [get_provider](#get_provider) - List all APIs for a particular provider
* [get_providers](#get_providers) - List all providers
* [get_service_api](#get_service_api) - Retrieve one version of a particular API with a serviceName.
* [get_services](#get_services) - List all serviceNames for a particular provider
* [list_ap_is](#list_ap_is) - List all APIs

## get_api

Returns the API entry for one specific version of an API where there is no serviceName.

### Example Usage

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

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [operations.GetAPIRequest](../../models/operations/getapirequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.GetAPIResponse](../../models/operations/getapiresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_metrics

Some basic metrics for the entire directory.
Just stunning numbers to put on a front page and are intended purely for WoW effect :)


### Example Usage

```python
import openapi

s = openapi.Openapi()


res = s.ap_is.get_metrics()

if res.metrics is not None:
    # handle response
    pass
```


### Response

**[operations.GetMetricsResponse](../../models/operations/getmetricsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_provider

List all APIs in the directory for a particular providerName
Returns links to the individual API entry for each API.


### Example Usage

```python
import openapi
from openapi.models import operations

s = openapi.Openapi()

req = operations.GetProviderRequest(
    provider='apis.guru',
)

res = s.ap_is.get_provider(req)

if res.ap_is is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetProviderRequest](../../models/operations/getproviderrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetProviderResponse](../../models/operations/getproviderresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_providers

List all the providers in the directory


### Example Usage

```python
import openapi

s = openapi.Openapi()


res = s.ap_is.get_providers()

if res.object is not None:
    # handle response
    pass
```


### Response

**[operations.GetProvidersResponse](../../models/operations/getprovidersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_service_api

Returns the API entry for one specific version of an API where there is a serviceName.

### Example Usage

```python
import openapi
from openapi.models import operations

s = openapi.Openapi()

req = operations.GetServiceAPIRequest(
    api='2.1.0',
    provider='apis.guru',
    service='graph',
)

res = s.ap_is.get_service_api(req)

if res.api is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetServiceAPIRequest](../../models/operations/getserviceapirequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetServiceAPIResponse](../../models/operations/getserviceapiresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_services

List all serviceNames in the directory for a particular providerName


### Example Usage

```python
import openapi
from openapi.models import operations

s = openapi.Openapi()

req = operations.GetServicesRequest(
    provider='apis.guru',
)

res = s.ap_is.get_services(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetServicesRequest](../../models/operations/getservicesrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetServicesResponse](../../models/operations/getservicesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_ap_is

List all APIs in the directory.
Returns links to the OpenAPI definitions for each API in the directory.
If API exist in multiple versions `preferred` one is explicitly marked.
Some basic info from the OpenAPI definition is cached inside each object.
This allows you to generate some simple views without needing to fetch the OpenAPI definition for each API.


### Example Usage

```python
import openapi

s = openapi.Openapi()


res = s.ap_is.list_ap_is()

if res.ap_is is not None:
    # handle response
    pass
```


### Response

**[operations.ListAPIsResponse](../../models/operations/listapisresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
