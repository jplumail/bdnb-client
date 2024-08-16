# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .info import (
    InfoResource,
    AsyncInfoResource,
    InfoResourceWithRawResponse,
    AsyncInfoResourceWithRawResponse,
    InfoResourceWithStreamingResponse,
    AsyncInfoResourceWithStreamingResponse,
)
from .table import (
    TableResource,
    AsyncTableResource,
    TableResourceWithRawResponse,
    AsyncTableResourceWithRawResponse,
    TableResourceWithStreamingResponse,
    AsyncTableResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .fournisseur import (
    FournisseurResource,
    AsyncFournisseurResource,
    FournisseurResourceWithRawResponse,
    AsyncFournisseurResourceWithRawResponse,
    FournisseurResourceWithStreamingResponse,
    AsyncFournisseurResourceWithStreamingResponse,
)
from .contrainte_acces import (
    ContrainteAccesResource,
    AsyncContrainteAccesResource,
    ContrainteAccesResourceWithRawResponse,
    AsyncContrainteAccesResourceWithRawResponse,
    ContrainteAccesResourceWithStreamingResponse,
    AsyncContrainteAccesResourceWithStreamingResponse,
)

__all__ = ["MetaDonneesResource", "AsyncMetaDonneesResource"]


class MetaDonneesResource(SyncAPIResource):
    @cached_property
    def info(self) -> InfoResource:
        return InfoResource(self._client)

    @cached_property
    def table(self) -> TableResource:
        return TableResource(self._client)

    @cached_property
    def fournisseur(self) -> FournisseurResource:
        return FournisseurResource(self._client)

    @cached_property
    def contrainte_acces(self) -> ContrainteAccesResource:
        return ContrainteAccesResource(self._client)

    @cached_property
    def with_raw_response(self) -> MetaDonneesResourceWithRawResponse:
        return MetaDonneesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetaDonneesResourceWithStreamingResponse:
        return MetaDonneesResourceWithStreamingResponse(self)


class AsyncMetaDonneesResource(AsyncAPIResource):
    @cached_property
    def info(self) -> AsyncInfoResource:
        return AsyncInfoResource(self._client)

    @cached_property
    def table(self) -> AsyncTableResource:
        return AsyncTableResource(self._client)

    @cached_property
    def fournisseur(self) -> AsyncFournisseurResource:
        return AsyncFournisseurResource(self._client)

    @cached_property
    def contrainte_acces(self) -> AsyncContrainteAccesResource:
        return AsyncContrainteAccesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMetaDonneesResourceWithRawResponse:
        return AsyncMetaDonneesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetaDonneesResourceWithStreamingResponse:
        return AsyncMetaDonneesResourceWithStreamingResponse(self)


class MetaDonneesResourceWithRawResponse:
    def __init__(self, meta_donnees: MetaDonneesResource) -> None:
        self._meta_donnees = meta_donnees

    @cached_property
    def info(self) -> InfoResourceWithRawResponse:
        return InfoResourceWithRawResponse(self._meta_donnees.info)

    @cached_property
    def table(self) -> TableResourceWithRawResponse:
        return TableResourceWithRawResponse(self._meta_donnees.table)

    @cached_property
    def fournisseur(self) -> FournisseurResourceWithRawResponse:
        return FournisseurResourceWithRawResponse(self._meta_donnees.fournisseur)

    @cached_property
    def contrainte_acces(self) -> ContrainteAccesResourceWithRawResponse:
        return ContrainteAccesResourceWithRawResponse(self._meta_donnees.contrainte_acces)


class AsyncMetaDonneesResourceWithRawResponse:
    def __init__(self, meta_donnees: AsyncMetaDonneesResource) -> None:
        self._meta_donnees = meta_donnees

    @cached_property
    def info(self) -> AsyncInfoResourceWithRawResponse:
        return AsyncInfoResourceWithRawResponse(self._meta_donnees.info)

    @cached_property
    def table(self) -> AsyncTableResourceWithRawResponse:
        return AsyncTableResourceWithRawResponse(self._meta_donnees.table)

    @cached_property
    def fournisseur(self) -> AsyncFournisseurResourceWithRawResponse:
        return AsyncFournisseurResourceWithRawResponse(self._meta_donnees.fournisseur)

    @cached_property
    def contrainte_acces(self) -> AsyncContrainteAccesResourceWithRawResponse:
        return AsyncContrainteAccesResourceWithRawResponse(self._meta_donnees.contrainte_acces)


class MetaDonneesResourceWithStreamingResponse:
    def __init__(self, meta_donnees: MetaDonneesResource) -> None:
        self._meta_donnees = meta_donnees

    @cached_property
    def info(self) -> InfoResourceWithStreamingResponse:
        return InfoResourceWithStreamingResponse(self._meta_donnees.info)

    @cached_property
    def table(self) -> TableResourceWithStreamingResponse:
        return TableResourceWithStreamingResponse(self._meta_donnees.table)

    @cached_property
    def fournisseur(self) -> FournisseurResourceWithStreamingResponse:
        return FournisseurResourceWithStreamingResponse(self._meta_donnees.fournisseur)

    @cached_property
    def contrainte_acces(self) -> ContrainteAccesResourceWithStreamingResponse:
        return ContrainteAccesResourceWithStreamingResponse(self._meta_donnees.contrainte_acces)


class AsyncMetaDonneesResourceWithStreamingResponse:
    def __init__(self, meta_donnees: AsyncMetaDonneesResource) -> None:
        self._meta_donnees = meta_donnees

    @cached_property
    def info(self) -> AsyncInfoResourceWithStreamingResponse:
        return AsyncInfoResourceWithStreamingResponse(self._meta_donnees.info)

    @cached_property
    def table(self) -> AsyncTableResourceWithStreamingResponse:
        return AsyncTableResourceWithStreamingResponse(self._meta_donnees.table)

    @cached_property
    def fournisseur(self) -> AsyncFournisseurResourceWithStreamingResponse:
        return AsyncFournisseurResourceWithStreamingResponse(self._meta_donnees.fournisseur)

    @cached_property
    def contrainte_acces(self) -> AsyncContrainteAccesResourceWithStreamingResponse:
        return AsyncContrainteAccesResourceWithStreamingResponse(self._meta_donnees.contrainte_acces)
