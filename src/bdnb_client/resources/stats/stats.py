# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .batiment_groupe import (
    BatimentGroupeResource,
    AsyncBatimentGroupeResource,
    BatimentGroupeResourceWithRawResponse,
    AsyncBatimentGroupeResourceWithRawResponse,
    BatimentGroupeResourceWithStreamingResponse,
    AsyncBatimentGroupeResourceWithStreamingResponse,
)

__all__ = ["StatsResource", "AsyncStatsResource"]


class StatsResource(SyncAPIResource):
    @cached_property
    def batiment_groupe(self) -> BatimentGroupeResource:
        return BatimentGroupeResource(self._client)

    @cached_property
    def with_raw_response(self) -> StatsResourceWithRawResponse:
        return StatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatsResourceWithStreamingResponse:
        return StatsResourceWithStreamingResponse(self)


class AsyncStatsResource(AsyncAPIResource):
    @cached_property
    def batiment_groupe(self) -> AsyncBatimentGroupeResource:
        return AsyncBatimentGroupeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStatsResourceWithRawResponse:
        return AsyncStatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatsResourceWithStreamingResponse:
        return AsyncStatsResourceWithStreamingResponse(self)


class StatsResourceWithRawResponse:
    def __init__(self, stats: StatsResource) -> None:
        self._stats = stats

    @cached_property
    def batiment_groupe(self) -> BatimentGroupeResourceWithRawResponse:
        return BatimentGroupeResourceWithRawResponse(self._stats.batiment_groupe)


class AsyncStatsResourceWithRawResponse:
    def __init__(self, stats: AsyncStatsResource) -> None:
        self._stats = stats

    @cached_property
    def batiment_groupe(self) -> AsyncBatimentGroupeResourceWithRawResponse:
        return AsyncBatimentGroupeResourceWithRawResponse(self._stats.batiment_groupe)


class StatsResourceWithStreamingResponse:
    def __init__(self, stats: StatsResource) -> None:
        self._stats = stats

    @cached_property
    def batiment_groupe(self) -> BatimentGroupeResourceWithStreamingResponse:
        return BatimentGroupeResourceWithStreamingResponse(self._stats.batiment_groupe)


class AsyncStatsResourceWithStreamingResponse:
    def __init__(self, stats: AsyncStatsResource) -> None:
        self._stats = stats

    @cached_property
    def batiment_groupe(self) -> AsyncBatimentGroupeResourceWithStreamingResponse:
        return AsyncBatimentGroupeResourceWithStreamingResponse(self._stats.batiment_groupe)