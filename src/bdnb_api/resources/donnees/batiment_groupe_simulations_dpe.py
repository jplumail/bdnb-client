# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    is_given,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.donnees import batiment_groupe_simulations_dpe_list_params
from ...types.donnees.batiment_groupe_simulations_dpe_list_response import BatimentGroupeSimulationsDpeListResponse

__all__ = ["BatimentGroupeSimulationsDpeResource", "AsyncBatimentGroupeSimulationsDpeResource"]


class BatimentGroupeSimulationsDpeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatimentGroupeSimulationsDpeResourceWithRawResponse:
        return BatimentGroupeSimulationsDpeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentGroupeSimulationsDpeResourceWithStreamingResponse:
        return BatimentGroupeSimulationsDpeResourceWithStreamingResponse(self)

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
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatimentGroupeSimulationsDpeListResponse:
        """
        Simulations CSTB des Ã©tiquettes DPE estimÃ©es pour les bÃ¢timents de logement
        en France. Les rÃ©sultats estimÃ©s sont fournis avec des indicateurs qui sont
        pour la plupart des probabilitÃ©s. Version actuelle 2023-01-20-v073.4

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          code_departement_insee: Code dÃ©partement INSEE

          etat_initial_consommation_energie_estim_inc: Incertitude des estimations de consommation Ã©nergÃ©tique finale avant
              rÃ©novation [kWh/m2/an]

          etat_initial_consommation_energie_estim_lower: Estimation basse de la consommation Ã©nergÃ©tique finale avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_energie_estim_mean: Estimation moyenne de la consommation Ã©nergÃ©tique finale avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_energie_estim_upper: Estimation haute de la consommation Ã©nergÃ©tique finale avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_lower: Estimation basse de la consommation Ã©nergÃ©tique primaire avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_mean: Estimation moyenne de la consommation Ã©nergÃ©tique primaire avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_upper: Estimation haute de la consommation Ã©nergÃ©tique primaire avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_ges_estim_inc: Incertitude sur l'estimation de consommation de GES avant rÃ©novation
              [kgeqC02/m2/an]

          etat_initial_ges_estim_lower: Estimation basse de la consommation de GES avant rÃ©novation [kgeqC02/m2/an]

          etat_initial_ges_estim_mean: Estimation moyenne de la consommation de GES avant rÃ©novation [kgeqC02/m2/an]

          etat_initial_ges_estim_upper: Estimation haute de la consommation de GES avant rÃ©novation [kgeqC02/m2/an]

          etat_initial_risque_canicule: Estimation du risque canicule avant rÃ©novation [1-5]

          etat_initial_risque_canicule_inc: Incertitude de l'estimation du risque canicule avant rÃ©novation [1-5]

          etat_renove_consommation_energie_estim_inc: Incertitude sur les estimations des consommations Ã©nergÃ©tiques finales aprÃ¨s
              un scÃ©nario de rÃ©novation globale "standard" (isolation des principaux
              composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de chauffage)
              [kWh/m2/an]

          etat_renove_consommation_energie_estim_lower: Estimation basse de la consommation Ã©nergÃ©tique finale aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_estim_mean: Estimation moyenne de la consommation Ã©nergÃ©tique finale aprÃ¨s un scÃ©nario
              de rÃ©novation globale "standard" (isolation des principaux composants
              d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_estim_upper: Estimation haute de la consommation Ã©nergÃ©tique finale aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_lower: Estimation basse de la consommation d'Ã©nergie primaire aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_mean: Estimation moyenne de la consommation d'Ã©nergie primaire aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_upper: Estimation haute de la consommation d'Ã©nergie primaire aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_ges_estim_inc: Incertitude sur l'estimation de consommation de GES aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kgeqC02/m2/an]

          etat_renove_ges_estim_lower: Estimation basse des Ã©missions de GES aprÃ¨s un scÃ©nario de rÃ©novation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_ges_estim_mean: Estimation moyenne des Ã©missions de GES aprÃ¨s un scÃ©nario de rÃ©novation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_ges_estim_upper: Estimation haute des Ã©missions de GES aprÃ¨s un scÃ©nario de rÃ©novation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_risque_canicule: Estimation du risque canicule aprÃ¨s rÃ©novation [1-5]

          etat_renove_risque_canicule_inc: Incertitude de l'estimation du risque canicule aprÃ¨s rÃ©novation [1-5]

          etiquette_dpe_initial_a: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette A dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_b: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette B dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_c: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette C dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_d: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette D dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_e: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette E dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_error: Erreur sur la simulation de DPE pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_f: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette F dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_g: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette G dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_inc: Classe d'incertitude de classe sur l'Ã©tiquette dpe avec la plus grande
              probabilitÃ© avant rÃ©novation [1 Ã 5]. Cet indicateur se lit de 1 = peu fiable
              Ã 5 = fiable.

          etiquette_dpe_initial_map: Etiquette ayant la plus grande probabilitÃ© pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_map_2nd: 2 Ã©tiquettes ayant la plus grande probabilitÃ© pour l'Ã©tat actuel du
              bÃ¢timent. Si le champs vaut F-G alors F la premiÃ¨re Ã©tiquette est
              l'Ã©tiquette la plus probable , G la seconde Ã©tiquette la plus probable.

          etiquette_dpe_initial_map_2nd_prob: ProbabilitÃ© que le bÃ¢timent ait une Ã©tiquette DPE parmi les 2 Ã©tiquettes
              ayant la plus grande probabilitÃ© pour l'Ã©tat actuel du bÃ¢timent. Si
              etiquette_dpe_initial_map_2nd = F-G et que etiquette_dpe_initial_map_2nd_prob =
              0.95 alors il y a 95% de chance que l'Ã©tiquette DPE de ce bÃ¢timent soit
              classÃ© F ou G.

          etiquette_dpe_initial_map_prob: ProbabilitÃ© que le bÃ¢timent ait une Ã©tiquette DPE Ã©gale Ã l'Ã©tiquette ayant
              la plus grande probabilitÃ© pour l'Ã©tat actuel du bÃ¢timent. C'est la
              probabilitÃ© d'avoir pour ce bÃ¢timent l'Ã©tiquette etiquette_dpe_initial_map.
              Si etiquette_dpe_initial_map = F et que etiquette_dpe_initial_map_prob = 0.64
              alors il y a 64% de chance que l'Ã©tiquette DPE de ce bÃ¢timent soit classÃ© F

          etiquette_dpe_renove_a: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette A dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_b: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette B dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_c: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette C dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_d: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette D dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_e: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette E dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_error: Erreur sur la simulation de DPE avant rÃ©novation

          etiquette_dpe_renove_f: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette F dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_g: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette G dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_inc: Incertitude de classe sur l'Ã©tiquette dpe avec la plus grande probabilitÃ©
              aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des principaux
              composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de chauffage)
              [1-5]

          etiquette_dpe_renove_map: Etiquette ayant la plus grande probabilitÃ© aprÃ¨s un scÃ©nario de rÃ©novation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de systÃ¨me Ã©nergÃ©tique de chauffage)

          etiquette_dpe_renove_map_2nd: 2 Ã©tiquettes ayant la plus grande probabilitÃ© aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage)

          etiquette_dpe_renove_map_2nd_prob: ProbabilitÃ© que le bÃ¢timent ait une Ã©tiquette DPE parmi les 2 Ã©tiquettes
              ayant la plus grande probabilitÃ© aprÃ¨s un scÃ©nario de rÃ©novation globale
              "standard" (isolation des principaux composants d'enveloppe et changement de
              systÃ¨me Ã©nergÃ©tique de chauffage)

          etiquette_dpe_renove_map_prob: ProbabilitÃ© que le bÃ¢timent ait une Ã©tiquette DPE Ã©gale Ã l'Ã©tiquette ayant
              la plus grande probabilitÃ© aprÃ¨s un scÃ©nario de rÃ©novation globale
              "standard" (isolation des principaux composants d'enveloppe et changement de
              systÃ¨me Ã©nergÃ©tique de chauffage)

          gisement_gain_conso_finale_total: Estimation du gisement de gain de consommation finale total

          gisement_gain_energetique_mean: Estimation du gain Ã©nergÃ©tique moyen

          gisement_gain_ges_mean: Estimation moyenne du gisement de gain sur les Ã©missions de gaz Ã effets de
              serre

          indecence_energetique_initial: probabilitÃ© du bÃ¢timent d'Ãªtre en indÃ©cence Ã©nergÃ©tique dans son Ã©tat
              initial

          indecence_energetique_renove: probabilitÃ© du bÃ¢timent d'Ãªtre en indÃ©cence Ã©nergÃ©tique dans son Ã©tat
              rÃ©novÃ© (rÃ©novation globale)

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          surface_deperditive: Estimation de la surface dÃ©perditive du bÃ¢timent [mÂ²]

          surface_deperditive_verticale: Estimation de la surface dÃ©perditive verticale du bÃ¢timent [mÂ²]

          surface_enveloppe: Estimation de la surface de l'enveloppe [mÂ²]

          surface_facade_ext: Estimation de la surface de faÃ§ade donnant sur l'exterieur [mÂ²]

          surface_facade_mitoyenne: Estimation de la surface de faÃ§ade donnant sur un autre bÃ¢timent [mÂ²]

          surface_facade_totale: Estimation de la surface totale de faÃ§ade (murs + baies) [mÂ²]

          surface_facade_vitree: Estimation de la surface de faÃ§ade vitrÃ©e [mÂ²]

          surface_toiture: Estimation de la surface de toiture du bÃ¢timent [mÂ²]

          surface_verticale: Estimation de la surface verticale du bÃ¢timent [mÂ²]

          volume_brut: Volume brut du bÃ¢timent [m3]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/donnees/batiment_groupe_simulations_dpe",
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
                    batiment_groupe_simulations_dpe_list_params.BatimentGroupeSimulationsDpeListParams,
                ),
            ),
            cast_to=BatimentGroupeSimulationsDpeListResponse,
        )


class AsyncBatimentGroupeSimulationsDpeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatimentGroupeSimulationsDpeResourceWithRawResponse:
        return AsyncBatimentGroupeSimulationsDpeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentGroupeSimulationsDpeResourceWithStreamingResponse:
        return AsyncBatimentGroupeSimulationsDpeResourceWithStreamingResponse(self)

    async def list(
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
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatimentGroupeSimulationsDpeListResponse:
        """
        Simulations CSTB des Ã©tiquettes DPE estimÃ©es pour les bÃ¢timents de logement
        en France. Les rÃ©sultats estimÃ©s sont fournis avec des indicateurs qui sont
        pour la plupart des probabilitÃ©s. Version actuelle 2023-01-20-v073.4

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          code_departement_insee: Code dÃ©partement INSEE

          etat_initial_consommation_energie_estim_inc: Incertitude des estimations de consommation Ã©nergÃ©tique finale avant
              rÃ©novation [kWh/m2/an]

          etat_initial_consommation_energie_estim_lower: Estimation basse de la consommation Ã©nergÃ©tique finale avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_energie_estim_mean: Estimation moyenne de la consommation Ã©nergÃ©tique finale avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_energie_estim_upper: Estimation haute de la consommation Ã©nergÃ©tique finale avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_lower: Estimation basse de la consommation Ã©nergÃ©tique primaire avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_mean: Estimation moyenne de la consommation Ã©nergÃ©tique primaire avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_energie_primaire_estim_upper: Estimation haute de la consommation Ã©nergÃ©tique primaire avant rÃ©novation
              [kWh/m2/an]

          etat_initial_consommation_ges_estim_inc: Incertitude sur l'estimation de consommation de GES avant rÃ©novation
              [kgeqC02/m2/an]

          etat_initial_ges_estim_lower: Estimation basse de la consommation de GES avant rÃ©novation [kgeqC02/m2/an]

          etat_initial_ges_estim_mean: Estimation moyenne de la consommation de GES avant rÃ©novation [kgeqC02/m2/an]

          etat_initial_ges_estim_upper: Estimation haute de la consommation de GES avant rÃ©novation [kgeqC02/m2/an]

          etat_initial_risque_canicule: Estimation du risque canicule avant rÃ©novation [1-5]

          etat_initial_risque_canicule_inc: Incertitude de l'estimation du risque canicule avant rÃ©novation [1-5]

          etat_renove_consommation_energie_estim_inc: Incertitude sur les estimations des consommations Ã©nergÃ©tiques finales aprÃ¨s
              un scÃ©nario de rÃ©novation globale "standard" (isolation des principaux
              composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de chauffage)
              [kWh/m2/an]

          etat_renove_consommation_energie_estim_lower: Estimation basse de la consommation Ã©nergÃ©tique finale aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_estim_mean: Estimation moyenne de la consommation Ã©nergÃ©tique finale aprÃ¨s un scÃ©nario
              de rÃ©novation globale "standard" (isolation des principaux composants
              d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_estim_upper: Estimation haute de la consommation Ã©nergÃ©tique finale aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_lower: Estimation basse de la consommation d'Ã©nergie primaire aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_mean: Estimation moyenne de la consommation d'Ã©nergie primaire aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_energie_primaire_estim_upper: Estimation haute de la consommation d'Ã©nergie primaire aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_consommation_ges_estim_inc: Incertitude sur l'estimation de consommation de GES aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kgeqC02/m2/an]

          etat_renove_ges_estim_lower: Estimation basse des Ã©missions de GES aprÃ¨s un scÃ©nario de rÃ©novation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_ges_estim_mean: Estimation moyenne des Ã©missions de GES aprÃ¨s un scÃ©nario de rÃ©novation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_ges_estim_upper: Estimation haute des Ã©missions de GES aprÃ¨s un scÃ©nario de rÃ©novation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]

          etat_renove_risque_canicule: Estimation du risque canicule aprÃ¨s rÃ©novation [1-5]

          etat_renove_risque_canicule_inc: Incertitude de l'estimation du risque canicule aprÃ¨s rÃ©novation [1-5]

          etiquette_dpe_initial_a: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette A dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_b: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette B dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_c: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette C dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_d: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette D dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_e: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette E dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_error: Erreur sur la simulation de DPE pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_f: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette F dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_g: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette G dans le
              bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_inc: Classe d'incertitude de classe sur l'Ã©tiquette dpe avec la plus grande
              probabilitÃ© avant rÃ©novation [1 Ã 5]. Cet indicateur se lit de 1 = peu fiable
              Ã 5 = fiable.

          etiquette_dpe_initial_map: Etiquette ayant la plus grande probabilitÃ© pour l'Ã©tat actuel du bÃ¢timent

          etiquette_dpe_initial_map_2nd: 2 Ã©tiquettes ayant la plus grande probabilitÃ© pour l'Ã©tat actuel du
              bÃ¢timent. Si le champs vaut F-G alors F la premiÃ¨re Ã©tiquette est
              l'Ã©tiquette la plus probable , G la seconde Ã©tiquette la plus probable.

          etiquette_dpe_initial_map_2nd_prob: ProbabilitÃ© que le bÃ¢timent ait une Ã©tiquette DPE parmi les 2 Ã©tiquettes
              ayant la plus grande probabilitÃ© pour l'Ã©tat actuel du bÃ¢timent. Si
              etiquette_dpe_initial_map_2nd = F-G et que etiquette_dpe_initial_map_2nd_prob =
              0.95 alors il y a 95% de chance que l'Ã©tiquette DPE de ce bÃ¢timent soit
              classÃ© F ou G.

          etiquette_dpe_initial_map_prob: ProbabilitÃ© que le bÃ¢timent ait une Ã©tiquette DPE Ã©gale Ã l'Ã©tiquette ayant
              la plus grande probabilitÃ© pour l'Ã©tat actuel du bÃ¢timent. C'est la
              probabilitÃ© d'avoir pour ce bÃ¢timent l'Ã©tiquette etiquette_dpe_initial_map.
              Si etiquette_dpe_initial_map = F et que etiquette_dpe_initial_map_prob = 0.64
              alors il y a 64% de chance que l'Ã©tiquette DPE de ce bÃ¢timent soit classÃ© F

          etiquette_dpe_renove_a: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette A dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_b: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette B dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_c: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette C dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_d: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette D dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_e: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette E dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_error: Erreur sur la simulation de DPE avant rÃ©novation

          etiquette_dpe_renove_f: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette F dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_g: Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette G dans le
              bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
              principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
              chauffage)

          etiquette_dpe_renove_inc: Incertitude de classe sur l'Ã©tiquette dpe avec la plus grande probabilitÃ©
              aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des principaux
              composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de chauffage)
              [1-5]

          etiquette_dpe_renove_map: Etiquette ayant la plus grande probabilitÃ© aprÃ¨s un scÃ©nario de rÃ©novation
              globale "standard" (isolation des principaux composants d'enveloppe et
              changement de systÃ¨me Ã©nergÃ©tique de chauffage)

          etiquette_dpe_renove_map_2nd: 2 Ã©tiquettes ayant la plus grande probabilitÃ© aprÃ¨s un scÃ©nario de
              rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
              et changement de systÃ¨me Ã©nergÃ©tique de chauffage)

          etiquette_dpe_renove_map_2nd_prob: ProbabilitÃ© que le bÃ¢timent ait une Ã©tiquette DPE parmi les 2 Ã©tiquettes
              ayant la plus grande probabilitÃ© aprÃ¨s un scÃ©nario de rÃ©novation globale
              "standard" (isolation des principaux composants d'enveloppe et changement de
              systÃ¨me Ã©nergÃ©tique de chauffage)

          etiquette_dpe_renove_map_prob: ProbabilitÃ© que le bÃ¢timent ait une Ã©tiquette DPE Ã©gale Ã l'Ã©tiquette ayant
              la plus grande probabilitÃ© aprÃ¨s un scÃ©nario de rÃ©novation globale
              "standard" (isolation des principaux composants d'enveloppe et changement de
              systÃ¨me Ã©nergÃ©tique de chauffage)

          gisement_gain_conso_finale_total: Estimation du gisement de gain de consommation finale total

          gisement_gain_energetique_mean: Estimation du gain Ã©nergÃ©tique moyen

          gisement_gain_ges_mean: Estimation moyenne du gisement de gain sur les Ã©missions de gaz Ã effets de
              serre

          indecence_energetique_initial: probabilitÃ© du bÃ¢timent d'Ãªtre en indÃ©cence Ã©nergÃ©tique dans son Ã©tat
              initial

          indecence_energetique_renove: probabilitÃ© du bÃ¢timent d'Ãªtre en indÃ©cence Ã©nergÃ©tique dans son Ã©tat
              rÃ©novÃ© (rÃ©novation globale)

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          surface_deperditive: Estimation de la surface dÃ©perditive du bÃ¢timent [mÂ²]

          surface_deperditive_verticale: Estimation de la surface dÃ©perditive verticale du bÃ¢timent [mÂ²]

          surface_enveloppe: Estimation de la surface de l'enveloppe [mÂ²]

          surface_facade_ext: Estimation de la surface de faÃ§ade donnant sur l'exterieur [mÂ²]

          surface_facade_mitoyenne: Estimation de la surface de faÃ§ade donnant sur un autre bÃ¢timent [mÂ²]

          surface_facade_totale: Estimation de la surface totale de faÃ§ade (murs + baies) [mÂ²]

          surface_facade_vitree: Estimation de la surface de faÃ§ade vitrÃ©e [mÂ²]

          surface_toiture: Estimation de la surface de toiture du bÃ¢timent [mÂ²]

          surface_verticale: Estimation de la surface verticale du bÃ¢timent [mÂ²]

          volume_brut: Volume brut du bÃ¢timent [m3]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            "/donnees/batiment_groupe_simulations_dpe",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
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
                    batiment_groupe_simulations_dpe_list_params.BatimentGroupeSimulationsDpeListParams,
                ),
            ),
            cast_to=BatimentGroupeSimulationsDpeListResponse,
        )


