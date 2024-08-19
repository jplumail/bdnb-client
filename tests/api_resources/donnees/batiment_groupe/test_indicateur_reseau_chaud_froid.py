# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client.pagination import SyncDefault, AsyncDefault
from bdnb_client.types.donnees.batiment_groupe import (
    BatimentGroupeIndicateurReseauChaudFroid,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIndicateurReseauChaudFroid:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        indicateur_reseau_chaud_froid = client.donnees.batiment_groupe.indicateur_reseau_chaud_froid.list()
        assert_matches_type(
            SyncDefault[BatimentGroupeIndicateurReseauChaudFroid], indicateur_reseau_chaud_froid, path=["response"]
        )

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        indicateur_reseau_chaud_froid = client.donnees.batiment_groupe.indicateur_reseau_chaud_froid.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            consommation_chaleur_par_rapport_distance_au_reseau="consommation_chaleur_par_rapport_distance_au_reseau",
            id_reseau="id_reseau",
            id_reseau_bdnb="id_reseau_bdnb",
            indicateur_distance_au_reseau="indicateur_distance_au_reseau",
            indicateur_systeme_chauffage="indicateur_systeme_chauffage",
            limit="limit",
            offset="offset",
            order="order",
            potentiel_obligation_raccordement="potentiel_obligation_raccordement",
            potentiel_raccordement_reseau_chaleur="potentiel_raccordement_reseau_chaleur",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(
            SyncDefault[BatimentGroupeIndicateurReseauChaudFroid], indicateur_reseau_chaud_froid, path=["response"]
        )

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.batiment_groupe.indicateur_reseau_chaud_froid.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicateur_reseau_chaud_froid = response.parse()
        assert_matches_type(
            SyncDefault[BatimentGroupeIndicateurReseauChaudFroid], indicateur_reseau_chaud_froid, path=["response"]
        )

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.batiment_groupe.indicateur_reseau_chaud_froid.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicateur_reseau_chaud_froid = response.parse()
            assert_matches_type(
                SyncDefault[BatimentGroupeIndicateurReseauChaudFroid], indicateur_reseau_chaud_froid, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncIndicateurReseauChaudFroid:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        indicateur_reseau_chaud_froid = await async_client.donnees.batiment_groupe.indicateur_reseau_chaud_froid.list()
        assert_matches_type(
            AsyncDefault[BatimentGroupeIndicateurReseauChaudFroid], indicateur_reseau_chaud_froid, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        indicateur_reseau_chaud_froid = await async_client.donnees.batiment_groupe.indicateur_reseau_chaud_froid.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            consommation_chaleur_par_rapport_distance_au_reseau="consommation_chaleur_par_rapport_distance_au_reseau",
            id_reseau="id_reseau",
            id_reseau_bdnb="id_reseau_bdnb",
            indicateur_distance_au_reseau="indicateur_distance_au_reseau",
            indicateur_systeme_chauffage="indicateur_systeme_chauffage",
            limit="limit",
            offset="offset",
            order="order",
            potentiel_obligation_raccordement="potentiel_obligation_raccordement",
            potentiel_raccordement_reseau_chaleur="potentiel_raccordement_reseau_chaleur",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(
            AsyncDefault[BatimentGroupeIndicateurReseauChaudFroid], indicateur_reseau_chaud_froid, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.batiment_groupe.indicateur_reseau_chaud_froid.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicateur_reseau_chaud_froid = await response.parse()
        assert_matches_type(
            AsyncDefault[BatimentGroupeIndicateurReseauChaudFroid], indicateur_reseau_chaud_froid, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.batiment_groupe.indicateur_reseau_chaud_froid.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicateur_reseau_chaud_froid = await response.parse()
            assert_matches_type(
                AsyncDefault[BatimentGroupeIndicateurReseauChaudFroid], indicateur_reseau_chaud_froid, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
