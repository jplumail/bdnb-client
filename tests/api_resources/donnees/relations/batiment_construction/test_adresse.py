# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client.pagination import SyncDefault, AsyncDefault
from bdnb_client.types.donnees.relations.batiment_construction import (
    RelBatimentConstructionAdresse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdresse:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        adresse = client.donnees.relations.batiment_construction.adresse.list()
        assert_matches_type(SyncDefault[RelBatimentConstructionAdresse], adresse, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        adresse = client.donnees.relations.batiment_construction.adresse.list(
            adresse_principale="adresse_principale",
            batiment_construction_id="batiment_construction_id",
            cle_interop_adr="cle_interop_adr",
            code_departement_insee="code_departement_insee",
            distance_batiment_construction_adresse="distance_batiment_construction_adresse",
            fiabilite="fiabilite",
            limit="limit",
            offset="offset",
            order="order",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(SyncDefault[RelBatimentConstructionAdresse], adresse, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.relations.batiment_construction.adresse.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        adresse = response.parse()
        assert_matches_type(SyncDefault[RelBatimentConstructionAdresse], adresse, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.relations.batiment_construction.adresse.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            adresse = response.parse()
            assert_matches_type(SyncDefault[RelBatimentConstructionAdresse], adresse, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAdresse:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        adresse = await async_client.donnees.relations.batiment_construction.adresse.list()
        assert_matches_type(AsyncDefault[RelBatimentConstructionAdresse], adresse, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        adresse = await async_client.donnees.relations.batiment_construction.adresse.list(
            adresse_principale="adresse_principale",
            batiment_construction_id="batiment_construction_id",
            cle_interop_adr="cle_interop_adr",
            code_departement_insee="code_departement_insee",
            distance_batiment_construction_adresse="distance_batiment_construction_adresse",
            fiabilite="fiabilite",
            limit="limit",
            offset="offset",
            order="order",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AsyncDefault[RelBatimentConstructionAdresse], adresse, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.relations.batiment_construction.adresse.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        adresse = await response.parse()
        assert_matches_type(AsyncDefault[RelBatimentConstructionAdresse], adresse, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.relations.batiment_construction.adresse.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            adresse = await response.parse()
            assert_matches_type(AsyncDefault[RelBatimentConstructionAdresse], adresse, path=["response"])

        assert cast(Any, response.is_closed) is True
