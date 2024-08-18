# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client.pagination import SyncDefault, AsyncDefault
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeMerimee

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMerimee:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        merimee = client.donnees.batiment_groupe.merimee.list()
        assert_matches_type(SyncDefault[BatimentGroupeMerimee], merimee, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        merimee = client.donnees.batiment_groupe.merimee.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            distance_batiment_historique_plus_proche="distance_batiment_historique_plus_proche",
            limit="limit",
            nom_batiment_historique_plus_proche="nom_batiment_historique_plus_proche",
            offset="offset",
            order="order",
            perimetre_bat_historique="perimetre_bat_historique",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(SyncDefault[BatimentGroupeMerimee], merimee, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.batiment_groupe.merimee.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        merimee = response.parse()
        assert_matches_type(SyncDefault[BatimentGroupeMerimee], merimee, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.batiment_groupe.merimee.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            merimee = response.parse()
            assert_matches_type(SyncDefault[BatimentGroupeMerimee], merimee, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMerimee:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        merimee = await async_client.donnees.batiment_groupe.merimee.list()
        assert_matches_type(AsyncDefault[BatimentGroupeMerimee], merimee, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        merimee = await async_client.donnees.batiment_groupe.merimee.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            distance_batiment_historique_plus_proche="distance_batiment_historique_plus_proche",
            limit="limit",
            nom_batiment_historique_plus_proche="nom_batiment_historique_plus_proche",
            offset="offset",
            order="order",
            perimetre_bat_historique="perimetre_bat_historique",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AsyncDefault[BatimentGroupeMerimee], merimee, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.batiment_groupe.merimee.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        merimee = await response.parse()
        assert_matches_type(AsyncDefault[BatimentGroupeMerimee], merimee, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.batiment_groupe.merimee.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            merimee = await response.parse()
            assert_matches_type(AsyncDefault[BatimentGroupeMerimee], merimee, path=["response"])

        assert cast(Any, response.is_closed) is True
