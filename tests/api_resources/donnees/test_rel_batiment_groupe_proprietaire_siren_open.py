# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_api.pagination import SyncDefault, AsyncDefault
from bdnb_api.types.donnees import (
    RelBatimentGroupeProprietaireSirenOpen,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRelBatimentGroupeProprietaireSirenOpen:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        rel_batiment_groupe_proprietaire_siren_open = client.donnees.rel_batiment_groupe_proprietaire_siren_open.list()
        assert_matches_type(
            SyncDefault[RelBatimentGroupeProprietaireSirenOpen],
            rel_batiment_groupe_proprietaire_siren_open,
            path=["response"],
        )

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        rel_batiment_groupe_proprietaire_siren_open = client.donnees.rel_batiment_groupe_proprietaire_siren_open.list(
            bat_prop_denomination_proprietaire="bat_prop_denomination_proprietaire",
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
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
        assert_matches_type(
            SyncDefault[RelBatimentGroupeProprietaireSirenOpen],
            rel_batiment_groupe_proprietaire_siren_open,
            path=["response"],
        )

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.rel_batiment_groupe_proprietaire_siren_open.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rel_batiment_groupe_proprietaire_siren_open = response.parse()
        assert_matches_type(
            SyncDefault[RelBatimentGroupeProprietaireSirenOpen],
            rel_batiment_groupe_proprietaire_siren_open,
            path=["response"],
        )

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.rel_batiment_groupe_proprietaire_siren_open.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rel_batiment_groupe_proprietaire_siren_open = response.parse()
            assert_matches_type(
                SyncDefault[RelBatimentGroupeProprietaireSirenOpen],
                rel_batiment_groupe_proprietaire_siren_open,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncRelBatimentGroupeProprietaireSirenOpen:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        rel_batiment_groupe_proprietaire_siren_open = (
            await async_client.donnees.rel_batiment_groupe_proprietaire_siren_open.list()
        )
        assert_matches_type(
            AsyncDefault[RelBatimentGroupeProprietaireSirenOpen],
            rel_batiment_groupe_proprietaire_siren_open,
            path=["response"],
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        rel_batiment_groupe_proprietaire_siren_open = (
            await async_client.donnees.rel_batiment_groupe_proprietaire_siren_open.list(
                bat_prop_denomination_proprietaire="bat_prop_denomination_proprietaire",
                batiment_groupe_id="batiment_groupe_id",
                code_departement_insee="code_departement_insee",
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
        )
        assert_matches_type(
            AsyncDefault[RelBatimentGroupeProprietaireSirenOpen],
            rel_batiment_groupe_proprietaire_siren_open,
            path=["response"],
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.rel_batiment_groupe_proprietaire_siren_open.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rel_batiment_groupe_proprietaire_siren_open = await response.parse()
        assert_matches_type(
            AsyncDefault[RelBatimentGroupeProprietaireSirenOpen],
            rel_batiment_groupe_proprietaire_siren_open,
            path=["response"],
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.rel_batiment_groupe_proprietaire_siren_open.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rel_batiment_groupe_proprietaire_siren_open = await response.parse()
            assert_matches_type(
                AsyncDefault[RelBatimentGroupeProprietaireSirenOpen],
                rel_batiment_groupe_proprietaire_siren_open,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True
