# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .adresse import (
    AdresseResource,
    AsyncAdresseResource,
    AdresseResourceWithRawResponse,
    AsyncAdresseResourceWithRawResponse,
    AdresseResourceWithStreamingResponse,
    AsyncAdresseResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["BatimentConstructionResource", "AsyncBatimentConstructionResource"]


class BatimentConstructionResource(SyncAPIResource):
    @cached_property
    def adresse(self) -> AdresseResource:
        return AdresseResource(self._client)

    @cached_property
    def with_raw_response(self) -> BatimentConstructionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return BatimentConstructionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentConstructionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return BatimentConstructionResourceWithStreamingResponse(self)


class AsyncBatimentConstructionResource(AsyncAPIResource):
    @cached_property
    def adresse(self) -> AsyncAdresseResource:
        return AsyncAdresseResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBatimentConstructionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncBatimentConstructionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentConstructionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncBatimentConstructionResourceWithStreamingResponse(self)


class BatimentConstructionResourceWithRawResponse:
    def __init__(self, batiment_construction: BatimentConstructionResource) -> None:
        self._batiment_construction = batiment_construction

    @cached_property
    def adresse(self) -> AdresseResourceWithRawResponse:
        return AdresseResourceWithRawResponse(self._batiment_construction.adresse)


class AsyncBatimentConstructionResourceWithRawResponse:
    def __init__(self, batiment_construction: AsyncBatimentConstructionResource) -> None:
        self._batiment_construction = batiment_construction

    @cached_property
    def adresse(self) -> AsyncAdresseResourceWithRawResponse:
        return AsyncAdresseResourceWithRawResponse(self._batiment_construction.adresse)


class BatimentConstructionResourceWithStreamingResponse:
    def __init__(self, batiment_construction: BatimentConstructionResource) -> None:
        self._batiment_construction = batiment_construction

    @cached_property
    def adresse(self) -> AdresseResourceWithStreamingResponse:
        return AdresseResourceWithStreamingResponse(self._batiment_construction.adresse)


class AsyncBatimentConstructionResourceWithStreamingResponse:
    def __init__(self, batiment_construction: AsyncBatimentConstructionResource) -> None:
        self._batiment_construction = batiment_construction

    @cached_property
    def adresse(self) -> AsyncAdresseResourceWithStreamingResponse:
        return AsyncAdresseResourceWithStreamingResponse(self._batiment_construction.adresse)
