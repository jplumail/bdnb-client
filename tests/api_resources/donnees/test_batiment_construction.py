# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client.pagination import SyncDefault, AsyncDefault
from bdnb_client.types.donnees import BatimentConstruction

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatimentConstruction:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        batiment_construction = client.donnees.batiment_construction.list()
        assert_matches_type(SyncDefault[BatimentConstruction], batiment_construction, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        batiment_construction = client.donnees.batiment_construction.list(
            altitude_sol="altitude_sol",
            batiment_construction_id="batiment_construction_id",
            batiment_groupe_id="batiment_groupe_id",
            code_commune_insee="code_commune_insee",
            code_departement_insee="code_departement_insee",
            code_iris="code_iris",
            fictive_geom_cstr="fictive_geom_cstr",
            geom_cstr="geom_cstr",
            hauteur="hauteur",
            limit="limit",
            offset="offset",
            order="order",
            rnb_id="rnb_id",
            s_geom_cstr="s_geom_cstr",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(SyncDefault[BatimentConstruction], batiment_construction, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.batiment_construction.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_construction = response.parse()
        assert_matches_type(SyncDefault[BatimentConstruction], batiment_construction, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.batiment_construction.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_construction = response.parse()
            assert_matches_type(SyncDefault[BatimentConstruction], batiment_construction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatimentConstruction:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        batiment_construction = await async_client.donnees.batiment_construction.list()
        assert_matches_type(AsyncDefault[BatimentConstruction], batiment_construction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        batiment_construction = await async_client.donnees.batiment_construction.list(
            altitude_sol="altitude_sol",
            batiment_construction_id="batiment_construction_id",
            batiment_groupe_id="batiment_groupe_id",
            code_commune_insee="code_commune_insee",
            code_departement_insee="code_departement_insee",
            code_iris="code_iris",
            fictive_geom_cstr="fictive_geom_cstr",
            geom_cstr="geom_cstr",
            hauteur="hauteur",
            limit="limit",
            offset="offset",
            order="order",
            rnb_id="rnb_id",
            s_geom_cstr="s_geom_cstr",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AsyncDefault[BatimentConstruction], batiment_construction, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.batiment_construction.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_construction = await response.parse()
        assert_matches_type(AsyncDefault[BatimentConstruction], batiment_construction, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.batiment_construction.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_construction = await response.parse()
            assert_matches_type(AsyncDefault[BatimentConstruction], batiment_construction, path=["response"])

        assert cast(Any, response.is_closed) is True
