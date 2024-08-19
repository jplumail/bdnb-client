# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client.pagination import SyncDefault, AsyncDefault
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeDvfOpenStatistique

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDvfOpenStatistique:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        dvf_open_statistique = client.donnees.batiment_groupe.dvf_open_statistique.list()
        assert_matches_type(SyncDefault[BatimentGroupeDvfOpenStatistique], dvf_open_statistique, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        dvf_open_statistique = client.donnees.batiment_groupe.dvf_open_statistique.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            limit="limit",
            nb_appartement_mutee="nb_appartement_mutee",
            nb_dependance_mutee="nb_dependance_mutee",
            nb_locaux_mutee="nb_locaux_mutee",
            nb_locaux_tertiaire_mutee="nb_locaux_tertiaire_mutee",
            nb_maisons_mutee="nb_maisons_mutee",
            nb_mutation="nb_mutation",
            offset="offset",
            order="order",
            prix_m2_local_max="prix_m2_local_max",
            prix_m2_local_median="prix_m2_local_median",
            prix_m2_local_min="prix_m2_local_min",
            prix_m2_local_moyen="prix_m2_local_moyen",
            prix_m2_terrain_max="prix_m2_terrain_max",
            prix_m2_terrain_median="prix_m2_terrain_median",
            prix_m2_terrain_min="prix_m2_terrain_min",
            prix_m2_terrain_moyen="prix_m2_terrain_moyen",
            select="select",
            valeur_fonciere_max="valeur_fonciere_max",
            valeur_fonciere_median="valeur_fonciere_median",
            valeur_fonciere_min="valeur_fonciere_min",
            valeur_fonciere_moyenne="valeur_fonciere_moyenne",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(SyncDefault[BatimentGroupeDvfOpenStatistique], dvf_open_statistique, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.batiment_groupe.dvf_open_statistique.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dvf_open_statistique = response.parse()
        assert_matches_type(SyncDefault[BatimentGroupeDvfOpenStatistique], dvf_open_statistique, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.batiment_groupe.dvf_open_statistique.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dvf_open_statistique = response.parse()
            assert_matches_type(SyncDefault[BatimentGroupeDvfOpenStatistique], dvf_open_statistique, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDvfOpenStatistique:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        dvf_open_statistique = await async_client.donnees.batiment_groupe.dvf_open_statistique.list()
        assert_matches_type(AsyncDefault[BatimentGroupeDvfOpenStatistique], dvf_open_statistique, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        dvf_open_statistique = await async_client.donnees.batiment_groupe.dvf_open_statistique.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            limit="limit",
            nb_appartement_mutee="nb_appartement_mutee",
            nb_dependance_mutee="nb_dependance_mutee",
            nb_locaux_mutee="nb_locaux_mutee",
            nb_locaux_tertiaire_mutee="nb_locaux_tertiaire_mutee",
            nb_maisons_mutee="nb_maisons_mutee",
            nb_mutation="nb_mutation",
            offset="offset",
            order="order",
            prix_m2_local_max="prix_m2_local_max",
            prix_m2_local_median="prix_m2_local_median",
            prix_m2_local_min="prix_m2_local_min",
            prix_m2_local_moyen="prix_m2_local_moyen",
            prix_m2_terrain_max="prix_m2_terrain_max",
            prix_m2_terrain_median="prix_m2_terrain_median",
            prix_m2_terrain_min="prix_m2_terrain_min",
            prix_m2_terrain_moyen="prix_m2_terrain_moyen",
            select="select",
            valeur_fonciere_max="valeur_fonciere_max",
            valeur_fonciere_median="valeur_fonciere_median",
            valeur_fonciere_min="valeur_fonciere_min",
            valeur_fonciere_moyenne="valeur_fonciere_moyenne",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AsyncDefault[BatimentGroupeDvfOpenStatistique], dvf_open_statistique, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.batiment_groupe.dvf_open_statistique.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dvf_open_statistique = await response.parse()
        assert_matches_type(AsyncDefault[BatimentGroupeDvfOpenStatistique], dvf_open_statistique, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.batiment_groupe.dvf_open_statistique.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dvf_open_statistique = await response.parse()
            assert_matches_type(AsyncDefault[BatimentGroupeDvfOpenStatistique], dvf_open_statistique, path=["response"])

        assert cast(Any, response.is_closed) is True
