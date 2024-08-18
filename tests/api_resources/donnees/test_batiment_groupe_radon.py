# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_api.pagination import SyncDefault, AsyncDefault
from bdnb_api.types.donnees import BatimentGroupeRadon

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatimentGroupeRadon:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        batiment_groupe_radon = client.donnees.batiment_groupe_radon.list()
        assert_matches_type(SyncDefault[BatimentGroupeRadon], batiment_groupe_radon, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        batiment_groupe_radon = client.donnees.batiment_groupe_radon.list(
            alea="alea",
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            limit="limit",
            offset="offset",
            order="order",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(SyncDefault[BatimentGroupeRadon], batiment_groupe_radon, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.batiment_groupe_radon.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_groupe_radon = response.parse()
        assert_matches_type(SyncDefault[BatimentGroupeRadon], batiment_groupe_radon, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.batiment_groupe_radon.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_groupe_radon = response.parse()
            assert_matches_type(SyncDefault[BatimentGroupeRadon], batiment_groupe_radon, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatimentGroupeRadon:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        batiment_groupe_radon = await async_client.donnees.batiment_groupe_radon.list()
        assert_matches_type(AsyncDefault[BatimentGroupeRadon], batiment_groupe_radon, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        batiment_groupe_radon = await async_client.donnees.batiment_groupe_radon.list(
            alea="alea",
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            limit="limit",
            offset="offset",
            order="order",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AsyncDefault[BatimentGroupeRadon], batiment_groupe_radon, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.batiment_groupe_radon.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_groupe_radon = await response.parse()
        assert_matches_type(AsyncDefault[BatimentGroupeRadon], batiment_groupe_radon, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.batiment_groupe_radon.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_groupe_radon = await response.parse()
            assert_matches_type(AsyncDefault[BatimentGroupeRadon], batiment_groupe_radon, path=["response"])

        assert cast(Any, response.is_closed) is True
