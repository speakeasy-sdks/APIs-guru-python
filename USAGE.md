<!-- Start SDK Example Usage [usage] -->
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