"""
This library implements various methods for working with the Google Taskqueue
APIs.

## Installation

```console
$ pip install --upgrade gcloud-aio-taskqueue
```

## Usage

We're still working on documentation -- for now, you can use the
[smoke tests][smoke-tests] as an example.

## Emulators

For testing purposes, you may want to use `gcloud-aio-taskqueue` along with a
local emulator. Setting the `$CLOUDTASKS_EMULATOR_HOST` environment variable to
the address of your emulator should be enough to do the trick.

[smoke-tests]:
https://github.com/talkiq/gcloud-aio/tree/master/taskqueue/tests/integration
"""
import sys

from gcloud.aio.taskqueue.queue import PushQueue
from gcloud.aio.taskqueue.queue import SCOPES


if sys.version_info >= (3, 8):
    from importlib import metadata
else:
    import importlib_metadata as metadata


__version__ = metadata.version('gcloud-aio-taskqueue')
__all__ = [
    'PushQueue',
    'SCOPES',
    '__version__',
]
