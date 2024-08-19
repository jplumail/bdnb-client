# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client.types.stats import BatimentGroupeJsonStats

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatimentGroupe:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        batiment_groupe = client.stats.batiment_groupe.list(
            groupby="siren,code_departement_insee",
        )
        assert_matches_type(BatimentGroupeJsonStats, batiment_groupe, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        batiment_groupe = client.stats.batiment_groupe.list(
            groupby="siren,code_departement_insee",
            colonnes="nb_batiment,nb_logement",
            epsg=0,
            filter='{"anee_construction":"gte.1980"}',
            output_format="json",
        )
        assert_matches_type(BatimentGroupeJsonStats, batiment_groupe, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.stats.batiment_groupe.with_raw_response.list(
            groupby="siren,code_departement_insee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_groupe = response.parse()
        assert_matches_type(BatimentGroupeJsonStats, batiment_groupe, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.stats.batiment_groupe.with_streaming_response.list(
            groupby="siren,code_departement_insee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_groupe = response.parse()
            assert_matches_type(BatimentGroupeJsonStats, batiment_groupe, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatimentGroupe:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        batiment_groupe = await async_client.stats.batiment_groupe.list(
            groupby="siren,code_departement_insee",
        )
        assert_matches_type(BatimentGroupeJsonStats, batiment_groupe, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        batiment_groupe = await async_client.stats.batiment_groupe.list(
            groupby="siren,code_departement_insee",
            colonnes="nb_batiment,nb_logement",
            epsg=0,
            filter='{"anee_construction":"gte.1980"}',
            output_format="json",
        )
        assert_matches_type(BatimentGroupeJsonStats, batiment_groupe, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.stats.batiment_groupe.with_raw_response.list(
            groupby="siren,code_departement_insee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_groupe = await response.parse()
        assert_matches_type(BatimentGroupeJsonStats, batiment_groupe, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.stats.batiment_groupe.with_streaming_response.list(
            groupby="siren,code_departement_insee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_groupe = await response.parse()
            assert_matches_type(BatimentGroupeJsonStats, batiment_groupe, path=["response"])

        assert cast(Any, response.is_closed) is True