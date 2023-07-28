"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from openapi import utils
from typing import Optional



@dataclasses.dataclass
class GetServicesRequest:
    provider: str = dataclasses.field(metadata={'path_param': { 'field_name': 'provider', 'style': 'simple', 'explode': False }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetServices200ApplicationJSON:
    r"""OK"""
    data: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class GetServicesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_services_200_application_json_object: Optional[GetServices200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
