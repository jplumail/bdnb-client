# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .epci import (
    EpciResource,
    AsyncEpciResource,
    EpciResourceWithRawResponse,
    AsyncEpciResourceWithRawResponse,
    EpciResourceWithStreamingResponse,
    AsyncEpciResourceWithStreamingResponse,
)
from .iris import (
    IrisResource,
    AsyncIrisResource,
    IrisResourceWithRawResponse,
    AsyncIrisResourceWithRawResponse,
    IrisResourceWithStreamingResponse,
    AsyncIrisResourceWithStreamingResponse,
)
from .region import (
    RegionResource,
    AsyncRegionResource,
    RegionResourceWithRawResponse,
    AsyncRegionResourceWithRawResponse,
    RegionResourceWithStreamingResponse,
    AsyncRegionResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .departement import (
    DepartementResource,
    AsyncDepartementResource,
    DepartementResourceWithRawResponse,
    AsyncDepartementResourceWithRawResponse,
    DepartementResourceWithStreamingResponse,
    AsyncDepartementResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from .batiment_groupe import (
    BatimentGroupeResource,
    AsyncBatimentGroupeResource,
    BatimentGroupeResourceWithRawResponse,
    AsyncBatimentGroupeResourceWithRawResponse,
    BatimentGroupeResourceWithStreamingResponse,
    AsyncBatimentGroupeResourceWithStreamingResponse,
)

__all__ = ["VectoriellesResource", "AsyncVectoriellesResource"]


class VectoriellesResource(SyncAPIResource):
    @cached_property
    def epci(self) -> EpciResource:
        return EpciResource(self._client)

    @cached_property
    def region(self) -> RegionResource:
        return RegionResource(self._client)

    @cached_property
    def iris(self) -> IrisResource:
        return IrisResource(self._client)

    @cached_property
    def departement(self) -> DepartementResource:
        return DepartementResource(self._client)

    @cached_property
    def batiment_groupe(self) -> BatimentGroupeResource:
        return BatimentGroupeResource(self._client)

    @cached_property
    def with_raw_response(self) -> VectoriellesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return VectoriellesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VectoriellesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return VectoriellesResourceWithStreamingResponse(self)


class AsyncVectoriellesResource(AsyncAPIResource):
    @cached_property
    def epci(self) -> AsyncEpciResource:
        return AsyncEpciResource(self._client)

    @cached_property
    def region(self) -> AsyncRegionResource:
        return AsyncRegionResource(self._client)

    @cached_property
    def iris(self) -> AsyncIrisResource:
        return AsyncIrisResource(self._client)

    @cached_property
    def departement(self) -> AsyncDepartementResource:
        return AsyncDepartementResource(self._client)

    @cached_property
    def batiment_groupe(self) -> AsyncBatimentGroupeResource:
        return AsyncBatimentGroupeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVectoriellesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncVectoriellesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVectoriellesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncVectoriellesResourceWithStreamingResponse(self)


class VectoriellesResourceWithRawResponse:
    def __init__(self, vectorielles: VectoriellesResource) -> None:
        self._vectorielles = vectorielles

    @cached_property
    def epci(self) -> EpciResourceWithRawResponse:
        return EpciResourceWithRawResponse(self._vectorielles.epci)

    @cached_property
    def region(self) -> RegionResourceWithRawResponse:
        return RegionResourceWithRawResponse(self._vectorielles.region)

    @cached_property
    def iris(self) -> IrisResourceWithRawResponse:
        return IrisResourceWithRawResponse(self._vectorielles.iris)

    @cached_property
    def departement(self) -> DepartementResourceWithRawResponse:
        return DepartementResourceWithRawResponse(self._vectorielles.departement)

    @cached_property
    def batiment_groupe(self) -> BatimentGroupeResourceWithRawResponse:
        return BatimentGroupeResourceWithRawResponse(self._vectorielles.batiment_groupe)


class AsyncVectoriellesResourceWithRawResponse:
    def __init__(self, vectorielles: AsyncVectoriellesResource) -> None:
        self._vectorielles = vectorielles

    @cached_property
    def epci(self) -> AsyncEpciResourceWithRawResponse:
        return AsyncEpciResourceWithRawResponse(self._vectorielles.epci)

    @cached_property
    def region(self) -> AsyncRegionResourceWithRawResponse:
        return AsyncRegionResourceWithRawResponse(self._vectorielles.region)

    @cached_property
    def iris(self) -> AsyncIrisResourceWithRawResponse:
        return AsyncIrisResourceWithRawResponse(self._vectorielles.iris)

    @cached_property
    def departement(self) -> AsyncDepartementResourceWithRawResponse:
        return AsyncDepartementResourceWithRawResponse(self._vectorielles.departement)

    @cached_property
    def batiment_groupe(self) -> AsyncBatimentGroupeResourceWithRawResponse:
        return AsyncBatimentGroupeResourceWithRawResponse(self._vectorielles.batiment_groupe)


class VectoriellesResourceWithStreamingResponse:
    def __init__(self, vectorielles: VectoriellesResource) -> None:
        self._vectorielles = vectorielles

    @cached_property
    def epci(self) -> EpciResourceWithStreamingResponse:
        return EpciResourceWithStreamingResponse(self._vectorielles.epci)

    @cached_property
    def region(self) -> RegionResourceWithStreamingResponse:
        return RegionResourceWithStreamingResponse(self._vectorielles.region)

    @cached_property
    def iris(self) -> IrisResourceWithStreamingResponse:
        return IrisResourceWithStreamingResponse(self._vectorielles.iris)

    @cached_property
    def departement(self) -> DepartementResourceWithStreamingResponse:
        return DepartementResourceWithStreamingResponse(self._vectorielles.departement)

    @cached_property
    def batiment_groupe(self) -> BatimentGroupeResourceWithStreamingResponse:
        return BatimentGroupeResourceWithStreamingResponse(self._vectorielles.batiment_groupe)


class AsyncVectoriellesResourceWithStreamingResponse:
    def __init__(self, vectorielles: AsyncVectoriellesResource) -> None:
        self._vectorielles = vectorielles

    @cached_property
    def epci(self) -> AsyncEpciResourceWithStreamingResponse:
        return AsyncEpciResourceWithStreamingResponse(self._vectorielles.epci)

    @cached_property
    def region(self) -> AsyncRegionResourceWithStreamingResponse:
        return AsyncRegionResourceWithStreamingResponse(self._vectorielles.region)

    @cached_property
    def iris(self) -> AsyncIrisResourceWithStreamingResponse:
        return AsyncIrisResourceWithStreamingResponse(self._vectorielles.iris)

    @cached_property
    def departement(self) -> AsyncDepartementResourceWithStreamingResponse:
        return AsyncDepartementResourceWithStreamingResponse(self._vectorielles.departement)

    @cached_property
    def batiment_groupe(self) -> AsyncBatimentGroupeResourceWithStreamingResponse:
        return AsyncBatimentGroupeResourceWithStreamingResponse(self._vectorielles.batiment_groupe)
