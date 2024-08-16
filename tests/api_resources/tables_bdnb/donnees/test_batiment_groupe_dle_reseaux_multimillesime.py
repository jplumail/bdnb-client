# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import BdnbAPI, AsyncBdnbAPI
from tests.utils import assert_matches_type
from bdnb_api.types.tables_bdnb.donnees import (
    BatimentGroupeDleReseauxMultimillesimeListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatimentGroupeDleReseauxMultimillesime:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: BdnbAPI) -> None:
        batiment_groupe_dle_reseaux_multimillesime = (
            client.tables_bdnb.donnees.batiment_groupe_dle_reseaux_multimillesime.list()
        )
        assert_matches_type(
            BatimentGroupeDleReseauxMultimillesimeListResponse,
            batiment_groupe_dle_reseaux_multimillesime,
            path=["response"],
        )

    @parametrize
    def test_method_list_with_all_params(self, client: BdnbAPI) -> None:
        batiment_groupe_dle_reseaux_multimillesime = (
            client.tables_bdnb.donnees.batiment_groupe_dle_reseaux_multimillesime.list(
                batiment_groupe_id="batiment_groupe_id",
                code_departement_insee="code_departement_insee",
                conso_pro="conso_pro",
                conso_pro_par_pdl="conso_pro_par_pdl",
                conso_res="conso_res",
                conso_res_par_pdl="conso_res_par_pdl",
                conso_tot="conso_tot",
                conso_tot_par_pdl="conso_tot_par_pdl",
                identifiant_reseau="identifiant_reseau",
                limit="limit",
                millesime="millesime",
                nb_pdl_pro="nb_pdl_pro",
                nb_pdl_res="nb_pdl_res",
                nb_pdl_tot="nb_pdl_tot",
                offset="offset",
                order="order",
                select="select",
                type_reseau="type_reseau",
                prefer="count=none",
                range="Range",
                range_unit="Range-Unit",
            )
        )
        assert_matches_type(
            BatimentGroupeDleReseauxMultimillesimeListResponse,
            batiment_groupe_dle_reseaux_multimillesime,
            path=["response"],
        )

    @parametrize
    def test_raw_response_list(self, client: BdnbAPI) -> None:
        response = client.tables_bdnb.donnees.batiment_groupe_dle_reseaux_multimillesime.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_groupe_dle_reseaux_multimillesime = response.parse()
        assert_matches_type(
            BatimentGroupeDleReseauxMultimillesimeListResponse,
            batiment_groupe_dle_reseaux_multimillesime,
            path=["response"],
        )

    @parametrize
    def test_streaming_response_list(self, client: BdnbAPI) -> None:
        with client.tables_bdnb.donnees.batiment_groupe_dle_reseaux_multimillesime.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_groupe_dle_reseaux_multimillesime = response.parse()
            assert_matches_type(
                BatimentGroupeDleReseauxMultimillesimeListResponse,
                batiment_groupe_dle_reseaux_multimillesime,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncBatimentGroupeDleReseauxMultimillesime:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnbAPI) -> None:
        batiment_groupe_dle_reseaux_multimillesime = (
            await async_client.tables_bdnb.donnees.batiment_groupe_dle_reseaux_multimillesime.list()
        )
        assert_matches_type(
            BatimentGroupeDleReseauxMultimillesimeListResponse,
            batiment_groupe_dle_reseaux_multimillesime,
            path=["response"],
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        batiment_groupe_dle_reseaux_multimillesime = (
            await async_client.tables_bdnb.donnees.batiment_groupe_dle_reseaux_multimillesime.list(
                batiment_groupe_id="batiment_groupe_id",
                code_departement_insee="code_departement_insee",
                conso_pro="conso_pro",
                conso_pro_par_pdl="conso_pro_par_pdl",
                conso_res="conso_res",
                conso_res_par_pdl="conso_res_par_pdl",
                conso_tot="conso_tot",
                conso_tot_par_pdl="conso_tot_par_pdl",
                identifiant_reseau="identifiant_reseau",
                limit="limit",
                millesime="millesime",
                nb_pdl_pro="nb_pdl_pro",
                nb_pdl_res="nb_pdl_res",
                nb_pdl_tot="nb_pdl_tot",
                offset="offset",
                order="order",
                select="select",
                type_reseau="type_reseau",
                prefer="count=none",
                range="Range",
                range_unit="Range-Unit",
            )
        )
        assert_matches_type(
            BatimentGroupeDleReseauxMultimillesimeListResponse,
            batiment_groupe_dle_reseaux_multimillesime,
            path=["response"],
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnbAPI) -> None:
        response = (
            await async_client.tables_bdnb.donnees.batiment_groupe_dle_reseaux_multimillesime.with_raw_response.list()
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_groupe_dle_reseaux_multimillesime = await response.parse()
        assert_matches_type(
            BatimentGroupeDleReseauxMultimillesimeListResponse,
            batiment_groupe_dle_reseaux_multimillesime,
            path=["response"],
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.tables_bdnb.donnees.batiment_groupe_dle_reseaux_multimillesime.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_groupe_dle_reseaux_multimillesime = await response.parse()
            assert_matches_type(
                BatimentGroupeDleReseauxMultimillesimeListResponse,
                batiment_groupe_dle_reseaux_multimillesime,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True
