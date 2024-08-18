# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client.pagination import SyncDefault, AsyncDefault
from bdnb_client.types.metadonnees import Colonne

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestColonnes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        colonne = client.metadonnees.colonnes.list()
        assert_matches_type(SyncDefault[Colonne], colonne, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        colonne = client.metadonnees.colonnes.list(
            api_expert="api_expert",
            api_open="api_open",
            colonne_gorenove_legacy="colonne_gorenove_legacy",
            contrainte_acces="contrainte_acces",
            description="description",
            description_table="description_table",
            index="index",
            libelle_metier="libelle_metier",
            limit="limit",
            nom_colonne="nom_colonne",
            nom_table="nom_table",
            offset="offset",
            order="order",
            route="route",
            select="select",
            type="type",
            unite="unite",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(SyncDefault[Colonne], colonne, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.metadonnees.colonnes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        colonne = response.parse()
        assert_matches_type(SyncDefault[Colonne], colonne, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.metadonnees.colonnes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            colonne = response.parse()
            assert_matches_type(SyncDefault[Colonne], colonne, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncColonnes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        colonne = await async_client.metadonnees.colonnes.list()
        assert_matches_type(AsyncDefault[Colonne], colonne, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        colonne = await async_client.metadonnees.colonnes.list(
            api_expert="api_expert",
            api_open="api_open",
            colonne_gorenove_legacy="colonne_gorenove_legacy",
            contrainte_acces="contrainte_acces",
            description="description",
            description_table="description_table",
            index="index",
            libelle_metier="libelle_metier",
            limit="limit",
            nom_colonne="nom_colonne",
            nom_table="nom_table",
            offset="offset",
            order="order",
            route="route",
            select="select",
            type="type",
            unite="unite",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AsyncDefault[Colonne], colonne, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.metadonnees.colonnes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        colonne = await response.parse()
        assert_matches_type(AsyncDefault[Colonne], colonne, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.metadonnees.colonnes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            colonne = await response.parse()
            assert_matches_type(AsyncDefault[Colonne], colonne, path=["response"])

        assert cast(Any, response.is_closed) is True
