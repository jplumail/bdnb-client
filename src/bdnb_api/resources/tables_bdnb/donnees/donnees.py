# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .batiment_groupe_bpe import (
    BatimentGroupeBpeResource,
    AsyncBatimentGroupeBpeResource,
    BatimentGroupeBpeResourceWithRawResponse,
    AsyncBatimentGroupeBpeResourceWithRawResponse,
    BatimentGroupeBpeResourceWithStreamingResponse,
    AsyncBatimentGroupeBpeResourceWithStreamingResponse,
)
from .batiment_groupe_rnc import (
    BatimentGroupeRncResource,
    AsyncBatimentGroupeRncResource,
    BatimentGroupeRncResourceWithRawResponse,
    AsyncBatimentGroupeRncResourceWithRawResponse,
    BatimentGroupeRncResourceWithStreamingResponse,
    AsyncBatimentGroupeRncResourceWithStreamingResponse,
)
from .batiment_groupe_argiles import (
    BatimentGroupeArgilesResource,
    AsyncBatimentGroupeArgilesResource,
    BatimentGroupeArgilesResourceWithRawResponse,
    AsyncBatimentGroupeArgilesResourceWithRawResponse,
    BatimentGroupeArgilesResourceWithStreamingResponse,
    AsyncBatimentGroupeArgilesResourceWithStreamingResponse,
)
from .batiment_groupe_ffo_bat import (
    BatimentGroupeFfoBatResource,
    AsyncBatimentGroupeFfoBatResource,
    BatimentGroupeFfoBatResourceWithRawResponse,
    AsyncBatimentGroupeFfoBatResourceWithRawResponse,
    BatimentGroupeFfoBatResourceWithStreamingResponse,
    AsyncBatimentGroupeFfoBatResourceWithStreamingResponse,
)
from .rel_batiment_groupe_rnc import (
    RelBatimentGroupeRncResource,
    AsyncRelBatimentGroupeRncResource,
    RelBatimentGroupeRncResourceWithRawResponse,
    AsyncRelBatimentGroupeRncResourceWithRawResponse,
    RelBatimentGroupeRncResourceWithStreamingResponse,
    AsyncRelBatimentGroupeRncResourceWithStreamingResponse,
)
from .iris_contexte_geographique import (
    IrisContexteGeographiqueResource,
    AsyncIrisContexteGeographiqueResource,
    IrisContexteGeographiqueResourceWithRawResponse,
    AsyncIrisContexteGeographiqueResourceWithRawResponse,
    IrisContexteGeographiqueResourceWithStreamingResponse,
    AsyncIrisContexteGeographiqueResourceWithStreamingResponse,
)
from .iris_simulations_valeur_verte import (
    IrisSimulationsValeurVerteResource,
    AsyncIrisSimulationsValeurVerteResource,
    IrisSimulationsValeurVerteResourceWithRawResponse,
    AsyncIrisSimulationsValeurVerteResourceWithRawResponse,
    IrisSimulationsValeurVerteResourceWithStreamingResponse,
    AsyncIrisSimulationsValeurVerteResourceWithStreamingResponse,
)
from .rel_batiment_groupe_siren_complet import (
    RelBatimentGroupeSirenCompletResource,
    AsyncRelBatimentGroupeSirenCompletResource,
    RelBatimentGroupeSirenCompletResourceWithRawResponse,
    AsyncRelBatimentGroupeSirenCompletResourceWithRawResponse,
    RelBatimentGroupeSirenCompletResourceWithStreamingResponse,
    AsyncRelBatimentGroupeSirenCompletResourceWithStreamingResponse,
)
from .rel_batiment_groupe_siret_complet import (
    RelBatimentGroupeSiretCompletResource,
    AsyncRelBatimentGroupeSiretCompletResource,
    RelBatimentGroupeSiretCompletResourceWithRawResponse,
    AsyncRelBatimentGroupeSiretCompletResourceWithRawResponse,
    RelBatimentGroupeSiretCompletResourceWithStreamingResponse,
    AsyncRelBatimentGroupeSiretCompletResourceWithStreamingResponse,
)
from .batiment_groupe_dle_reseaux_multimillesime import (
    BatimentGroupeDleReseauxMultimillesimeResource,
    AsyncBatimentGroupeDleReseauxMultimillesimeResource,
    BatimentGroupeDleReseauxMultimillesimeResourceWithRawResponse,
    AsyncBatimentGroupeDleReseauxMultimillesimeResourceWithRawResponse,
    BatimentGroupeDleReseauxMultimillesimeResourceWithStreamingResponse,
    AsyncBatimentGroupeDleReseauxMultimillesimeResourceWithStreamingResponse,
)

