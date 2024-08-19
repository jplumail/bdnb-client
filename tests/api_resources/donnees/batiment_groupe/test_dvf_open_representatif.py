# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client._utils import parse_date
from bdnb_client.pagination import SyncDefault, AsyncDefault
from bdnb_client.types.donnees.batiment_groupe import (
    BatimentGroupeDvfOpenRepresentatif,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDvfOpenRepresentatif:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        dvf_open_representatif = client.donnees.batiment_groupe.dvf_open_representatif.list()
        assert_matches_type(SyncDefault[BatimentGroupeDvfOpenRepresentatif], dvf_open_representatif, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        dvf_open_representatif = client.donnees.batiment_groupe.dvf_open_representatif.list(
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
        assert_matches_type(SyncDefault[BatimentGroupeDvfOpenRepresentatif], dvf_open_representatif, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.batiment_groupe.dvf_open_representatif.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dvf_open_representatif = response.parse()
        assert_matches_type(SyncDefault[BatimentGroupeDvfOpenRepresentatif], dvf_open_representatif, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.batiment_groupe.dvf_open_representatif.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dvf_open_representatif = response.parse()
            assert_matches_type(
                SyncDefault[BatimentGroupeDvfOpenRepresentatif], dvf_open_representatif, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncDvfOpenRepresentatif:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        dvf_open_representatif = await async_client.donnees.batiment_groupe.dvf_open_representatif.list()
        assert_matches_type(AsyncDefault[BatimentGroupeDvfOpenRepresentatif], dvf_open_representatif, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        dvf_open_representatif = await async_client.donnees.batiment_groupe.dvf_open_representatif.list(
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
        assert_matches_type(AsyncDefault[BatimentGroupeDvfOpenRepresentatif], dvf_open_representatif, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.batiment_groupe.dvf_open_representatif.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dvf_open_representatif = await response.parse()
        assert_matches_type(AsyncDefault[BatimentGroupeDvfOpenRepresentatif], dvf_open_representatif, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.batiment_groupe.dvf_open_representatif.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dvf_open_representatif = await response.parse()
            assert_matches_type(
                AsyncDefault[BatimentGroupeDvfOpenRepresentatif], dvf_open_representatif, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
