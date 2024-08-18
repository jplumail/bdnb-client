# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client.pagination import SyncDefault, AsyncDefault
from bdnb_client.types.donnees.batiment_groupe import IrisContexteGeographique

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIrisContexteGeographique:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        iris_contexte_geographique = client.donnees.batiment_groupe.iris_contexte_geographique.list()
        assert_matches_type(SyncDefault[IrisContexteGeographique], iris_contexte_geographique, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        iris_contexte_geographique = client.donnees.batiment_groupe.iris_contexte_geographique.list(
            action_coeur_ville_code_anct="action_coeur_ville_code_anct",
            action_coeur_ville_libelle="action_coeur_ville_libelle",
            aire_attraction_ville_catg="aire_attraction_ville_catg",
            aire_attraction_ville_catg_libelle="aire_attraction_ville_catg_libelle",
            aire_attraction_ville_code_insee="aire_attraction_ville_code_insee",
            aire_attraction_ville_libelle="aire_attraction_ville_libelle",
            aire_urbaine_fonctionnelle_eurostat="aire_urbaine_fonctionnelle_eurostat",
            aire_urbaine_fonctionnelle_libelle="aire_urbaine_fonctionnelle_libelle",
            bassin_vie_catg="bassin_vie_catg",
            bassin_vie_catg_libelle="bassin_vie_catg_libelle",
            bassin_vie_code_insee="bassin_vie_code_insee",
            bassin_vie_libelle="bassin_vie_libelle",
            code_departement_insee="code_departement_insee",
            code_iris="code_iris",
            contrat_relance_trans_eco_code_anct="contrat_relance_trans_eco_code_anct",
            contrat_relance_trans_eco_libelle="contrat_relance_trans_eco_libelle",
            en_littoral="en_littoral",
            en_montagne="en_montagne",
            geom_iris="geom_iris",
            grille_communale_densite_catg="grille_communale_densite_catg",
            grille_communale_densite_catg_libelle="grille_communale_densite_catg_libelle",
            limit="limit",
            offset="offset",
            order="order",
            petites_villes_demain_code_anct="petites_villes_demain_code_anct",
            select="select",
            territoires_industrie_code_anct="territoires_industrie_code_anct",
            territoires_industrie_libelle="territoires_industrie_libelle",
            unite_urbaine_catg="unite_urbaine_catg",
            unite_urbaine_catg_libelle="unite_urbaine_catg_libelle",
            unite_urbaine_code_insee="unite_urbaine_code_insee",
            unite_urbaine_libelle="unite_urbaine_libelle",
            zone_aide_finalite_reg_catg="zone_aide_finalite_reg_catg",
            zone_aide_finalite_reg_code_anct="zone_aide_finalite_reg_code_anct",
            zone_emploi_code_insee="zone_emploi_code_insee",
            zone_emploi_libelle="zone_emploi_libelle",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(SyncDefault[IrisContexteGeographique], iris_contexte_geographique, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.batiment_groupe.iris_contexte_geographique.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        iris_contexte_geographique = response.parse()
        assert_matches_type(SyncDefault[IrisContexteGeographique], iris_contexte_geographique, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.batiment_groupe.iris_contexte_geographique.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            iris_contexte_geographique = response.parse()
            assert_matches_type(SyncDefault[IrisContexteGeographique], iris_contexte_geographique, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIrisContexteGeographique:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        iris_contexte_geographique = await async_client.donnees.batiment_groupe.iris_contexte_geographique.list()
        assert_matches_type(AsyncDefault[IrisContexteGeographique], iris_contexte_geographique, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        iris_contexte_geographique = await async_client.donnees.batiment_groupe.iris_contexte_geographique.list(
            action_coeur_ville_code_anct="action_coeur_ville_code_anct",
            action_coeur_ville_libelle="action_coeur_ville_libelle",
            aire_attraction_ville_catg="aire_attraction_ville_catg",
            aire_attraction_ville_catg_libelle="aire_attraction_ville_catg_libelle",
            aire_attraction_ville_code_insee="aire_attraction_ville_code_insee",
            aire_attraction_ville_libelle="aire_attraction_ville_libelle",
            aire_urbaine_fonctionnelle_eurostat="aire_urbaine_fonctionnelle_eurostat",
            aire_urbaine_fonctionnelle_libelle="aire_urbaine_fonctionnelle_libelle",
            bassin_vie_catg="bassin_vie_catg",
            bassin_vie_catg_libelle="bassin_vie_catg_libelle",
            bassin_vie_code_insee="bassin_vie_code_insee",
            bassin_vie_libelle="bassin_vie_libelle",
            code_departement_insee="code_departement_insee",
            code_iris="code_iris",
            contrat_relance_trans_eco_code_anct="contrat_relance_trans_eco_code_anct",
            contrat_relance_trans_eco_libelle="contrat_relance_trans_eco_libelle",
            en_littoral="en_littoral",
            en_montagne="en_montagne",
            geom_iris="geom_iris",
            grille_communale_densite_catg="grille_communale_densite_catg",
            grille_communale_densite_catg_libelle="grille_communale_densite_catg_libelle",
            limit="limit",
            offset="offset",
            order="order",
            petites_villes_demain_code_anct="petites_villes_demain_code_anct",
            select="select",
            territoires_industrie_code_anct="territoires_industrie_code_anct",
            territoires_industrie_libelle="territoires_industrie_libelle",
            unite_urbaine_catg="unite_urbaine_catg",
            unite_urbaine_catg_libelle="unite_urbaine_catg_libelle",
            unite_urbaine_code_insee="unite_urbaine_code_insee",
            unite_urbaine_libelle="unite_urbaine_libelle",
            zone_aide_finalite_reg_catg="zone_aide_finalite_reg_catg",
            zone_aide_finalite_reg_code_anct="zone_aide_finalite_reg_code_anct",
            zone_emploi_code_insee="zone_emploi_code_insee",
            zone_emploi_libelle="zone_emploi_libelle",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AsyncDefault[IrisContexteGeographique], iris_contexte_geographique, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.batiment_groupe.iris_contexte_geographique.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        iris_contexte_geographique = await response.parse()
        assert_matches_type(AsyncDefault[IrisContexteGeographique], iris_contexte_geographique, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.batiment_groupe.iris_contexte_geographique.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            iris_contexte_geographique = await response.parse()
            assert_matches_type(AsyncDefault[IrisContexteGeographique], iris_contexte_geographique, path=["response"])

        assert cast(Any, response.is_closed) is True
