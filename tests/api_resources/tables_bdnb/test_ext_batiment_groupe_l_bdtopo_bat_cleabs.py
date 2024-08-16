# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import BdnbAPI, AsyncBdnbAPI
from tests.utils import assert_matches_type
from bdnb_api.types.tables_bdnb import (
    ExtBatimentGroupeLBdtopoBatCleabListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExtBatimentGroupeLBdtopoBatCleabs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: BdnbAPI) -> None:
        ext_batiment_groupe_l_bdtopo_bat_cleab = client.tables_bdnb.ext_batiment_groupe_l_bdtopo_bat_cleabs.list()
        assert_matches_type(
            ExtBatimentGroupeLBdtopoBatCleabListResponse, ext_batiment_groupe_l_bdtopo_bat_cleab, path=["response"]
        )

    @parametrize
    def test_method_list_with_all_params(self, client: BdnbAPI) -> None:
        ext_batiment_groupe_l_bdtopo_bat_cleab = client.tables_bdnb.ext_batiment_groupe_l_bdtopo_bat_cleabs.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            l_bdtopo_bat_cleabs="l_bdtopo_bat_cleabs",
            limit="limit",
            offset="offset",
            order="order",
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(
            ExtBatimentGroupeLBdtopoBatCleabListResponse, ext_batiment_groupe_l_bdtopo_bat_cleab, path=["response"]
        )

    @parametrize
    def test_raw_response_list(self, client: BdnbAPI) -> None:
        response = client.tables_bdnb.ext_batiment_groupe_l_bdtopo_bat_cleabs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ext_batiment_groupe_l_bdtopo_bat_cleab = response.parse()
        assert_matches_type(
            ExtBatimentGroupeLBdtopoBatCleabListResponse, ext_batiment_groupe_l_bdtopo_bat_cleab, path=["response"]
        )

    @parametrize
    def test_streaming_response_list(self, client: BdnbAPI) -> None:
        with client.tables_bdnb.ext_batiment_groupe_l_bdtopo_bat_cleabs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ext_batiment_groupe_l_bdtopo_bat_cleab = response.parse()
            assert_matches_type(
                ExtBatimentGroupeLBdtopoBatCleabListResponse, ext_batiment_groupe_l_bdtopo_bat_cleab, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncExtBatimentGroupeLBdtopoBatCleabs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnbAPI) -> None:
        ext_batiment_groupe_l_bdtopo_bat_cleab = (
            await async_client.tables_bdnb.ext_batiment_groupe_l_bdtopo_bat_cleabs.list()
        )
        assert_matches_type(
            ExtBatimentGroupeLBdtopoBatCleabListResponse, ext_batiment_groupe_l_bdtopo_bat_cleab, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        ext_batiment_groupe_l_bdtopo_bat_cleab = (
            await async_client.tables_bdnb.ext_batiment_groupe_l_bdtopo_bat_cleabs.list(
                batiment_groupe_id="batiment_groupe_id",
                code_departement_insee="code_departement_insee",
                l_bdtopo_bat_cleabs="l_bdtopo_bat_cleabs",
                limit="limit",
                offset="offset",
                order="order",
                select="select",
                prefer="count=none",
                range="Range",
                range_unit="Range-Unit",
            )
        )
        assert_matches_type(
            ExtBatimentGroupeLBdtopoBatCleabListResponse, ext_batiment_groupe_l_bdtopo_bat_cleab, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.tables_bdnb.ext_batiment_groupe_l_bdtopo_bat_cleabs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ext_batiment_groupe_l_bdtopo_bat_cleab = await response.parse()
        assert_matches_type(
            ExtBatimentGroupeLBdtopoBatCleabListResponse, ext_batiment_groupe_l_bdtopo_bat_cleab, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.tables_bdnb.ext_batiment_groupe_l_bdtopo_bat_cleabs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ext_batiment_groupe_l_bdtopo_bat_cleab = await response.parse()
            assert_matches_type(
                ExtBatimentGroupeLBdtopoBatCleabListResponse, ext_batiment_groupe_l_bdtopo_bat_cleab, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
