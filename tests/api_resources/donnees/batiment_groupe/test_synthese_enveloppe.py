# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client.pagination import SyncDefault, AsyncDefault
from bdnb_client.types.donnees.batiment_groupe import BatimentGroupeSyntheseEnveloppe

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSyntheseEnveloppe:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        synthese_enveloppe = client.donnees.batiment_groupe.synthese_enveloppe.list()
        assert_matches_type(SyncDefault[BatimentGroupeSyntheseEnveloppe], synthese_enveloppe, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        synthese_enveloppe = client.donnees.batiment_groupe.synthese_enveloppe.list(
            batiment_groupe_id="batiment_groupe_id",
            classe_inertie="classe_inertie",
            code_departement_insee="code_departement_insee",
            epaisseur_isolation_mur_exterieur_estim="epaisseur_isolation_mur_exterieur_estim",
            epaisseur_lame="epaisseur_lame",
            epaisseur_structure_mur_exterieur="epaisseur_structure_mur_exterieur",
            facteur_solaire_baie_vitree="facteur_solaire_baie_vitree",
            l_local_non_chauffe_mur="l_local_non_chauffe_mur",
            l_local_non_chauffe_plancher_bas="l_local_non_chauffe_plancher_bas",
            l_local_non_chauffe_plancher_haut="l_local_non_chauffe_plancher_haut",
            l_orientation_baie_vitree="l_orientation_baie_vitree",
            l_orientation_mur_exterieur="l_orientation_mur_exterieur",
            limit="limit",
            local_non_chauffe_principal_mur="local_non_chauffe_principal_mur",
            local_non_chauffe_principal_plancher_bas="local_non_chauffe_principal_plancher_bas",
            local_non_chauffe_principal_plancher_haut="local_non_chauffe_principal_plancher_haut",
            materiaux_structure_mur_exterieur="materiaux_structure_mur_exterieur",
            materiaux_structure_mur_exterieur_simplifie="materiaux_structure_mur_exterieur_simplifie",
            materiaux_toiture_simplifie="materiaux_toiture_simplifie",
            offset="offset",
            order="order",
            pourcentage_surface_baie_vitree_exterieur="pourcentage_surface_baie_vitree_exterieur",
            presence_balcon="presence_balcon",
            score_fiabilite="score_fiabilite",
            select="select",
            source_information_principale="source_information_principale",
            traversant="traversant",
            type_adjacence_principal_plancher_bas="type_adjacence_principal_plancher_bas",
            type_adjacence_principal_plancher_haut="type_adjacence_principal_plancher_haut",
            type_batiment_dpe="type_batiment_dpe",
            type_fermeture="type_fermeture",
            type_gaz_lame="type_gaz_lame",
            type_isolation_mur_exterieur="type_isolation_mur_exterieur",
            type_isolation_plancher_bas="type_isolation_plancher_bas",
            type_isolation_plancher_haut="type_isolation_plancher_haut",
            type_materiaux_menuiserie="type_materiaux_menuiserie",
            type_plancher_bas_deperditif="type_plancher_bas_deperditif",
            type_plancher_haut_deperditif="type_plancher_haut_deperditif",
            type_porte="type_porte",
            type_vitrage="type_vitrage",
            u_baie_vitree="u_baie_vitree",
            u_mur_exterieur="u_mur_exterieur",
            u_plancher_bas_brut_deperditif="u_plancher_bas_brut_deperditif",
            u_plancher_bas_final_deperditif="u_plancher_bas_final_deperditif",
            u_plancher_haut_deperditif="u_plancher_haut_deperditif",
            u_porte="u_porte",
            uw="uw",
            vitrage_vir="vitrage_vir",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(SyncDefault[BatimentGroupeSyntheseEnveloppe], synthese_enveloppe, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.batiment_groupe.synthese_enveloppe.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        synthese_enveloppe = response.parse()
        assert_matches_type(SyncDefault[BatimentGroupeSyntheseEnveloppe], synthese_enveloppe, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.batiment_groupe.synthese_enveloppe.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            synthese_enveloppe = response.parse()
            assert_matches_type(SyncDefault[BatimentGroupeSyntheseEnveloppe], synthese_enveloppe, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSyntheseEnveloppe:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        synthese_enveloppe = await async_client.donnees.batiment_groupe.synthese_enveloppe.list()
        assert_matches_type(AsyncDefault[BatimentGroupeSyntheseEnveloppe], synthese_enveloppe, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        synthese_enveloppe = await async_client.donnees.batiment_groupe.synthese_enveloppe.list(
            batiment_groupe_id="batiment_groupe_id",
            classe_inertie="classe_inertie",
            code_departement_insee="code_departement_insee",
            epaisseur_isolation_mur_exterieur_estim="epaisseur_isolation_mur_exterieur_estim",
            epaisseur_lame="epaisseur_lame",
            epaisseur_structure_mur_exterieur="epaisseur_structure_mur_exterieur",
            facteur_solaire_baie_vitree="facteur_solaire_baie_vitree",
            l_local_non_chauffe_mur="l_local_non_chauffe_mur",
            l_local_non_chauffe_plancher_bas="l_local_non_chauffe_plancher_bas",
            l_local_non_chauffe_plancher_haut="l_local_non_chauffe_plancher_haut",
            l_orientation_baie_vitree="l_orientation_baie_vitree",
            l_orientation_mur_exterieur="l_orientation_mur_exterieur",
            limit="limit",
            local_non_chauffe_principal_mur="local_non_chauffe_principal_mur",
            local_non_chauffe_principal_plancher_bas="local_non_chauffe_principal_plancher_bas",
            local_non_chauffe_principal_plancher_haut="local_non_chauffe_principal_plancher_haut",
            materiaux_structure_mur_exterieur="materiaux_structure_mur_exterieur",
            materiaux_structure_mur_exterieur_simplifie="materiaux_structure_mur_exterieur_simplifie",
            materiaux_toiture_simplifie="materiaux_toiture_simplifie",
            offset="offset",
            order="order",
            pourcentage_surface_baie_vitree_exterieur="pourcentage_surface_baie_vitree_exterieur",
            presence_balcon="presence_balcon",
            score_fiabilite="score_fiabilite",
            select="select",
            source_information_principale="source_information_principale",
            traversant="traversant",
            type_adjacence_principal_plancher_bas="type_adjacence_principal_plancher_bas",
            type_adjacence_principal_plancher_haut="type_adjacence_principal_plancher_haut",
            type_batiment_dpe="type_batiment_dpe",
            type_fermeture="type_fermeture",
            type_gaz_lame="type_gaz_lame",
            type_isolation_mur_exterieur="type_isolation_mur_exterieur",
            type_isolation_plancher_bas="type_isolation_plancher_bas",
            type_isolation_plancher_haut="type_isolation_plancher_haut",
            type_materiaux_menuiserie="type_materiaux_menuiserie",
            type_plancher_bas_deperditif="type_plancher_bas_deperditif",
            type_plancher_haut_deperditif="type_plancher_haut_deperditif",
            type_porte="type_porte",
            type_vitrage="type_vitrage",
            u_baie_vitree="u_baie_vitree",
            u_mur_exterieur="u_mur_exterieur",
            u_plancher_bas_brut_deperditif="u_plancher_bas_brut_deperditif",
            u_plancher_bas_final_deperditif="u_plancher_bas_final_deperditif",
            u_plancher_haut_deperditif="u_plancher_haut_deperditif",
            u_porte="u_porte",
            uw="uw",
            vitrage_vir="vitrage_vir",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AsyncDefault[BatimentGroupeSyntheseEnveloppe], synthese_enveloppe, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.batiment_groupe.synthese_enveloppe.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        synthese_enveloppe = await response.parse()
        assert_matches_type(AsyncDefault[BatimentGroupeSyntheseEnveloppe], synthese_enveloppe, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.batiment_groupe.synthese_enveloppe.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            synthese_enveloppe = await response.parse()
            assert_matches_type(AsyncDefault[BatimentGroupeSyntheseEnveloppe], synthese_enveloppe, path=["response"])

        assert cast(Any, response.is_closed) is True
