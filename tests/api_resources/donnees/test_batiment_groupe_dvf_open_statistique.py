# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import BdnbAPI, AsyncBdnbAPI
from tests.utils import assert_matches_type
from bdnb_api.types.donnees import (
    BatimentGroupeDvfOpenStatistiqueListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatimentGroupeDvfOpenStatistique:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: BdnbAPI) -> None:
        batiment_groupe_dvf_open_statistique = client.donnees.batiment_groupe_dvf_open_statistique.list()
        assert_matches_type(
            BatimentGroupeDvfOpenStatistiqueListResponse, batiment_groupe_dvf_open_statistique, path=["response"]
        )

    @parametrize
    def test_method_list_with_all_params(self, client: BdnbAPI) -> None:
        batiment_groupe_dvf_open_statistique = client.donnees.batiment_groupe_dvf_open_statistique.list(
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
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(
            BatimentGroupeDvfOpenStatistiqueListResponse, batiment_groupe_dvf_open_statistique, path=["response"]
        )

    @parametrize
    def test_raw_response_list(self, client: BdnbAPI) -> None:
        response = client.donnees.batiment_groupe_dvf_open_statistique.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_groupe_dvf_open_statistique = response.parse()
        assert_matches_type(
            BatimentGroupeDvfOpenStatistiqueListResponse, batiment_groupe_dvf_open_statistique, path=["response"]
        )

    @parametrize
    def test_streaming_response_list(self, client: BdnbAPI) -> None:
        with client.donnees.batiment_groupe_dvf_open_statistique.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_groupe_dvf_open_statistique = response.parse()
            assert_matches_type(
                BatimentGroupeDvfOpenStatistiqueListResponse, batiment_groupe_dvf_open_statistique, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncBatimentGroupeDvfOpenStatistique:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnbAPI) -> None:
        batiment_groupe_dvf_open_statistique = await async_client.donnees.batiment_groupe_dvf_open_statistique.list()
        assert_matches_type(
            BatimentGroupeDvfOpenStatistiqueListResponse, batiment_groupe_dvf_open_statistique, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        batiment_groupe_dvf_open_statistique = await async_client.donnees.batiment_groupe_dvf_open_statistique.list(
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
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(
            BatimentGroupeDvfOpenStatistiqueListResponse, batiment_groupe_dvf_open_statistique, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.donnees.batiment_groupe_dvf_open_statistique.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batiment_groupe_dvf_open_statistique = await response.parse()
        assert_matches_type(
            BatimentGroupeDvfOpenStatistiqueListResponse, batiment_groupe_dvf_open_statistique, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.donnees.batiment_groupe_dvf_open_statistique.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batiment_groupe_dvf_open_statistique = await response.parse()
            assert_matches_type(
                BatimentGroupeDvfOpenStatistiqueListResponse, batiment_groupe_dvf_open_statistique, path=["response"]
            )

        assert cast(Any, response.is_closed) is True