__all__ = ["DonneesResource", "AsyncDonneesResource"]


class DonneesResource(SyncAPIResource):
    @cached_property
    def iris_simulations_valeur_verte(self) -> IrisSimulationsValeurVerteResource:
        return IrisSimulationsValeurVerteResource(self._client)

    @cached_property
    def iris_contexte_geographique(self) -> IrisContexteGeographiqueResource:
        return IrisContexteGeographiqueResource(self._client)

    @cached_property
    def rel_batiment_groupe_siren_complet(self) -> RelBatimentGroupeSirenCompletResource:
        return RelBatimentGroupeSirenCompletResource(self._client)

    @cached_property
    def rel_batiment_groupe_siret_complet(self) -> RelBatimentGroupeSiretCompletResource:
        return RelBatimentGroupeSiretCompletResource(self._client)

    @cached_property
    def batiment_groupe_dle_reseaux_multimillesime(self) -> BatimentGroupeDleReseauxMultimillesimeResource:
        return BatimentGroupeDleReseauxMultimillesimeResource(self._client)

    @cached_property
    def batiment_groupe_rnc(self) -> BatimentGroupeRncResource:
        return BatimentGroupeRncResource(self._client)

    @cached_property
    def batiment_groupe_bpe(self) -> BatimentGroupeBpeResource:
        return BatimentGroupeBpeResource(self._client)

    @cached_property
    def batiment_groupe_ffo_bat(self) -> BatimentGroupeFfoBatResource:
        return BatimentGroupeFfoBatResource(self._client)

    @cached_property
    def rel_batiment_groupe_rnc(self) -> RelBatimentGroupeRncResource:
        return RelBatimentGroupeRncResource(self._client)

    @cached_property
    def batiment_groupe_argiles(self) -> BatimentGroupeArgilesResource:
        return BatimentGroupeArgilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DonneesResourceWithRawResponse:
        return DonneesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DonneesResourceWithStreamingResponse:
        return DonneesResourceWithStreamingResponse(self)


class AsyncDonneesResource(AsyncAPIResource):
    @cached_property
    def iris_simulations_valeur_verte(self) -> AsyncIrisSimulationsValeurVerteResource:
        return AsyncIrisSimulationsValeurVerteResource(self._client)

    @cached_property
    def iris_contexte_geographique(self) -> AsyncIrisContexteGeographiqueResource:
        return AsyncIrisContexteGeographiqueResource(self._client)

    @cached_property
    def rel_batiment_groupe_siren_complet(self) -> AsyncRelBatimentGroupeSirenCompletResource:
        return AsyncRelBatimentGroupeSirenCompletResource(self._client)

    @cached_property
    def rel_batiment_groupe_siret_complet(self) -> AsyncRelBatimentGroupeSiretCompletResource:
        return AsyncRelBatimentGroupeSiretCompletResource(self._client)

    @cached_property
    def batiment_groupe_dle_reseaux_multimillesime(self) -> AsyncBatimentGroupeDleReseauxMultimillesimeResource:
        return AsyncBatimentGroupeDleReseauxMultimillesimeResource(self._client)

    @cached_property
    def batiment_groupe_rnc(self) -> AsyncBatimentGroupeRncResource:
        return AsyncBatimentGroupeRncResource(self._client)

    @cached_property
    def batiment_groupe_bpe(self) -> AsyncBatimentGroupeBpeResource:
        return AsyncBatimentGroupeBpeResource(self._client)

    @cached_property
    def batiment_groupe_ffo_bat(self) -> AsyncBatimentGroupeFfoBatResource:
        return AsyncBatimentGroupeFfoBatResource(self._client)

    @cached_property
    def rel_batiment_groupe_rnc(self) -> AsyncRelBatimentGroupeRncResource:
        return AsyncRelBatimentGroupeRncResource(self._client)

    @cached_property
    def batiment_groupe_argiles(self) -> AsyncBatimentGroupeArgilesResource:
        return AsyncBatimentGroupeArgilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDonneesResourceWithRawResponse:
        return AsyncDonneesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDonneesResourceWithStreamingResponse:
        return AsyncDonneesResourceWithStreamingResponse(self)


