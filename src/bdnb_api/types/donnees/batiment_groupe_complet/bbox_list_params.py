# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BboxListParams"]


class BboxListParams(TypedDict, total=False):
    xmax: Required[float]

    xmin: Required[float]

    ymax: Required[float]

    ymin: Required[float]

    srid: int
