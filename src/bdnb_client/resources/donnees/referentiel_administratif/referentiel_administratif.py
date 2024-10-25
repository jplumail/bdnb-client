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
from .referentiel_administratif_iris import (
    ReferentielAdministratifIrisResource,
    AsyncReferentielAdministratifIrisResource,
    ReferentielAdministratifIrisResourceWithRawResponse,
    AsyncReferentielAdministratifIrisResourceWithRawResponse,
    ReferentielAdministratifIrisResourceWithStreamingResponse,
    AsyncReferentielAdministratifIrisResourceWithStreamingResponse,
)

__all__ = ["ReferentielAdministratifResource", "AsyncReferentielAdministratifResource"]


class ReferentielAdministratifResource(SyncAPIResource):
    @cached_property
    def referentiel_administratif_iris(self) -> ReferentielAdministratifIrisResource:
        return ReferentielAdministratifIrisResource(self._client)

    @cached_property
    def epci(self) -> EpciResource:
        return EpciResource(self._client)

    @cached_property
    def departement(self) -> DepartementResource:
        return DepartementResource(self._client)

    @cached_property
    def region(self) -> RegionResource:
        return RegionResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReferentielAdministratifResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return ReferentielAdministratifResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReferentielAdministratifResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return ReferentielAdministratifResourceWithStreamingResponse(self)


class AsyncReferentielAdministratifResource(AsyncAPIResource):
    @cached_property
    def referentiel_administratif_iris(self) -> AsyncReferentielAdministratifIrisResource:
        return AsyncReferentielAdministratifIrisResource(self._client)

    @cached_property
    def epci(self) -> AsyncEpciResource:
        return AsyncEpciResource(self._client)

    @cached_property
    def departement(self) -> AsyncDepartementResource:
        return AsyncDepartementResource(self._client)

    @cached_property
    def region(self) -> AsyncRegionResource:
        return AsyncRegionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReferentielAdministratifResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncReferentielAdministratifResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReferentielAdministratifResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncReferentielAdministratifResourceWithStreamingResponse(self)


class ReferentielAdministratifResourceWithRawResponse:
    def __init__(self, referentiel_administratif: ReferentielAdministratifResource) -> None:
        self._referentiel_administratif = referentiel_administratif

    @cached_property
    def referentiel_administratif_iris(self) -> ReferentielAdministratifIrisResourceWithRawResponse:
        return ReferentielAdministratifIrisResourceWithRawResponse(
            self._referentiel_administratif.referentiel_administratif_iris
        )

    @cached_property
    def epci(self) -> EpciResourceWithRawResponse:
        return EpciResourceWithRawResponse(self._referentiel_administratif.epci)

    @cached_property
    def departement(self) -> DepartementResourceWithRawResponse:
        return DepartementResourceWithRawResponse(self._referentiel_administratif.departement)

    @cached_property
    def region(self) -> RegionResourceWithRawResponse:
        return RegionResourceWithRawResponse(self._referentiel_administratif.region)


class AsyncReferentielAdministratifResourceWithRawResponse:
    def __init__(self, referentiel_administratif: AsyncReferentielAdministratifResource) -> None:
        self._referentiel_administratif = referentiel_administratif

    @cached_property
    def referentiel_administratif_iris(self) -> AsyncReferentielAdministratifIrisResourceWithRawResponse:
        return AsyncReferentielAdministratifIrisResourceWithRawResponse(
            self._referentiel_administratif.referentiel_administratif_iris
        )

    @cached_property
    def epci(self) -> AsyncEpciResourceWithRawResponse:
        return AsyncEpciResourceWithRawResponse(self._referentiel_administratif.epci)

    @cached_property
    def departement(self) -> AsyncDepartementResourceWithRawResponse:
        return AsyncDepartementResourceWithRawResponse(self._referentiel_administratif.departement)

    @cached_property
    def region(self) -> AsyncRegionResourceWithRawResponse:
        return AsyncRegionResourceWithRawResponse(self._referentiel_administratif.region)


class ReferentielAdministratifResourceWithStreamingResponse:
    def __init__(self, referentiel_administratif: ReferentielAdministratifResource) -> None:
        self._referentiel_administratif = referentiel_administratif

    @cached_property
    def referentiel_administratif_iris(self) -> ReferentielAdministratifIrisResourceWithStreamingResponse:
        return ReferentielAdministratifIrisResourceWithStreamingResponse(
            self._referentiel_administratif.referentiel_administratif_iris
        )

    @cached_property
    def epci(self) -> EpciResourceWithStreamingResponse:
        return EpciResourceWithStreamingResponse(self._referentiel_administratif.epci)

    @cached_property
    def departement(self) -> DepartementResourceWithStreamingResponse:
        return DepartementResourceWithStreamingResponse(self._referentiel_administratif.departement)

    @cached_property
    def region(self) -> RegionResourceWithStreamingResponse:
        return RegionResourceWithStreamingResponse(self._referentiel_administratif.region)


class AsyncReferentielAdministratifResourceWithStreamingResponse:
    def __init__(self, referentiel_administratif: AsyncReferentielAdministratifResource) -> None:
        self._referentiel_administratif = referentiel_administratif

    @cached_property
    def referentiel_administratif_iris(self) -> AsyncReferentielAdministratifIrisResourceWithStreamingResponse:
        return AsyncReferentielAdministratifIrisResourceWithStreamingResponse(
            self._referentiel_administratif.referentiel_administratif_iris
        )

    @cached_property
    def epci(self) -> AsyncEpciResourceWithStreamingResponse:
        return AsyncEpciResourceWithStreamingResponse(self._referentiel_administratif.epci)

    @cached_property
    def departement(self) -> AsyncDepartementResourceWithStreamingResponse:
        return AsyncDepartementResourceWithStreamingResponse(self._referentiel_administratif.departement)

    @cached_property
    def region(self) -> AsyncRegionResourceWithStreamingResponse:
        return AsyncRegionResourceWithStreamingResponse(self._referentiel_administratif.region)