class DonneesResourceWithRawResponse:
    def __init__(self, donnees: DonneesResource) -> None:
        self._donnees = donnees

    @cached_property
    def iris_simulations_valeur_verte(self) -> IrisSimulationsValeurVerteResourceWithRawResponse:
        return IrisSimulationsValeurVerteResourceWithRawResponse(self._donnees.iris_simulations_valeur_verte)

    @cached_property
    def iris_contexte_geographique(self) -> IrisContexteGeographiqueResourceWithRawResponse:
        return IrisContexteGeographiqueResourceWithRawResponse(self._donnees.iris_contexte_geographique)

    @cached_property
    def rel_batiment_groupe_siren_complet(self) -> RelBatimentGroupeSirenCompletResourceWithRawResponse:
        return RelBatimentGroupeSirenCompletResourceWithRawResponse(self._donnees.rel_batiment_groupe_siren_complet)

    @cached_property
    def rel_batiment_groupe_siret_complet(self) -> RelBatimentGroupeSiretCompletResourceWithRawResponse:
        return RelBatimentGroupeSiretCompletResourceWithRawResponse(self._donnees.rel_batiment_groupe_siret_complet)

    @cached_property
    def batiment_groupe_dle_reseaux_multimillesime(
        self,
    ) -> BatimentGroupeDleReseauxMultimillesimeResourceWithRawResponse:
        return BatimentGroupeDleReseauxMultimillesimeResourceWithRawResponse(
            self._donnees.batiment_groupe_dle_reseaux_multimillesime
        )

    @cached_property
    def batiment_groupe_rnc(self) -> BatimentGroupeRncResourceWithRawResponse:
        return BatimentGroupeRncResourceWithRawResponse(self._donnees.batiment_groupe_rnc)

    @cached_property
    def batiment_groupe_bpe(self) -> BatimentGroupeBpeResourceWithRawResponse:
        return BatimentGroupeBpeResourceWithRawResponse(self._donnees.batiment_groupe_bpe)

    @cached_property
    def batiment_groupe_ffo_bat(self) -> BatimentGroupeFfoBatResourceWithRawResponse:
        return BatimentGroupeFfoBatResourceWithRawResponse(self._donnees.batiment_groupe_ffo_bat)

    @cached_property
    def rel_batiment_groupe_rnc(self) -> RelBatimentGroupeRncResourceWithRawResponse:
        return RelBatimentGroupeRncResourceWithRawResponse(self._donnees.rel_batiment_groupe_rnc)

    @cached_property
    def batiment_groupe_argiles(self) -> BatimentGroupeArgilesResourceWithRawResponse:
        return BatimentGroupeArgilesResourceWithRawResponse(self._donnees.batiment_groupe_argiles)


