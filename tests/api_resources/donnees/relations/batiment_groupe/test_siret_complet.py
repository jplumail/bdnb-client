# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client._utils import parse_date
from bdnb_client.pagination import SyncDefault, AsyncDefault
from bdnb_client.types.donnees.relations.batiment_groupe import RelBatimentGroupeSiretComplet

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSiretComplet:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        siret_complet = client.donnees.relations.batiment_groupe.siret_complet.list()
        assert_matches_type(SyncDefault[RelBatimentGroupeSiretComplet], siret_complet, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        siret_complet = client.donnees.relations.batiment_groupe.siret_complet.list(
            activite_registre_metier="activite_registre_metier",
            batiment_groupe_id="batiment_groupe_id",
            cle_interop_adr="cle_interop_adr",
            code_activite_principale="code_activite_principale",
            code_departement_insee="code_departement_insee",
            date_creation=parse_date("2019-12-27"),
            date_dernier_traitement=parse_date("2019-12-27"),
            denomination_etablissement="denomination_etablissement",
            etat_administratif_actif="etat_administratif_actif",
            libelle_activite_principale="libelle_activite_principale",
            limit="limit",
            nic="nic",
            offset="offset",
            order="order",
            select="select",
            siege_social="siege_social",
            siren="siren",
            siret="siret",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(SyncDefault[RelBatimentGroupeSiretComplet], siret_complet, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.relations.batiment_groupe.siret_complet.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        siret_complet = response.parse()
        assert_matches_type(SyncDefault[RelBatimentGroupeSiretComplet], siret_complet, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.relations.batiment_groupe.siret_complet.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            siret_complet = response.parse()
            assert_matches_type(SyncDefault[RelBatimentGroupeSiretComplet], siret_complet, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSiretComplet:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        siret_complet = await async_client.donnees.relations.batiment_groupe.siret_complet.list()
        assert_matches_type(AsyncDefault[RelBatimentGroupeSiretComplet], siret_complet, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        siret_complet = await async_client.donnees.relations.batiment_groupe.siret_complet.list(
            activite_registre_metier="activite_registre_metier",
            batiment_groupe_id="batiment_groupe_id",
            cle_interop_adr="cle_interop_adr",
            code_activite_principale="code_activite_principale",
            code_departement_insee="code_departement_insee",
            date_creation=parse_date("2019-12-27"),
            date_dernier_traitement=parse_date("2019-12-27"),
            denomination_etablissement="denomination_etablissement",
            etat_administratif_actif="etat_administratif_actif",
            libelle_activite_principale="libelle_activite_principale",
            limit="limit",
            nic="nic",
            offset="offset",
            order="order",
            select="select",
            siege_social="siege_social",
            siren="siren",
            siret="siret",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AsyncDefault[RelBatimentGroupeSiretComplet], siret_complet, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.relations.batiment_groupe.siret_complet.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        siret_complet = await response.parse()
        assert_matches_type(AsyncDefault[RelBatimentGroupeSiretComplet], siret_complet, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.relations.batiment_groupe.siret_complet.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            siret_complet = await response.parse()
            assert_matches_type(AsyncDefault[RelBatimentGroupeSiretComplet], siret_complet, path=["response"])

        assert cast(Any, response.is_closed) is True
