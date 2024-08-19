# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client.pagination import SyncDefault, AsyncDefault
from bdnb_client.types.donnees.batiment_groupe import (
    BatimentGroupeDpeRepresentatifLogement,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDpeRepresentatifLogement:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        dpe_representatif_logement = client.donnees.batiment_groupe.dpe_representatif_logement.list()
        assert_matches_type(
            SyncDefault[BatimentGroupeDpeRepresentatifLogement], dpe_representatif_logement, path=["response"]
        )

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        dpe_representatif_logement = client.donnees.batiment_groupe.dpe_representatif_logement.list(
            annee_construction_dpe="annee_construction_dpe",
            arrete_2021="arrete_2021",
            batiment_groupe_id="batiment_groupe_id",
            chauffage_solaire="chauffage_solaire",
            classe_bilan_dpe="classe_bilan_dpe",
            classe_conso_energie_arrete_2012="classe_conso_energie_arrete_2012",
            classe_emission_ges="classe_emission_ges",
            classe_emission_ges_arrete_2012="classe_emission_ges_arrete_2012",
            classe_inertie="classe_inertie",
            code_departement_insee="code_departement_insee",
            conso_3_usages_ep_m2_arrete_2012="conso_3_usages_ep_m2_arrete_2012",
            conso_5_usages_ef_m2="conso_5_usages_ef_m2",
            conso_5_usages_ep_m2="conso_5_usages_ep_m2",
            date_etablissement_dpe="date_etablissement_dpe",
            date_reception_dpe="date_reception_dpe",
            deperdition_baie_vitree="deperdition_baie_vitree",
            deperdition_mur="deperdition_mur",
            deperdition_plancher_bas="deperdition_plancher_bas",
            deperdition_plancher_haut="deperdition_plancher_haut",
            deperdition_pont_thermique="deperdition_pont_thermique",
            deperdition_porte="deperdition_porte",
            ecs_solaire="ecs_solaire",
            emission_ges_3_usages_ep_m2_arrete_2012="emission_ges_3_usages_ep_m2_arrete_2012",
            emission_ges_5_usages_m2="emission_ges_5_usages_m2",
            epaisseur_isolation_mur_exterieur_estim="epaisseur_isolation_mur_exterieur_estim",
            epaisseur_lame="epaisseur_lame",
            epaisseur_structure_mur_exterieur="epaisseur_structure_mur_exterieur",
            facteur_solaire_baie_vitree="facteur_solaire_baie_vitree",
            identifiant_dpe="identifiant_dpe",
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
            nb_generateur_chauffage="nb_generateur_chauffage",
            nb_generateur_ecs="nb_generateur_ecs",
            nb_installation_chauffage="nb_installation_chauffage",
            nb_installation_ecs="nb_installation_ecs",
            nombre_niveau_immeuble="nombre_niveau_immeuble",
            nombre_niveau_logement="nombre_niveau_logement",
            offset="offset",
            order="order",
            periode_construction_dpe="periode_construction_dpe",
            plusieurs_facade_exposee="plusieurs_facade_exposee",
            pourcentage_surface_baie_vitree_exterieur="pourcentage_surface_baie_vitree_exterieur",
            presence_balcon="presence_balcon",
            select="select",
            surface_habitable_immeuble="surface_habitable_immeuble",
            surface_habitable_logement="surface_habitable_logement",
            surface_mur_deperditif="surface_mur_deperditif",
            surface_mur_exterieur="surface_mur_exterieur",
            surface_mur_totale="surface_mur_totale",
            surface_plancher_bas_deperditif="surface_plancher_bas_deperditif",
            surface_plancher_bas_totale="surface_plancher_bas_totale",
            surface_plancher_haut_deperditif="surface_plancher_haut_deperditif",
            surface_plancher_haut_totale="surface_plancher_haut_totale",
            surface_porte="surface_porte",
            surface_vitree_est="surface_vitree_est",
            surface_vitree_horizontal="surface_vitree_horizontal",
            surface_vitree_nord="surface_vitree_nord",
            surface_vitree_ouest="surface_vitree_ouest",
            surface_vitree_sud="surface_vitree_sud",
            traversant="traversant",
            type_adjacence_principal_plancher_bas="type_adjacence_principal_plancher_bas",
            type_adjacence_principal_plancher_haut="type_adjacence_principal_plancher_haut",
            type_batiment_dpe="type_batiment_dpe",
            type_dpe="type_dpe",
            type_energie_chauffage="type_energie_chauffage",
            type_energie_chauffage_appoint="type_energie_chauffage_appoint",
            type_energie_climatisation="type_energie_climatisation",
            type_energie_ecs="type_energie_ecs",
            type_energie_ecs_appoint="type_energie_ecs_appoint",
            type_fermeture="type_fermeture",
            type_gaz_lame="type_gaz_lame",
            type_generateur_chauffage="type_generateur_chauffage",
            type_generateur_chauffage_anciennete="type_generateur_chauffage_anciennete",
            type_generateur_chauffage_anciennete_appoint="type_generateur_chauffage_anciennete_appoint",
            type_generateur_chauffage_appoint="type_generateur_chauffage_appoint",
            type_generateur_climatisation="type_generateur_climatisation",
            type_generateur_climatisation_anciennete="type_generateur_climatisation_anciennete",
            type_generateur_ecs="type_generateur_ecs",
            type_generateur_ecs_anciennete="type_generateur_ecs_anciennete",
            type_generateur_ecs_anciennete_appoint="type_generateur_ecs_anciennete_appoint",
            type_generateur_ecs_appoint="type_generateur_ecs_appoint",
            type_installation_chauffage="type_installation_chauffage",
            type_installation_ecs="type_installation_ecs",
            type_isolation_mur_exterieur="type_isolation_mur_exterieur",
            type_isolation_plancher_bas="type_isolation_plancher_bas",
            type_isolation_plancher_haut="type_isolation_plancher_haut",
            type_materiaux_menuiserie="type_materiaux_menuiserie",
            type_plancher_bas_deperditif="type_plancher_bas_deperditif",
            type_plancher_haut_deperditif="type_plancher_haut_deperditif",
            type_porte="type_porte",
            type_production_energie_renouvelable="type_production_energie_renouvelable",
            type_ventilation="type_ventilation",
            type_vitrage="type_vitrage",
            u_baie_vitree="u_baie_vitree",
            u_mur_exterieur="u_mur_exterieur",
            u_plancher_bas_brut_deperditif="u_plancher_bas_brut_deperditif",
            u_plancher_bas_final_deperditif="u_plancher_bas_final_deperditif",
            u_plancher_haut_deperditif="u_plancher_haut_deperditif",
            u_porte="u_porte",
            uw="uw",
            version="version",
            vitrage_vir="vitrage_vir",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(
            SyncDefault[BatimentGroupeDpeRepresentatifLogement], dpe_representatif_logement, path=["response"]
        )

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.batiment_groupe.dpe_representatif_logement.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dpe_representatif_logement = response.parse()
        assert_matches_type(
            SyncDefault[BatimentGroupeDpeRepresentatifLogement], dpe_representatif_logement, path=["response"]
        )

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.batiment_groupe.dpe_representatif_logement.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dpe_representatif_logement = response.parse()
            assert_matches_type(
                SyncDefault[BatimentGroupeDpeRepresentatifLogement], dpe_representatif_logement, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncDpeRepresentatifLogement:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        dpe_representatif_logement = await async_client.donnees.batiment_groupe.dpe_representatif_logement.list()
        assert_matches_type(
            AsyncDefault[BatimentGroupeDpeRepresentatifLogement], dpe_representatif_logement, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        dpe_representatif_logement = await async_client.donnees.batiment_groupe.dpe_representatif_logement.list(
            annee_construction_dpe="annee_construction_dpe",
            arrete_2021="arrete_2021",
            batiment_groupe_id="batiment_groupe_id",
            chauffage_solaire="chauffage_solaire",
            classe_bilan_dpe="classe_bilan_dpe",
            classe_conso_energie_arrete_2012="classe_conso_energie_arrete_2012",
            classe_emission_ges="classe_emission_ges",
            classe_emission_ges_arrete_2012="classe_emission_ges_arrete_2012",
            classe_inertie="classe_inertie",
            code_departement_insee="code_departement_insee",
            conso_3_usages_ep_m2_arrete_2012="conso_3_usages_ep_m2_arrete_2012",
            conso_5_usages_ef_m2="conso_5_usages_ef_m2",
            conso_5_usages_ep_m2="conso_5_usages_ep_m2",
            date_etablissement_dpe="date_etablissement_dpe",
            date_reception_dpe="date_reception_dpe",
            deperdition_baie_vitree="deperdition_baie_vitree",
            deperdition_mur="deperdition_mur",
            deperdition_plancher_bas="deperdition_plancher_bas",
            deperdition_plancher_haut="deperdition_plancher_haut",
            deperdition_pont_thermique="deperdition_pont_thermique",
            deperdition_porte="deperdition_porte",
            ecs_solaire="ecs_solaire",
            emission_ges_3_usages_ep_m2_arrete_2012="emission_ges_3_usages_ep_m2_arrete_2012",
            emission_ges_5_usages_m2="emission_ges_5_usages_m2",
            epaisseur_isolation_mur_exterieur_estim="epaisseur_isolation_mur_exterieur_estim",
            epaisseur_lame="epaisseur_lame",
            epaisseur_structure_mur_exterieur="epaisseur_structure_mur_exterieur",
            facteur_solaire_baie_vitree="facteur_solaire_baie_vitree",
            identifiant_dpe="identifiant_dpe",
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
            nb_generateur_chauffage="nb_generateur_chauffage",
            nb_generateur_ecs="nb_generateur_ecs",
            nb_installation_chauffage="nb_installation_chauffage",
            nb_installation_ecs="nb_installation_ecs",
            nombre_niveau_immeuble="nombre_niveau_immeuble",
            nombre_niveau_logement="nombre_niveau_logement",
            offset="offset",
            order="order",
            periode_construction_dpe="periode_construction_dpe",
            plusieurs_facade_exposee="plusieurs_facade_exposee",
            pourcentage_surface_baie_vitree_exterieur="pourcentage_surface_baie_vitree_exterieur",
            presence_balcon="presence_balcon",
            select="select",
            surface_habitable_immeuble="surface_habitable_immeuble",
            surface_habitable_logement="surface_habitable_logement",
            surface_mur_deperditif="surface_mur_deperditif",
            surface_mur_exterieur="surface_mur_exterieur",
            surface_mur_totale="surface_mur_totale",
            surface_plancher_bas_deperditif="surface_plancher_bas_deperditif",
            surface_plancher_bas_totale="surface_plancher_bas_totale",
            surface_plancher_haut_deperditif="surface_plancher_haut_deperditif",
            surface_plancher_haut_totale="surface_plancher_haut_totale",
            surface_porte="surface_porte",
            surface_vitree_est="surface_vitree_est",
            surface_vitree_horizontal="surface_vitree_horizontal",
            surface_vitree_nord="surface_vitree_nord",
            surface_vitree_ouest="surface_vitree_ouest",
            surface_vitree_sud="surface_vitree_sud",
            traversant="traversant",
            type_adjacence_principal_plancher_bas="type_adjacence_principal_plancher_bas",
            type_adjacence_principal_plancher_haut="type_adjacence_principal_plancher_haut",
            type_batiment_dpe="type_batiment_dpe",
            type_dpe="type_dpe",
            type_energie_chauffage="type_energie_chauffage",
            type_energie_chauffage_appoint="type_energie_chauffage_appoint",
            type_energie_climatisation="type_energie_climatisation",
            type_energie_ecs="type_energie_ecs",
            type_energie_ecs_appoint="type_energie_ecs_appoint",
            type_fermeture="type_fermeture",
            type_gaz_lame="type_gaz_lame",
            type_generateur_chauffage="type_generateur_chauffage",
            type_generateur_chauffage_anciennete="type_generateur_chauffage_anciennete",
            type_generateur_chauffage_anciennete_appoint="type_generateur_chauffage_anciennete_appoint",
            type_generateur_chauffage_appoint="type_generateur_chauffage_appoint",
            type_generateur_climatisation="type_generateur_climatisation",
            type_generateur_climatisation_anciennete="type_generateur_climatisation_anciennete",
            type_generateur_ecs="type_generateur_ecs",
            type_generateur_ecs_anciennete="type_generateur_ecs_anciennete",
            type_generateur_ecs_anciennete_appoint="type_generateur_ecs_anciennete_appoint",
            type_generateur_ecs_appoint="type_generateur_ecs_appoint",
            type_installation_chauffage="type_installation_chauffage",
            type_installation_ecs="type_installation_ecs",
            type_isolation_mur_exterieur="type_isolation_mur_exterieur",
            type_isolation_plancher_bas="type_isolation_plancher_bas",
            type_isolation_plancher_haut="type_isolation_plancher_haut",
            type_materiaux_menuiserie="type_materiaux_menuiserie",
            type_plancher_bas_deperditif="type_plancher_bas_deperditif",
            type_plancher_haut_deperditif="type_plancher_haut_deperditif",
            type_porte="type_porte",
            type_production_energie_renouvelable="type_production_energie_renouvelable",
            type_ventilation="type_ventilation",
            type_vitrage="type_vitrage",
            u_baie_vitree="u_baie_vitree",
            u_mur_exterieur="u_mur_exterieur",
            u_plancher_bas_brut_deperditif="u_plancher_bas_brut_deperditif",
            u_plancher_bas_final_deperditif="u_plancher_bas_final_deperditif",
            u_plancher_haut_deperditif="u_plancher_haut_deperditif",
            u_porte="u_porte",
            uw="uw",
            version="version",
            vitrage_vir="vitrage_vir",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(
            AsyncDefault[BatimentGroupeDpeRepresentatifLogement], dpe_representatif_logement, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.batiment_groupe.dpe_representatif_logement.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dpe_representatif_logement = await response.parse()
        assert_matches_type(
            AsyncDefault[BatimentGroupeDpeRepresentatifLogement], dpe_representatif_logement, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.batiment_groupe.dpe_representatif_logement.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dpe_representatif_logement = await response.parse()
            assert_matches_type(
                AsyncDefault[BatimentGroupeDpeRepresentatifLogement], dpe_representatif_logement, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
