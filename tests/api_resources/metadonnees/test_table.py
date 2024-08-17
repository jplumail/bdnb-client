# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import BdnbAPI, AsyncBdnbAPI
from tests.utils import assert_matches_type
from bdnb_api.types.metadonnees import TableListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTable:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: BdnbAPI) -> None:
        table = client.metadonnees.table.list()
        assert_matches_type(TableListResponse, table, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: BdnbAPI) -> None:
        table = client.metadonnees.table.list(
            description="description",
            external_pk="external_pk",
            limit="limit",
            nom_table="nom_table",
            offset="offset",
            order="order",
            quality_elements="quality_elements",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(TableListResponse, table, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BdnbAPI) -> None:
        response = client.metadonnees.table.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert_matches_type(TableListResponse, table, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BdnbAPI) -> None:
        with client.metadonnees.table.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert_matches_type(TableListResponse, table, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTable:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnbAPI) -> None:
        table = await async_client.metadonnees.table.list()
        assert_matches_type(TableListResponse, table, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        table = await async_client.metadonnees.table.list(
            description="description",
            external_pk="external_pk",
            limit="limit",
            nom_table="nom_table",
            offset="offset",
            order="order",
            quality_elements="quality_elements",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(TableListResponse, table, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.metadonnees.table.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert_matches_type(TableListResponse, table, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.metadonnees.table.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert_matches_type(TableListResponse, table, path=["response"])

        assert cast(Any, response.is_closed) is True
