# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .batiment_groupe import (
    BatimentGroupeResource,
    AsyncBatimentGroupeResource,
    BatimentGroupeResourceWithRawResponse,
    AsyncBatimentGroupeResourceWithRawResponse,
    BatimentGroupeResourceWithStreamingResponse,
    AsyncBatimentGroupeResourceWithStreamingResponse,
)
from .batiment_construction import (
    BatimentConstructionResource,
    AsyncBatimentConstructionResource,
    BatimentConstructionResourceWithRawResponse,
    AsyncBatimentConstructionResourceWithRawResponse,
    BatimentConstructionResourceWithStreamingResponse,
    AsyncBatimentConstructionResourceWithStreamingResponse,
)
from .batiment_groupe.batiment_groupe import BatimentGroupeResource, AsyncBatimentGroupeResource
from .batiment_construction.batiment_construction import BatimentConstructionResource, AsyncBatimentConstructionResource

__all__ = ["RelationsResource", "AsyncRelationsResource"]


class RelationsResource(SyncAPIResource):
    @cached_property
    def batiment_construction(self) -> BatimentConstructionResource:
        return BatimentConstructionResource(self._client)

    @cached_property
    def batiment_groupe(self) -> BatimentGroupeResource:
        return BatimentGroupeResource(self._client)

    @cached_property
    def with_raw_response(self) -> RelationsResourceWithRawResponse:
        return RelationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RelationsResourceWithStreamingResponse:
        return RelationsResourceWithStreamingResponse(self)


class AsyncRelationsResource(AsyncAPIResource):
    @cached_property
    def batiment_construction(self) -> AsyncBatimentConstructionResource:
        return AsyncBatimentConstructionResource(self._client)

    @cached_property
    def batiment_groupe(self) -> AsyncBatimentGroupeResource:
        return AsyncBatimentGroupeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRelationsResourceWithRawResponse:
        return AsyncRelationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRelationsResourceWithStreamingResponse:
        return AsyncRelationsResourceWithStreamingResponse(self)


class RelationsResourceWithRawResponse:
    def __init__(self, relations: RelationsResource) -> None:
        self._relations = relations

    @cached_property
    def batiment_construction(self) -> BatimentConstructionResourceWithRawResponse:
        return BatimentConstructionResourceWithRawResponse(self._relations.batiment_construction)

    @cached_property
    def batiment_groupe(self) -> BatimentGroupeResourceWithRawResponse:
        return BatimentGroupeResourceWithRawResponse(self._relations.batiment_groupe)


class AsyncRelationsResourceWithRawResponse:
    def __init__(self, relations: AsyncRelationsResource) -> None:
        self._relations = relations

    @cached_property
    def batiment_construction(self) -> AsyncBatimentConstructionResourceWithRawResponse:
        return AsyncBatimentConstructionResourceWithRawResponse(self._relations.batiment_construction)

    @cached_property
    def batiment_groupe(self) -> AsyncBatimentGroupeResourceWithRawResponse:
        return AsyncBatimentGroupeResourceWithRawResponse(self._relations.batiment_groupe)


class RelationsResourceWithStreamingResponse:
    def __init__(self, relations: RelationsResource) -> None:
        self._relations = relations

    @cached_property
    def batiment_construction(self) -> BatimentConstructionResourceWithStreamingResponse:
        return BatimentConstructionResourceWithStreamingResponse(self._relations.batiment_construction)

    @cached_property
    def batiment_groupe(self) -> BatimentGroupeResourceWithStreamingResponse:
        return BatimentGroupeResourceWithStreamingResponse(self._relations.batiment_groupe)


class AsyncRelationsResourceWithStreamingResponse:
    def __init__(self, relations: AsyncRelationsResource) -> None:
        self._relations = relations

    @cached_property
    def batiment_construction(self) -> AsyncBatimentConstructionResourceWithStreamingResponse:
        return AsyncBatimentConstructionResourceWithStreamingResponse(self._relations.batiment_construction)

    @cached_property
    def batiment_groupe(self) -> AsyncBatimentGroupeResourceWithStreamingResponse:
        return AsyncBatimentGroupeResourceWithStreamingResponse(self._relations.batiment_groupe)
