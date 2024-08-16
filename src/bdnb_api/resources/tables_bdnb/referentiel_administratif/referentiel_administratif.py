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

__all__ = ["ReferentielAdministratifResource", "AsyncReferentielAdministratifResource"]


class ReferentielAdministratifResource(SyncAPIResource):
    @cached_property
    def epci(self) -> EpciResource:
        return EpciResource(self._client)

    @cached_property
    def departement(self) -> DepartementResource:
        return DepartementResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReferentielAdministratifResourceWithRawResponse:
        return ReferentielAdministratifResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReferentielAdministratifResourceWithStreamingResponse:
        return ReferentielAdministratifResourceWithStreamingResponse(self)


class AsyncReferentielAdministratifResource(AsyncAPIResource):
    @cached_property
    def epci(self) -> AsyncEpciResource:
        return AsyncEpciResource(self._client)

    @cached_property
    def departement(self) -> AsyncDepartementResource:
        return AsyncDepartementResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReferentielAdministratifResourceWithRawResponse:
        return AsyncReferentielAdministratifResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReferentielAdministratifResourceWithStreamingResponse:
        return AsyncReferentielAdministratifResourceWithStreamingResponse(self)


class ReferentielAdministratifResourceWithRawResponse:
    def __init__(self, referentiel_administratif: ReferentielAdministratifResource) -> None:
        self._referentiel_administratif = referentiel_administratif

    @cached_property
    def epci(self) -> EpciResourceWithRawResponse:
        return EpciResourceWithRawResponse(self._referentiel_administratif.epci)

    @cached_property
    def departement(self) -> DepartementResourceWithRawResponse:
        return DepartementResourceWithRawResponse(self._referentiel_administratif.departement)


class AsyncReferentielAdministratifResourceWithRawResponse:
    def __init__(self, referentiel_administratif: AsyncReferentielAdministratifResource) -> None:
        self._referentiel_administratif = referentiel_administratif

    @cached_property
    def epci(self) -> AsyncEpciResourceWithRawResponse:
        return AsyncEpciResourceWithRawResponse(self._referentiel_administratif.epci)

    @cached_property
    def departement(self) -> AsyncDepartementResourceWithRawResponse:
        return AsyncDepartementResourceWithRawResponse(self._referentiel_administratif.departement)


class ReferentielAdministratifResourceWithStreamingResponse:
    def __init__(self, referentiel_administratif: ReferentielAdministratifResource) -> None:
        self._referentiel_administratif = referentiel_administratif

    @cached_property
    def epci(self) -> EpciResourceWithStreamingResponse:
        return EpciResourceWithStreamingResponse(self._referentiel_administratif.epci)

    @cached_property
    def departement(self) -> DepartementResourceWithStreamingResponse:
        return DepartementResourceWithStreamingResponse(self._referentiel_administratif.departement)


class AsyncReferentielAdministratifResourceWithStreamingResponse:
    def __init__(self, referentiel_administratif: AsyncReferentielAdministratifResource) -> None:
        self._referentiel_administratif = referentiel_administratif

    @cached_property
    def epci(self) -> AsyncEpciResourceWithStreamingResponse:
        return AsyncEpciResourceWithStreamingResponse(self._referentiel_administratif.epci)

    @cached_property
    def departement(self) -> AsyncDepartementResourceWithStreamingResponse:
        return AsyncDepartementResourceWithStreamingResponse(self._referentiel_administratif.departement)
