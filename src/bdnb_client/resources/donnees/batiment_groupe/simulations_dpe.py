# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, strip_not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncDefault, AsyncDefault
from ...._base_client import AsyncPaginator, make_request_options
from ....types.donnees.batiment_groupe import simulations_dpe_list_params
from ....types.donnees.batiment_groupe.batiment_groupe_simulations_dpe import BatimentGroupeSimulationsDpe

__all__ = ["SimulationsDpeResource", "AsyncSimulationsDpeResource"]


class SimulationsDpeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimulationsDpeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return SimulationsDpeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulationsDpeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return SimulationsDpeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_estim_inc: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_primaire_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_primaire_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_primaire_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_ges_estim_inc: str | NotGiven = NOT_GIVEN,
        etat_initial_ges_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_initial_ges_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_initial_ges_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_initial_risque_canicule: str | NotGiven = NOT_GIVEN,
        etat_initial_risque_canicule_inc: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_estim_inc: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_primaire_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_primaire_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_primaire_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_ges_estim_inc: str | NotGiven = NOT_GIVEN,
        etat_renove_ges_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_renove_ges_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_renove_ges_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_renove_risque_canicule: str | NotGiven = NOT_GIVEN,
        etat_renove_risque_canicule_inc: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_a: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_b: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_c: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_d: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_e: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_error: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_f: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_g: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_inc: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_map: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_map_2nd: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_map_2nd_prob: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_map_prob: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_a: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_b: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_c: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_d: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_e: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_error: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_f: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_g: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_inc: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_map: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_map_2nd: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_map_2nd_prob: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_map_prob: str | NotGiven = NOT_GIVEN,
        gisement_gain_conso_finale_total: str | NotGiven = NOT_GIVEN,
        gisement_gain_energetique_mean: str | NotGiven = NOT_GIVEN,
        gisement_gain_ges_mean: str | NotGiven = NOT_GIVEN,
        indecence_energetique_initial: str | NotGiven = NOT_GIVEN,
        indecence_energetique_renove: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        surface_deperditive: str | NotGiven = NOT_GIVEN,
        surface_deperditive_verticale: str | NotGiven = NOT_GIVEN,
        surface_enveloppe: str | NotGiven = NOT_GIVEN,
        surface_facade_ext: str | NotGiven = NOT_GIVEN,
        surface_facade_mitoyenne: str | NotGiven = NOT_GIVEN,
        surface_facade_totale: str | NotGiven = NOT_GIVEN,
        surface_facade_vitree: str | NotGiven = NOT_GIVEN,
        surface_toiture: str | NotGiven = NOT_GIVEN,
        surface_verticale: str | NotGiven = NOT_GIVEN,
        volume_brut: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[BatimentGroupeSimulationsDpe]:
        """
        Simulations CSTB des étiquettes DPE estimées pour les bâtiments de logement en
        France. Les résultats estimés sont fournis avec des indicateurs qui sont pour la
        plupart des probabilités. Version actuelle 2023-01-20-v073.4

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          etat_initial_consommation_energie_estim_inc: Incertitude des estimations de consommation énergétique finale avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_estim_lower: Estimation basse de la consommation énergétique finale avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_estim_mean: Estimation moyenne de la consommation énergétique finale avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_estim_upper: Estimation haute de la consommation énergétique finale avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_lower: Estimation basse de la consommation énergétique primaire avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_mean: Estimation moyenne de la consommation énergétique primaire avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_upper: Estimation haute de la consommation énergétique primaire avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_ges_estim_inc: Incertitude sur l'estimation de consommation de GES avant rénovation
              [kgeqC02/m2/an]

          etat_initial_ges_estim_lower: Estimation basse de la consommation de GES avant rénovation [kgeqC02/m2/an]

          etat_initial_ges_estim_mean: Estimation moyenne de la consommation de GES avant rénovation [kgeqC02/m2/an]

          etat_initial_ges_estim_upper: Estimation haute de la consommation de GES avant rénovation [kgeqC02/m2/an]

          etat_initial_risque_canicule: Estimation du risque canicule avant rénovation [1-5]

          etat_initial_risque_canicule_inc: Incertitude de l'estimation du risque canicule avant rénovation [1-5]

          etat_renove_consommation_energie_estim_inc: Incertitude sur les estimations des consommations énergétiques finales après un
              scénario de rénovation globale "standard" (isolation des principaux composants
              d'enveloppe et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_estim_lower: Estimation basse de la consommation énergétique finale après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_estim_mean: Estimation moyenne de la consommation énergétique finale après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_estim_upper: Estimation haute de la consommation énergétique finale après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_lower: Estimation basse de la consommation d'énergie primaire après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_mean: Estimation moyenne de la consommation d'énergie primaire après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_upper: Estimation haute de la consommation d'énergie primaire après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_ges_estim_inc: Incertitude sur l'estimation de consommation de GES après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kgeqC02/m2/an]

          etat_renove_ges_estim_lower: Estimation basse des émissions de GES après un scénario de rénovation globale
              "standard" (isolation des principaux composants d'enveloppe et changement de
              système énergétique de chauffage) [kWh/m2/an]

          etat_renove_ges_estim_mean: Estimation moyenne des émissions de GES après un scénario de rénovation globale
              "standard" (isolation des principaux composants d'enveloppe et changement de
              système énergétique de chauffage) [kWh/m2/an]

          etat_renove_ges_estim_upper: Estimation haute des émissions de GES après un scénario de rénovation globale
              "standard" (isolation des principaux composants d'enveloppe et changement de
              système énergétique de chauffage) [kWh/m2/an]

          etat_renove_risque_canicule: Estimation du risque canicule après rénovation [1-5]

          etat_renove_risque_canicule_inc: Incertitude de l'estimation du risque canicule après rénovation [1-5]

          etiquette_dpe_initial_a: Estimation de la probabilité d'avoir des logements d'étiquette A dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_b: Estimation de la probabilité d'avoir des logements d'étiquette B dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_c: Estimation de la probabilité d'avoir des logements d'étiquette C dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_d: Estimation de la probabilité d'avoir des logements d'étiquette D dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_e: Estimation de la probabilité d'avoir des logements d'étiquette E dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_error: Erreur sur la simulation de DPE pour l'état actuel du bâtiment

          etiquette_dpe_initial_f: Estimation de la probabilité d'avoir des logements d'étiquette F dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_g: Estimation de la probabilité d'avoir des logements d'étiquette G dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_inc: Classe d'incertitude de classe sur l'étiquette dpe avec la plus grande
              probabilité avant rénovation [1 à 5]. Cet indicateur se lit de 1 = peu fiable à
              5 = fiable.

          etiquette_dpe_initial_map: Etiquette ayant la plus grande probabilité pour l'état actuel du bâtiment

          etiquette_dpe_initial_map_2nd: 2 étiquettes ayant la plus grande probabilité pour l'état actuel du bâtiment. Si
              le champs vaut F-G alors F la première étiquette est l'étiquette la plus
              probable , G la seconde étiquette la plus probable.

          etiquette_dpe_initial_map_2nd_prob: Probabilité que le bâtiment ait une étiquette DPE parmi les 2 étiquettes ayant
              la plus grande probabilité pour l'état actuel du bâtiment. Si
              etiquette_dpe_initial_map_2nd = F-G et que etiquette_dpe_initial_map_2nd_prob =
              0.95 alors il y a 95% de chance que l'étiquette DPE de ce bâtiment soit classé F
              ou G.

          etiquette_dpe_initial_map_prob: Probabilité que le bâtiment ait une étiquette DPE égale à l'étiquette ayant la
              plus grande probabilité pour l'état actuel du bâtiment. C'est la probabilité
              d'avoir pour ce bâtiment l'étiquette etiquette_dpe_initial_map. Si
              etiquette_dpe_initial_map = F et que etiquette_dpe_initial_map_prob = 0.64 alors
              il y a 64% de chance que l'étiquette DPE de ce bâtiment soit classé F

          etiquette_dpe_renove_a: Estimation de la probabilité d'avoir des logements d'étiquette A dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_b: Estimation de la probabilité d'avoir des logements d'étiquette B dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_c: Estimation de la probabilité d'avoir des logements d'étiquette C dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_d: Estimation de la probabilité d'avoir des logements d'étiquette D dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_e: Estimation de la probabilité d'avoir des logements d'étiquette E dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_error: Erreur sur la simulation de DPE avant rénovation

          etiquette_dpe_renove_f: Estimation de la probabilité d'avoir des logements d'étiquette F dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_g: Estimation de la probabilité d'avoir des logements d'étiquette G dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_inc: Incertitude de classe sur l'étiquette dpe avec la plus grande probabilité après
              un scénario de rénovation globale "standard" (isolation des principaux
              composants d'enveloppe et changement de système énergétique de chauffage) [1-5]

          etiquette_dpe_renove_map: Etiquette ayant la plus grande probabilité après un scénario de rénovation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de système énergétique de chauffage)

          etiquette_dpe_renove_map_2nd: 2 étiquettes ayant la plus grande probabilité après un scénario de rénovation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de système énergétique de chauffage)

          etiquette_dpe_renove_map_2nd_prob: Probabilité que le bâtiment ait une étiquette DPE parmi les 2 étiquettes ayant
              la plus grande probabilité après un scénario de rénovation globale "standard"
              (isolation des principaux composants d'enveloppe et changement de système
              énergétique de chauffage)

          etiquette_dpe_renove_map_prob: Probabilité que le bâtiment ait une étiquette DPE égale à l'étiquette ayant la
              plus grande probabilité après un scénario de rénovation globale "standard"
              (isolation des principaux composants d'enveloppe et changement de système
              énergétique de chauffage)

          gisement_gain_conso_finale_total: Estimation du gisement de gain de consommation finale total

          gisement_gain_energetique_mean: Estimation du gain énergétique moyen

          gisement_gain_ges_mean: Estimation moyenne du gisement de gain sur les émissions de gaz à effets de
              serre

          indecence_energetique_initial: probabilité du bâtiment d'àªtre en indécence énergétique dans son état initial

          indecence_energetique_renove: probabilité du bâtiment d'àªtre en indécence énergétique dans son état rénové
              (rénovation globale)

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          surface_deperditive: Estimation de la surface déperditive du bâtiment [mÂ²]

          surface_deperditive_verticale: Estimation de la surface déperditive verticale du bâtiment [mÂ²]

          surface_enveloppe: Estimation de la surface de l'enveloppe [mÂ²]

          surface_facade_ext: Estimation de la surface de faà§ade donnant sur l'exterieur [mÂ²]

          surface_facade_mitoyenne: Estimation de la surface de faà§ade donnant sur un autre bâtiment [mÂ²]

          surface_facade_totale: Estimation de la surface totale de faà§ade (murs + baies) [mÂ²]

          surface_facade_vitree: Estimation de la surface de faà§ade vitrée [mÂ²]

          surface_toiture: Estimation de la surface de toiture du bâtiment [mÂ²]

          surface_verticale: Estimation de la surface verticale du bâtiment [mÂ²]

          volume_brut: Volume brut du bâtiment [m3]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get_api_list(
            "/donnees/batiment_groupe_simulations_dpe",
            page=SyncDefault[BatimentGroupeSimulationsDpe],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "etat_initial_consommation_energie_estim_inc": etat_initial_consommation_energie_estim_inc,
                        "etat_initial_consommation_energie_estim_lower": etat_initial_consommation_energie_estim_lower,
                        "etat_initial_consommation_energie_estim_mean": etat_initial_consommation_energie_estim_mean,
                        "etat_initial_consommation_energie_estim_upper": etat_initial_consommation_energie_estim_upper,
                        "etat_initial_consommation_energie_primaire_estim_lower": etat_initial_consommation_energie_primaire_estim_lower,
                        "etat_initial_consommation_energie_primaire_estim_mean": etat_initial_consommation_energie_primaire_estim_mean,
                        "etat_initial_consommation_energie_primaire_estim_upper": etat_initial_consommation_energie_primaire_estim_upper,
                        "etat_initial_consommation_ges_estim_inc": etat_initial_consommation_ges_estim_inc,
                        "etat_initial_ges_estim_lower": etat_initial_ges_estim_lower,
                        "etat_initial_ges_estim_mean": etat_initial_ges_estim_mean,
                        "etat_initial_ges_estim_upper": etat_initial_ges_estim_upper,
                        "etat_initial_risque_canicule": etat_initial_risque_canicule,
                        "etat_initial_risque_canicule_inc": etat_initial_risque_canicule_inc,
                        "etat_renove_consommation_energie_estim_inc": etat_renove_consommation_energie_estim_inc,
                        "etat_renove_consommation_energie_estim_lower": etat_renove_consommation_energie_estim_lower,
                        "etat_renove_consommation_energie_estim_mean": etat_renove_consommation_energie_estim_mean,
                        "etat_renove_consommation_energie_estim_upper": etat_renove_consommation_energie_estim_upper,
                        "etat_renove_consommation_energie_primaire_estim_lower": etat_renove_consommation_energie_primaire_estim_lower,
                        "etat_renove_consommation_energie_primaire_estim_mean": etat_renove_consommation_energie_primaire_estim_mean,
                        "etat_renove_consommation_energie_primaire_estim_upper": etat_renove_consommation_energie_primaire_estim_upper,
                        "etat_renove_consommation_ges_estim_inc": etat_renove_consommation_ges_estim_inc,
                        "etat_renove_ges_estim_lower": etat_renove_ges_estim_lower,
                        "etat_renove_ges_estim_mean": etat_renove_ges_estim_mean,
                        "etat_renove_ges_estim_upper": etat_renove_ges_estim_upper,
                        "etat_renove_risque_canicule": etat_renove_risque_canicule,
                        "etat_renove_risque_canicule_inc": etat_renove_risque_canicule_inc,
                        "etiquette_dpe_initial_a": etiquette_dpe_initial_a,
                        "etiquette_dpe_initial_b": etiquette_dpe_initial_b,
                        "etiquette_dpe_initial_c": etiquette_dpe_initial_c,
                        "etiquette_dpe_initial_d": etiquette_dpe_initial_d,
                        "etiquette_dpe_initial_e": etiquette_dpe_initial_e,
                        "etiquette_dpe_initial_error": etiquette_dpe_initial_error,
                        "etiquette_dpe_initial_f": etiquette_dpe_initial_f,
                        "etiquette_dpe_initial_g": etiquette_dpe_initial_g,
                        "etiquette_dpe_initial_inc": etiquette_dpe_initial_inc,
                        "etiquette_dpe_initial_map": etiquette_dpe_initial_map,
                        "etiquette_dpe_initial_map_2nd": etiquette_dpe_initial_map_2nd,
                        "etiquette_dpe_initial_map_2nd_prob": etiquette_dpe_initial_map_2nd_prob,
                        "etiquette_dpe_initial_map_prob": etiquette_dpe_initial_map_prob,
                        "etiquette_dpe_renove_a": etiquette_dpe_renove_a,
                        "etiquette_dpe_renove_b": etiquette_dpe_renove_b,
                        "etiquette_dpe_renove_c": etiquette_dpe_renove_c,
                        "etiquette_dpe_renove_d": etiquette_dpe_renove_d,
                        "etiquette_dpe_renove_e": etiquette_dpe_renove_e,
                        "etiquette_dpe_renove_error": etiquette_dpe_renove_error,
                        "etiquette_dpe_renove_f": etiquette_dpe_renove_f,
                        "etiquette_dpe_renove_g": etiquette_dpe_renove_g,
                        "etiquette_dpe_renove_inc": etiquette_dpe_renove_inc,
                        "etiquette_dpe_renove_map": etiquette_dpe_renove_map,
                        "etiquette_dpe_renove_map_2nd": etiquette_dpe_renove_map_2nd,
                        "etiquette_dpe_renove_map_2nd_prob": etiquette_dpe_renove_map_2nd_prob,
                        "etiquette_dpe_renove_map_prob": etiquette_dpe_renove_map_prob,
                        "gisement_gain_conso_finale_total": gisement_gain_conso_finale_total,
                        "gisement_gain_energetique_mean": gisement_gain_energetique_mean,
                        "gisement_gain_ges_mean": gisement_gain_ges_mean,
                        "indecence_energetique_initial": indecence_energetique_initial,
                        "indecence_energetique_renove": indecence_energetique_renove,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                        "surface_deperditive": surface_deperditive,
                        "surface_deperditive_verticale": surface_deperditive_verticale,
                        "surface_enveloppe": surface_enveloppe,
                        "surface_facade_ext": surface_facade_ext,
                        "surface_facade_mitoyenne": surface_facade_mitoyenne,
                        "surface_facade_totale": surface_facade_totale,
                        "surface_facade_vitree": surface_facade_vitree,
                        "surface_toiture": surface_toiture,
                        "surface_verticale": surface_verticale,
                        "volume_brut": volume_brut,
                    },
                    simulations_dpe_list_params.SimulationsDpeListParams,
                ),
            ),
            model=BatimentGroupeSimulationsDpe,
        )


class AsyncSimulationsDpeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimulationsDpeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncSimulationsDpeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulationsDpeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncSimulationsDpeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_estim_inc: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_primaire_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_primaire_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_energie_primaire_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_initial_consommation_ges_estim_inc: str | NotGiven = NOT_GIVEN,
        etat_initial_ges_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_initial_ges_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_initial_ges_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_initial_risque_canicule: str | NotGiven = NOT_GIVEN,
        etat_initial_risque_canicule_inc: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_estim_inc: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_primaire_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_primaire_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_energie_primaire_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_renove_consommation_ges_estim_inc: str | NotGiven = NOT_GIVEN,
        etat_renove_ges_estim_lower: str | NotGiven = NOT_GIVEN,
        etat_renove_ges_estim_mean: str | NotGiven = NOT_GIVEN,
        etat_renove_ges_estim_upper: str | NotGiven = NOT_GIVEN,
        etat_renove_risque_canicule: str | NotGiven = NOT_GIVEN,
        etat_renove_risque_canicule_inc: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_a: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_b: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_c: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_d: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_e: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_error: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_f: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_g: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_inc: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_map: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_map_2nd: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_map_2nd_prob: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_initial_map_prob: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_a: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_b: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_c: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_d: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_e: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_error: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_f: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_g: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_inc: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_map: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_map_2nd: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_map_2nd_prob: str | NotGiven = NOT_GIVEN,
        etiquette_dpe_renove_map_prob: str | NotGiven = NOT_GIVEN,
        gisement_gain_conso_finale_total: str | NotGiven = NOT_GIVEN,
        gisement_gain_energetique_mean: str | NotGiven = NOT_GIVEN,
        gisement_gain_ges_mean: str | NotGiven = NOT_GIVEN,
        indecence_energetique_initial: str | NotGiven = NOT_GIVEN,
        indecence_energetique_renove: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        surface_deperditive: str | NotGiven = NOT_GIVEN,
        surface_deperditive_verticale: str | NotGiven = NOT_GIVEN,
        surface_enveloppe: str | NotGiven = NOT_GIVEN,
        surface_facade_ext: str | NotGiven = NOT_GIVEN,
        surface_facade_mitoyenne: str | NotGiven = NOT_GIVEN,
        surface_facade_totale: str | NotGiven = NOT_GIVEN,
        surface_facade_vitree: str | NotGiven = NOT_GIVEN,
        surface_toiture: str | NotGiven = NOT_GIVEN,
        surface_verticale: str | NotGiven = NOT_GIVEN,
        volume_brut: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BatimentGroupeSimulationsDpe, AsyncDefault[BatimentGroupeSimulationsDpe]]:
        """
        Simulations CSTB des étiquettes DPE estimées pour les bâtiments de logement en
        France. Les résultats estimés sont fournis avec des indicateurs qui sont pour la
        plupart des probabilités. Version actuelle 2023-01-20-v073.4

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          etat_initial_consommation_energie_estim_inc: Incertitude des estimations de consommation énergétique finale avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_estim_lower: Estimation basse de la consommation énergétique finale avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_estim_mean: Estimation moyenne de la consommation énergétique finale avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_estim_upper: Estimation haute de la consommation énergétique finale avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_lower: Estimation basse de la consommation énergétique primaire avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_mean: Estimation moyenne de la consommation énergétique primaire avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_upper: Estimation haute de la consommation énergétique primaire avant rénovation
              [kWh/m2/an]

          etat_initial_consommation_ges_estim_inc: Incertitude sur l'estimation de consommation de GES avant rénovation
              [kgeqC02/m2/an]

          etat_initial_ges_estim_lower: Estimation basse de la consommation de GES avant rénovation [kgeqC02/m2/an]

          etat_initial_ges_estim_mean: Estimation moyenne de la consommation de GES avant rénovation [kgeqC02/m2/an]

          etat_initial_ges_estim_upper: Estimation haute de la consommation de GES avant rénovation [kgeqC02/m2/an]

          etat_initial_risque_canicule: Estimation du risque canicule avant rénovation [1-5]

          etat_initial_risque_canicule_inc: Incertitude de l'estimation du risque canicule avant rénovation [1-5]

          etat_renove_consommation_energie_estim_inc: Incertitude sur les estimations des consommations énergétiques finales après un
              scénario de rénovation globale "standard" (isolation des principaux composants
              d'enveloppe et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_estim_lower: Estimation basse de la consommation énergétique finale après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_estim_mean: Estimation moyenne de la consommation énergétique finale après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_estim_upper: Estimation haute de la consommation énergétique finale après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_lower: Estimation basse de la consommation d'énergie primaire après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_mean: Estimation moyenne de la consommation d'énergie primaire après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_upper: Estimation haute de la consommation d'énergie primaire après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kWh/m2/an]

          etat_renove_consommation_ges_estim_inc: Incertitude sur l'estimation de consommation de GES après un scénario de
              rénovation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de système énergétique de chauffage) [kgeqC02/m2/an]

          etat_renove_ges_estim_lower: Estimation basse des émissions de GES après un scénario de rénovation globale
              "standard" (isolation des principaux composants d'enveloppe et changement de
              système énergétique de chauffage) [kWh/m2/an]

          etat_renove_ges_estim_mean: Estimation moyenne des émissions de GES après un scénario de rénovation globale
              "standard" (isolation des principaux composants d'enveloppe et changement de
              système énergétique de chauffage) [kWh/m2/an]

          etat_renove_ges_estim_upper: Estimation haute des émissions de GES après un scénario de rénovation globale
              "standard" (isolation des principaux composants d'enveloppe et changement de
              système énergétique de chauffage) [kWh/m2/an]

          etat_renove_risque_canicule: Estimation du risque canicule après rénovation [1-5]

          etat_renove_risque_canicule_inc: Incertitude de l'estimation du risque canicule après rénovation [1-5]

          etiquette_dpe_initial_a: Estimation de la probabilité d'avoir des logements d'étiquette A dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_b: Estimation de la probabilité d'avoir des logements d'étiquette B dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_c: Estimation de la probabilité d'avoir des logements d'étiquette C dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_d: Estimation de la probabilité d'avoir des logements d'étiquette D dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_e: Estimation de la probabilité d'avoir des logements d'étiquette E dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_error: Erreur sur la simulation de DPE pour l'état actuel du bâtiment

          etiquette_dpe_initial_f: Estimation de la probabilité d'avoir des logements d'étiquette F dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_g: Estimation de la probabilité d'avoir des logements d'étiquette G dans le
              bâtiment pour l'état actuel du bâtiment

          etiquette_dpe_initial_inc: Classe d'incertitude de classe sur l'étiquette dpe avec la plus grande
              probabilité avant rénovation [1 à 5]. Cet indicateur se lit de 1 = peu fiable à
              5 = fiable.

          etiquette_dpe_initial_map: Etiquette ayant la plus grande probabilité pour l'état actuel du bâtiment

          etiquette_dpe_initial_map_2nd: 2 étiquettes ayant la plus grande probabilité pour l'état actuel du bâtiment. Si
              le champs vaut F-G alors F la première étiquette est l'étiquette la plus
              probable , G la seconde étiquette la plus probable.

          etiquette_dpe_initial_map_2nd_prob: Probabilité que le bâtiment ait une étiquette DPE parmi les 2 étiquettes ayant
              la plus grande probabilité pour l'état actuel du bâtiment. Si
              etiquette_dpe_initial_map_2nd = F-G et que etiquette_dpe_initial_map_2nd_prob =
              0.95 alors il y a 95% de chance que l'étiquette DPE de ce bâtiment soit classé F
              ou G.

          etiquette_dpe_initial_map_prob: Probabilité que le bâtiment ait une étiquette DPE égale à l'étiquette ayant la
              plus grande probabilité pour l'état actuel du bâtiment. C'est la probabilité
              d'avoir pour ce bâtiment l'étiquette etiquette_dpe_initial_map. Si
              etiquette_dpe_initial_map = F et que etiquette_dpe_initial_map_prob = 0.64 alors
              il y a 64% de chance que l'étiquette DPE de ce bâtiment soit classé F

          etiquette_dpe_renove_a: Estimation de la probabilité d'avoir des logements d'étiquette A dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_b: Estimation de la probabilité d'avoir des logements d'étiquette B dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_c: Estimation de la probabilité d'avoir des logements d'étiquette C dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_d: Estimation de la probabilité d'avoir des logements d'étiquette D dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_e: Estimation de la probabilité d'avoir des logements d'étiquette E dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_error: Erreur sur la simulation de DPE avant rénovation

          etiquette_dpe_renove_f: Estimation de la probabilité d'avoir des logements d'étiquette F dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_g: Estimation de la probabilité d'avoir des logements d'étiquette G dans le
              bâtiment après un scénario de rénovation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de système énergétique de
              chauffage)

          etiquette_dpe_renove_inc: Incertitude de classe sur l'étiquette dpe avec la plus grande probabilité après
              un scénario de rénovation globale "standard" (isolation des principaux
              composants d'enveloppe et changement de système énergétique de chauffage) [1-5]

          etiquette_dpe_renove_map: Etiquette ayant la plus grande probabilité après un scénario de rénovation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de système énergétique de chauffage)

          etiquette_dpe_renove_map_2nd: 2 étiquettes ayant la plus grande probabilité après un scénario de rénovation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de système énergétique de chauffage)

          etiquette_dpe_renove_map_2nd_prob: Probabilité que le bâtiment ait une étiquette DPE parmi les 2 étiquettes ayant
              la plus grande probabilité après un scénario de rénovation globale "standard"
              (isolation des principaux composants d'enveloppe et changement de système
              énergétique de chauffage)

          etiquette_dpe_renove_map_prob: Probabilité que le bâtiment ait une étiquette DPE égale à l'étiquette ayant la
              plus grande probabilité après un scénario de rénovation globale "standard"
              (isolation des principaux composants d'enveloppe et changement de système
              énergétique de chauffage)

          gisement_gain_conso_finale_total: Estimation du gisement de gain de consommation finale total

          gisement_gain_energetique_mean: Estimation du gain énergétique moyen

          gisement_gain_ges_mean: Estimation moyenne du gisement de gain sur les émissions de gaz à effets de
              serre

          indecence_energetique_initial: probabilité du bâtiment d'àªtre en indécence énergétique dans son état initial

          indecence_energetique_renove: probabilité du bâtiment d'àªtre en indécence énergétique dans son état rénové
              (rénovation globale)

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          surface_deperditive: Estimation de la surface déperditive du bâtiment [mÂ²]

          surface_deperditive_verticale: Estimation de la surface déperditive verticale du bâtiment [mÂ²]

          surface_enveloppe: Estimation de la surface de l'enveloppe [mÂ²]

          surface_facade_ext: Estimation de la surface de faà§ade donnant sur l'exterieur [mÂ²]

          surface_facade_mitoyenne: Estimation de la surface de faà§ade donnant sur un autre bâtiment [mÂ²]

          surface_facade_totale: Estimation de la surface totale de faà§ade (murs + baies) [mÂ²]

          surface_facade_vitree: Estimation de la surface de faà§ade vitrée [mÂ²]

          surface_toiture: Estimation de la surface de toiture du bâtiment [mÂ²]

          surface_verticale: Estimation de la surface verticale du bâtiment [mÂ²]

          volume_brut: Volume brut du bâtiment [m3]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get_api_list(
            "/donnees/batiment_groupe_simulations_dpe",
            page=AsyncDefault[BatimentGroupeSimulationsDpe],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "etat_initial_consommation_energie_estim_inc": etat_initial_consommation_energie_estim_inc,
                        "etat_initial_consommation_energie_estim_lower": etat_initial_consommation_energie_estim_lower,
                        "etat_initial_consommation_energie_estim_mean": etat_initial_consommation_energie_estim_mean,
                        "etat_initial_consommation_energie_estim_upper": etat_initial_consommation_energie_estim_upper,
                        "etat_initial_consommation_energie_primaire_estim_lower": etat_initial_consommation_energie_primaire_estim_lower,
                        "etat_initial_consommation_energie_primaire_estim_mean": etat_initial_consommation_energie_primaire_estim_mean,
                        "etat_initial_consommation_energie_primaire_estim_upper": etat_initial_consommation_energie_primaire_estim_upper,
                        "etat_initial_consommation_ges_estim_inc": etat_initial_consommation_ges_estim_inc,
                        "etat_initial_ges_estim_lower": etat_initial_ges_estim_lower,
                        "etat_initial_ges_estim_mean": etat_initial_ges_estim_mean,
                        "etat_initial_ges_estim_upper": etat_initial_ges_estim_upper,
                        "etat_initial_risque_canicule": etat_initial_risque_canicule,
                        "etat_initial_risque_canicule_inc": etat_initial_risque_canicule_inc,
                        "etat_renove_consommation_energie_estim_inc": etat_renove_consommation_energie_estim_inc,
                        "etat_renove_consommation_energie_estim_lower": etat_renove_consommation_energie_estim_lower,
                        "etat_renove_consommation_energie_estim_mean": etat_renove_consommation_energie_estim_mean,
                        "etat_renove_consommation_energie_estim_upper": etat_renove_consommation_energie_estim_upper,
                        "etat_renove_consommation_energie_primaire_estim_lower": etat_renove_consommation_energie_primaire_estim_lower,
                        "etat_renove_consommation_energie_primaire_estim_mean": etat_renove_consommation_energie_primaire_estim_mean,
                        "etat_renove_consommation_energie_primaire_estim_upper": etat_renove_consommation_energie_primaire_estim_upper,
                        "etat_renove_consommation_ges_estim_inc": etat_renove_consommation_ges_estim_inc,
                        "etat_renove_ges_estim_lower": etat_renove_ges_estim_lower,
                        "etat_renove_ges_estim_mean": etat_renove_ges_estim_mean,
                        "etat_renove_ges_estim_upper": etat_renove_ges_estim_upper,
                        "etat_renove_risque_canicule": etat_renove_risque_canicule,
                        "etat_renove_risque_canicule_inc": etat_renove_risque_canicule_inc,
                        "etiquette_dpe_initial_a": etiquette_dpe_initial_a,
                        "etiquette_dpe_initial_b": etiquette_dpe_initial_b,
                        "etiquette_dpe_initial_c": etiquette_dpe_initial_c,
                        "etiquette_dpe_initial_d": etiquette_dpe_initial_d,
                        "etiquette_dpe_initial_e": etiquette_dpe_initial_e,
                        "etiquette_dpe_initial_error": etiquette_dpe_initial_error,
                        "etiquette_dpe_initial_f": etiquette_dpe_initial_f,
                        "etiquette_dpe_initial_g": etiquette_dpe_initial_g,
                        "etiquette_dpe_initial_inc": etiquette_dpe_initial_inc,
                        "etiquette_dpe_initial_map": etiquette_dpe_initial_map,
                        "etiquette_dpe_initial_map_2nd": etiquette_dpe_initial_map_2nd,
                        "etiquette_dpe_initial_map_2nd_prob": etiquette_dpe_initial_map_2nd_prob,
                        "etiquette_dpe_initial_map_prob": etiquette_dpe_initial_map_prob,
                        "etiquette_dpe_renove_a": etiquette_dpe_renove_a,
                        "etiquette_dpe_renove_b": etiquette_dpe_renove_b,
                        "etiquette_dpe_renove_c": etiquette_dpe_renove_c,
                        "etiquette_dpe_renove_d": etiquette_dpe_renove_d,
                        "etiquette_dpe_renove_e": etiquette_dpe_renove_e,
                        "etiquette_dpe_renove_error": etiquette_dpe_renove_error,
                        "etiquette_dpe_renove_f": etiquette_dpe_renove_f,
                        "etiquette_dpe_renove_g": etiquette_dpe_renove_g,
                        "etiquette_dpe_renove_inc": etiquette_dpe_renove_inc,
                        "etiquette_dpe_renove_map": etiquette_dpe_renove_map,
                        "etiquette_dpe_renove_map_2nd": etiquette_dpe_renove_map_2nd,
                        "etiquette_dpe_renove_map_2nd_prob": etiquette_dpe_renove_map_2nd_prob,
                        "etiquette_dpe_renove_map_prob": etiquette_dpe_renove_map_prob,
                        "gisement_gain_conso_finale_total": gisement_gain_conso_finale_total,
                        "gisement_gain_energetique_mean": gisement_gain_energetique_mean,
                        "gisement_gain_ges_mean": gisement_gain_ges_mean,
                        "indecence_energetique_initial": indecence_energetique_initial,
                        "indecence_energetique_renove": indecence_energetique_renove,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                        "surface_deperditive": surface_deperditive,
                        "surface_deperditive_verticale": surface_deperditive_verticale,
                        "surface_enveloppe": surface_enveloppe,
                        "surface_facade_ext": surface_facade_ext,
                        "surface_facade_mitoyenne": surface_facade_mitoyenne,
                        "surface_facade_totale": surface_facade_totale,
                        "surface_facade_vitree": surface_facade_vitree,
                        "surface_toiture": surface_toiture,
                        "surface_verticale": surface_verticale,
                        "volume_brut": volume_brut,
                    },
                    simulations_dpe_list_params.SimulationsDpeListParams,
                ),
            ),
            model=BatimentGroupeSimulationsDpe,
        )


class SimulationsDpeResourceWithRawResponse:
    def __init__(self, simulations_dpe: SimulationsDpeResource) -> None:
        self._simulations_dpe = simulations_dpe

        self.list = to_raw_response_wrapper(
            simulations_dpe.list,
        )


class AsyncSimulationsDpeResourceWithRawResponse:
    def __init__(self, simulations_dpe: AsyncSimulationsDpeResource) -> None:
        self._simulations_dpe = simulations_dpe

        self.list = async_to_raw_response_wrapper(
            simulations_dpe.list,
        )


class SimulationsDpeResourceWithStreamingResponse:
    def __init__(self, simulations_dpe: SimulationsDpeResource) -> None:
        self._simulations_dpe = simulations_dpe

        self.list = to_streamed_response_wrapper(
            simulations_dpe.list,
        )


class AsyncSimulationsDpeResourceWithStreamingResponse:
    def __init__(self, simulations_dpe: AsyncSimulationsDpeResource) -> None:
        self._simulations_dpe = simulations_dpe

        self.list = async_to_streamed_response_wrapper(
            simulations_dpe.list,
        )
