# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client.pagination import SyncDefault, AsyncDefault
from bdnb_client.types.metadonnees import Table

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTable:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        table = client.metadonnees.table.list()
        assert_matches_type(SyncDefault[Table], table, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
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
        assert_matches_type(SyncDefault[Table], table, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.metadonnees.table.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert_matches_type(SyncDefault[Table], table, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.metadonnees.table.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert_matches_type(SyncDefault[Table], table, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTable:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        table = await async_client.metadonnees.table.list()
        assert_matches_type(AsyncDefault[Table], table, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
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
        assert_matches_type(AsyncDefault[Table], table, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.metadonnees.table.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert_matches_type(AsyncDefault[Table], table, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.metadonnees.table.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert_matches_type(AsyncDefault[Table], table, path=["response"])

        assert cast(Any, response.is_closed) is True
