# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .qpv import (
    QpvResource,
    AsyncQpvResource,
    QpvResourceWithRawResponse,
    AsyncQpvResourceWithRawResponse,
    QpvResourceWithStreamingResponse,
    AsyncQpvResourceWithStreamingResponse,
)
from .rnc import (
    RncResource,
    AsyncRncResource,
    RncResourceWithRawResponse,
    AsyncRncResourceWithRawResponse,
    RncResourceWithStreamingResponse,
    AsyncRncResourceWithStreamingResponse,
)
from .adresse import (
    AdresseResource,
    AsyncAdresseResource,
    AdresseResourceWithRawResponse,
    AsyncAdresseResourceWithRawResponse,
    AdresseResourceWithStreamingResponse,
    AsyncAdresseResourceWithStreamingResponse,
)
from .merimee import (
    MerimeeResource,
    AsyncMerimeeResource,
    MerimeeResourceWithRawResponse,
    AsyncMerimeeResourceWithRawResponse,
    MerimeeResourceWithStreamingResponse,
    AsyncMerimeeResourceWithStreamingResponse,
)
from .parcelle import (
    ParcelleResource,
    AsyncParcelleResource,
    ParcelleResourceWithRawResponse,
    AsyncParcelleResourceWithRawResponse,
    ParcelleResourceWithStreamingResponse,
    AsyncParcelleResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .siren_complet import (
    SirenCompletResource,
    AsyncSirenCompletResource,
    SirenCompletResourceWithRawResponse,
    AsyncSirenCompletResourceWithRawResponse,
    SirenCompletResourceWithStreamingResponse,
    AsyncSirenCompletResourceWithStreamingResponse,
)
from .siret_complet import (
    SiretCompletResource,
    AsyncSiretCompletResource,
    SiretCompletResourceWithRawResponse,
    AsyncSiretCompletResourceWithRawResponse,
    SiretCompletResourceWithStreamingResponse,
    AsyncSiretCompletResourceWithStreamingResponse,
)
from .proprietaire_siren import (
    ProprietaireSirenResource,
    AsyncProprietaireSirenResource,
    ProprietaireSirenResourceWithRawResponse,
    AsyncProprietaireSirenResourceWithRawResponse,
    ProprietaireSirenResourceWithStreamingResponse,
    AsyncProprietaireSirenResourceWithStreamingResponse,
)
from .proprietaire_siren_open import (
    ProprietaireSirenOpenResource,
    AsyncProprietaireSirenOpenResource,
    ProprietaireSirenOpenResourceWithRawResponse,
    AsyncProprietaireSirenOpenResourceWithRawResponse,
    ProprietaireSirenOpenResourceWithStreamingResponse,
    AsyncProprietaireSirenOpenResourceWithStreamingResponse,
)

__all__ = ["BatimentGroupeResource", "AsyncBatimentGroupeResource"]


class BatimentGroupeResource(SyncAPIResource):
    @cached_property
    def proprietaire_siren(self) -> ProprietaireSirenResource:
        return ProprietaireSirenResource(self._client)

    @cached_property
    def qpv(self) -> QpvResource:
        return QpvResource(self._client)

    @cached_property
    def adresse(self) -> AdresseResource:
        return AdresseResource(self._client)

    @cached_property
    def merimee(self) -> MerimeeResource:
        return MerimeeResource(self._client)

    @cached_property
    def parcelle(self) -> ParcelleResource:
        return ParcelleResource(self._client)

    @cached_property
    def siren_complet(self) -> SirenCompletResource:
        return SirenCompletResource(self._client)

    @cached_property
    def siret_complet(self) -> SiretCompletResource:
        return SiretCompletResource(self._client)

    @cached_property
    def rnc(self) -> RncResource:
        return RncResource(self._client)

    @cached_property
    def proprietaire_siren_open(self) -> ProprietaireSirenOpenResource:
        return ProprietaireSirenOpenResource(self._client)

    @cached_property
    def with_raw_response(self) -> BatimentGroupeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return BatimentGroupeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentGroupeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return BatimentGroupeResourceWithStreamingResponse(self)


class AsyncBatimentGroupeResource(AsyncAPIResource):
    @cached_property
    def proprietaire_siren(self) -> AsyncProprietaireSirenResource:
        return AsyncProprietaireSirenResource(self._client)

    @cached_property
    def qpv(self) -> AsyncQpvResource:
        return AsyncQpvResource(self._client)

    @cached_property
    def adresse(self) -> AsyncAdresseResource:
        return AsyncAdresseResource(self._client)

    @cached_property
    def merimee(self) -> AsyncMerimeeResource:
        return AsyncMerimeeResource(self._client)

    @cached_property
    def parcelle(self) -> AsyncParcelleResource:
        return AsyncParcelleResource(self._client)

    @cached_property
    def siren_complet(self) -> AsyncSirenCompletResource:
        return AsyncSirenCompletResource(self._client)

    @cached_property
    def siret_complet(self) -> AsyncSiretCompletResource:
        return AsyncSiretCompletResource(self._client)

    @cached_property
    def rnc(self) -> AsyncRncResource:
        return AsyncRncResource(self._client)

    @cached_property
    def proprietaire_siren_open(self) -> AsyncProprietaireSirenOpenResource:
        return AsyncProprietaireSirenOpenResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBatimentGroupeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncBatimentGroupeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentGroupeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncBatimentGroupeResourceWithStreamingResponse(self)


class BatimentGroupeResourceWithRawResponse:
    def __init__(self, batiment_groupe: BatimentGroupeResource) -> None:
        self._batiment_groupe = batiment_groupe

    @cached_property
    def proprietaire_siren(self) -> ProprietaireSirenResourceWithRawResponse:
        return ProprietaireSirenResourceWithRawResponse(self._batiment_groupe.proprietaire_siren)

    @cached_property
    def qpv(self) -> QpvResourceWithRawResponse:
        return QpvResourceWithRawResponse(self._batiment_groupe.qpv)

    @cached_property
    def adresse(self) -> AdresseResourceWithRawResponse:
        return AdresseResourceWithRawResponse(self._batiment_groupe.adresse)

    @cached_property
    def merimee(self) -> MerimeeResourceWithRawResponse:
        return MerimeeResourceWithRawResponse(self._batiment_groupe.merimee)

    @cached_property
    def parcelle(self) -> ParcelleResourceWithRawResponse:
        return ParcelleResourceWithRawResponse(self._batiment_groupe.parcelle)

    @cached_property
    def siren_complet(self) -> SirenCompletResourceWithRawResponse:
        return SirenCompletResourceWithRawResponse(self._batiment_groupe.siren_complet)

    @cached_property
    def siret_complet(self) -> SiretCompletResourceWithRawResponse:
        return SiretCompletResourceWithRawResponse(self._batiment_groupe.siret_complet)

    @cached_property
    def rnc(self) -> RncResourceWithRawResponse:
        return RncResourceWithRawResponse(self._batiment_groupe.rnc)

    @cached_property
    def proprietaire_siren_open(self) -> ProprietaireSirenOpenResourceWithRawResponse:
        return ProprietaireSirenOpenResourceWithRawResponse(self._batiment_groupe.proprietaire_siren_open)


class AsyncBatimentGroupeResourceWithRawResponse:
    def __init__(self, batiment_groupe: AsyncBatimentGroupeResource) -> None:
        self._batiment_groupe = batiment_groupe

    @cached_property
    def proprietaire_siren(self) -> AsyncProprietaireSirenResourceWithRawResponse:
        return AsyncProprietaireSirenResourceWithRawResponse(self._batiment_groupe.proprietaire_siren)

    @cached_property
    def qpv(self) -> AsyncQpvResourceWithRawResponse:
        return AsyncQpvResourceWithRawResponse(self._batiment_groupe.qpv)

    @cached_property
    def adresse(self) -> AsyncAdresseResourceWithRawResponse:
        return AsyncAdresseResourceWithRawResponse(self._batiment_groupe.adresse)

    @cached_property
    def merimee(self) -> AsyncMerimeeResourceWithRawResponse:
        return AsyncMerimeeResourceWithRawResponse(self._batiment_groupe.merimee)

    @cached_property
    def parcelle(self) -> AsyncParcelleResourceWithRawResponse:
        return AsyncParcelleResourceWithRawResponse(self._batiment_groupe.parcelle)

    @cached_property
    def siren_complet(self) -> AsyncSirenCompletResourceWithRawResponse:
        return AsyncSirenCompletResourceWithRawResponse(self._batiment_groupe.siren_complet)

    @cached_property
    def siret_complet(self) -> AsyncSiretCompletResourceWithRawResponse:
        return AsyncSiretCompletResourceWithRawResponse(self._batiment_groupe.siret_complet)

    @cached_property
    def rnc(self) -> AsyncRncResourceWithRawResponse:
        return AsyncRncResourceWithRawResponse(self._batiment_groupe.rnc)

    @cached_property
    def proprietaire_siren_open(self) -> AsyncProprietaireSirenOpenResourceWithRawResponse:
        return AsyncProprietaireSirenOpenResourceWithRawResponse(self._batiment_groupe.proprietaire_siren_open)


class BatimentGroupeResourceWithStreamingResponse:
    def __init__(self, batiment_groupe: BatimentGroupeResource) -> None:
        self._batiment_groupe = batiment_groupe

    @cached_property
    def proprietaire_siren(self) -> ProprietaireSirenResourceWithStreamingResponse:
        return ProprietaireSirenResourceWithStreamingResponse(self._batiment_groupe.proprietaire_siren)

    @cached_property
    def qpv(self) -> QpvResourceWithStreamingResponse:
        return QpvResourceWithStreamingResponse(self._batiment_groupe.qpv)

    @cached_property
    def adresse(self) -> AdresseResourceWithStreamingResponse:
        return AdresseResourceWithStreamingResponse(self._batiment_groupe.adresse)

    @cached_property
    def merimee(self) -> MerimeeResourceWithStreamingResponse:
        return MerimeeResourceWithStreamingResponse(self._batiment_groupe.merimee)

    @cached_property
    def parcelle(self) -> ParcelleResourceWithStreamingResponse:
        return ParcelleResourceWithStreamingResponse(self._batiment_groupe.parcelle)

    @cached_property
    def siren_complet(self) -> SirenCompletResourceWithStreamingResponse:
        return SirenCompletResourceWithStreamingResponse(self._batiment_groupe.siren_complet)

    @cached_property
    def siret_complet(self) -> SiretCompletResourceWithStreamingResponse:
        return SiretCompletResourceWithStreamingResponse(self._batiment_groupe.siret_complet)

    @cached_property
    def rnc(self) -> RncResourceWithStreamingResponse:
        return RncResourceWithStreamingResponse(self._batiment_groupe.rnc)

    @cached_property
    def proprietaire_siren_open(self) -> ProprietaireSirenOpenResourceWithStreamingResponse:
        return ProprietaireSirenOpenResourceWithStreamingResponse(self._batiment_groupe.proprietaire_siren_open)


class AsyncBatimentGroupeResourceWithStreamingResponse:
    def __init__(self, batiment_groupe: AsyncBatimentGroupeResource) -> None:
        self._batiment_groupe = batiment_groupe

    @cached_property
    def proprietaire_siren(self) -> AsyncProprietaireSirenResourceWithStreamingResponse:
        return AsyncProprietaireSirenResourceWithStreamingResponse(self._batiment_groupe.proprietaire_siren)

    @cached_property
    def qpv(self) -> AsyncQpvResourceWithStreamingResponse:
        return AsyncQpvResourceWithStreamingResponse(self._batiment_groupe.qpv)

    @cached_property
    def adresse(self) -> AsyncAdresseResourceWithStreamingResponse:
        return AsyncAdresseResourceWithStreamingResponse(self._batiment_groupe.adresse)

    @cached_property
    def merimee(self) -> AsyncMerimeeResourceWithStreamingResponse:
        return AsyncMerimeeResourceWithStreamingResponse(self._batiment_groupe.merimee)

    @cached_property
    def parcelle(self) -> AsyncParcelleResourceWithStreamingResponse:
        return AsyncParcelleResourceWithStreamingResponse(self._batiment_groupe.parcelle)

    @cached_property
    def siren_complet(self) -> AsyncSirenCompletResourceWithStreamingResponse:
        return AsyncSirenCompletResourceWithStreamingResponse(self._batiment_groupe.siren_complet)

    @cached_property
    def siret_complet(self) -> AsyncSiretCompletResourceWithStreamingResponse:
        return AsyncSiretCompletResourceWithStreamingResponse(self._batiment_groupe.siret_complet)

    @cached_property
    def rnc(self) -> AsyncRncResourceWithStreamingResponse:
        return AsyncRncResourceWithStreamingResponse(self._batiment_groupe.rnc)

    @cached_property
    def proprietaire_siren_open(self) -> AsyncProprietaireSirenOpenResourceWithStreamingResponse:
        return AsyncProprietaireSirenOpenResourceWithStreamingResponse(self._batiment_groupe.proprietaire_siren_open)
