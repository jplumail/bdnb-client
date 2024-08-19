# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client._utils import parse_date
from bdnb_client.pagination import SyncDefault, AsyncDefault
from bdnb_client.types.donnees.relations.batiment_groupe import RelBatimentGroupeSirenComplet

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSirenComplet:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        siren_complet = client.donnees.relations.batiment_groupe.siren_complet.list()
        assert_matches_type(SyncDefault[RelBatimentGroupeSirenComplet], siren_complet, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        siren_complet = client.donnees.relations.batiment_groupe.siren_complet.list(
            batiment_groupe_id="batiment_groupe_id",
            cat_org="cat_org",
            cat_org_simplifie="cat_org_simplifie",
            code_departement_insee="code_departement_insee",
            dans_majic_pm="dans_majic_pm",
            dans_majic_pm_ou_etablissement="dans_majic_pm_ou_etablissement",
            date_creation=parse_date("2019-12-27"),
            date_dernier_traitement=parse_date("2019-12-27"),
            denomination_personne_morale="denomination_personne_morale",
            etablissement="etablissement",
            etat_administratif_actif="etat_administratif_actif",
            limit="limit",
            nb_locaux_open="nb_locaux_open",
            nb_siret_actifs="nb_siret_actifs",
            offset="offset",
            order="order",
            personne_type="personne_type",
            proprietaire_open="proprietaire_open",
            select="select",
            siren="siren",
            siren_dans_sirene="siren_dans_sirene",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(SyncDefault[RelBatimentGroupeSirenComplet], siren_complet, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.relations.batiment_groupe.siren_complet.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        siren_complet = response.parse()
        assert_matches_type(SyncDefault[RelBatimentGroupeSirenComplet], siren_complet, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.relations.batiment_groupe.siren_complet.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            siren_complet = response.parse()
            assert_matches_type(SyncDefault[RelBatimentGroupeSirenComplet], siren_complet, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSirenComplet:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        siren_complet = await async_client.donnees.relations.batiment_groupe.siren_complet.list()
        assert_matches_type(AsyncDefault[RelBatimentGroupeSirenComplet], siren_complet, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        siren_complet = await async_client.donnees.relations.batiment_groupe.siren_complet.list(
            batiment_groupe_id="batiment_groupe_id",
            cat_org="cat_org",
            cat_org_simplifie="cat_org_simplifie",
            code_departement_insee="code_departement_insee",
            dans_majic_pm="dans_majic_pm",
            dans_majic_pm_ou_etablissement="dans_majic_pm_ou_etablissement",
            date_creation=parse_date("2019-12-27"),
            date_dernier_traitement=parse_date("2019-12-27"),
            denomination_personne_morale="denomination_personne_morale",
            etablissement="etablissement",
            etat_administratif_actif="etat_administratif_actif",
            limit="limit",
            nb_locaux_open="nb_locaux_open",
            nb_siret_actifs="nb_siret_actifs",
            offset="offset",
            order="order",
            personne_type="personne_type",
            proprietaire_open="proprietaire_open",
            select="select",
            siren="siren",
            siren_dans_sirene="siren_dans_sirene",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AsyncDefault[RelBatimentGroupeSirenComplet], siren_complet, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.relations.batiment_groupe.siren_complet.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        siren_complet = await response.parse()
        assert_matches_type(AsyncDefault[RelBatimentGroupeSirenComplet], siren_complet, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.relations.batiment_groupe.siren_complet.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            siren_complet = await response.parse()
            assert_matches_type(AsyncDefault[RelBatimentGroupeSirenComplet], siren_complet, path=["response"])

        assert cast(Any, response.is_closed) is True
