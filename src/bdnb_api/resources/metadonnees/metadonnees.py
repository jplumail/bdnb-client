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
from .fournisseur import (
    FournisseurResource,
    AsyncFournisseurResource,
    FournisseurResourceWithRawResponse,
    AsyncFournisseurResourceWithRawResponse,
    FournisseurResourceWithStreamingResponse,
    AsyncFournisseurResourceWithStreamingResponse,
)
from .jeu_de_donnees import (
    JeuDeDonneesResource,
    AsyncJeuDeDonneesResource,
    JeuDeDonneesResourceWithRawResponse,
    AsyncJeuDeDonneesResourceWithRawResponse,
    JeuDeDonneesResourceWithStreamingResponse,
    AsyncJeuDeDonneesResourceWithStreamingResponse,
)
from .contrainte_acces import (
    ContrainteAccesResource,
    AsyncContrainteAccesResource,
    ContrainteAccesResourceWithRawResponse,
    AsyncContrainteAccesResourceWithRawResponse,
    ContrainteAccesResourceWithStreamingResponse,
    AsyncContrainteAccesResourceWithStreamingResponse,
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
    def info(self) -> InfoResource:
        return InfoResource(self._client)

    @cached_property
    def table(self) -> TableResource:
        return TableResource(self._client)

    @cached_property
    def rel_colonne_jeu_de_donnees(self) -> RelColonneJeuDeDonneesResource:
        return RelColonneJeuDeDonneesResource(self._client)

    @cached_property
    def jeu_de_donnees(self) -> JeuDeDonneesResource:
        return JeuDeDonneesResource(self._client)

    @cached_property
    def fournisseur(self) -> FournisseurResource:
        return FournisseurResource(self._client)

    @cached_property
    def contrainte_acces(self) -> ContrainteAccesResource:
        return ContrainteAccesResource(self._client)

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
    def info(self) -> AsyncInfoResource:
        return AsyncInfoResource(self._client)

    @cached_property
    def table(self) -> AsyncTableResource:
        return AsyncTableResource(self._client)

    @cached_property
    def rel_colonne_jeu_de_donnees(self) -> AsyncRelColonneJeuDeDonneesResource:
        return AsyncRelColonneJeuDeDonneesResource(self._client)

    @cached_property
    def jeu_de_donnees(self) -> AsyncJeuDeDonneesResource:
        return AsyncJeuDeDonneesResource(self._client)

    @cached_property
    def fournisseur(self) -> AsyncFournisseurResource:
        return AsyncFournisseurResource(self._client)

    @cached_property
    def contrainte_acces(self) -> AsyncContrainteAccesResource:
        return AsyncContrainteAccesResource(self._client)

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
    def info(self) -> InfoResourceWithRawResponse:
        return InfoResourceWithRawResponse(self._metadonnees.info)

    @cached_property
    def table(self) -> TableResourceWithRawResponse:
        return TableResourceWithRawResponse(self._metadonnees.table)

    @cached_property
    def rel_colonne_jeu_de_donnees(self) -> RelColonneJeuDeDonneesResourceWithRawResponse:
        return RelColonneJeuDeDonneesResourceWithRawResponse(self._metadonnees.rel_colonne_jeu_de_donnees)

    @cached_property
    def jeu_de_donnees(self) -> JeuDeDonneesResourceWithRawResponse:
        return JeuDeDonneesResourceWithRawResponse(self._metadonnees.jeu_de_donnees)

    @cached_property
    def fournisseur(self) -> FournisseurResourceWithRawResponse:
        return FournisseurResourceWithRawResponse(self._metadonnees.fournisseur)

    @cached_property
    def contrainte_acces(self) -> ContrainteAccesResourceWithRawResponse:
        return ContrainteAccesResourceWithRawResponse(self._metadonnees.contrainte_acces)


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
    def info(self) -> AsyncInfoResourceWithRawResponse:
        return AsyncInfoResourceWithRawResponse(self._metadonnees.info)

    @cached_property
    def table(self) -> AsyncTableResourceWithRawResponse:
        return AsyncTableResourceWithRawResponse(self._metadonnees.table)

    @cached_property
    def rel_colonne_jeu_de_donnees(self) -> AsyncRelColonneJeuDeDonneesResourceWithRawResponse:
        return AsyncRelColonneJeuDeDonneesResourceWithRawResponse(self._metadonnees.rel_colonne_jeu_de_donnees)

    @cached_property
    def jeu_de_donnees(self) -> AsyncJeuDeDonneesResourceWithRawResponse:
        return AsyncJeuDeDonneesResourceWithRawResponse(self._metadonnees.jeu_de_donnees)

    @cached_property
    def fournisseur(self) -> AsyncFournisseurResourceWithRawResponse:
        return AsyncFournisseurResourceWithRawResponse(self._metadonnees.fournisseur)

    @cached_property
    def contrainte_acces(self) -> AsyncContrainteAccesResourceWithRawResponse:
        return AsyncContrainteAccesResourceWithRawResponse(self._metadonnees.contrainte_acces)


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
    def info(self) -> InfoResourceWithStreamingResponse:
        return InfoResourceWithStreamingResponse(self._metadonnees.info)

    @cached_property
    def table(self) -> TableResourceWithStreamingResponse:
        return TableResourceWithStreamingResponse(self._metadonnees.table)

    @cached_property
    def rel_colonne_jeu_de_donnees(self) -> RelColonneJeuDeDonneesResourceWithStreamingResponse:
        return RelColonneJeuDeDonneesResourceWithStreamingResponse(self._metadonnees.rel_colonne_jeu_de_donnees)

    @cached_property
    def jeu_de_donnees(self) -> JeuDeDonneesResourceWithStreamingResponse:
        return JeuDeDonneesResourceWithStreamingResponse(self._metadonnees.jeu_de_donnees)

    @cached_property
    def fournisseur(self) -> FournisseurResourceWithStreamingResponse:
        return FournisseurResourceWithStreamingResponse(self._metadonnees.fournisseur)

    @cached_property
    def contrainte_acces(self) -> ContrainteAccesResourceWithStreamingResponse:
        return ContrainteAccesResourceWithStreamingResponse(self._metadonnees.contrainte_acces)


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
    def info(self) -> AsyncInfoResourceWithStreamingResponse:
        return AsyncInfoResourceWithStreamingResponse(self._metadonnees.info)

    @cached_property
    def table(self) -> AsyncTableResourceWithStreamingResponse:
        return AsyncTableResourceWithStreamingResponse(self._metadonnees.table)

    @cached_property
    def rel_colonne_jeu_de_donnees(self) -> AsyncRelColonneJeuDeDonneesResourceWithStreamingResponse:
        return AsyncRelColonneJeuDeDonneesResourceWithStreamingResponse(self._metadonnees.rel_colonne_jeu_de_donnees)

    @cached_property
    def jeu_de_donnees(self) -> AsyncJeuDeDonneesResourceWithStreamingResponse:
        return AsyncJeuDeDonneesResourceWithStreamingResponse(self._metadonnees.jeu_de_donnees)

    @cached_property
    def fournisseur(self) -> AsyncFournisseurResourceWithStreamingResponse:
        return AsyncFournisseurResourceWithStreamingResponse(self._metadonnees.fournisseur)

    @cached_property
    def contrainte_acces(self) -> AsyncContrainteAccesResourceWithStreamingResponse:
        return AsyncContrainteAccesResourceWithStreamingResponse(self._metadonnees.contrainte_acces)
