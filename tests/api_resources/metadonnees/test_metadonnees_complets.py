# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import BdnbAPI, AsyncBdnbAPI
from tests.utils import assert_matches_type
from bdnb_api.types.metadonnees import MetadonneesCompletListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetadonneesComplets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: BdnbAPI) -> None:
        metadonnees_complet = client.metadonnees.metadonnees_complets.list()
        assert_matches_type(MetadonneesCompletListResponse, metadonnees_complet, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: BdnbAPI) -> None:
        metadonnees_complet = client.metadonnees.metadonnees_complets.list(
            api_expert="api_expert",
            api_open="api_open",
            colonne_gorenove_legacy="colonne_gorenove_legacy",
            contrainte_acces="contrainte_acces",
            contrainte_acces_table="contrainte_acces_table",
            couverture_spatiale="couverture_spatiale",
            couverture_temporelle="couverture_temporelle",
            date_publication="date_publication",
            denomination_serie="denomination_serie",
            description="description",
            description_jeu_de_donnees="description_jeu_de_donnees",
            description_table="description_table",
            index="index",
            libelle_metier="libelle_metier",
            limit="limit",
            millesime_jeu_de_donnees="millesime_jeu_de_donnees",
            nom_colonne="nom_colonne",
            nom_table="nom_table",
            offset="offset",
            order="order",
            route="route",
            row_number="row_number",
            select="select",
            type="type",
            unite="unite",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(MetadonneesCompletListResponse, metadonnees_complet, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BdnbAPI) -> None:
        response = client.metadonnees.metadonnees_complets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadonnees_complet = response.parse()
        assert_matches_type(MetadonneesCompletListResponse, metadonnees_complet, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BdnbAPI) -> None:
        with client.metadonnees.metadonnees_complets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadonnees_complet = response.parse()
            assert_matches_type(MetadonneesCompletListResponse, metadonnees_complet, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMetadonneesComplets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnbAPI) -> None:
        metadonnees_complet = await async_client.metadonnees.metadonnees_complets.list()
        assert_matches_type(MetadonneesCompletListResponse, metadonnees_complet, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        metadonnees_complet = await async_client.metadonnees.metadonnees_complets.list(
            api_expert="api_expert",
            api_open="api_open",
            colonne_gorenove_legacy="colonne_gorenove_legacy",
            contrainte_acces="contrainte_acces",
            contrainte_acces_table="contrainte_acces_table",
            couverture_spatiale="couverture_spatiale",
            couverture_temporelle="couverture_temporelle",
            date_publication="date_publication",
            denomination_serie="denomination_serie",
            description="description",
            description_jeu_de_donnees="description_jeu_de_donnees",
            description_table="description_table",
            index="index",
            libelle_metier="libelle_metier",
            limit="limit",
            millesime_jeu_de_donnees="millesime_jeu_de_donnees",
            nom_colonne="nom_colonne",
            nom_table="nom_table",
            offset="offset",
            order="order",
            route="route",
            row_number="row_number",
            select="select",
            type="type",
            unite="unite",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(MetadonneesCompletListResponse, metadonnees_complet, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.metadonnees.metadonnees_complets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadonnees_complet = await response.parse()
        assert_matches_type(MetadonneesCompletListResponse, metadonnees_complet, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.metadonnees.metadonnees_complets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadonnees_complet = await response.parse()
            assert_matches_type(MetadonneesCompletListResponse, metadonnees_complet, path=["response"])

        assert cast(Any, response.is_closed) is True
