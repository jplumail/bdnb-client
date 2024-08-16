# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import BdnbAPI, AsyncBdnbAPI
from tests.utils import assert_matches_type
from bdnb_api.types.donnees import BatimentGroupeAdresseListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatimentGroupeAdresse:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: BdnbAPI) -> None:
        batiment_groupe_adresse = client.donnees.batiment_groupe_adresse.list()
        assert_matches_type(BatimentGroupeAdresseListResponse, batiment_groupe_adresse, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: BdnbAPI) -> None:
        batiment_groupe_adresse = client.donnees.batiment_groupe_adresse.list(
            batiment_groupe_id="batiment_groupe_id",
            cle_interop_adr_principale_ban="cle_interop_adr_principale_ban",
            code_departement_insee="code_departement_insee",
            fiabilite_cr_adr_niv_1="fiabilite_cr_adr_niv_1",
            fiabilite_cr_adr_niv_2="fiabilite_cr_adr_niv_2",
            libelle_adr_principale_ban="libelle_adr_principale_ban",
            limit="limit",
            nb_adresse_valid_ban="nb_adresse_valid_ban",
            offset="offset",
            order="order",
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(BatimentGroupeAdresseListResponse, batiment_groupe_adresse, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BdnbAPI) -> None:
        response = client.donnees.batiment_groupe_adresse.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_groupe_adresse = response.parse()
        assert_matches_type(BatimentGroupeAdresseListResponse, batiment_groupe_adresse, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BdnbAPI) -> None:
        with client.donnees.batiment_groupe_adresse.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_groupe_adresse = response.parse()
            assert_matches_type(BatimentGroupeAdresseListResponse, batiment_groupe_adresse, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatimentGroupeAdresse:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnbAPI) -> None:
        batiment_groupe_adresse = await async_client.donnees.batiment_groupe_adresse.list()
        assert_matches_type(BatimentGroupeAdresseListResponse, batiment_groupe_adresse, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        batiment_groupe_adresse = await async_client.donnees.batiment_groupe_adresse.list(
            batiment_groupe_id="batiment_groupe_id",
            cle_interop_adr_principale_ban="cle_interop_adr_principale_ban",
            code_departement_insee="code_departement_insee",
            fiabilite_cr_adr_niv_1="fiabilite_cr_adr_niv_1",
            fiabilite_cr_adr_niv_2="fiabilite_cr_adr_niv_2",
            libelle_adr_principale_ban="libelle_adr_principale_ban",
            limit="limit",
            nb_adresse_valid_ban="nb_adresse_valid_ban",
            offset="offset",
            order="order",
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(BatimentGroupeAdresseListResponse, batiment_groupe_adresse, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.donnees.batiment_groupe_adresse.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_groupe_adresse = await response.parse()
        assert_matches_type(BatimentGroupeAdresseListResponse, batiment_groupe_adresse, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.donnees.batiment_groupe_adresse.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_groupe_adresse = await response.parse()
            assert_matches_type(BatimentGroupeAdresseListResponse, batiment_groupe_adresse, path=["response"])

        assert cast(Any, response.is_closed) is True
