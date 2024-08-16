# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import BdnbAPI, AsyncBdnbAPI
from tests.utils import assert_matches_type
from bdnb_api.types.metadonnees import JeuDeDonneeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJeuDeDonnees:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: BdnbAPI) -> None:
        jeu_de_donnee = client.metadonnees.jeu_de_donnees.list()
        assert_matches_type(JeuDeDonneeListResponse, jeu_de_donnee, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: BdnbAPI) -> None:
        jeu_de_donnee = client.metadonnees.jeu_de_donnees.list(
            contrainte_acces="contrainte_acces",
            couverture_spatiale="couverture_spatiale",
            couverture_temporelle="couverture_temporelle",
            date_publication="date_publication",
            denomination_serie="denomination_serie",
            description="description",
            limit="limit",
            millesime_jeu_de_donnees="millesime_jeu_de_donnees",
            offset="offset",
            order="order",
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(JeuDeDonneeListResponse, jeu_de_donnee, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BdnbAPI) -> None:
        response = client.metadonnees.jeu_de_donnees.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        jeu_de_donnee = response.parse()
        assert_matches_type(JeuDeDonneeListResponse, jeu_de_donnee, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BdnbAPI) -> None:
        with client.metadonnees.jeu_de_donnees.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            jeu_de_donnee = response.parse()
            assert_matches_type(JeuDeDonneeListResponse, jeu_de_donnee, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncJeuDeDonnees:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnbAPI) -> None:
        jeu_de_donnee = await async_client.metadonnees.jeu_de_donnees.list()
        assert_matches_type(JeuDeDonneeListResponse, jeu_de_donnee, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        jeu_de_donnee = await async_client.metadonnees.jeu_de_donnees.list(
            contrainte_acces="contrainte_acces",
            couverture_spatiale="couverture_spatiale",
            couverture_temporelle="couverture_temporelle",
            date_publication="date_publication",
            denomination_serie="denomination_serie",
            description="description",
            limit="limit",
            millesime_jeu_de_donnees="millesime_jeu_de_donnees",
            offset="offset",
            order="order",
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(JeuDeDonneeListResponse, jeu_de_donnee, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.metadonnees.jeu_de_donnees.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        jeu_de_donnee = await response.parse()
        assert_matches_type(JeuDeDonneeListResponse, jeu_de_donnee, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.metadonnees.jeu_de_donnees.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            jeu_de_donnee = await response.parse()
            assert_matches_type(JeuDeDonneeListResponse, jeu_de_donnee, path=["response"])

        assert cast(Any, response.is_closed) is True
