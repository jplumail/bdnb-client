# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client.pagination import SyncDefault, AsyncDefault
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeSimulationsDvf

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimulationsDvf:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        simulations_dvf = client.donnees.batiment_groupe.simulations_dvf.list()
        assert_matches_type(SyncDefault[BatimentGroupeSimulationsDvf], simulations_dvf, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        simulations_dvf = client.donnees.batiment_groupe.simulations_dvf.list(
            batiment_groupe_id="batiment_groupe_id",
            classe_dpe_conso_initial="classe_dpe_conso_initial",
            classe_dpe_conso_renove="classe_dpe_conso_renove",
            code_departement_insee="code_departement_insee",
            difference_abs_valeur_fonciere_etat_initial_renove="difference_abs_valeur_fonciere_etat_initial_renove",
            difference_rel_valeur_fonciere_etat_initial_renove="difference_rel_valeur_fonciere_etat_initial_renove",
            difference_rel_valeur_fonciere_etat_initial_renove_categorie="difference_rel_valeur_fonciere_etat_initial_renove_categorie",
            difference_rel_valeur_fonciere_initial_mean_iris="difference_rel_valeur_fonciere_initial_mean_iris",
            difference_rel_valeur_fonciere_renove_mean_iris="difference_rel_valeur_fonciere_renove_mean_iris",
            limit="limit",
            offset="offset",
            order="order",
            r2="r2",
            select="select",
            usage_niveau_1_txt="usage_niveau_1_txt",
            valeur_fonciere_etat_initial_estim_lower="valeur_fonciere_etat_initial_estim_lower",
            valeur_fonciere_etat_initial_estim_mean="valeur_fonciere_etat_initial_estim_mean",
            valeur_fonciere_etat_initial_estim_upper="valeur_fonciere_etat_initial_estim_upper",
            valeur_fonciere_etat_initial_incertitude="valeur_fonciere_etat_initial_incertitude",
            valeur_fonciere_etat_renove_estim_lower="valeur_fonciere_etat_renove_estim_lower",
            valeur_fonciere_etat_renove_estim_mean="valeur_fonciere_etat_renove_estim_mean",
            valeur_fonciere_etat_renove_estim_upper="valeur_fonciere_etat_renove_estim_upper",
            valeur_fonciere_etat_renove_incertitude="valeur_fonciere_etat_renove_incertitude",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(SyncDefault[BatimentGroupeSimulationsDvf], simulations_dvf, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.batiment_groupe.simulations_dvf.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulations_dvf = response.parse()
        assert_matches_type(SyncDefault[BatimentGroupeSimulationsDvf], simulations_dvf, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.batiment_groupe.simulations_dvf.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulations_dvf = response.parse()
            assert_matches_type(SyncDefault[BatimentGroupeSimulationsDvf], simulations_dvf, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSimulationsDvf:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        simulations_dvf = await async_client.donnees.batiment_groupe.simulations_dvf.list()
        assert_matches_type(AsyncDefault[BatimentGroupeSimulationsDvf], simulations_dvf, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        simulations_dvf = await async_client.donnees.batiment_groupe.simulations_dvf.list(
            batiment_groupe_id="batiment_groupe_id",
            classe_dpe_conso_initial="classe_dpe_conso_initial",
            classe_dpe_conso_renove="classe_dpe_conso_renove",
            code_departement_insee="code_departement_insee",
            difference_abs_valeur_fonciere_etat_initial_renove="difference_abs_valeur_fonciere_etat_initial_renove",
            difference_rel_valeur_fonciere_etat_initial_renove="difference_rel_valeur_fonciere_etat_initial_renove",
            difference_rel_valeur_fonciere_etat_initial_renove_categorie="difference_rel_valeur_fonciere_etat_initial_renove_categorie",
            difference_rel_valeur_fonciere_initial_mean_iris="difference_rel_valeur_fonciere_initial_mean_iris",
            difference_rel_valeur_fonciere_renove_mean_iris="difference_rel_valeur_fonciere_renove_mean_iris",
            limit="limit",
            offset="offset",
            order="order",
            r2="r2",
            select="select",
            usage_niveau_1_txt="usage_niveau_1_txt",
            valeur_fonciere_etat_initial_estim_lower="valeur_fonciere_etat_initial_estim_lower",
            valeur_fonciere_etat_initial_estim_mean="valeur_fonciere_etat_initial_estim_mean",
            valeur_fonciere_etat_initial_estim_upper="valeur_fonciere_etat_initial_estim_upper",
            valeur_fonciere_etat_initial_incertitude="valeur_fonciere_etat_initial_incertitude",
            valeur_fonciere_etat_renove_estim_lower="valeur_fonciere_etat_renove_estim_lower",
            valeur_fonciere_etat_renove_estim_mean="valeur_fonciere_etat_renove_estim_mean",
            valeur_fonciere_etat_renove_estim_upper="valeur_fonciere_etat_renove_estim_upper",
            valeur_fonciere_etat_renove_incertitude="valeur_fonciere_etat_renove_incertitude",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AsyncDefault[BatimentGroupeSimulationsDvf], simulations_dvf, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.batiment_groupe.simulations_dvf.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulations_dvf = await response.parse()
        assert_matches_type(AsyncDefault[BatimentGroupeSimulationsDvf], simulations_dvf, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.batiment_groupe.simulations_dvf.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulations_dvf = await response.parse()
            assert_matches_type(AsyncDefault[BatimentGroupeSimulationsDvf], simulations_dvf, path=["response"])

        assert cast(Any, response.is_closed) is True
