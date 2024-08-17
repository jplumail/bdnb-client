# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import BdnbAPI, AsyncBdnbAPI
from tests.utils import assert_matches_type
from bdnb_api.types.donnees import RelBatimentGroupeAdresseListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRelBatimentGroupeAdresse:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: BdnbAPI) -> None:
        rel_batiment_groupe_adresse = client.donnees.rel_batiment_groupe_adresse.list()
        assert_matches_type(RelBatimentGroupeAdresseListResponse, rel_batiment_groupe_adresse, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: BdnbAPI) -> None:
        rel_batiment_groupe_adresse = client.donnees.rel_batiment_groupe_adresse.list(
            batiment_groupe_id="batiment_groupe_id",
            classe="classe",
            cle_interop_adr="cle_interop_adr",
            code_departement_insee="code_departement_insee",
            geom_bat_adresse="geom_bat_adresse",
            lien_valide="lien_valide",
            limit="limit",
            offset="offset",
            order="order",
            origine="origine",
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(RelBatimentGroupeAdresseListResponse, rel_batiment_groupe_adresse, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BdnbAPI) -> None:
        response = client.donnees.rel_batiment_groupe_adresse.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rel_batiment_groupe_adresse = response.parse()
        assert_matches_type(RelBatimentGroupeAdresseListResponse, rel_batiment_groupe_adresse, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BdnbAPI) -> None:
        with client.donnees.rel_batiment_groupe_adresse.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rel_batiment_groupe_adresse = response.parse()
            assert_matches_type(RelBatimentGroupeAdresseListResponse, rel_batiment_groupe_adresse, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRelBatimentGroupeAdresse:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnbAPI) -> None:
        rel_batiment_groupe_adresse = await async_client.donnees.rel_batiment_groupe_adresse.list()
        assert_matches_type(RelBatimentGroupeAdresseListResponse, rel_batiment_groupe_adresse, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        rel_batiment_groupe_adresse = await async_client.donnees.rel_batiment_groupe_adresse.list(
            batiment_groupe_id="batiment_groupe_id",
            classe="classe",
            cle_interop_adr="cle_interop_adr",
            code_departement_insee="code_departement_insee",
            geom_bat_adresse="geom_bat_adresse",
            lien_valide="lien_valide",
            limit="limit",
            offset="offset",
            order="order",
            origine="origine",
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(RelBatimentGroupeAdresseListResponse, rel_batiment_groupe_adresse, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.donnees.rel_batiment_groupe_adresse.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rel_batiment_groupe_adresse = await response.parse()
        assert_matches_type(RelBatimentGroupeAdresseListResponse, rel_batiment_groupe_adresse, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.donnees.rel_batiment_groupe_adresse.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rel_batiment_groupe_adresse = await response.parse()
            assert_matches_type(RelBatimentGroupeAdresseListResponse, rel_batiment_groupe_adresse, path=["response"])

        assert cast(Any, response.is_closed) is True
