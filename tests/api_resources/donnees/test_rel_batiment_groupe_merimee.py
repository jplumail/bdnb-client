# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_api.pagination import SyncDefault, AsyncDefault
from bdnb_api.types.donnees import RelBatimentGroupeMerimee

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRelBatimentGroupeMerimee:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        rel_batiment_groupe_merimee = client.donnees.rel_batiment_groupe_merimee.list()
        assert_matches_type(SyncDefault[RelBatimentGroupeMerimee], rel_batiment_groupe_merimee, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        rel_batiment_groupe_merimee = client.donnees.rel_batiment_groupe_merimee.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            distance_batiment_historique="distance_batiment_historique",
            limit="limit",
            merimee_ref="merimee_ref",
            offset="offset",
            order="order",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(SyncDefault[RelBatimentGroupeMerimee], rel_batiment_groupe_merimee, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.rel_batiment_groupe_merimee.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rel_batiment_groupe_merimee = response.parse()
        assert_matches_type(SyncDefault[RelBatimentGroupeMerimee], rel_batiment_groupe_merimee, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.rel_batiment_groupe_merimee.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rel_batiment_groupe_merimee = response.parse()
            assert_matches_type(SyncDefault[RelBatimentGroupeMerimee], rel_batiment_groupe_merimee, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRelBatimentGroupeMerimee:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        rel_batiment_groupe_merimee = await async_client.donnees.rel_batiment_groupe_merimee.list()
        assert_matches_type(AsyncDefault[RelBatimentGroupeMerimee], rel_batiment_groupe_merimee, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        rel_batiment_groupe_merimee = await async_client.donnees.rel_batiment_groupe_merimee.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            distance_batiment_historique="distance_batiment_historique",
            limit="limit",
            merimee_ref="merimee_ref",
            offset="offset",
            order="order",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AsyncDefault[RelBatimentGroupeMerimee], rel_batiment_groupe_merimee, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.rel_batiment_groupe_merimee.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rel_batiment_groupe_merimee = await response.parse()
        assert_matches_type(AsyncDefault[RelBatimentGroupeMerimee], rel_batiment_groupe_merimee, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.rel_batiment_groupe_merimee.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rel_batiment_groupe_merimee = await response.parse()
            assert_matches_type(AsyncDefault[RelBatimentGroupeMerimee], rel_batiment_groupe_merimee, path=["response"])

        assert cast(Any, response.is_closed) is True
