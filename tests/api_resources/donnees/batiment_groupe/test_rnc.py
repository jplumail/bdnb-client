# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client.pagination import SyncDefault, AsyncDefault
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeRnc

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRnc:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        rnc = client.donnees.batiment_groupe.rnc.list()
        assert_matches_type(SyncDefault[BatimentGroupeRnc], rnc, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        rnc = client.donnees.batiment_groupe.rnc.list(
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
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(SyncDefault[BatimentGroupeRnc], rnc, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.batiment_groupe.rnc.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rnc = response.parse()
        assert_matches_type(SyncDefault[BatimentGroupeRnc], rnc, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.batiment_groupe.rnc.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rnc = response.parse()
            assert_matches_type(SyncDefault[BatimentGroupeRnc], rnc, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRnc:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        rnc = await async_client.donnees.batiment_groupe.rnc.list()
        assert_matches_type(AsyncDefault[BatimentGroupeRnc], rnc, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        rnc = await async_client.donnees.batiment_groupe.rnc.list(
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
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AsyncDefault[BatimentGroupeRnc], rnc, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.batiment_groupe.rnc.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rnc = await response.parse()
        assert_matches_type(AsyncDefault[BatimentGroupeRnc], rnc, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.batiment_groupe.rnc.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rnc = await response.parse()
            assert_matches_type(AsyncDefault[BatimentGroupeRnc], rnc, path=["response"])

        assert cast(Any, response.is_closed) is True
