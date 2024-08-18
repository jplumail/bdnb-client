# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client.pagination import SyncDefault, AsyncDefault
from bdnb_client.types.donnees.batiment_groupe import (
    BatimentGroupeDleGazMultimillesime,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDleGazMultimillesime:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        dle_gaz_multimillesime = client.donnees.batiment_groupe.dle_gaz_multimillesime.list()
        assert_matches_type(SyncDefault[BatimentGroupeDleGazMultimillesime], dle_gaz_multimillesime, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        dle_gaz_multimillesime = client.donnees.batiment_groupe.dle_gaz_multimillesime.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            conso_pro="conso_pro",
            conso_pro_par_pdl="conso_pro_par_pdl",
            conso_res="conso_res",
            conso_res_par_pdl="conso_res_par_pdl",
            conso_tot="conso_tot",
            conso_tot_par_pdl="conso_tot_par_pdl",
            limit="limit",
            millesime="millesime",
            nb_pdl_pro="nb_pdl_pro",
            nb_pdl_res="nb_pdl_res",
            nb_pdl_tot="nb_pdl_tot",
            offset="offset",
            order="order",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(SyncDefault[BatimentGroupeDleGazMultimillesime], dle_gaz_multimillesime, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.batiment_groupe.dle_gaz_multimillesime.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dle_gaz_multimillesime = response.parse()
        assert_matches_type(SyncDefault[BatimentGroupeDleGazMultimillesime], dle_gaz_multimillesime, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.batiment_groupe.dle_gaz_multimillesime.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dle_gaz_multimillesime = response.parse()
            assert_matches_type(
                SyncDefault[BatimentGroupeDleGazMultimillesime], dle_gaz_multimillesime, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncDleGazMultimillesime:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        dle_gaz_multimillesime = await async_client.donnees.batiment_groupe.dle_gaz_multimillesime.list()
        assert_matches_type(AsyncDefault[BatimentGroupeDleGazMultimillesime], dle_gaz_multimillesime, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        dle_gaz_multimillesime = await async_client.donnees.batiment_groupe.dle_gaz_multimillesime.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            conso_pro="conso_pro",
            conso_pro_par_pdl="conso_pro_par_pdl",
            conso_res="conso_res",
            conso_res_par_pdl="conso_res_par_pdl",
            conso_tot="conso_tot",
            conso_tot_par_pdl="conso_tot_par_pdl",
            limit="limit",
            millesime="millesime",
            nb_pdl_pro="nb_pdl_pro",
            nb_pdl_res="nb_pdl_res",
            nb_pdl_tot="nb_pdl_tot",
            offset="offset",
            order="order",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AsyncDefault[BatimentGroupeDleGazMultimillesime], dle_gaz_multimillesime, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.batiment_groupe.dle_gaz_multimillesime.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dle_gaz_multimillesime = await response.parse()
        assert_matches_type(AsyncDefault[BatimentGroupeDleGazMultimillesime], dle_gaz_multimillesime, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.batiment_groupe.dle_gaz_multimillesime.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dle_gaz_multimillesime = await response.parse()
            assert_matches_type(
                AsyncDefault[BatimentGroupeDleGazMultimillesime], dle_gaz_multimillesime, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
