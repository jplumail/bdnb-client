# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import BdnbAPI, AsyncBdnbAPI
from tests.utils import assert_matches_type
from bdnb_api.pagination import SyncDefault, AsyncDefault
from bdnb_api.types.donnees import RelBatimentGroupeQpv

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRelBatimentGroupeQpv:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: BdnbAPI) -> None:
        rel_batiment_groupe_qpv = client.donnees.rel_batiment_groupe_qpv.list()
        assert_matches_type(SyncDefault[RelBatimentGroupeQpv], rel_batiment_groupe_qpv, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: BdnbAPI) -> None:
        rel_batiment_groupe_qpv = client.donnees.rel_batiment_groupe_qpv.list(
            batiment_construction_id="batiment_construction_id",
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            limit="limit",
            offset="offset",
            order="order",
            qpv_code_qp="qpv_code_qp",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(SyncDefault[RelBatimentGroupeQpv], rel_batiment_groupe_qpv, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BdnbAPI) -> None:
        response = client.donnees.rel_batiment_groupe_qpv.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rel_batiment_groupe_qpv = response.parse()
        assert_matches_type(SyncDefault[RelBatimentGroupeQpv], rel_batiment_groupe_qpv, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BdnbAPI) -> None:
        with client.donnees.rel_batiment_groupe_qpv.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rel_batiment_groupe_qpv = response.parse()
            assert_matches_type(SyncDefault[RelBatimentGroupeQpv], rel_batiment_groupe_qpv, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRelBatimentGroupeQpv:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnbAPI) -> None:
        rel_batiment_groupe_qpv = await async_client.donnees.rel_batiment_groupe_qpv.list()
        assert_matches_type(AsyncDefault[RelBatimentGroupeQpv], rel_batiment_groupe_qpv, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        rel_batiment_groupe_qpv = await async_client.donnees.rel_batiment_groupe_qpv.list(
            batiment_construction_id="batiment_construction_id",
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            limit="limit",
            offset="offset",
            order="order",
            qpv_code_qp="qpv_code_qp",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AsyncDefault[RelBatimentGroupeQpv], rel_batiment_groupe_qpv, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.donnees.rel_batiment_groupe_qpv.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rel_batiment_groupe_qpv = await response.parse()
        assert_matches_type(AsyncDefault[RelBatimentGroupeQpv], rel_batiment_groupe_qpv, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.donnees.rel_batiment_groupe_qpv.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rel_batiment_groupe_qpv = await response.parse()
            assert_matches_type(AsyncDefault[RelBatimentGroupeQpv], rel_batiment_groupe_qpv, path=["response"])

        assert cast(Any, response.is_closed) is True
