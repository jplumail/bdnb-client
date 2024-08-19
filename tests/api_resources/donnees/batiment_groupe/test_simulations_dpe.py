# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client.pagination import SyncDefault, AsyncDefault
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeSimulationsDpe

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimulationsDpe:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        simulations_dpe = client.donnees.batiment_groupe.simulations_dpe.list()
        assert_matches_type(SyncDefault[BatimentGroupeSimulationsDpe], simulations_dpe, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        simulations_dpe = client.donnees.batiment_groupe.simulations_dpe.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            etat_initial_consommation_energie_estim_inc="etat_initial_consommation_energie_estim_inc",
            etat_initial_consommation_energie_estim_lower="etat_initial_consommation_energie_estim_lower",
            etat_initial_consommation_energie_estim_mean="etat_initial_consommation_energie_estim_mean",
            etat_initial_consommation_energie_estim_upper="etat_initial_consommation_energie_estim_upper",
            etat_initial_consommation_energie_primaire_estim_lower="etat_initial_consommation_energie_primaire_estim_lower",
            etat_initial_consommation_energie_primaire_estim_mean="etat_initial_consommation_energie_primaire_estim_mean",
            etat_initial_consommation_energie_primaire_estim_upper="etat_initial_consommation_energie_primaire_estim_upper",
            etat_initial_consommation_ges_estim_inc="etat_initial_consommation_ges_estim_inc",
            etat_initial_ges_estim_lower="etat_initial_ges_estim_lower",
            etat_initial_ges_estim_mean="etat_initial_ges_estim_mean",
            etat_initial_ges_estim_upper="etat_initial_ges_estim_upper",
            etat_initial_risque_canicule="etat_initial_risque_canicule",
            etat_initial_risque_canicule_inc="etat_initial_risque_canicule_inc",
            etat_renove_consommation_energie_estim_inc="etat_renove_consommation_energie_estim_inc",
            etat_renove_consommation_energie_estim_lower="etat_renove_consommation_energie_estim_lower",
            etat_renove_consommation_energie_estim_mean="etat_renove_consommation_energie_estim_mean",
            etat_renove_consommation_energie_estim_upper="etat_renove_consommation_energie_estim_upper",
            etat_renove_consommation_energie_primaire_estim_lower="etat_renove_consommation_energie_primaire_estim_lower",
            etat_renove_consommation_energie_primaire_estim_mean="etat_renove_consommation_energie_primaire_estim_mean",
            etat_renove_consommation_energie_primaire_estim_upper="etat_renove_consommation_energie_primaire_estim_upper",
            etat_renove_consommation_ges_estim_inc="etat_renove_consommation_ges_estim_inc",
            etat_renove_ges_estim_lower="etat_renove_ges_estim_lower",
            etat_renove_ges_estim_mean="etat_renove_ges_estim_mean",
            etat_renove_ges_estim_upper="etat_renove_ges_estim_upper",
            etat_renove_risque_canicule="etat_renove_risque_canicule",
            etat_renove_risque_canicule_inc="etat_renove_risque_canicule_inc",
            etiquette_dpe_initial_a="etiquette_dpe_initial_a",
            etiquette_dpe_initial_b="etiquette_dpe_initial_b",
            etiquette_dpe_initial_c="etiquette_dpe_initial_c",
            etiquette_dpe_initial_d="etiquette_dpe_initial_d",
            etiquette_dpe_initial_e="etiquette_dpe_initial_e",
            etiquette_dpe_initial_error="etiquette_dpe_initial_error",
            etiquette_dpe_initial_f="etiquette_dpe_initial_f",
            etiquette_dpe_initial_g="etiquette_dpe_initial_g",
            etiquette_dpe_initial_inc="etiquette_dpe_initial_inc",
            etiquette_dpe_initial_map="etiquette_dpe_initial_map",
            etiquette_dpe_initial_map_2nd="etiquette_dpe_initial_map_2nd",
            etiquette_dpe_initial_map_2nd_prob="etiquette_dpe_initial_map_2nd_prob",
            etiquette_dpe_initial_map_prob="etiquette_dpe_initial_map_prob",
            etiquette_dpe_renove_a="etiquette_dpe_renove_a",
            etiquette_dpe_renove_b="etiquette_dpe_renove_b",
            etiquette_dpe_renove_c="etiquette_dpe_renove_c",
            etiquette_dpe_renove_d="etiquette_dpe_renove_d",
            etiquette_dpe_renove_e="etiquette_dpe_renove_e",
            etiquette_dpe_renove_error="etiquette_dpe_renove_error",
            etiquette_dpe_renove_f="etiquette_dpe_renove_f",
            etiquette_dpe_renove_g="etiquette_dpe_renove_g",
            etiquette_dpe_renove_inc="etiquette_dpe_renove_inc",
            etiquette_dpe_renove_map="etiquette_dpe_renove_map",
            etiquette_dpe_renove_map_2nd="etiquette_dpe_renove_map_2nd",
            etiquette_dpe_renove_map_2nd_prob="etiquette_dpe_renove_map_2nd_prob",
            etiquette_dpe_renove_map_prob="etiquette_dpe_renove_map_prob",
            gisement_gain_conso_finale_total="gisement_gain_conso_finale_total",
            gisement_gain_energetique_mean="gisement_gain_energetique_mean",
            gisement_gain_ges_mean="gisement_gain_ges_mean",
            indecence_energetique_initial="indecence_energetique_initial",
            indecence_energetique_renove="indecence_energetique_renove",
            limit="limit",
            offset="offset",
            order="order",
            select="select",
            surface_deperditive="surface_deperditive",
            surface_deperditive_verticale="surface_deperditive_verticale",
            surface_enveloppe="surface_enveloppe",
            surface_facade_ext="surface_facade_ext",
            surface_facade_mitoyenne="surface_facade_mitoyenne",
            surface_facade_totale="surface_facade_totale",
            surface_facade_vitree="surface_facade_vitree",
            surface_toiture="surface_toiture",
            surface_verticale="surface_verticale",
            volume_brut="volume_brut",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(SyncDefault[BatimentGroupeSimulationsDpe], simulations_dpe, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.batiment_groupe.simulations_dpe.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulations_dpe = response.parse()
        assert_matches_type(SyncDefault[BatimentGroupeSimulationsDpe], simulations_dpe, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.batiment_groupe.simulations_dpe.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulations_dpe = response.parse()
            assert_matches_type(SyncDefault[BatimentGroupeSimulationsDpe], simulations_dpe, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSimulationsDpe:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        simulations_dpe = await async_client.donnees.batiment_groupe.simulations_dpe.list()
        assert_matches_type(AsyncDefault[BatimentGroupeSimulationsDpe], simulations_dpe, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        simulations_dpe = await async_client.donnees.batiment_groupe.simulations_dpe.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            etat_initial_consommation_energie_estim_inc="etat_initial_consommation_energie_estim_inc",
            etat_initial_consommation_energie_estim_lower="etat_initial_consommation_energie_estim_lower",
            etat_initial_consommation_energie_estim_mean="etat_initial_consommation_energie_estim_mean",
            etat_initial_consommation_energie_estim_upper="etat_initial_consommation_energie_estim_upper",
            etat_initial_consommation_energie_primaire_estim_lower="etat_initial_consommation_energie_primaire_estim_lower",
            etat_initial_consommation_energie_primaire_estim_mean="etat_initial_consommation_energie_primaire_estim_mean",
            etat_initial_consommation_energie_primaire_estim_upper="etat_initial_consommation_energie_primaire_estim_upper",
            etat_initial_consommation_ges_estim_inc="etat_initial_consommation_ges_estim_inc",
            etat_initial_ges_estim_lower="etat_initial_ges_estim_lower",
            etat_initial_ges_estim_mean="etat_initial_ges_estim_mean",
            etat_initial_ges_estim_upper="etat_initial_ges_estim_upper",
            etat_initial_risque_canicule="etat_initial_risque_canicule",
            etat_initial_risque_canicule_inc="etat_initial_risque_canicule_inc",
            etat_renove_consommation_energie_estim_inc="etat_renove_consommation_energie_estim_inc",
            etat_renove_consommation_energie_estim_lower="etat_renove_consommation_energie_estim_lower",
            etat_renove_consommation_energie_estim_mean="etat_renove_consommation_energie_estim_mean",
            etat_renove_consommation_energie_estim_upper="etat_renove_consommation_energie_estim_upper",
            etat_renove_consommation_energie_primaire_estim_lower="etat_renove_consommation_energie_primaire_estim_lower",
            etat_renove_consommation_energie_primaire_estim_mean="etat_renove_consommation_energie_primaire_estim_mean",
            etat_renove_consommation_energie_primaire_estim_upper="etat_renove_consommation_energie_primaire_estim_upper",
            etat_renove_consommation_ges_estim_inc="etat_renove_consommation_ges_estim_inc",
            etat_renove_ges_estim_lower="etat_renove_ges_estim_lower",
            etat_renove_ges_estim_mean="etat_renove_ges_estim_mean",
            etat_renove_ges_estim_upper="etat_renove_ges_estim_upper",
            etat_renove_risque_canicule="etat_renove_risque_canicule",
            etat_renove_risque_canicule_inc="etat_renove_risque_canicule_inc",
            etiquette_dpe_initial_a="etiquette_dpe_initial_a",
            etiquette_dpe_initial_b="etiquette_dpe_initial_b",
            etiquette_dpe_initial_c="etiquette_dpe_initial_c",
            etiquette_dpe_initial_d="etiquette_dpe_initial_d",
            etiquette_dpe_initial_e="etiquette_dpe_initial_e",
            etiquette_dpe_initial_error="etiquette_dpe_initial_error",
            etiquette_dpe_initial_f="etiquette_dpe_initial_f",
            etiquette_dpe_initial_g="etiquette_dpe_initial_g",
            etiquette_dpe_initial_inc="etiquette_dpe_initial_inc",
            etiquette_dpe_initial_map="etiquette_dpe_initial_map",
            etiquette_dpe_initial_map_2nd="etiquette_dpe_initial_map_2nd",
            etiquette_dpe_initial_map_2nd_prob="etiquette_dpe_initial_map_2nd_prob",
            etiquette_dpe_initial_map_prob="etiquette_dpe_initial_map_prob",
            etiquette_dpe_renove_a="etiquette_dpe_renove_a",
            etiquette_dpe_renove_b="etiquette_dpe_renove_b",
            etiquette_dpe_renove_c="etiquette_dpe_renove_c",
            etiquette_dpe_renove_d="etiquette_dpe_renove_d",
            etiquette_dpe_renove_e="etiquette_dpe_renove_e",
            etiquette_dpe_renove_error="etiquette_dpe_renove_error",
            etiquette_dpe_renove_f="etiquette_dpe_renove_f",
            etiquette_dpe_renove_g="etiquette_dpe_renove_g",
            etiquette_dpe_renove_inc="etiquette_dpe_renove_inc",
            etiquette_dpe_renove_map="etiquette_dpe_renove_map",
            etiquette_dpe_renove_map_2nd="etiquette_dpe_renove_map_2nd",
            etiquette_dpe_renove_map_2nd_prob="etiquette_dpe_renove_map_2nd_prob",
            etiquette_dpe_renove_map_prob="etiquette_dpe_renove_map_prob",
            gisement_gain_conso_finale_total="gisement_gain_conso_finale_total",
            gisement_gain_energetique_mean="gisement_gain_energetique_mean",
            gisement_gain_ges_mean="gisement_gain_ges_mean",
            indecence_energetique_initial="indecence_energetique_initial",
            indecence_energetique_renove="indecence_energetique_renove",
            limit="limit",
            offset="offset",
            order="order",
            select="select",
            surface_deperditive="surface_deperditive",
            surface_deperditive_verticale="surface_deperditive_verticale",
            surface_enveloppe="surface_enveloppe",
            surface_facade_ext="surface_facade_ext",
            surface_facade_mitoyenne="surface_facade_mitoyenne",
            surface_facade_totale="surface_facade_totale",
            surface_facade_vitree="surface_facade_vitree",
            surface_toiture="surface_toiture",
            surface_verticale="surface_verticale",
            volume_brut="volume_brut",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AsyncDefault[BatimentGroupeSimulationsDpe], simulations_dpe, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.batiment_groupe.simulations_dpe.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulations_dpe = await response.parse()
        assert_matches_type(AsyncDefault[BatimentGroupeSimulationsDpe], simulations_dpe, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.batiment_groupe.simulations_dpe.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulations_dpe = await response.parse()
            assert_matches_type(AsyncDefault[BatimentGroupeSimulationsDpe], simulations_dpe, path=["response"])

        assert cast(Any, response.is_closed) is True
