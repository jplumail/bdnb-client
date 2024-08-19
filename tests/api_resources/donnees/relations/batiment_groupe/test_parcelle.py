# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client.pagination import SyncDefault, AsyncDefault
from bdnb_client.types.donnees.relations.batiment_groupe import RelBatimentGroupeParcelle

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParcelle:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        parcelle = client.donnees.relations.batiment_groupe.parcelle.list()
        assert_matches_type(SyncDefault[RelBatimentGroupeParcelle], parcelle, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        parcelle = client.donnees.relations.batiment_groupe.parcelle.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            limit="limit",
            offset="offset",
            order="order",
            parcelle_id="parcelle_id",
            parcelle_principale="parcelle_principale",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(SyncDefault[RelBatimentGroupeParcelle], parcelle, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.relations.batiment_groupe.parcelle.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parcelle = response.parse()
        assert_matches_type(SyncDefault[RelBatimentGroupeParcelle], parcelle, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.relations.batiment_groupe.parcelle.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parcelle = response.parse()
            assert_matches_type(SyncDefault[RelBatimentGroupeParcelle], parcelle, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncParcelle:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        parcelle = await async_client.donnees.relations.batiment_groupe.parcelle.list()
        assert_matches_type(AsyncDefault[RelBatimentGroupeParcelle], parcelle, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        parcelle = await async_client.donnees.relations.batiment_groupe.parcelle.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            limit="limit",
            offset="offset",
            order="order",
            parcelle_id="parcelle_id",
            parcelle_principale="parcelle_principale",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AsyncDefault[RelBatimentGroupeParcelle], parcelle, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.relations.batiment_groupe.parcelle.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parcelle = await response.parse()
        assert_matches_type(AsyncDefault[RelBatimentGroupeParcelle], parcelle, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.relations.batiment_groupe.parcelle.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parcelle = await response.parse()
            assert_matches_type(AsyncDefault[RelBatimentGroupeParcelle], parcelle, path=["response"])

        assert cast(Any, response.is_closed) is True
