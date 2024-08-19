# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client.types.donnees.relations.batiment_groupe import QpvListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQpv:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        qpv = client.donnees.relations.batiment_groupe.qpv.list()
        assert_matches_type(QpvListResponse, qpv, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        qpv = client.donnees.relations.batiment_groupe.qpv.list(
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
        assert_matches_type(QpvListResponse, qpv, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.relations.batiment_groupe.qpv.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qpv = response.parse()
        assert_matches_type(QpvListResponse, qpv, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.relations.batiment_groupe.qpv.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qpv = response.parse()
            assert_matches_type(QpvListResponse, qpv, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQpv:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        qpv = await async_client.donnees.relations.batiment_groupe.qpv.list()
        assert_matches_type(QpvListResponse, qpv, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        qpv = await async_client.donnees.relations.batiment_groupe.qpv.list(
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
        assert_matches_type(QpvListResponse, qpv, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.relations.batiment_groupe.qpv.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qpv = await response.parse()
        assert_matches_type(QpvListResponse, qpv, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.relations.batiment_groupe.qpv.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qpv = await response.parse()
            assert_matches_type(QpvListResponse, qpv, path=["response"])

        assert cast(Any, response.is_closed) is True