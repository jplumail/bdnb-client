# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client.pagination import SyncDefault, AsyncDefault
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupe

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatimentGroupe:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        batiment_groupe = client.donnees.batiment_groupe.list()
        assert_matches_type(SyncDefault[BatimentGroupe], batiment_groupe, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        batiment_groupe = client.donnees.batiment_groupe.list(
            batiment_groupe_id="batiment_groupe_id",
            code_commune_insee="code_commune_insee",
            code_departement_insee="code_departement_insee",
            code_epci_insee="code_epci_insee",
            code_iris="code_iris",
            code_qp="code_qp",
            code_region_insee="code_region_insee",
            contient_fictive_geom_groupe="contient_fictive_geom_groupe",
            geom_groupe="geom_groupe",
            geom_groupe_pos_wgs84="geom_groupe_pos_wgs84",
            libelle_commune_insee="libelle_commune_insee",
            limit="limit",
            nom_qp="nom_qp",
            offset="offset",
            order="order",
            quartier_prioritaire="quartier_prioritaire",
            s_geom_groupe="s_geom_groupe",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(SyncDefault[BatimentGroupe], batiment_groupe, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.batiment_groupe.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_groupe = response.parse()
        assert_matches_type(SyncDefault[BatimentGroupe], batiment_groupe, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.batiment_groupe.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_groupe = response.parse()
            assert_matches_type(SyncDefault[BatimentGroupe], batiment_groupe, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatimentGroupe:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        batiment_groupe = await async_client.donnees.batiment_groupe.list()
        assert_matches_type(AsyncDefault[BatimentGroupe], batiment_groupe, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        batiment_groupe = await async_client.donnees.batiment_groupe.list(
            batiment_groupe_id="batiment_groupe_id",
            code_commune_insee="code_commune_insee",
            code_departement_insee="code_departement_insee",
            code_epci_insee="code_epci_insee",
            code_iris="code_iris",
            code_qp="code_qp",
            code_region_insee="code_region_insee",
            contient_fictive_geom_groupe="contient_fictive_geom_groupe",
            geom_groupe="geom_groupe",
            geom_groupe_pos_wgs84="geom_groupe_pos_wgs84",
            libelle_commune_insee="libelle_commune_insee",
            limit="limit",
            nom_qp="nom_qp",
            offset="offset",
            order="order",
            quartier_prioritaire="quartier_prioritaire",
            s_geom_groupe="s_geom_groupe",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AsyncDefault[BatimentGroupe], batiment_groupe, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.batiment_groupe.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_groupe = await response.parse()
        assert_matches_type(AsyncDefault[BatimentGroupe], batiment_groupe, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.batiment_groupe.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_groupe = await response.parse()
            assert_matches_type(AsyncDefault[BatimentGroupe], batiment_groupe, path=["response"])

        assert cast(Any, response.is_closed) is True
