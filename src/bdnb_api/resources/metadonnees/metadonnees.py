# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .colonnes import (
    ColonnesResource,
    AsyncColonnesResource,
    ColonnesResourceWithRawResponse,
    AsyncColonnesResourceWithRawResponse,
    ColonnesResourceWithStreamingResponse,
    AsyncColonnesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .jeu_de_donnees import (
    JeuDeDonneesResource,
    AsyncJeuDeDonneesResource,
    JeuDeDonneesResourceWithRawResponse,
    AsyncJeuDeDonneesResourceWithRawResponse,
    JeuDeDonneesResourceWithStreamingResponse,
    AsyncJeuDeDonneesResourceWithStreamingResponse,
)
from .metadonnees_complets import (
    MetadonneesCompletsResource,
    AsyncMetadonneesCompletsResource,
    MetadonneesCompletsResourceWithRawResponse,
    AsyncMetadonneesCompletsResourceWithRawResponse,
    MetadonneesCompletsResourceWithStreamingResponse,
    AsyncMetadonneesCompletsResourceWithStreamingResponse,
)
from .colonnes_souscription import (
    ColonnesSouscriptionResource,
    AsyncColonnesSouscriptionResource,
    ColonnesSouscriptionResourceWithRawResponse,
    AsyncColonnesSouscriptionResourceWithRawResponse,
    ColonnesSouscriptionResourceWithStreamingResponse,
    AsyncColonnesSouscriptionResourceWithStreamingResponse,
)
from .rel_colonne_jeu_de_donnees import (
    RelColonneJeuDeDonneesResource,
    AsyncRelColonneJeuDeDonneesResource,
    RelColonneJeuDeDonneesResourceWithRawResponse,
    AsyncRelColonneJeuDeDonneesResourceWithRawResponse,
    RelColonneJeuDeDonneesResourceWithStreamingResponse,
    AsyncRelColonneJeuDeDonneesResourceWithStreamingResponse,
)

__all__ = ["MetadonneesResource", "AsyncMetadonneesResource"]


class MetadonneesResource(SyncAPIResource):
    @cached_property
    def colonnes_souscription(self) -> ColonnesSouscriptionResource:
        return ColonnesSouscriptionResource(self._client)

    @cached_property
    def colonnes(self) -> ColonnesResource:
        return ColonnesResource(self._client)

    @cached_property
    def metadonnees_complets(self) -> MetadonneesCompletsResource:
        return MetadonneesCompletsResource(self._client)

    @cached_property
    def rel_colonne_jeu_de_donnees(self) -> RelColonneJeuDeDonneesResource:
        return RelColonneJeuDeDonneesResource(self._client)

    @cached_property
    def jeu_de_donnees(self) -> JeuDeDonneesResource:
        return JeuDeDonneesResource(self._client)

    @cached_property
    def with_raw_response(self) -> MetadonneesResourceWithRawResponse:
        return MetadonneesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetadonneesResourceWithStreamingResponse:
        return MetadonneesResourceWithStreamingResponse(self)


class AsyncMetadonneesResource(AsyncAPIResource):
    @cached_property
    def colonnes_souscription(self) -> AsyncColonnesSouscriptionResource:
        return AsyncColonnesSouscriptionResource(self._client)

    @cached_property
    def colonnes(self) -> AsyncColonnesResource:
        return AsyncColonnesResource(self._client)

    @cached_property
    def metadonnees_complets(self) -> AsyncMetadonneesCompletsResource:
        return AsyncMetadonneesCompletsResource(self._client)

    @cached_property
    def rel_colonne_jeu_de_donnees(self) -> AsyncRelColonneJeuDeDonneesResource:
        return AsyncRelColonneJeuDeDonneesResource(self._client)

    @cached_property
    def jeu_de_donnees(self) -> AsyncJeuDeDonneesResource:
        return AsyncJeuDeDonneesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMetadonneesResourceWithRawResponse:
        return AsyncMetadonneesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetadonneesResourceWithStreamingResponse:
        return AsyncMetadonneesResourceWithStreamingResponse(self)


class MetadonneesResourceWithRawResponse:
    def __init__(self, metadonnees: MetadonneesResource) -> None:
        self._metadonnees = metadonnees

    @cached_property
    def colonnes_souscription(self) -> ColonnesSouscriptionResourceWithRawResponse:
        return ColonnesSouscriptionResourceWithRawResponse(self._metadonnees.colonnes_souscription)

    @cached_property
    def colonnes(self) -> ColonnesResourceWithRawResponse:
        return ColonnesResourceWithRawResponse(self._metadonnees.colonnes)

    @cached_property
    def metadonnees_complets(self) -> MetadonneesCompletsResourceWithRawResponse:
        return MetadonneesCompletsResourceWithRawResponse(self._metadonnees.metadonnees_complets)

    @cached_property
    def rel_colonne_jeu_de_donnees(self) -> RelColonneJeuDeDonneesResourceWithRawResponse:
        return RelColonneJeuDeDonneesResourceWithRawResponse(self._metadonnees.rel_colonne_jeu_de_donnees)

    @cached_property
    def jeu_de_donnees(self) -> JeuDeDonneesResourceWithRawResponse:
        return JeuDeDonneesResourceWithRawResponse(self._metadonnees.jeu_de_donnees)


