from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `local_protocol.resources` module.

    This is used so that we can lazily import `local_protocol.resources` only when
    needed *and* so that users can just import `local_protocol` and reference `local_protocol.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("local_protocol.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
