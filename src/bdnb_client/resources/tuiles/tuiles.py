# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .vectorielles import (
    VectoriellesResource,
    AsyncVectoriellesResource,
    VectoriellesResourceWithRawResponse,
    AsyncVectoriellesResourceWithRawResponse,
    VectoriellesResourceWithStreamingResponse,
    AsyncVectoriellesResourceWithStreamingResponse,
)
from .vectorielles.vectorielles import VectoriellesResource, AsyncVectoriellesResource

__all__ = ["TuilesResource", "AsyncTuilesResource"]


class TuilesResource(SyncAPIResource):
    @cached_property
    def vectorielles(self) -> VectoriellesResource:
        return VectoriellesResource(self._client)

    @cached_property
    def with_raw_response(self) -> TuilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return TuilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TuilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return TuilesResourceWithStreamingResponse(self)


class AsyncTuilesResource(AsyncAPIResource):
    @cached_property
    def vectorielles(self) -> AsyncVectoriellesResource:
        return AsyncVectoriellesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTuilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncTuilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTuilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncTuilesResourceWithStreamingResponse(self)


class TuilesResourceWithRawResponse:
    def __init__(self, tuiles: TuilesResource) -> None:
        self._tuiles = tuiles

    @cached_property
    def vectorielles(self) -> VectoriellesResourceWithRawResponse:
        return VectoriellesResourceWithRawResponse(self._tuiles.vectorielles)


class AsyncTuilesResourceWithRawResponse:
    def __init__(self, tuiles: AsyncTuilesResource) -> None:
        self._tuiles = tuiles

    @cached_property
    def vectorielles(self) -> AsyncVectoriellesResourceWithRawResponse:
        return AsyncVectoriellesResourceWithRawResponse(self._tuiles.vectorielles)


class TuilesResourceWithStreamingResponse:
    def __init__(self, tuiles: TuilesResource) -> None:
        self._tuiles = tuiles

    @cached_property
    def vectorielles(self) -> VectoriellesResourceWithStreamingResponse:
        return VectoriellesResourceWithStreamingResponse(self._tuiles.vectorielles)


class AsyncTuilesResourceWithStreamingResponse:
    def __init__(self, tuiles: AsyncTuilesResource) -> None:
        self._tuiles = tuiles

    @cached_property
    def vectorielles(self) -> AsyncVectoriellesResourceWithStreamingResponse:
        return AsyncVectoriellesResourceWithStreamingResponse(self._tuiles.vectorielles)
