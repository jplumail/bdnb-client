# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import BdnbAPI, AsyncBdnbAPI
from tests.utils import assert_matches_type
from bdnb_api.types.donnees import (
    TablesBdnbRetrieveBatimentGroupeQpvResponse,
    TablesBdnbRetrieveBatimentGroupeGeospxResponse,
    TablesBdnbRetrieveRelBatimentGroupeQpvResponse,
    TablesBdnbRetrieveBatimentGroupeBdtopoZoacResponse,
    TablesBdnbRetrieveRelBatimentGroupeAdresseResponse,
    TablesBdnbRetrieveReferentielAdministratifIrisResponse,
    TablesBdnbRetrieveRelBatimentConstructionAdresseResponse,
    TablesBdnbRetrieveBatimentGroupeSyntheseEnveloppeResponse,
    TablesBdnbRetrieveBatimentGroupeDvfOpenStatistiqueResponse,
    TablesBdnbRetrieveRelBatimentGroupeProprietaireSirenResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTablesBdnb:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_batiment_groupe_bdtopo_zoac(self, client: BdnbAPI) -> None:
        tables_bdnb = client.donnees.tables_bdnb.retrieve_batiment_groupe_bdtopo_zoac()
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeBdtopoZoacResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_method_retrieve_batiment_groupe_bdtopo_zoac_with_all_params(self, client: BdnbAPI) -> None:
        tables_bdnb = client.donnees.tables_bdnb.retrieve_batiment_groupe_bdtopo_zoac(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            l_nature="l_nature",
            l_nature_detaillee="l_nature_detaillee",
            l_toponyme="l_toponyme",
            limit="limit",
            offset="offset",
            order="order",
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeBdtopoZoacResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_raw_response_retrieve_batiment_groupe_bdtopo_zoac(self, client: BdnbAPI) -> None:
        response = client.donnees.tables_bdnb.with_raw_response.retrieve_batiment_groupe_bdtopo_zoac()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tables_bdnb = response.parse()
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeBdtopoZoacResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_batiment_groupe_bdtopo_zoac(self, client: BdnbAPI) -> None:
        with client.donnees.tables_bdnb.with_streaming_response.retrieve_batiment_groupe_bdtopo_zoac() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tables_bdnb = response.parse()
            assert_matches_type(TablesBdnbRetrieveBatimentGroupeBdtopoZoacResponse, tables_bdnb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_batiment_groupe_dvf_open_statistique(self, client: BdnbAPI) -> None:
        tables_bdnb = client.donnees.tables_bdnb.retrieve_batiment_groupe_dvf_open_statistique()
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeDvfOpenStatistiqueResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_method_retrieve_batiment_groupe_dvf_open_statistique_with_all_params(self, client: BdnbAPI) -> None:
        tables_bdnb = client.donnees.tables_bdnb.retrieve_batiment_groupe_dvf_open_statistique(
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
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeDvfOpenStatistiqueResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_raw_response_retrieve_batiment_groupe_dvf_open_statistique(self, client: BdnbAPI) -> None:
        response = client.donnees.tables_bdnb.with_raw_response.retrieve_batiment_groupe_dvf_open_statistique()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tables_bdnb = response.parse()
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeDvfOpenStatistiqueResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_batiment_groupe_dvf_open_statistique(self, client: BdnbAPI) -> None:
        with client.donnees.tables_bdnb.with_streaming_response.retrieve_batiment_groupe_dvf_open_statistique() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tables_bdnb = response.parse()
            assert_matches_type(
                TablesBdnbRetrieveBatimentGroupeDvfOpenStatistiqueResponse, tables_bdnb, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_batiment_groupe_geospx(self, client: BdnbAPI) -> None:
        tables_bdnb = client.donnees.tables_bdnb.retrieve_batiment_groupe_geospx()
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeGeospxResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_method_retrieve_batiment_groupe_geospx_with_all_params(self, client: BdnbAPI) -> None:
        tables_bdnb = client.donnees.tables_bdnb.retrieve_batiment_groupe_geospx(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            croisement_geospx_reussi="croisement_geospx_reussi",
            fiabilite_adresse="fiabilite_adresse",
            fiabilite_emprise_sol="fiabilite_emprise_sol",
            fiabilite_hauteur="fiabilite_hauteur",
            limit="limit",
            offset="offset",
            order="order",
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeGeospxResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_raw_response_retrieve_batiment_groupe_geospx(self, client: BdnbAPI) -> None:
        response = client.donnees.tables_bdnb.with_raw_response.retrieve_batiment_groupe_geospx()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tables_bdnb = response.parse()
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeGeospxResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_batiment_groupe_geospx(self, client: BdnbAPI) -> None:
        with client.donnees.tables_bdnb.with_streaming_response.retrieve_batiment_groupe_geospx() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tables_bdnb = response.parse()
            assert_matches_type(TablesBdnbRetrieveBatimentGroupeGeospxResponse, tables_bdnb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_batiment_groupe_qpv(self, client: BdnbAPI) -> None:
        tables_bdnb = client.donnees.tables_bdnb.retrieve_batiment_groupe_qpv()
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeQpvResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_method_retrieve_batiment_groupe_qpv_with_all_params(self, client: BdnbAPI) -> None:
        tables_bdnb = client.donnees.tables_bdnb.retrieve_batiment_groupe_qpv(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            limit="limit",
            nom_quartier="nom_quartier",
            offset="offset",
            order="order",
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeQpvResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_raw_response_retrieve_batiment_groupe_qpv(self, client: BdnbAPI) -> None:
        response = client.donnees.tables_bdnb.with_raw_response.retrieve_batiment_groupe_qpv()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tables_bdnb = response.parse()
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeQpvResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_batiment_groupe_qpv(self, client: BdnbAPI) -> None:
        with client.donnees.tables_bdnb.with_streaming_response.retrieve_batiment_groupe_qpv() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tables_bdnb = response.parse()
            assert_matches_type(TablesBdnbRetrieveBatimentGroupeQpvResponse, tables_bdnb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_batiment_groupe_synthese_enveloppe(self, client: BdnbAPI) -> None:
        tables_bdnb = client.donnees.tables_bdnb.retrieve_batiment_groupe_synthese_enveloppe()
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeSyntheseEnveloppeResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_method_retrieve_batiment_groupe_synthese_enveloppe_with_all_params(self, client: BdnbAPI) -> None:
        tables_bdnb = client.donnees.tables_bdnb.retrieve_batiment_groupe_synthese_enveloppe(
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
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeSyntheseEnveloppeResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_raw_response_retrieve_batiment_groupe_synthese_enveloppe(self, client: BdnbAPI) -> None:
        response = client.donnees.tables_bdnb.with_raw_response.retrieve_batiment_groupe_synthese_enveloppe()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tables_bdnb = response.parse()
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeSyntheseEnveloppeResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_batiment_groupe_synthese_enveloppe(self, client: BdnbAPI) -> None:
        with client.donnees.tables_bdnb.with_streaming_response.retrieve_batiment_groupe_synthese_enveloppe() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tables_bdnb = response.parse()
            assert_matches_type(
                TablesBdnbRetrieveBatimentGroupeSyntheseEnveloppeResponse, tables_bdnb, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_referentiel_administratif_iris(self, client: BdnbAPI) -> None:
        tables_bdnb = client.donnees.tables_bdnb.retrieve_referentiel_administratif_iris()
        assert_matches_type(TablesBdnbRetrieveReferentielAdministratifIrisResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_method_retrieve_referentiel_administratif_iris_with_all_params(self, client: BdnbAPI) -> None:
        tables_bdnb = client.donnees.tables_bdnb.retrieve_referentiel_administratif_iris(
            code_commune_insee="code_commune_insee",
            code_departement_insee="code_departement_insee",
            code_iris="code_iris",
            geom_iris="geom_iris",
            libelle_iris="libelle_iris",
            limit="limit",
            offset="offset",
            order="order",
            select="select",
            type_iris="type_iris",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(TablesBdnbRetrieveReferentielAdministratifIrisResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_raw_response_retrieve_referentiel_administratif_iris(self, client: BdnbAPI) -> None:
        response = client.donnees.tables_bdnb.with_raw_response.retrieve_referentiel_administratif_iris()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tables_bdnb = response.parse()
        assert_matches_type(TablesBdnbRetrieveReferentielAdministratifIrisResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_referentiel_administratif_iris(self, client: BdnbAPI) -> None:
        with client.donnees.tables_bdnb.with_streaming_response.retrieve_referentiel_administratif_iris() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tables_bdnb = response.parse()
            assert_matches_type(TablesBdnbRetrieveReferentielAdministratifIrisResponse, tables_bdnb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_rel_batiment_construction_adresse(self, client: BdnbAPI) -> None:
        tables_bdnb = client.donnees.tables_bdnb.retrieve_rel_batiment_construction_adresse()
        assert_matches_type(TablesBdnbRetrieveRelBatimentConstructionAdresseResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_method_retrieve_rel_batiment_construction_adresse_with_all_params(self, client: BdnbAPI) -> None:
        tables_bdnb = client.donnees.tables_bdnb.retrieve_rel_batiment_construction_adresse(
            adresse_principale="adresse_principale",
            batiment_construction_id="batiment_construction_id",
            cle_interop_adr="cle_interop_adr",
            code_departement_insee="code_departement_insee",
            distance_batiment_construction_adresse="distance_batiment_construction_adresse",
            fiabilite="fiabilite",
            limit="limit",
            offset="offset",
            order="order",
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(TablesBdnbRetrieveRelBatimentConstructionAdresseResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_raw_response_retrieve_rel_batiment_construction_adresse(self, client: BdnbAPI) -> None:
        response = client.donnees.tables_bdnb.with_raw_response.retrieve_rel_batiment_construction_adresse()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tables_bdnb = response.parse()
        assert_matches_type(TablesBdnbRetrieveRelBatimentConstructionAdresseResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_rel_batiment_construction_adresse(self, client: BdnbAPI) -> None:
        with client.donnees.tables_bdnb.with_streaming_response.retrieve_rel_batiment_construction_adresse() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tables_bdnb = response.parse()
            assert_matches_type(
                TablesBdnbRetrieveRelBatimentConstructionAdresseResponse, tables_bdnb, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_rel_batiment_groupe_adresse(self, client: BdnbAPI) -> None:
        tables_bdnb = client.donnees.tables_bdnb.retrieve_rel_batiment_groupe_adresse()
        assert_matches_type(TablesBdnbRetrieveRelBatimentGroupeAdresseResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_method_retrieve_rel_batiment_groupe_adresse_with_all_params(self, client: BdnbAPI) -> None:
        tables_bdnb = client.donnees.tables_bdnb.retrieve_rel_batiment_groupe_adresse(
            batiment_groupe_id="batiment_groupe_id",
            classe="classe",
            cle_interop_adr="cle_interop_adr",
            code_departement_insee="code_departement_insee",
            geom_bat_adresse="geom_bat_adresse",
            lien_valide="lien_valide",
            limit="limit",
            offset="offset",
            order="order",
            origine="origine",
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(TablesBdnbRetrieveRelBatimentGroupeAdresseResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_raw_response_retrieve_rel_batiment_groupe_adresse(self, client: BdnbAPI) -> None:
        response = client.donnees.tables_bdnb.with_raw_response.retrieve_rel_batiment_groupe_adresse()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tables_bdnb = response.parse()
        assert_matches_type(TablesBdnbRetrieveRelBatimentGroupeAdresseResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_rel_batiment_groupe_adresse(self, client: BdnbAPI) -> None:
        with client.donnees.tables_bdnb.with_streaming_response.retrieve_rel_batiment_groupe_adresse() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tables_bdnb = response.parse()
            assert_matches_type(TablesBdnbRetrieveRelBatimentGroupeAdresseResponse, tables_bdnb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_rel_batiment_groupe_proprietaire_siren(self, client: BdnbAPI) -> None:
        tables_bdnb = client.donnees.tables_bdnb.retrieve_rel_batiment_groupe_proprietaire_siren()
        assert_matches_type(
            TablesBdnbRetrieveRelBatimentGroupeProprietaireSirenResponse, tables_bdnb, path=["response"]
        )

    @parametrize
    def test_method_retrieve_rel_batiment_groupe_proprietaire_siren_with_all_params(self, client: BdnbAPI) -> None:
        tables_bdnb = client.donnees.tables_bdnb.retrieve_rel_batiment_groupe_proprietaire_siren(
            bat_prop_denomination_proprietaire="bat_prop_denomination_proprietaire",
            dans_majic_pm="dans_majic_pm",
            is_bailleur="is_bailleur",
            limit="limit",
            nb_locaux_open="nb_locaux_open",
            offset="offset",
            order="order",
            select="select",
            siren="siren",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(
            TablesBdnbRetrieveRelBatimentGroupeProprietaireSirenResponse, tables_bdnb, path=["response"]
        )

    @parametrize
    def test_raw_response_retrieve_rel_batiment_groupe_proprietaire_siren(self, client: BdnbAPI) -> None:
        response = client.donnees.tables_bdnb.with_raw_response.retrieve_rel_batiment_groupe_proprietaire_siren()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tables_bdnb = response.parse()
        assert_matches_type(
            TablesBdnbRetrieveRelBatimentGroupeProprietaireSirenResponse, tables_bdnb, path=["response"]
        )

    @parametrize
    def test_streaming_response_retrieve_rel_batiment_groupe_proprietaire_siren(self, client: BdnbAPI) -> None:
        with client.donnees.tables_bdnb.with_streaming_response.retrieve_rel_batiment_groupe_proprietaire_siren() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tables_bdnb = response.parse()
            assert_matches_type(
                TablesBdnbRetrieveRelBatimentGroupeProprietaireSirenResponse, tables_bdnb, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_rel_batiment_groupe_qpv(self, client: BdnbAPI) -> None:
        tables_bdnb = client.donnees.tables_bdnb.retrieve_rel_batiment_groupe_qpv()
        assert_matches_type(TablesBdnbRetrieveRelBatimentGroupeQpvResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_method_retrieve_rel_batiment_groupe_qpv_with_all_params(self, client: BdnbAPI) -> None:
        tables_bdnb = client.donnees.tables_bdnb.retrieve_rel_batiment_groupe_qpv(
            batiment_construction_id="batiment_construction_id",
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            limit="limit",
            offset="offset",
            order="order",
            qpv_code_qp="qpv_code_qp",
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(TablesBdnbRetrieveRelBatimentGroupeQpvResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_raw_response_retrieve_rel_batiment_groupe_qpv(self, client: BdnbAPI) -> None:
        response = client.donnees.tables_bdnb.with_raw_response.retrieve_rel_batiment_groupe_qpv()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tables_bdnb = response.parse()
        assert_matches_type(TablesBdnbRetrieveRelBatimentGroupeQpvResponse, tables_bdnb, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_rel_batiment_groupe_qpv(self, client: BdnbAPI) -> None:
        with client.donnees.tables_bdnb.with_streaming_response.retrieve_rel_batiment_groupe_qpv() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tables_bdnb = response.parse()
            assert_matches_type(TablesBdnbRetrieveRelBatimentGroupeQpvResponse, tables_bdnb, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTablesBdnb:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve_batiment_groupe_bdtopo_zoac(self, async_client: AsyncBdnbAPI) -> None:
        tables_bdnb = await async_client.donnees.tables_bdnb.retrieve_batiment_groupe_bdtopo_zoac()
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeBdtopoZoacResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_method_retrieve_batiment_groupe_bdtopo_zoac_with_all_params(
        self, async_client: AsyncBdnbAPI
    ) -> None:
        tables_bdnb = await async_client.donnees.tables_bdnb.retrieve_batiment_groupe_bdtopo_zoac(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            l_nature="l_nature",
            l_nature_detaillee="l_nature_detaillee",
            l_toponyme="l_toponyme",
            limit="limit",
            offset="offset",
            order="order",
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeBdtopoZoacResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_batiment_groupe_bdtopo_zoac(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.donnees.tables_bdnb.with_raw_response.retrieve_batiment_groupe_bdtopo_zoac()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tables_bdnb = await response.parse()
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeBdtopoZoacResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_batiment_groupe_bdtopo_zoac(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.donnees.tables_bdnb.with_streaming_response.retrieve_batiment_groupe_bdtopo_zoac() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tables_bdnb = await response.parse()
            assert_matches_type(TablesBdnbRetrieveBatimentGroupeBdtopoZoacResponse, tables_bdnb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_batiment_groupe_dvf_open_statistique(self, async_client: AsyncBdnbAPI) -> None:
        tables_bdnb = await async_client.donnees.tables_bdnb.retrieve_batiment_groupe_dvf_open_statistique()
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeDvfOpenStatistiqueResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_method_retrieve_batiment_groupe_dvf_open_statistique_with_all_params(
        self, async_client: AsyncBdnbAPI
    ) -> None:
        tables_bdnb = await async_client.donnees.tables_bdnb.retrieve_batiment_groupe_dvf_open_statistique(
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
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeDvfOpenStatistiqueResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_batiment_groupe_dvf_open_statistique(self, async_client: AsyncBdnbAPI) -> None:
        response = (
            await async_client.donnees.tables_bdnb.with_raw_response.retrieve_batiment_groupe_dvf_open_statistique()
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tables_bdnb = await response.parse()
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeDvfOpenStatistiqueResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_batiment_groupe_dvf_open_statistique(
        self, async_client: AsyncBdnbAPI
    ) -> None:
        async with async_client.donnees.tables_bdnb.with_streaming_response.retrieve_batiment_groupe_dvf_open_statistique() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tables_bdnb = await response.parse()
            assert_matches_type(
                TablesBdnbRetrieveBatimentGroupeDvfOpenStatistiqueResponse, tables_bdnb, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_batiment_groupe_geospx(self, async_client: AsyncBdnbAPI) -> None:
        tables_bdnb = await async_client.donnees.tables_bdnb.retrieve_batiment_groupe_geospx()
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeGeospxResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_method_retrieve_batiment_groupe_geospx_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        tables_bdnb = await async_client.donnees.tables_bdnb.retrieve_batiment_groupe_geospx(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            croisement_geospx_reussi="croisement_geospx_reussi",
            fiabilite_adresse="fiabilite_adresse",
            fiabilite_emprise_sol="fiabilite_emprise_sol",
            fiabilite_hauteur="fiabilite_hauteur",
            limit="limit",
            offset="offset",
            order="order",
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeGeospxResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_batiment_groupe_geospx(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.donnees.tables_bdnb.with_raw_response.retrieve_batiment_groupe_geospx()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tables_bdnb = await response.parse()
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeGeospxResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_batiment_groupe_geospx(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.donnees.tables_bdnb.with_streaming_response.retrieve_batiment_groupe_geospx() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tables_bdnb = await response.parse()
            assert_matches_type(TablesBdnbRetrieveBatimentGroupeGeospxResponse, tables_bdnb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_batiment_groupe_qpv(self, async_client: AsyncBdnbAPI) -> None:
        tables_bdnb = await async_client.donnees.tables_bdnb.retrieve_batiment_groupe_qpv()
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeQpvResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_method_retrieve_batiment_groupe_qpv_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        tables_bdnb = await async_client.donnees.tables_bdnb.retrieve_batiment_groupe_qpv(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            limit="limit",
            nom_quartier="nom_quartier",
            offset="offset",
            order="order",
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeQpvResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_batiment_groupe_qpv(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.donnees.tables_bdnb.with_raw_response.retrieve_batiment_groupe_qpv()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tables_bdnb = await response.parse()
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeQpvResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_batiment_groupe_qpv(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.donnees.tables_bdnb.with_streaming_response.retrieve_batiment_groupe_qpv() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tables_bdnb = await response.parse()
            assert_matches_type(TablesBdnbRetrieveBatimentGroupeQpvResponse, tables_bdnb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_batiment_groupe_synthese_enveloppe(self, async_client: AsyncBdnbAPI) -> None:
        tables_bdnb = await async_client.donnees.tables_bdnb.retrieve_batiment_groupe_synthese_enveloppe()
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeSyntheseEnveloppeResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_method_retrieve_batiment_groupe_synthese_enveloppe_with_all_params(
        self, async_client: AsyncBdnbAPI
    ) -> None:
        tables_bdnb = await async_client.donnees.tables_bdnb.retrieve_batiment_groupe_synthese_enveloppe(
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
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeSyntheseEnveloppeResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_batiment_groupe_synthese_enveloppe(self, async_client: AsyncBdnbAPI) -> None:
        response = (
            await async_client.donnees.tables_bdnb.with_raw_response.retrieve_batiment_groupe_synthese_enveloppe()
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tables_bdnb = await response.parse()
        assert_matches_type(TablesBdnbRetrieveBatimentGroupeSyntheseEnveloppeResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_batiment_groupe_synthese_enveloppe(
        self, async_client: AsyncBdnbAPI
    ) -> None:
        async with async_client.donnees.tables_bdnb.with_streaming_response.retrieve_batiment_groupe_synthese_enveloppe() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tables_bdnb = await response.parse()
            assert_matches_type(
                TablesBdnbRetrieveBatimentGroupeSyntheseEnveloppeResponse, tables_bdnb, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_referentiel_administratif_iris(self, async_client: AsyncBdnbAPI) -> None:
        tables_bdnb = await async_client.donnees.tables_bdnb.retrieve_referentiel_administratif_iris()
        assert_matches_type(TablesBdnbRetrieveReferentielAdministratifIrisResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_method_retrieve_referentiel_administratif_iris_with_all_params(
        self, async_client: AsyncBdnbAPI
    ) -> None:
        tables_bdnb = await async_client.donnees.tables_bdnb.retrieve_referentiel_administratif_iris(
            code_commune_insee="code_commune_insee",
            code_departement_insee="code_departement_insee",
            code_iris="code_iris",
            geom_iris="geom_iris",
            libelle_iris="libelle_iris",
            limit="limit",
            offset="offset",
            order="order",
            select="select",
            type_iris="type_iris",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(TablesBdnbRetrieveReferentielAdministratifIrisResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_referentiel_administratif_iris(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.donnees.tables_bdnb.with_raw_response.retrieve_referentiel_administratif_iris()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tables_bdnb = await response.parse()
        assert_matches_type(TablesBdnbRetrieveReferentielAdministratifIrisResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_referentiel_administratif_iris(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.donnees.tables_bdnb.with_streaming_response.retrieve_referentiel_administratif_iris() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tables_bdnb = await response.parse()
            assert_matches_type(TablesBdnbRetrieveReferentielAdministratifIrisResponse, tables_bdnb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_rel_batiment_construction_adresse(self, async_client: AsyncBdnbAPI) -> None:
        tables_bdnb = await async_client.donnees.tables_bdnb.retrieve_rel_batiment_construction_adresse()
        assert_matches_type(TablesBdnbRetrieveRelBatimentConstructionAdresseResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_method_retrieve_rel_batiment_construction_adresse_with_all_params(
        self, async_client: AsyncBdnbAPI
    ) -> None:
        tables_bdnb = await async_client.donnees.tables_bdnb.retrieve_rel_batiment_construction_adresse(
            adresse_principale="adresse_principale",
            batiment_construction_id="batiment_construction_id",
            cle_interop_adr="cle_interop_adr",
            code_departement_insee="code_departement_insee",
            distance_batiment_construction_adresse="distance_batiment_construction_adresse",
            fiabilite="fiabilite",
            limit="limit",
            offset="offset",
            order="order",
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(TablesBdnbRetrieveRelBatimentConstructionAdresseResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_rel_batiment_construction_adresse(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.donnees.tables_bdnb.with_raw_response.retrieve_rel_batiment_construction_adresse()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tables_bdnb = await response.parse()
        assert_matches_type(TablesBdnbRetrieveRelBatimentConstructionAdresseResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_rel_batiment_construction_adresse(
        self, async_client: AsyncBdnbAPI
    ) -> None:
        async with async_client.donnees.tables_bdnb.with_streaming_response.retrieve_rel_batiment_construction_adresse() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tables_bdnb = await response.parse()
            assert_matches_type(
                TablesBdnbRetrieveRelBatimentConstructionAdresseResponse, tables_bdnb, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_rel_batiment_groupe_adresse(self, async_client: AsyncBdnbAPI) -> None:
        tables_bdnb = await async_client.donnees.tables_bdnb.retrieve_rel_batiment_groupe_adresse()
        assert_matches_type(TablesBdnbRetrieveRelBatimentGroupeAdresseResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_method_retrieve_rel_batiment_groupe_adresse_with_all_params(
        self, async_client: AsyncBdnbAPI
    ) -> None:
        tables_bdnb = await async_client.donnees.tables_bdnb.retrieve_rel_batiment_groupe_adresse(
            batiment_groupe_id="batiment_groupe_id",
            classe="classe",
            cle_interop_adr="cle_interop_adr",
            code_departement_insee="code_departement_insee",
            geom_bat_adresse="geom_bat_adresse",
            lien_valide="lien_valide",
            limit="limit",
            offset="offset",
            order="order",
            origine="origine",
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(TablesBdnbRetrieveRelBatimentGroupeAdresseResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_rel_batiment_groupe_adresse(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.donnees.tables_bdnb.with_raw_response.retrieve_rel_batiment_groupe_adresse()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tables_bdnb = await response.parse()
        assert_matches_type(TablesBdnbRetrieveRelBatimentGroupeAdresseResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_rel_batiment_groupe_adresse(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.donnees.tables_bdnb.with_streaming_response.retrieve_rel_batiment_groupe_adresse() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tables_bdnb = await response.parse()
            assert_matches_type(TablesBdnbRetrieveRelBatimentGroupeAdresseResponse, tables_bdnb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_rel_batiment_groupe_proprietaire_siren(self, async_client: AsyncBdnbAPI) -> None:
        tables_bdnb = await async_client.donnees.tables_bdnb.retrieve_rel_batiment_groupe_proprietaire_siren()
        assert_matches_type(
            TablesBdnbRetrieveRelBatimentGroupeProprietaireSirenResponse, tables_bdnb, path=["response"]
        )

    @parametrize
    async def test_method_retrieve_rel_batiment_groupe_proprietaire_siren_with_all_params(
        self, async_client: AsyncBdnbAPI
    ) -> None:
        tables_bdnb = await async_client.donnees.tables_bdnb.retrieve_rel_batiment_groupe_proprietaire_siren(
            bat_prop_denomination_proprietaire="bat_prop_denomination_proprietaire",
            dans_majic_pm="dans_majic_pm",
            is_bailleur="is_bailleur",
            limit="limit",
            nb_locaux_open="nb_locaux_open",
            offset="offset",
            order="order",
            select="select",
            siren="siren",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(
            TablesBdnbRetrieveRelBatimentGroupeProprietaireSirenResponse, tables_bdnb, path=["response"]
        )

    @parametrize
    async def test_raw_response_retrieve_rel_batiment_groupe_proprietaire_siren(
        self, async_client: AsyncBdnbAPI
    ) -> None:
        response = (
            await async_client.donnees.tables_bdnb.with_raw_response.retrieve_rel_batiment_groupe_proprietaire_siren()
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tables_bdnb = await response.parse()
        assert_matches_type(
            TablesBdnbRetrieveRelBatimentGroupeProprietaireSirenResponse, tables_bdnb, path=["response"]
        )

    @parametrize
    async def test_streaming_response_retrieve_rel_batiment_groupe_proprietaire_siren(
        self, async_client: AsyncBdnbAPI
    ) -> None:
        async with async_client.donnees.tables_bdnb.with_streaming_response.retrieve_rel_batiment_groupe_proprietaire_siren() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tables_bdnb = await response.parse()
            assert_matches_type(
                TablesBdnbRetrieveRelBatimentGroupeProprietaireSirenResponse, tables_bdnb, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_rel_batiment_groupe_qpv(self, async_client: AsyncBdnbAPI) -> None:
        tables_bdnb = await async_client.donnees.tables_bdnb.retrieve_rel_batiment_groupe_qpv()
        assert_matches_type(TablesBdnbRetrieveRelBatimentGroupeQpvResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_method_retrieve_rel_batiment_groupe_qpv_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        tables_bdnb = await async_client.donnees.tables_bdnb.retrieve_rel_batiment_groupe_qpv(
            batiment_construction_id="batiment_construction_id",
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            limit="limit",
            offset="offset",
            order="order",
            qpv_code_qp="qpv_code_qp",
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(TablesBdnbRetrieveRelBatimentGroupeQpvResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_rel_batiment_groupe_qpv(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.donnees.tables_bdnb.with_raw_response.retrieve_rel_batiment_groupe_qpv()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tables_bdnb = await response.parse()
        assert_matches_type(TablesBdnbRetrieveRelBatimentGroupeQpvResponse, tables_bdnb, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_rel_batiment_groupe_qpv(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.donnees.tables_bdnb.with_streaming_response.retrieve_rel_batiment_groupe_qpv() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tables_bdnb = await response.parse()
            assert_matches_type(TablesBdnbRetrieveRelBatimentGroupeQpvResponse, tables_bdnb, path=["response"])

        assert cast(Any, response.is_closed) is True
