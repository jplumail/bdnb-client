# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client.pagination import SyncDefault, AsyncDefault
from bdnb_client.types.donnees.relations.batiment_groupe import (
    RelBatimentGroupeProprietaireSiren,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProprietaireSiren:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        proprietaire_siren = client.donnees.relations.batiment_groupe.proprietaire_siren.list()
        assert_matches_type(SyncDefault[RelBatimentGroupeProprietaireSiren], proprietaire_siren, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        proprietaire_siren = client.donnees.relations.batiment_groupe.proprietaire_siren.list(
            bat_prop_denomination_proprietaire="bat_prop_denomination_proprietaire",
            dans_majic_pm="dans_majic_pm",
            is_bailleur="is_bailleur",
            limit="limit",
            nb_locaux_open="nb_locaux_open",
            offset="offset",
            order="order",
            select="select",
            siren="siren",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(SyncDefault[RelBatimentGroupeProprietaireSiren], proprietaire_siren, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.relations.batiment_groupe.proprietaire_siren.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proprietaire_siren = response.parse()
        assert_matches_type(SyncDefault[RelBatimentGroupeProprietaireSiren], proprietaire_siren, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.relations.batiment_groupe.proprietaire_siren.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proprietaire_siren = response.parse()
            assert_matches_type(SyncDefault[RelBatimentGroupeProprietaireSiren], proprietaire_siren, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProprietaireSiren:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        proprietaire_siren = await async_client.donnees.relations.batiment_groupe.proprietaire_siren.list()
        assert_matches_type(AsyncDefault[RelBatimentGroupeProprietaireSiren], proprietaire_siren, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        proprietaire_siren = await async_client.donnees.relations.batiment_groupe.proprietaire_siren.list(
            bat_prop_denomination_proprietaire="bat_prop_denomination_proprietaire",
            dans_majic_pm="dans_majic_pm",
            is_bailleur="is_bailleur",
            limit="limit",
            nb_locaux_open="nb_locaux_open",
            offset="offset",
            order="order",
            select="select",
            siren="siren",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AsyncDefault[RelBatimentGroupeProprietaireSiren], proprietaire_siren, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.relations.batiment_groupe.proprietaire_siren.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proprietaire_siren = await response.parse()
        assert_matches_type(AsyncDefault[RelBatimentGroupeProprietaireSiren], proprietaire_siren, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.relations.batiment_groupe.proprietaire_siren.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proprietaire_siren = await response.parse()
            assert_matches_type(AsyncDefault[RelBatimentGroupeProprietaireSiren], proprietaire_siren, path=["response"])

        assert cast(Any, response.is_closed) is True