class AsyncMetadonneesResourceWithRawResponse:
    def __init__(self, metadonnees: AsyncMetadonneesResource) -> None:
        self._metadonnees = metadonnees

    @cached_property
    def colonnes_souscription(self) -> AsyncColonnesSouscriptionResourceWithRawResponse:
        return AsyncColonnesSouscriptionResourceWithRawResponse(self._metadonnees.colonnes_souscription)

    @cached_property
    def colonnes(self) -> AsyncColonnesResourceWithRawResponse:
        return AsyncColonnesResourceWithRawResponse(self._metadonnees.colonnes)

    @cached_property
    def metadonnees_complets(self) -> AsyncMetadonneesCompletsResourceWithRawResponse:
        return AsyncMetadonneesCompletsResourceWithRawResponse(self._metadonnees.metadonnees_complets)

    @cached_property
    def rel_colonne_jeu_de_donnees(self) -> AsyncRelColonneJeuDeDonneesResourceWithRawResponse:
        return AsyncRelColonneJeuDeDonneesResourceWithRawResponse(self._metadonnees.rel_colonne_jeu_de_donnees)

    @cached_property
    def jeu_de_donnees(self) -> AsyncJeuDeDonneesResourceWithRawResponse:
        return AsyncJeuDeDonneesResourceWithRawResponse(self._metadonnees.jeu_de_donnees)


class MetadonneesResourceWithStreamingResponse:
    def __init__(self, metadonnees: MetadonneesResource) -> None:
        self._metadonnees = metadonnees

    @cached_property
    def colonnes_souscription(self) -> ColonnesSouscriptionResourceWithStreamingResponse:
        return ColonnesSouscriptionResourceWithStreamingResponse(self._metadonnees.colonnes_souscription)

    @cached_property
    def colonnes(self) -> ColonnesResourceWithStreamingResponse:
        return ColonnesResourceWithStreamingResponse(self._metadonnees.colonnes)

    @cached_property
    def metadonnees_complets(self) -> MetadonneesCompletsResourceWithStreamingResponse:
        return MetadonneesCompletsResourceWithStreamingResponse(self._metadonnees.metadonnees_complets)

    @cached_property
    def rel_colonne_jeu_de_donnees(self) -> RelColonneJeuDeDonneesResourceWithStreamingResponse:
        return RelColonneJeuDeDonneesResourceWithStreamingResponse(self._metadonnees.rel_colonne_jeu_de_donnees)

    @cached_property
    def jeu_de_donnees(self) -> JeuDeDonneesResourceWithStreamingResponse:
        return JeuDeDonneesResourceWithStreamingResponse(self._metadonnees.jeu_de_donnees)


class AsyncMetadonneesResourceWithStreamingResponse:
    def __init__(self, metadonnees: AsyncMetadonneesResource) -> None:
        self._metadonnees = metadonnees

    @cached_property
    def colonnes_souscription(self) -> AsyncColonnesSouscriptionResourceWithStreamingResponse:
        return AsyncColonnesSouscriptionResourceWithStreamingResponse(self._metadonnees.colonnes_souscription)

    @cached_property
    def colonnes(self) -> AsyncColonnesResourceWithStreamingResponse:
        return AsyncColonnesResourceWithStreamingResponse(self._metadonnees.colonnes)

    @cached_property
    def metadonnees_complets(self) -> AsyncMetadonneesCompletsResourceWithStreamingResponse:
        return AsyncMetadonneesCompletsResourceWithStreamingResponse(self._metadonnees.metadonnees_complets)

    @cached_property
    def rel_colonne_jeu_de_donnees(self) -> AsyncRelColonneJeuDeDonneesResourceWithStreamingResponse:
        return AsyncRelColonneJeuDeDonneesResourceWithStreamingResponse(self._metadonnees.rel_colonne_jeu_de_donnees)

    @cached_property
    def jeu_de_donnees(self) -> AsyncJeuDeDonneesResourceWithStreamingResponse:
        return AsyncJeuDeDonneesResourceWithStreamingResponse(self._metadonnees.jeu_de_donnees)
