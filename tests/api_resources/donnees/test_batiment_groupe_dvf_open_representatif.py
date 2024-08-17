# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import BdnbAPI, AsyncBdnbAPI
from tests.utils import assert_matches_type
from bdnb_api._utils import parse_date
from bdnb_api.types.donnees import (
    BatimentGroupeDvfOpenRepresentatifListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatimentGroupeDvfOpenRepresentatif:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: BdnbAPI) -> None:
        batiment_groupe_dvf_open_representatif = client.donnees.batiment_groupe_dvf_open_representatif.list()
        assert_matches_type(
            BatimentGroupeDvfOpenRepresentatifListResponse, batiment_groupe_dvf_open_representatif, path=["response"]
        )

    @parametrize
    def test_method_list_with_all_params(self, client: BdnbAPI) -> None:
        batiment_groupe_dvf_open_representatif = client.donnees.batiment_groupe_dvf_open_representatif.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            date_mutation=parse_date("2019-12-27"),
            id_opendata="id_opendata",
            limit="limit",
            nb_appartement_mutee_mutation="nb_appartement_mutee_mutation",
            nb_dependance_mutee_mutation="nb_dependance_mutee_mutation",
            nb_locaux_mutee_mutation="nb_locaux_mutee_mutation",
            nb_locaux_tertiaire_mutee_mutation="nb_locaux_tertiaire_mutee_mutation",
            nb_maison_mutee_mutation="nb_maison_mutee_mutation",
            nb_piece_principale="nb_piece_principale",
            offset="offset",
            order="order",
            prix_m2_local="prix_m2_local",
            prix_m2_terrain="prix_m2_terrain",
            select="select",
            surface_bati_mutee_dependance="surface_bati_mutee_dependance",
            surface_bati_mutee_residencielle_collective="surface_bati_mutee_residencielle_collective",
            surface_bati_mutee_residencielle_individuelle="surface_bati_mutee_residencielle_individuelle",
            surface_bati_mutee_tertiaire="surface_bati_mutee_tertiaire",
            surface_terrain_mutee="surface_terrain_mutee",
            valeur_fonciere="valeur_fonciere",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(
            BatimentGroupeDvfOpenRepresentatifListResponse, batiment_groupe_dvf_open_representatif, path=["response"]
        )

    @parametrize
    def test_raw_response_list(self, client: BdnbAPI) -> None:
        response = client.donnees.batiment_groupe_dvf_open_representatif.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_groupe_dvf_open_representatif = response.parse()
        assert_matches_type(
            BatimentGroupeDvfOpenRepresentatifListResponse, batiment_groupe_dvf_open_representatif, path=["response"]
        )

    @parametrize
    def test_streaming_response_list(self, client: BdnbAPI) -> None:
        with client.donnees.batiment_groupe_dvf_open_representatif.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_groupe_dvf_open_representatif = response.parse()
            assert_matches_type(
                BatimentGroupeDvfOpenRepresentatifListResponse,
                batiment_groupe_dvf_open_representatif,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncBatimentGroupeDvfOpenRepresentatif:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnbAPI) -> None:
        batiment_groupe_dvf_open_representatif = (
            await async_client.donnees.batiment_groupe_dvf_open_representatif.list()
        )
        assert_matches_type(
            BatimentGroupeDvfOpenRepresentatifListResponse, batiment_groupe_dvf_open_representatif, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        batiment_groupe_dvf_open_representatif = await async_client.donnees.batiment_groupe_dvf_open_representatif.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            date_mutation=parse_date("2019-12-27"),
            id_opendata="id_opendata",
            limit="limit",
            nb_appartement_mutee_mutation="nb_appartement_mutee_mutation",
            nb_dependance_mutee_mutation="nb_dependance_mutee_mutation",
            nb_locaux_mutee_mutation="nb_locaux_mutee_mutation",
            nb_locaux_tertiaire_mutee_mutation="nb_locaux_tertiaire_mutee_mutation",
            nb_maison_mutee_mutation="nb_maison_mutee_mutation",
            nb_piece_principale="nb_piece_principale",
            offset="offset",
            order="order",
            prix_m2_local="prix_m2_local",
            prix_m2_terrain="prix_m2_terrain",
            select="select",
            surface_bati_mutee_dependance="surface_bati_mutee_dependance",
            surface_bati_mutee_residencielle_collective="surface_bati_mutee_residencielle_collective",
            surface_bati_mutee_residencielle_individuelle="surface_bati_mutee_residencielle_individuelle",
            surface_bati_mutee_tertiaire="surface_bati_mutee_tertiaire",
            surface_terrain_mutee="surface_terrain_mutee",
            valeur_fonciere="valeur_fonciere",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(
            BatimentGroupeDvfOpenRepresentatifListResponse, batiment_groupe_dvf_open_representatif, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.donnees.batiment_groupe_dvf_open_representatif.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_groupe_dvf_open_representatif = await response.parse()
        assert_matches_type(
            BatimentGroupeDvfOpenRepresentatifListResponse, batiment_groupe_dvf_open_representatif, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.donnees.batiment_groupe_dvf_open_representatif.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_groupe_dvf_open_representatif = await response.parse()
            assert_matches_type(
                BatimentGroupeDvfOpenRepresentatifListResponse,
                batiment_groupe_dvf_open_representatif,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True
