# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .bbox import (
    BboxResource,
    AsyncBboxResource,
    BboxResourceWithRawResponse,
    AsyncBboxResourceWithRawResponse,
    BboxResourceWithStreamingResponse,
    AsyncBboxResourceWithStreamingResponse,
)
from .polygon import (
    PolygonResource,
    AsyncPolygonResource,
    PolygonResourceWithRawResponse,
    AsyncPolygonResourceWithRawResponse,
    PolygonResourceWithStreamingResponse,
    AsyncPolygonResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["BatimentGroupeCompletResource", "AsyncBatimentGroupeCompletResource"]


class BatimentGroupeCompletResource(SyncAPIResource):
    @cached_property
    def bbox(self) -> BboxResource:
        return BboxResource(self._client)

    @cached_property
    def polygon(self) -> PolygonResource:
        return PolygonResource(self._client)

    @cached_property
    def with_raw_response(self) -> BatimentGroupeCompletResourceWithRawResponse:
        return BatimentGroupeCompletResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentGroupeCompletResourceWithStreamingResponse:
        return BatimentGroupeCompletResourceWithStreamingResponse(self)


class AsyncBatimentGroupeCompletResource(AsyncAPIResource):
    @cached_property
    def bbox(self) -> AsyncBboxResource:
        return AsyncBboxResource(self._client)

    @cached_property
    def polygon(self) -> AsyncPolygonResource:
        return AsyncPolygonResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBatimentGroupeCompletResourceWithRawResponse:
        return AsyncBatimentGroupeCompletResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentGroupeCompletResourceWithStreamingResponse:
        return AsyncBatimentGroupeCompletResourceWithStreamingResponse(self)


class BatimentGroupeCompletResourceWithRawResponse:
    def __init__(self, batiment_groupe_complet: BatimentGroupeCompletResource) -> None:
        self._batiment_groupe_complet = batiment_groupe_complet

    @cached_property
    def bbox(self) -> BboxResourceWithRawResponse:
        return BboxResourceWithRawResponse(self._batiment_groupe_complet.bbox)

    @cached_property
    def polygon(self) -> PolygonResourceWithRawResponse:
        return PolygonResourceWithRawResponse(self._batiment_groupe_complet.polygon)


class AsyncBatimentGroupeCompletResourceWithRawResponse:
    def __init__(self, batiment_groupe_complet: AsyncBatimentGroupeCompletResource) -> None:
        self._batiment_groupe_complet = batiment_groupe_complet

    @cached_property
    def bbox(self) -> AsyncBboxResourceWithRawResponse:
        return AsyncBboxResourceWithRawResponse(self._batiment_groupe_complet.bbox)

    @cached_property
    def polygon(self) -> AsyncPolygonResourceWithRawResponse:
        return AsyncPolygonResourceWithRawResponse(self._batiment_groupe_complet.polygon)


class BatimentGroupeCompletResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_complet: BatimentGroupeCompletResource) -> None:
        self._batiment_groupe_complet = batiment_groupe_complet

    @cached_property
    def bbox(self) -> BboxResourceWithStreamingResponse:
        return BboxResourceWithStreamingResponse(self._batiment_groupe_complet.bbox)

    @cached_property
    def polygon(self) -> PolygonResourceWithStreamingResponse:
        return PolygonResourceWithStreamingResponse(self._batiment_groupe_complet.polygon)


class AsyncBatimentGroupeCompletResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_complet: AsyncBatimentGroupeCompletResource) -> None:
        self._batiment_groupe_complet = batiment_groupe_complet

    @cached_property
    def bbox(self) -> AsyncBboxResourceWithStreamingResponse:
        return AsyncBboxResourceWithStreamingResponse(self._batiment_groupe_complet.bbox)

    @cached_property
    def polygon(self) -> AsyncPolygonResourceWithStreamingResponse:
        return AsyncPolygonResourceWithStreamingResponse(self._batiment_groupe_complet.polygon)
