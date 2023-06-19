"""
This library implements various methods for working with the Google Bigquery
APIs.

## Installation

```console
$ pip install --upgrade gcloud-aio-bigquery
```

## Usage

We're still working on documentation -- for now, you can use the
[smoke test][smoke-test] as an example.

## Emulators

For testing purposes, you may want to use `gcloud-aio-bigquery` along with a
local emulator. Setting the `$BIGQUERY_EMULATOR_HOST` environment variable to
the address of your emulator should be enough to do the trick.

[smoke-test]:
https://github.com/talkiq/gcloud-aio/blob/master/bigquery/tests/integration/smoke_test.py
"""
import sys

from gcloud.aio.bigquery.bigquery import Disposition
from gcloud.aio.bigquery.bigquery import SchemaUpdateOption
from gcloud.aio.bigquery.bigquery import SCOPES
from gcloud.aio.bigquery.bigquery import SourceFormat
from gcloud.aio.bigquery.dataset import Dataset
from gcloud.aio.bigquery.job import Job
from gcloud.aio.bigquery.table import Table
from gcloud.aio.bigquery.utils import query_response_to_dict


if sys.version_info >= (3, 8):
    from importlib import metadata
else:
    import importlib_metadata as metadata


__version__ = metadata.version('gcloud-aio-bigquery')
__all__ = [
    'Dataset',
    'Disposition',
    'Job',
    'SCOPES',
    'SchemaUpdateOption',
    'SourceFormat',
    'Table',
    '__version__',
    'query_response_to_dict',
]