class BatimentGroupeSimulationsDpeResourceWithRawResponse:
    def __init__(self, batiment_groupe_simulations_dpe: BatimentGroupeSimulationsDpeResource) -> None:
        self._batiment_groupe_simulations_dpe = batiment_groupe_simulations_dpe

        self.list = to_raw_response_wrapper(
            batiment_groupe_simulations_dpe.list,
        )


class AsyncBatimentGroupeSimulationsDpeResourceWithRawResponse:
    def __init__(self, batiment_groupe_simulations_dpe: AsyncBatimentGroupeSimulationsDpeResource) -> None:
        self._batiment_groupe_simulations_dpe = batiment_groupe_simulations_dpe

        self.list = async_to_raw_response_wrapper(
            batiment_groupe_simulations_dpe.list,
        )


class BatimentGroupeSimulationsDpeResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_simulations_dpe: BatimentGroupeSimulationsDpeResource) -> None:
        self._batiment_groupe_simulations_dpe = batiment_groupe_simulations_dpe

        self.list = to_streamed_response_wrapper(
            batiment_groupe_simulations_dpe.list,
        )


class AsyncBatimentGroupeSimulationsDpeResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_simulations_dpe: AsyncBatimentGroupeSimulationsDpeResource) -> None:
        self._batiment_groupe_simulations_dpe = batiment_groupe_simulations_dpe

        self.list = async_to_streamed_response_wrapper(
            batiment_groupe_simulations_dpe.list,
        )
