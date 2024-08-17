# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import BdnbAPI, AsyncBdnbAPI
from tests.utils import assert_matches_type
from bdnb_api.types.donnees import BatimentGroupeBdtopoZoacListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatimentGroupeBdtopoZoac:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: BdnbAPI) -> None:
        batiment_groupe_bdtopo_zoac = client.donnees.batiment_groupe_bdtopo_zoac.list()
        assert_matches_type(BatimentGroupeBdtopoZoacListResponse, batiment_groupe_bdtopo_zoac, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: BdnbAPI) -> None:
        batiment_groupe_bdtopo_zoac = client.donnees.batiment_groupe_bdtopo_zoac.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            l_nature="l_nature",
            l_nature_detaillee="l_nature_detaillee",
            l_toponyme="l_toponyme",
            limit="limit",
            offset="offset",
            order="order",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(BatimentGroupeBdtopoZoacListResponse, batiment_groupe_bdtopo_zoac, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BdnbAPI) -> None:
        response = client.donnees.batiment_groupe_bdtopo_zoac.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_groupe_bdtopo_zoac = response.parse()
        assert_matches_type(BatimentGroupeBdtopoZoacListResponse, batiment_groupe_bdtopo_zoac, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BdnbAPI) -> None:
        with client.donnees.batiment_groupe_bdtopo_zoac.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_groupe_bdtopo_zoac = response.parse()
            assert_matches_type(BatimentGroupeBdtopoZoacListResponse, batiment_groupe_bdtopo_zoac, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatimentGroupeBdtopoZoac:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnbAPI) -> None:
        batiment_groupe_bdtopo_zoac = await async_client.donnees.batiment_groupe_bdtopo_zoac.list()
        assert_matches_type(BatimentGroupeBdtopoZoacListResponse, batiment_groupe_bdtopo_zoac, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        batiment_groupe_bdtopo_zoac = await async_client.donnees.batiment_groupe_bdtopo_zoac.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            l_nature="l_nature",
            l_nature_detaillee="l_nature_detaillee",
            l_toponyme="l_toponyme",
            limit="limit",
            offset="offset",
            order="order",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(BatimentGroupeBdtopoZoacListResponse, batiment_groupe_bdtopo_zoac, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.donnees.batiment_groupe_bdtopo_zoac.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_groupe_bdtopo_zoac = await response.parse()
        assert_matches_type(BatimentGroupeBdtopoZoacListResponse, batiment_groupe_bdtopo_zoac, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.donnees.batiment_groupe_bdtopo_zoac.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_groupe_bdtopo_zoac = await response.parse()
            assert_matches_type(BatimentGroupeBdtopoZoacListResponse, batiment_groupe_bdtopo_zoac, path=["response"])

        assert cast(Any, response.is_closed) is True
