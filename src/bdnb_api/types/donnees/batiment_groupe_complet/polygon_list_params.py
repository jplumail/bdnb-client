# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["PolygonListParams"]


class PolygonListParams(TypedDict, total=False):
    limit: str

    coordinates: Iterable[Iterable[Iterable[float]]]

    type: str
