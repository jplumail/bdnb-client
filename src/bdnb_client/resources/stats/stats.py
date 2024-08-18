# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .batiment_groupes import (
    BatimentGroupesResource,
    AsyncBatimentGroupesResource,
    BatimentGroupesResourceWithRawResponse,
    AsyncBatimentGroupesResourceWithRawResponse,
    BatimentGroupesResourceWithStreamingResponse,
    AsyncBatimentGroupesResourceWithStreamingResponse,
)

__all__ = ["StatsResource", "AsyncStatsResource"]


class StatsResource(SyncAPIResource):
    @cached_property
    def batiment_groupes(self) -> BatimentGroupesResource:
        return BatimentGroupesResource(self._client)

    @cached_property
    def with_raw_response(self) -> StatsResourceWithRawResponse:
        return StatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatsResourceWithStreamingResponse:
        return StatsResourceWithStreamingResponse(self)


class AsyncStatsResource(AsyncAPIResource):
    @cached_property
    def batiment_groupes(self) -> AsyncBatimentGroupesResource:
        return AsyncBatimentGroupesResource(self._client)

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
    def batiment_groupes(self) -> BatimentGroupesResourceWithRawResponse:
        return BatimentGroupesResourceWithRawResponse(self._stats.batiment_groupes)


class AsyncStatsResourceWithRawResponse:
    def __init__(self, stats: AsyncStatsResource) -> None:
        self._stats = stats

    @cached_property
    def batiment_groupes(self) -> AsyncBatimentGroupesResourceWithRawResponse:
        return AsyncBatimentGroupesResourceWithRawResponse(self._stats.batiment_groupes)


class StatsResourceWithStreamingResponse:
    def __init__(self, stats: StatsResource) -> None:
        self._stats = stats

    @cached_property
    def batiment_groupes(self) -> BatimentGroupesResourceWithStreamingResponse:
        return BatimentGroupesResourceWithStreamingResponse(self._stats.batiment_groupes)


class AsyncStatsResourceWithStreamingResponse:
    def __init__(self, stats: AsyncStatsResource) -> None:
        self._stats = stats

    @cached_property
    def batiment_groupes(self) -> AsyncBatimentGroupesResourceWithStreamingResponse:
        return AsyncBatimentGroupesResourceWithStreamingResponse(self._stats.batiment_groupes)
