# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import BdnbAPI, AsyncBdnbAPI
from tests.utils import assert_matches_type
from bdnb_api.types.tables_bdnb.donnees import BatimentGroupeRncListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatimentGroupeRnc:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: BdnbAPI) -> None:
        batiment_groupe_rnc = client.tables_bdnb.donnees.batiment_groupe_rnc.list()
        assert_matches_type(BatimentGroupeRncListResponse, batiment_groupe_rnc, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: BdnbAPI) -> None:
        batiment_groupe_rnc = client.tables_bdnb.donnees.batiment_groupe_rnc.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            copro_dans_pvd="copro_dans_pvd",
            l_annee_construction="l_annee_construction",
            l_nom_copro="l_nom_copro",
            l_siret="l_siret",
            limit="limit",
            nb_log="nb_log",
            nb_lot_garpark="nb_lot_garpark",
            nb_lot_tertiaire="nb_lot_tertiaire",
            nb_lot_tot="nb_lot_tot",
            numero_immat_principal="numero_immat_principal",
            offset="offset",
            order="order",
            periode_construction_max="periode_construction_max",
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(BatimentGroupeRncListResponse, batiment_groupe_rnc, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BdnbAPI) -> None:
        response = client.tables_bdnb.donnees.batiment_groupe_rnc.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_groupe_rnc = response.parse()
        assert_matches_type(BatimentGroupeRncListResponse, batiment_groupe_rnc, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BdnbAPI) -> None:
        with client.tables_bdnb.donnees.batiment_groupe_rnc.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_groupe_rnc = response.parse()
            assert_matches_type(BatimentGroupeRncListResponse, batiment_groupe_rnc, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatimentGroupeRnc:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnbAPI) -> None:
        batiment_groupe_rnc = await async_client.tables_bdnb.donnees.batiment_groupe_rnc.list()
        assert_matches_type(BatimentGroupeRncListResponse, batiment_groupe_rnc, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        batiment_groupe_rnc = await async_client.tables_bdnb.donnees.batiment_groupe_rnc.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            copro_dans_pvd="copro_dans_pvd",
            l_annee_construction="l_annee_construction",
            l_nom_copro="l_nom_copro",
            l_siret="l_siret",
            limit="limit",
            nb_log="nb_log",
            nb_lot_garpark="nb_lot_garpark",
            nb_lot_tertiaire="nb_lot_tertiaire",
            nb_lot_tot="nb_lot_tot",
            numero_immat_principal="numero_immat_principal",
            offset="offset",
            order="order",
            periode_construction_max="periode_construction_max",
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(BatimentGroupeRncListResponse, batiment_groupe_rnc, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.tables_bdnb.donnees.batiment_groupe_rnc.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_groupe_rnc = await response.parse()
        assert_matches_type(BatimentGroupeRncListResponse, batiment_groupe_rnc, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.tables_bdnb.donnees.batiment_groupe_rnc.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_groupe_rnc = await response.parse()
            assert_matches_type(BatimentGroupeRncListResponse, batiment_groupe_rnc, path=["response"])

        assert cast(Any, response.is_closed) is True
