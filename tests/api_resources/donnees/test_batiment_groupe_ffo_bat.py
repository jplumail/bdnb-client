# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import BdnbAPI, AsyncBdnbAPI
from tests.utils import assert_matches_type
from bdnb_api.pagination import SyncDefault, AsyncDefault
from bdnb_api.types.donnees import BatimentGroupeFfoBat

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatimentGroupeFfoBat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: BdnbAPI) -> None:
        batiment_groupe_ffo_bat = client.donnees.batiment_groupe_ffo_bat.list()
        assert_matches_type(SyncDefault[BatimentGroupeFfoBat], batiment_groupe_ffo_bat, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: BdnbAPI) -> None:
        batiment_groupe_ffo_bat = client.donnees.batiment_groupe_ffo_bat.list(
            annee_construction="annee_construction",
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            limit="limit",
            mat_mur_txt="mat_mur_txt",
            mat_toit_txt="mat_toit_txt",
            nb_log="nb_log",
            nb_niveau="nb_niveau",
            offset="offset",
            order="order",
            select="select",
            usage_niveau_1_txt="usage_niveau_1_txt",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(SyncDefault[BatimentGroupeFfoBat], batiment_groupe_ffo_bat, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BdnbAPI) -> None:
        response = client.donnees.batiment_groupe_ffo_bat.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_groupe_ffo_bat = response.parse()
        assert_matches_type(SyncDefault[BatimentGroupeFfoBat], batiment_groupe_ffo_bat, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BdnbAPI) -> None:
        with client.donnees.batiment_groupe_ffo_bat.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_groupe_ffo_bat = response.parse()
            assert_matches_type(SyncDefault[BatimentGroupeFfoBat], batiment_groupe_ffo_bat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatimentGroupeFfoBat:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnbAPI) -> None:
        batiment_groupe_ffo_bat = await async_client.donnees.batiment_groupe_ffo_bat.list()
        assert_matches_type(AsyncDefault[BatimentGroupeFfoBat], batiment_groupe_ffo_bat, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        batiment_groupe_ffo_bat = await async_client.donnees.batiment_groupe_ffo_bat.list(
            annee_construction="annee_construction",
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            limit="limit",
            mat_mur_txt="mat_mur_txt",
            mat_toit_txt="mat_toit_txt",
            nb_log="nb_log",
            nb_niveau="nb_niveau",
            offset="offset",
            order="order",
            select="select",
            usage_niveau_1_txt="usage_niveau_1_txt",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AsyncDefault[BatimentGroupeFfoBat], batiment_groupe_ffo_bat, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.donnees.batiment_groupe_ffo_bat.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_groupe_ffo_bat = await response.parse()
        assert_matches_type(AsyncDefault[BatimentGroupeFfoBat], batiment_groupe_ffo_bat, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.donnees.batiment_groupe_ffo_bat.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_groupe_ffo_bat = await response.parse()
            assert_matches_type(AsyncDefault[BatimentGroupeFfoBat], batiment_groupe_ffo_bat, path=["response"])

        assert cast(Any, response.is_closed) is True