class AsyncDonneesResourceWithRawResponse:
    def __init__(self, donnees: AsyncDonneesResource) -> None:
        self._donnees = donnees

    @cached_property
    def iris_simulations_valeur_verte(self) -> AsyncIrisSimulationsValeurVerteResourceWithRawResponse:
        return AsyncIrisSimulationsValeurVerteResourceWithRawResponse(self._donnees.iris_simulations_valeur_verte)

    @cached_property
    def iris_contexte_geographique(self) -> AsyncIrisContexteGeographiqueResourceWithRawResponse:
        return AsyncIrisContexteGeographiqueResourceWithRawResponse(self._donnees.iris_contexte_geographique)

    @cached_property
    def rel_batiment_groupe_siren_complet(self) -> AsyncRelBatimentGroupeSirenCompletResourceWithRawResponse:
        return AsyncRelBatimentGroupeSirenCompletResourceWithRawResponse(
            self._donnees.rel_batiment_groupe_siren_complet
        )

    @cached_property
    def rel_batiment_groupe_siret_complet(self) -> AsyncRelBatimentGroupeSiretCompletResourceWithRawResponse:
        return AsyncRelBatimentGroupeSiretCompletResourceWithRawResponse(
            self._donnees.rel_batiment_groupe_siret_complet
        )

    @cached_property
    def batiment_groupe_dle_reseaux_multimillesime(
        self,
    ) -> AsyncBatimentGroupeDleReseauxMultimillesimeResourceWithRawResponse:
        return AsyncBatimentGroupeDleReseauxMultimillesimeResourceWithRawResponse(
            self._donnees.batiment_groupe_dle_reseaux_multimillesime
        )

    @cached_property
    def batiment_groupe_rnc(self) -> AsyncBatimentGroupeRncResourceWithRawResponse:
        return AsyncBatimentGroupeRncResourceWithRawResponse(self._donnees.batiment_groupe_rnc)

    @cached_property
    def batiment_groupe_bpe(self) -> AsyncBatimentGroupeBpeResourceWithRawResponse:
        return AsyncBatimentGroupeBpeResourceWithRawResponse(self._donnees.batiment_groupe_bpe)

    @cached_property
    def batiment_groupe_ffo_bat(self) -> AsyncBatimentGroupeFfoBatResourceWithRawResponse:
        return AsyncBatimentGroupeFfoBatResourceWithRawResponse(self._donnees.batiment_groupe_ffo_bat)

    @cached_property
    def rel_batiment_groupe_rnc(self) -> AsyncRelBatimentGroupeRncResourceWithRawResponse:
        return AsyncRelBatimentGroupeRncResourceWithRawResponse(self._donnees.rel_batiment_groupe_rnc)

    @cached_property
    def batiment_groupe_argiles(self) -> AsyncBatimentGroupeArgilesResourceWithRawResponse:
        return AsyncBatimentGroupeArgilesResourceWithRawResponse(self._donnees.batiment_groupe_argiles)


class DonneesResourceWithStreamingResponse:
    def __init__(self, donnees: DonneesResource) -> None:
        self._donnees = donnees

    @cached_property
    def iris_simulations_valeur_verte(self) -> IrisSimulationsValeurVerteResourceWithStreamingResponse:
        return IrisSimulationsValeurVerteResourceWithStreamingResponse(self._donnees.iris_simulations_valeur_verte)

    @cached_property
    def iris_contexte_geographique(self) -> IrisContexteGeographiqueResourceWithStreamingResponse:
        return IrisContexteGeographiqueResourceWithStreamingResponse(self._donnees.iris_contexte_geographique)

    @cached_property
    def rel_batiment_groupe_siren_complet(self) -> RelBatimentGroupeSirenCompletResourceWithStreamingResponse:
        return RelBatimentGroupeSirenCompletResourceWithStreamingResponse(
            self._donnees.rel_batiment_groupe_siren_complet
        )

    @cached_property
    def rel_batiment_groupe_siret_complet(self) -> RelBatimentGroupeSiretCompletResourceWithStreamingResponse:
        return RelBatimentGroupeSiretCompletResourceWithStreamingResponse(
            self._donnees.rel_batiment_groupe_siret_complet
        )

    @cached_property
    def batiment_groupe_dle_reseaux_multimillesime(
        self,
    ) -> BatimentGroupeDleReseauxMultimillesimeResourceWithStreamingResponse:
        return BatimentGroupeDleReseauxMultimillesimeResourceWithStreamingResponse(
            self._donnees.batiment_groupe_dle_reseaux_multimillesime
        )

    @cached_property
    def batiment_groupe_rnc(self) -> BatimentGroupeRncResourceWithStreamingResponse:
        return BatimentGroupeRncResourceWithStreamingResponse(self._donnees.batiment_groupe_rnc)

    @cached_property
    def batiment_groupe_bpe(self) -> BatimentGroupeBpeResourceWithStreamingResponse:
        return BatimentGroupeBpeResourceWithStreamingResponse(self._donnees.batiment_groupe_bpe)

    @cached_property
    def batiment_groupe_ffo_bat(self) -> BatimentGroupeFfoBatResourceWithStreamingResponse:
        return BatimentGroupeFfoBatResourceWithStreamingResponse(self._donnees.batiment_groupe_ffo_bat)

    @cached_property
    def rel_batiment_groupe_rnc(self) -> RelBatimentGroupeRncResourceWithStreamingResponse:
        return RelBatimentGroupeRncResourceWithStreamingResponse(self._donnees.rel_batiment_groupe_rnc)

    @cached_property
    def batiment_groupe_argiles(self) -> BatimentGroupeArgilesResourceWithStreamingResponse:
        return BatimentGroupeArgilesResourceWithStreamingResponse(self._donnees.batiment_groupe_argiles)


