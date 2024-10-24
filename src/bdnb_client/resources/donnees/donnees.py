# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .ancqpv import (
    AncqpvResource,
    AsyncAncqpvResource,
    AncqpvResourceWithRawResponse,
    AsyncAncqpvResourceWithRawResponse,
    AncqpvResourceWithStreamingResponse,
    AsyncAncqpvResourceWithStreamingResponse,
)
from .adresse import (
    AdresseResource,
    AsyncAdresseResource,
    AdresseResourceWithRawResponse,
    AsyncAdresseResourceWithRawResponse,
    AdresseResourceWithStreamingResponse,
    AsyncAdresseResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .relations import (
    RelationsResource,
    AsyncRelationsResource,
    RelationsResourceWithRawResponse,
    AsyncRelationsResourceWithRawResponse,
    RelationsResourceWithStreamingResponse,
    AsyncRelationsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .proprietaire import (
    ProprietaireResource,
    AsyncProprietaireResource,
    ProprietaireResourceWithRawResponse,
    AsyncProprietaireResourceWithRawResponse,
    ProprietaireResourceWithStreamingResponse,
    AsyncProprietaireResourceWithStreamingResponse,
)
from .batiment_groupe import (
    BatimentGroupeResource,
    AsyncBatimentGroupeResource,
    BatimentGroupeResourceWithRawResponse,
    AsyncBatimentGroupeResourceWithRawResponse,
    BatimentGroupeResourceWithStreamingResponse,
    AsyncBatimentGroupeResourceWithStreamingResponse,
)
from .relations.relations import RelationsResource, AsyncRelationsResource
from .batiment_construction import (
    BatimentConstructionResource,
    AsyncBatimentConstructionResource,
    BatimentConstructionResourceWithRawResponse,
    AsyncBatimentConstructionResourceWithRawResponse,
    BatimentConstructionResourceWithStreamingResponse,
    AsyncBatimentConstructionResourceWithStreamingResponse,
)
from .referentiel_administratif import (
    ReferentielAdministratifResource,
    AsyncReferentielAdministratifResource,
    ReferentielAdministratifResourceWithRawResponse,
    AsyncReferentielAdministratifResourceWithRawResponse,
    ReferentielAdministratifResourceWithStreamingResponse,
    AsyncReferentielAdministratifResourceWithStreamingResponse,
)
from .batiment_groupe.batiment_groupe import BatimentGroupeResource, AsyncBatimentGroupeResource
from .referentiel_administratif.referentiel_administratif import (
    ReferentielAdministratifResource,
    AsyncReferentielAdministratifResource,
)

__all__ = ["DonneesResource", "AsyncDonneesResource"]


class DonneesResource(SyncAPIResource):
    @cached_property
    def batiment_groupe(self) -> BatimentGroupeResource:
        return BatimentGroupeResource(self._client)

    @cached_property
    def ancqpv(self) -> AncqpvResource:
        return AncqpvResource(self._client)

    @cached_property
    def proprietaire(self) -> ProprietaireResource:
        return ProprietaireResource(self._client)

    @cached_property
    def batiment_construction(self) -> BatimentConstructionResource:
        return BatimentConstructionResource(self._client)

    @cached_property
    def adresse(self) -> AdresseResource:
        return AdresseResource(self._client)

    @cached_property
    def referentiel_administratif(self) -> ReferentielAdministratifResource:
        return ReferentielAdministratifResource(self._client)

    @cached_property
    def relations(self) -> RelationsResource:
        return RelationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DonneesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return DonneesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DonneesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return DonneesResourceWithStreamingResponse(self)


class AsyncDonneesResource(AsyncAPIResource):
    @cached_property
    def batiment_groupe(self) -> AsyncBatimentGroupeResource:
        return AsyncBatimentGroupeResource(self._client)

    @cached_property
    def ancqpv(self) -> AsyncAncqpvResource:
        return AsyncAncqpvResource(self._client)

    @cached_property
    def proprietaire(self) -> AsyncProprietaireResource:
        return AsyncProprietaireResource(self._client)

    @cached_property
    def batiment_construction(self) -> AsyncBatimentConstructionResource:
        return AsyncBatimentConstructionResource(self._client)

    @cached_property
    def adresse(self) -> AsyncAdresseResource:
        return AsyncAdresseResource(self._client)

    @cached_property
    def referentiel_administratif(self) -> AsyncReferentielAdministratifResource:
        return AsyncReferentielAdministratifResource(self._client)

    @cached_property
    def relations(self) -> AsyncRelationsResource:
        return AsyncRelationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDonneesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncDonneesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDonneesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncDonneesResourceWithStreamingResponse(self)


class DonneesResourceWithRawResponse:
    def __init__(self, donnees: DonneesResource) -> None:
        self._donnees = donnees

    @cached_property
    def batiment_groupe(self) -> BatimentGroupeResourceWithRawResponse:
        return BatimentGroupeResourceWithRawResponse(self._donnees.batiment_groupe)

    @cached_property
    def ancqpv(self) -> AncqpvResourceWithRawResponse:
        return AncqpvResourceWithRawResponse(self._donnees.ancqpv)

    @cached_property
    def proprietaire(self) -> ProprietaireResourceWithRawResponse:
        return ProprietaireResourceWithRawResponse(self._donnees.proprietaire)

    @cached_property
    def batiment_construction(self) -> BatimentConstructionResourceWithRawResponse:
        return BatimentConstructionResourceWithRawResponse(self._donnees.batiment_construction)

    @cached_property
    def adresse(self) -> AdresseResourceWithRawResponse:
        return AdresseResourceWithRawResponse(self._donnees.adresse)

    @cached_property
    def referentiel_administratif(self) -> ReferentielAdministratifResourceWithRawResponse:
        return ReferentielAdministratifResourceWithRawResponse(self._donnees.referentiel_administratif)

    @cached_property
    def relations(self) -> RelationsResourceWithRawResponse:
        return RelationsResourceWithRawResponse(self._donnees.relations)


class AsyncDonneesResourceWithRawResponse:
    def __init__(self, donnees: AsyncDonneesResource) -> None:
        self._donnees = donnees

    @cached_property
    def batiment_groupe(self) -> AsyncBatimentGroupeResourceWithRawResponse:
        return AsyncBatimentGroupeResourceWithRawResponse(self._donnees.batiment_groupe)

    @cached_property
    def ancqpv(self) -> AsyncAncqpvResourceWithRawResponse:
        return AsyncAncqpvResourceWithRawResponse(self._donnees.ancqpv)

    @cached_property
    def proprietaire(self) -> AsyncProprietaireResourceWithRawResponse:
        return AsyncProprietaireResourceWithRawResponse(self._donnees.proprietaire)

    @cached_property
    def batiment_construction(self) -> AsyncBatimentConstructionResourceWithRawResponse:
        return AsyncBatimentConstructionResourceWithRawResponse(self._donnees.batiment_construction)

    @cached_property
    def adresse(self) -> AsyncAdresseResourceWithRawResponse:
        return AsyncAdresseResourceWithRawResponse(self._donnees.adresse)

    @cached_property
    def referentiel_administratif(self) -> AsyncReferentielAdministratifResourceWithRawResponse:
        return AsyncReferentielAdministratifResourceWithRawResponse(self._donnees.referentiel_administratif)

    @cached_property
    def relations(self) -> AsyncRelationsResourceWithRawResponse:
        return AsyncRelationsResourceWithRawResponse(self._donnees.relations)


class DonneesResourceWithStreamingResponse:
    def __init__(self, donnees: DonneesResource) -> None:
        self._donnees = donnees

    @cached_property
    def batiment_groupe(self) -> BatimentGroupeResourceWithStreamingResponse:
        return BatimentGroupeResourceWithStreamingResponse(self._donnees.batiment_groupe)

    @cached_property
    def ancqpv(self) -> AncqpvResourceWithStreamingResponse:
        return AncqpvResourceWithStreamingResponse(self._donnees.ancqpv)

    @cached_property
    def proprietaire(self) -> ProprietaireResourceWithStreamingResponse:
        return ProprietaireResourceWithStreamingResponse(self._donnees.proprietaire)

    @cached_property
    def batiment_construction(self) -> BatimentConstructionResourceWithStreamingResponse:
        return BatimentConstructionResourceWithStreamingResponse(self._donnees.batiment_construction)

    @cached_property
    def adresse(self) -> AdresseResourceWithStreamingResponse:
        return AdresseResourceWithStreamingResponse(self._donnees.adresse)

    @cached_property
    def referentiel_administratif(self) -> ReferentielAdministratifResourceWithStreamingResponse:
        return ReferentielAdministratifResourceWithStreamingResponse(self._donnees.referentiel_administratif)

    @cached_property
    def relations(self) -> RelationsResourceWithStreamingResponse:
        return RelationsResourceWithStreamingResponse(self._donnees.relations)


class AsyncDonneesResourceWithStreamingResponse:
    def __init__(self, donnees: AsyncDonneesResource) -> None:
        self._donnees = donnees

    @cached_property
    def batiment_groupe(self) -> AsyncBatimentGroupeResourceWithStreamingResponse:
        return AsyncBatimentGroupeResourceWithStreamingResponse(self._donnees.batiment_groupe)

    @cached_property
    def ancqpv(self) -> AsyncAncqpvResourceWithStreamingResponse:
        return AsyncAncqpvResourceWithStreamingResponse(self._donnees.ancqpv)

    @cached_property
    def proprietaire(self) -> AsyncProprietaireResourceWithStreamingResponse:
        return AsyncProprietaireResourceWithStreamingResponse(self._donnees.proprietaire)

    @cached_property
    def batiment_construction(self) -> AsyncBatimentConstructionResourceWithStreamingResponse:
        return AsyncBatimentConstructionResourceWithStreamingResponse(self._donnees.batiment_construction)

    @cached_property
    def adresse(self) -> AsyncAdresseResourceWithStreamingResponse:
        return AsyncAdresseResourceWithStreamingResponse(self._donnees.adresse)

    @cached_property
    def referentiel_administratif(self) -> AsyncReferentielAdministratifResourceWithStreamingResponse:
        return AsyncReferentielAdministratifResourceWithStreamingResponse(self._donnees.referentiel_administratif)

    @cached_property
    def relations(self) -> AsyncRelationsResourceWithStreamingResponse:
        return AsyncRelationsResourceWithStreamingResponse(self._donnees.relations)
