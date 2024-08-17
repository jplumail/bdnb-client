# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import BdnbAPI, AsyncBdnbAPI
from tests.utils import assert_matches_type
from bdnb_api.types.donnees import (
    BatimentGroupeDpeStatistiqueLogementListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatimentGroupeDpeStatistiqueLogement:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: BdnbAPI) -> None:
        batiment_groupe_dpe_statistique_logement = client.donnees.batiment_groupe_dpe_statistique_logement.list()
        assert_matches_type(
            BatimentGroupeDpeStatistiqueLogementListResponse,
            batiment_groupe_dpe_statistique_logement,
            path=["response"],
        )

    @parametrize
    def test_method_list_with_all_params(self, client: BdnbAPI) -> None:
        batiment_groupe_dpe_statistique_logement = client.donnees.batiment_groupe_dpe_statistique_logement.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            limit="limit",
            nb_classe_bilan_dpe_a="nb_classe_bilan_dpe_a",
            nb_classe_bilan_dpe_b="nb_classe_bilan_dpe_b",
            nb_classe_bilan_dpe_c="nb_classe_bilan_dpe_c",
            nb_classe_bilan_dpe_d="nb_classe_bilan_dpe_d",
            nb_classe_bilan_dpe_e="nb_classe_bilan_dpe_e",
            nb_classe_bilan_dpe_f="nb_classe_bilan_dpe_f",
            nb_classe_bilan_dpe_g="nb_classe_bilan_dpe_g",
            nb_classe_conso_energie_arrete_2012_a="nb_classe_conso_energie_arrete_2012_a",
            nb_classe_conso_energie_arrete_2012_b="nb_classe_conso_energie_arrete_2012_b",
            nb_classe_conso_energie_arrete_2012_c="nb_classe_conso_energie_arrete_2012_c",
            nb_classe_conso_energie_arrete_2012_d="nb_classe_conso_energie_arrete_2012_d",
            nb_classe_conso_energie_arrete_2012_e="nb_classe_conso_energie_arrete_2012_e",
            nb_classe_conso_energie_arrete_2012_f="nb_classe_conso_energie_arrete_2012_f",
            nb_classe_conso_energie_arrete_2012_g="nb_classe_conso_energie_arrete_2012_g",
            nb_classe_conso_energie_arrete_2012_nc="nb_classe_conso_energie_arrete_2012_nc",
            offset="offset",
            order="order",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(
            BatimentGroupeDpeStatistiqueLogementListResponse,
            batiment_groupe_dpe_statistique_logement,
            path=["response"],
        )

    @parametrize
    def test_raw_response_list(self, client: BdnbAPI) -> None:
        response = client.donnees.batiment_groupe_dpe_statistique_logement.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_groupe_dpe_statistique_logement = response.parse()
        assert_matches_type(
            BatimentGroupeDpeStatistiqueLogementListResponse,
            batiment_groupe_dpe_statistique_logement,
            path=["response"],
        )

    @parametrize
    def test_streaming_response_list(self, client: BdnbAPI) -> None:
        with client.donnees.batiment_groupe_dpe_statistique_logement.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_groupe_dpe_statistique_logement = response.parse()
            assert_matches_type(
                BatimentGroupeDpeStatistiqueLogementListResponse,
                batiment_groupe_dpe_statistique_logement,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncBatimentGroupeDpeStatistiqueLogement:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnbAPI) -> None:
        batiment_groupe_dpe_statistique_logement = (
            await async_client.donnees.batiment_groupe_dpe_statistique_logement.list()
        )
        assert_matches_type(
            BatimentGroupeDpeStatistiqueLogementListResponse,
            batiment_groupe_dpe_statistique_logement,
            path=["response"],
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        batiment_groupe_dpe_statistique_logement = (
            await async_client.donnees.batiment_groupe_dpe_statistique_logement.list(
                batiment_groupe_id="batiment_groupe_id",
                code_departement_insee="code_departement_insee",
                limit="limit",
                nb_classe_bilan_dpe_a="nb_classe_bilan_dpe_a",
                nb_classe_bilan_dpe_b="nb_classe_bilan_dpe_b",
                nb_classe_bilan_dpe_c="nb_classe_bilan_dpe_c",
                nb_classe_bilan_dpe_d="nb_classe_bilan_dpe_d",
                nb_classe_bilan_dpe_e="nb_classe_bilan_dpe_e",
                nb_classe_bilan_dpe_f="nb_classe_bilan_dpe_f",
                nb_classe_bilan_dpe_g="nb_classe_bilan_dpe_g",
                nb_classe_conso_energie_arrete_2012_a="nb_classe_conso_energie_arrete_2012_a",
                nb_classe_conso_energie_arrete_2012_b="nb_classe_conso_energie_arrete_2012_b",
                nb_classe_conso_energie_arrete_2012_c="nb_classe_conso_energie_arrete_2012_c",
                nb_classe_conso_energie_arrete_2012_d="nb_classe_conso_energie_arrete_2012_d",
                nb_classe_conso_energie_arrete_2012_e="nb_classe_conso_energie_arrete_2012_e",
                nb_classe_conso_energie_arrete_2012_f="nb_classe_conso_energie_arrete_2012_f",
                nb_classe_conso_energie_arrete_2012_g="nb_classe_conso_energie_arrete_2012_g",
                nb_classe_conso_energie_arrete_2012_nc="nb_classe_conso_energie_arrete_2012_nc",
                offset="offset",
                order="order",
                select="select",
                range="Range",
                range_unit="Range-Unit",
            )
        )
        assert_matches_type(
            BatimentGroupeDpeStatistiqueLogementListResponse,
            batiment_groupe_dpe_statistique_logement,
            path=["response"],
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.donnees.batiment_groupe_dpe_statistique_logement.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_groupe_dpe_statistique_logement = await response.parse()
        assert_matches_type(
            BatimentGroupeDpeStatistiqueLogementListResponse,
            batiment_groupe_dpe_statistique_logement,
            path=["response"],
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.donnees.batiment_groupe_dpe_statistique_logement.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_groupe_dpe_statistique_logement = await response.parse()
            assert_matches_type(
                BatimentGroupeDpeStatistiqueLogementListResponse,
                batiment_groupe_dpe_statistique_logement,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True