class AsyncDonneesResourceWithStreamingResponse:
    def __init__(self, donnees: AsyncDonneesResource) -> None:
        self._donnees = donnees

    @cached_property
    def iris_simulations_valeur_verte(self) -> AsyncIrisSimulationsValeurVerteResourceWithStreamingResponse:
        return AsyncIrisSimulationsValeurVerteResourceWithStreamingResponse(self._donnees.iris_simulations_valeur_verte)

    @cached_property
    def iris_contexte_geographique(self) -> AsyncIrisContexteGeographiqueResourceWithStreamingResponse:
        return AsyncIrisContexteGeographiqueResourceWithStreamingResponse(self._donnees.iris_contexte_geographique)

    @cached_property
    def rel_batiment_groupe_siren_complet(self) -> AsyncRelBatimentGroupeSirenCompletResourceWithStreamingResponse:
        return AsyncRelBatimentGroupeSirenCompletResourceWithStreamingResponse(
            self._donnees.rel_batiment_groupe_siren_complet
        )

    @cached_property
    def rel_batiment_groupe_siret_complet(self) -> AsyncRelBatimentGroupeSiretCompletResourceWithStreamingResponse:
        return AsyncRelBatimentGroupeSiretCompletResourceWithStreamingResponse(
            self._donnees.rel_batiment_groupe_siret_complet
        )

    @cached_property
    def batiment_groupe_dle_reseaux_multimillesime(
        self,
    ) -> AsyncBatimentGroupeDleReseauxMultimillesimeResourceWithStreamingResponse:
        return AsyncBatimentGroupeDleReseauxMultimillesimeResourceWithStreamingResponse(
            self._donnees.batiment_groupe_dle_reseaux_multimillesime
        )

    @cached_property
    def batiment_groupe_rnc(self) -> AsyncBatimentGroupeRncResourceWithStreamingResponse:
        return AsyncBatimentGroupeRncResourceWithStreamingResponse(self._donnees.batiment_groupe_rnc)

    @cached_property
    def batiment_groupe_bpe(self) -> AsyncBatimentGroupeBpeResourceWithStreamingResponse:
        return AsyncBatimentGroupeBpeResourceWithStreamingResponse(self._donnees.batiment_groupe_bpe)

    @cached_property
    def batiment_groupe_ffo_bat(self) -> AsyncBatimentGroupeFfoBatResourceWithStreamingResponse:
        return AsyncBatimentGroupeFfoBatResourceWithStreamingResponse(self._donnees.batiment_groupe_ffo_bat)

    @cached_property
    def rel_batiment_groupe_rnc(self) -> AsyncRelBatimentGroupeRncResourceWithStreamingResponse:
        return AsyncRelBatimentGroupeRncResourceWithStreamingResponse(self._donnees.rel_batiment_groupe_rnc)

    @cached_property
    def batiment_groupe_argiles(self) -> AsyncBatimentGroupeArgilesResourceWithStreamingResponse:
        return AsyncBatimentGroupeArgilesResourceWithStreamingResponse(self._donnees.batiment_groupe_argiles)
