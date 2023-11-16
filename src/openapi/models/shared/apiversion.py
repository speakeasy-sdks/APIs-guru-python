"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from openapi import utils
from typing import Optional


@dataclasses.dataclass
class ExternalDocs:
    r"""Copy of `externalDocs` section from OpenAPI definition"""
    



@dataclasses.dataclass
class Info:
    r"""Copy of `info` section from OpenAPI definition"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class APIVersion:
    added: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('added'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""Timestamp when the version was added"""
    info: Info = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('info') }})
    r"""Copy of `info` section from OpenAPI definition"""
    openapi_ver: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('openapiVer') }})
    r"""The value of the `openapi` or `swagger` property of the source definition"""
    swagger_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('swaggerUrl') }})
    r"""URL to OpenAPI definition in JSON format"""
    swagger_yaml_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('swaggerYamlUrl') }})
    r"""URL to OpenAPI definition in YAML format"""
    updated: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""Timestamp when the version was updated"""
    external_docs: Optional[ExternalDocs] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('externalDocs'), 'exclude': lambda f: f is None }})
    r"""Copy of `externalDocs` section from OpenAPI definition"""
    link: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link'), 'exclude': lambda f: f is None }})
    r"""Link to the individual API entry for this API"""
    

