# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CompletListParams"]


class CompletListParams(TypedDict, total=False):
    alea_argiles: str
    """(argiles) Aléa du risque argiles"""

    alea_radon: str
    """(radon) alea du risque radon"""

    altitude_sol_mean: str
    """(ign) Altitude au sol moyenne [m]"""

    annee_construction: str
    """Année de construction du bâtiment"""

    arrete_2021: str
    """
    précise si le DPE est un DPE qui est issu de la nouvelle réforme du DPE (arrété
    du 31 mars 2021) ou s'il s'agit d'un DPE issu de la modification antérieure
    de 2012.
    """

    batiment_groupe_id: str
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    chauffage_solaire: str
    """présence de chauffage solaire"""

    classe_bilan_dpe: str
    """
    Classe du DPE issu de la synthèse du double seuil sur les consommations énergie
    primaire et les émissions de CO2 sur les 5 usages
    (ecs/chauffage/climatisation/eclairage/auxiliaires). valable uniquement pour les
    DPE appliquant la méthode de l'arràªté du 31 mars 2021 (en vigueur actuellement)
    """

    classe_conso_energie_arrete_2012: str
    """classe d'émission GES du DPE 3 usages (Chauffage, ECS, Climatisation).

    Valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    classe_inertie: str
    """classe d'inertie du DPE (enum version BDNB)"""

    cle_interop_adr_principale_ban: str
    """Clé d'interopérabilité de l'adresse principale (issue de la BAN)"""

    code_commune_insee: str
    """Code INSEE de la commune"""

    code_departement_insee: str
    """Code département INSEE"""

    code_epci_insee: str
    """Code de l'EPCI"""

    code_iris: str
    """Code iris INSEE"""

    code_qp: str
    """identifiant de la table qpv"""

    code_region_insee: str
    """Code région INSEE"""

    conso_3_usages_ep_m2_arrete_2012: str
    """
    consommation annuelle 3 usages énergie primaire rapportée au m2 (Chauffage, ECS
    , Climatisation). valable uniquement pour les DPE appliquant la méthode de
    l'arràªté du 8 février 2012
    """

    conso_5_usages_ep_m2: str
    """
    consommation annuelle 5 usages
    (ecs/chauffage/climatisation/eclairage/auxiliaires) en énergie primaire (déduit
    de la production pv autoconsommée) (kWhep/mÂ²/an). valable uniquement pour les
    DPE appliquant la méthode de l'arràªté du 31 mars 2021 (en vigueur actuellement)
    """

    conso_pro_dle_elec_2020: str
    """Consommation professionnelle électrique [kWh/an]"""

    conso_pro_dle_gaz_2020: str
    """Consommation professionnelle gaz [kWh/an]"""

    conso_res_dle_elec_2020: str
    """Consommation résidentielle électrique [kWh/an]"""

    conso_res_dle_gaz_2020: str
    """Consommation résidentielle gaz [kWh/an]"""

    contient_fictive_geom_groupe: str
    """
    Vaut "vrai", si la géométrie du groupe de bâtiment est générée automatiquement
    et ne représente pas la géométrie du groupe de bâtiment.
    """

    croisement_geospx_reussi: str
    """
    le croisement géospatial entre la BDTOPO et les fichiers fonciers est considérée
    comme réussi
    """

    date_reception_dpe: str
    """date de réception du DPE dans la base de données de l'ADEME"""

    difference_rel_valeur_fonciere_etat_initial_renove_categorie: str
    """
    categorie de la difference relative de valeur fonciere avant et apres renovation
    (verbose)
    """

    distance_batiment_historique_plus_proche: str
    """(mer) Distance au bâtiment historique le plus proche (si moins de 500m) [m]"""

    ecs_solaire: str
    """présence d'ecs solaire"""

    emission_ges_3_usages_ep_m2_arrete_2012: str
    """
    emission GES totale 3 usages énergie primaire rapportée au m2 (Chauffage, ECS ,
    Climatisation). valable uniquement pour les DPE appliquant la méthode de
    l'arràªté du 8 février 2012 (kgCO2/m2/an).
    """

    emission_ges_5_usages_m2: str
    """
    emission GES totale 5 usages rapportée au mÂ² (déduit de la production pv
    autoconsommée) (ecs/chauffage/climatisation/eclairage/auxiliaires)(kgCO2/m2/an).
    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 31 mars
    2021 (en vigueur actuellement)
    """

    epaisseur_lame: str
    """
    epaisseur principale de la lame de gaz entre vitrages pour les baies vitrées du
    DPE.
    """

    etat_initial_consommation_energie_estim_inc: str
    """
    Incertitude des estimations de consommation énergétique finale avant rénovation
    [kWh/m2/an]
    """

    etat_initial_consommation_energie_estim_lower: str
    """
    Estimation basse de la consommation énergétique finale avant rénovation
    [kWh/m2/an]
    """

    etat_initial_consommation_energie_estim_mean: str
    """
    Estimation moyenne de la consommation énergétique finale avant rénovation
    [kWh/m2/an]
    """

    etat_initial_consommation_energie_estim_upper: str
    """
    Estimation haute de la consommation énergétique finale avant rénovation
    [kWh/m2/an]
    """

    etat_initial_consommation_energie_primaire_estim_lower: str
    """
    Estimation basse de la consommation énergétique primaire avant rénovation
    [kWh/m2/an]
    """

    etat_initial_consommation_energie_primaire_estim_mean: str
    """
    Estimation moyenne de la consommation énergétique primaire avant rénovation
    [kWh/m2/an]
    """

    etat_initial_consommation_energie_primaire_estim_upper: str
    """
    Estimation haute de la consommation énergétique primaire avant rénovation
    [kWh/m2/an]
    """

    etat_initial_consommation_ges_estim_inc: str
    """
    Incertitude sur l'estimation de consommation de GES avant rénovation
    [kgeqC02/m2/an]
    """

    etat_initial_ges_estim_lower: str
    """Estimation basse de la consommation de GES avant rénovation [kgeqC02/m2/an]"""

    etat_initial_ges_estim_mean: str
    """Estimation moyenne de la consommation de GES avant rénovation [kgeqC02/m2/an]"""

    etat_initial_ges_estim_upper: str
    """Estimation haute de la consommation de GES avant rénovation [kgeqC02/m2/an]"""

    etat_initial_risque_canicule: str
    """Estimation du risque canicule avant rénovation [1-5]"""

    etat_initial_risque_canicule_inc: str
    """Incertitude de l'estimation du risque canicule avant rénovation [1-5]"""

    etat_renove_consommation_energie_estim_inc: str
    """
    Incertitude sur les estimations des consommations énergétiques finales après un
    scénario de rénovation globale "standard" (isolation des principaux composants
    d'enveloppe et changement de système énergétique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_energie_estim_lower: str
    """
    Estimation basse de la consommation énergétique finale après un scénario de
    rénovation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de système énergétique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_energie_estim_mean: str
    """
    Estimation moyenne de la consommation énergétique finale après un scénario de
    rénovation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de système énergétique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_energie_estim_upper: str
    """
    Estimation haute de la consommation énergétique finale après un scénario de
    rénovation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de système énergétique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_energie_primaire_estim_lower: str
    """
    Estimation basse de la consommation d'énergie primaire après un scénario de
    rénovation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de système énergétique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_energie_primaire_estim_mean: str
    """
    Estimation moyenne de la consommation d'énergie primaire après un scénario de
    rénovation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de système énergétique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_energie_primaire_estim_upper: str
    """
    Estimation haute de la consommation d'énergie primaire après un scénario de
    rénovation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de système énergétique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_ges_estim_inc: str
    """
    Incertitude sur l'estimation de consommation de GES après un scénario de
    rénovation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de système énergétique de chauffage) [kgeqC02/m2/an]
    """

    etat_renove_ges_estim_lower: str
    """
    Estimation basse des émissions de GES après un scénario de rénovation globale
    "standard" (isolation des principaux composants d'enveloppe et changement de
    système énergétique de chauffage) [kWh/m2/an]
    """

    etat_renove_ges_estim_mean: str
    """
    Estimation moyenne des émissions de GES après un scénario de rénovation globale
    "standard" (isolation des principaux composants d'enveloppe et changement de
    système énergétique de chauffage) [kWh/m2/an]
    """

    etat_renove_ges_estim_upper: str
    """
    Estimation haute des émissions de GES après un scénario de rénovation globale
    "standard" (isolation des principaux composants d'enveloppe et changement de
    système énergétique de chauffage) [kWh/m2/an]
    """

    etat_renove_risque_canicule: str
    """Estimation du risque canicule après rénovation [1-5]"""

    etat_renove_risque_canicule_inc: str
    """Incertitude de l'estimation du risque canicule après rénovation [1-5]"""

    etiquette_dpe_initial_a: str
    """
    Estimation de la probabilité d'avoir des logements d'étiquette A dans le
    bâtiment pour l'état actuel du bâtiment
    """

    etiquette_dpe_initial_b: str
    """
    Estimation de la probabilité d'avoir des logements d'étiquette B dans le
    bâtiment pour l'état actuel du bâtiment
    """

    etiquette_dpe_initial_c: str
    """
    Estimation de la probabilité d'avoir des logements d'étiquette C dans le
    bâtiment pour l'état actuel du bâtiment
    """

    etiquette_dpe_initial_d: str
    """
    Estimation de la probabilité d'avoir des logements d'étiquette D dans le
    bâtiment pour l'état actuel du bâtiment
    """

    etiquette_dpe_initial_e: str
    """
    Estimation de la probabilité d'avoir des logements d'étiquette E dans le
    bâtiment pour l'état actuel du bâtiment
    """

    etiquette_dpe_initial_f: str
    """
    Estimation de la probabilité d'avoir des logements d'étiquette F dans le
    bâtiment pour l'état actuel du bâtiment
    """

    etiquette_dpe_initial_g: str
    """
    Estimation de la probabilité d'avoir des logements d'étiquette G dans le
    bâtiment pour l'état actuel du bâtiment
    """

    etiquette_dpe_initial_inc: str
    """
    Classe d'incertitude de classe sur l'étiquette dpe avec la plus grande
    probabilité avant rénovation [1 à 5]. Cet indicateur se lit de 1 = peu fiable à
    5 = fiable.
    """

    etiquette_dpe_initial_map: str
    """Etiquette ayant la plus grande probabilité pour l'état actuel du bâtiment"""

    etiquette_dpe_initial_map_2nd: str
    """2 étiquettes ayant la plus grande probabilité pour l'état actuel du bâtiment.

    Si le champs vaut F-G alors F la première étiquette est l'étiquette la plus
    probable , G la seconde étiquette la plus probable.
    """

    etiquette_dpe_initial_map_2nd_prob: str
    """
    Probabilité que le bâtiment ait une étiquette DPE parmi les 2 étiquettes ayant
    la plus grande probabilité pour l'état actuel du bâtiment. Si
    etiquette_dpe_initial_map_2nd = F-G et que etiquette_dpe_initial_map_2nd_prob =
    0.95 alors il y a 95% de chance que l'étiquette DPE de ce bâtiment soit classé F
    ou G.
    """

    etiquette_dpe_renove_a: str
    """
    Estimation de la probabilité d'avoir des logements d'étiquette A dans le
    bâtiment après un scénario de rénovation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de système énergétique de
    chauffage)
    """

    etiquette_dpe_renove_b: str
    """
    Estimation de la probabilité d'avoir des logements d'étiquette B dans le
    bâtiment après un scénario de rénovation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de système énergétique de
    chauffage)
    """

    etiquette_dpe_renove_c: str
    """
    Estimation de la probabilité d'avoir des logements d'étiquette C dans le
    bâtiment après un scénario de rénovation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de système énergétique de
    chauffage)
    """

    etiquette_dpe_renove_d: str
    """
    Estimation de la probabilité d'avoir des logements d'étiquette D dans le
    bâtiment après un scénario de rénovation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de système énergétique de
    chauffage)
    """

    etiquette_dpe_renove_e: str
    """
    Estimation de la probabilité d'avoir des logements d'étiquette E dans le
    bâtiment après un scénario de rénovation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de système énergétique de
    chauffage)
    """

    etiquette_dpe_renove_f: str
    """
    Estimation de la probabilité d'avoir des logements d'étiquette F dans le
    bâtiment après un scénario de rénovation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de système énergétique de
    chauffage)
    """

    etiquette_dpe_renove_g: str
    """
    Estimation de la probabilité d'avoir des logements d'étiquette G dans le
    bâtiment après un scénario de rénovation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de système énergétique de
    chauffage)
    """

    etiquette_dpe_renove_inc: str
    """
    Incertitude de classe sur l'étiquette dpe avec la plus grande probabilité après
    un scénario de rénovation globale "standard" (isolation des principaux
    composants d'enveloppe et changement de système énergétique de chauffage) [1-5]
    """

    etiquette_dpe_renove_map: str
    """
    Etiquette ayant la plus grande probabilité après un scénario de rénovation
    globale "standard" (isolation des principaux composants d'enveloppe et
    changement de système énergétique de chauffage)
    """

    etiquette_dpe_renove_map_2nd: str
    """
    2 étiquettes ayant la plus grande probabilité après un scénario de rénovation
    globale "standard" (isolation des principaux composants d'enveloppe et
    changement de système énergétique de chauffage)
    """

    etiquette_dpe_renove_map_2nd_prob: str
    """
    Probabilité que le bâtiment ait une étiquette DPE parmi les 2 étiquettes ayant
    la plus grande probabilité après un scénario de rénovation globale "standard"
    (isolation des principaux composants d'enveloppe et changement de système
    énergétique de chauffage)
    """

    etiquette_dpe_synthese_particulier_simple: str
    """Etiquette DPE selon l'arràªté 2021.

    Si un DPE existe, l'étiquette provient d'un DPE de l'AEDME, sinon, il s'agit
    d'une simulation.
    """

    etiquette_dpe_synthese_particulier_source: str
    """TODO"""

    facteur_solaire_baie_vitree: str
    """facteur de transmission du flux solaire par la baie vitrée.

    coefficient entre 0 et 1
    """

    fiabilite_cr_adr_niv_1: str
    """
    Fiabilité des données croisées à l'adresse ('données croisées à l'adresse
    fiables', 'données croisées à l'adresse fiables à l'echelle de la parcelle
    unifiee', 'données croisées à l'adresse moyennement fiables', 'problème de
    géocodage')
    """

    fiabilite_cr_adr_niv_2: str
    """Fiabilité détaillée des données croisées à l'adresse"""

    fiabilite_emprise_sol: str
    """Fiabilité de l'emprise au sol du bâtiment"""

    fiabilite_hauteur: str
    """Fiabilité de la hauteur du bâtiment"""

    geom_groupe: str
    """Géométrie multipolygonale du groupe de bâtiment (Lambert-93)"""

    gisement_gain_conso_finale_total: str
    """(cstb) Estimation du gisement de gain de consommation finale total (kWh/m2/an)"""

    gisement_gain_energetique_mean: str
    """Estimation du gain énergétique moyen"""

    gisement_gain_ges_mean: str
    """
    Estimation moyenne du gisement de gain sur les émissions de gaz à effets de
    serre
    """

    hauteur_mean: str
    """(ign) Hauteur moyenne des bâtiments [m]"""

    identifiant_dpe: str
    """identifiant de la table des DPE ademe"""

    indicateur_distance_au_reseau: str
    """
    Indication sur la distance entre le bâtiment et le point au réseau de chaleur le
    plus proche en vue d'un potentiel raccordement au réseau.
    """

    l_cle_interop_adr: str
    """Liste de clés d'interopérabilité de l'adresse postale"""

    l_denomination_proprietaire: str
    """Liste de dénominations de propriétaires"""

    l_libelle_adr: str
    """Liste de libellé complet de l'adresse"""

    l_orientation_baie_vitree: str
    """liste des orientations des baies vitrées (enum version BDNB)"""

    l_parcelle_id: str
    """
    Liste d'identifiants de parcelle (Concaténation de ccodep, ccocom, ccopre,
    ccosec, dnupla)
    """

    l_siren: str
    """Liste d'identifiants siren"""

    l_type_generateur_chauffage: str
    """
    type de générateur de chauffage principal (enum version simplifiée BDNB)
    concaténé en liste pour tous les DPE
    """

    l_type_generateur_ecs: str
    """
    type de générateur d'ECS principal (enum version simplifiée BDNB) concaténé en
    liste pour tous les DPE
    """

    libelle_adr_principale_ban: str
    """Libellé complet de l'adresse principale (issue de la BAN)"""

    libelle_commune_insee: str
    """(insee) Libellé de la commune accueillant le groupe de bâtiment"""

    limit: str
    """Limiting and Pagination"""

    mat_mur_txt: str
    """(ffo) Matériaux principal des murs extérieurs"""

    mat_toit_txt: str
    """(ffo) Matériau principal des toitures"""

    materiaux_structure_mur_exterieur: str
    """
    matériaux ou principe constructif principal utilisé pour les murs extérieurs
    (enum version BDNB)
    """

    materiaux_structure_mur_exterieur_simplifie: str
    """materiaux principal utilié pour les murs extérieur simplifié.

    Cette information peut àªtre récupérée de différentes sources (Fichiers Fonciers
    ou DPE pour le moment)
    """

    materiaux_toiture_simplifie: str
    """materiaux principal utilié pour la toiture simplifié.

    Cette information peut àªtre récupérée de différentes sources (Fichiers Fonciers
    ou DPE pour le moment)
    """

    nb_adresse_valid_ban: str
    """
    Nombre d'adresses valides différentes provenant de la BAN qui desservent le
    groupe de bâtiment
    """

    nb_classe_bilan_dpe_a: str
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe A
    """

    nb_classe_bilan_dpe_b: str
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe B
    """

    nb_classe_bilan_dpe_c: str
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe C
    """

    nb_classe_bilan_dpe_d: str
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe D
    """

    nb_classe_bilan_dpe_e: str
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe E
    """

    nb_classe_bilan_dpe_f: str
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe F
    """

    nb_classe_bilan_dpe_g: str
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe G
    """

    nb_classe_conso_energie_arrete_2012_a: str
    """(dpe) Nombre de DPE de la classe énergétique A.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_b: str
    """(dpe) Nombre de DPE de la classe énergétique B.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_c: str
    """(dpe) Nombre de DPE de la classe énergétique C.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_d: str
    """(dpe) Nombre de DPE de la classe énergétique D.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_e: str
    """(dpe) Nombre de DPE de la classe énergétique E.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_f: str
    """(dpe) Nombre de DPE de la classe énergétique F.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_g: str
    """(dpe) Nombre de DPE de la classe énergétique G.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_nc: str
    """
    (dpe) Nombre de DPE n'ayant pas fait l'objet d'un calcul d'étiquette énergie
    (DPE dits vierges). valable uniquement pour les DPE appliquant la méthode de
    l'arràªté du 8 février 2012
    """

    nb_log: str
    """(rnc) Nombre de logements"""

    nb_log_rnc: str
    """(rnc) Nombre de logements"""

    nb_lot_garpark_rnc: str
    """Nombre de lots de stationnement"""

    nb_lot_tertiaire_rnc: str
    """Nombre de lots de type bureau et commerce"""

    nb_niveau: str
    """(ffo) Nombre de niveau du bâtiment (ex: RDC = 1, R+1 = 2, etc..)"""

    nb_pdl_pro_dle_elec_2020: str
    """Nombre de points de livraison électrique professionnels [kWh/an]"""

    nb_pdl_pro_dle_gaz_2020: str
    """Nombre de points de livraison gaz professionnels [kWh/an]"""

    nb_pdl_res_dle_elec_2020: str
    """Nombre de points de livraison électrique résidentiels [kWh/an]"""

    nb_pdl_res_dle_gaz_2020: str
    """Nombre de points de livraison gaz résidentiels [kWh/an]"""

    nom_batiment_historique_plus_proche: str
    """(mer:tico) nom du bâtiment historique le plus proche"""

    nom_qp: str
    """Nom du quartier prioritaire dans lequel se trouve le bâtiment"""

    nom_quartier_qpv: str
    """Nom du quartier prioritaire dans lequel se trouve le bâtiment"""

    numero_immat_principal: str
    """numéro d'immatriculation principal associé au bâtiment groupe.

    (numéro d'immatriculation copropriété qui comporte le plus de lots)
    """

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    potentiel_raccordement_reseau_chaleur: str
    """Indicateur de potentiel de raccordement au réseau de chaleur.

    L'indicateur dépend de la distance entre le bâtiment et le réseau et du type de
    circuit de chauffage existant du bâtiment. Enfin, si le bâtiment est déjà
    raccordé alors il est indiqué comme tel.
    """

    pourcentage_surface_baie_vitree_exterieur: str
    """pourcentage de surface de baies vitrées sur les murs extérieurs"""

    presence_balcon: str
    """
    présence de balcons identifiés par analyse des coefficients de masques solaires
    du DPE.
    """

    quartier_prioritaire: str
    """Est situé dans un quartier prioritaire"""

    s_geom_groupe: str
    """Surface au sol de la géométrie du bâtiment groupe (geom_groupe)"""

    select: str
    """Filtering Columns"""

    surface_emprise_sol: str
    """Surface au sol de la géométrie du bâtiment groupe (geom_groupe)"""

    surface_facade_ext: str
    """Estimation de la surface de faà§ade donnant sur l'exterieur [mÂ²]"""

    surface_facade_mitoyenne: str
    """Estimation de la surface de faà§ade donnant sur un autre bâtiment [mÂ²]"""

    surface_facade_totale: str
    """Estimation de la surface totale de faà§ade (murs + baies) [mÂ²]"""

    surface_facade_vitree: str
    """Estimation de la surface de faà§ade vitrée [mÂ²]"""

    traversant: str
    """indicateur du cà´té traversant du logement."""

    type_dpe: str
    """type de DPE.

    Permet de préciser le type de DPE (arràªté 2012/arràªté 2021), son objet
    (logement, immeuble de logement, tertiaire) et la méthode de calcul utilisé (3CL
    conventionel,facture ou RT2012/RE2020)
    """

    type_energie_chauffage: str
    """
    type d'énergie pour le générateur de chauffage principal (enum version
    simplifiée BDNB)
    """

    type_energie_chauffage_appoint: str
    """
    type d'énergie pour le générateur de chauffage d'appoint (enum version
    simplifiée BDNB)
    """

    type_fermeture: str
    """
    type de fermeture principale installée sur les baies vitrées du DPE
    (volet,persienne etc..) (enum version BDNB)
    """

    type_gaz_lame: str
    """
    type de gaz injecté principalement dans la lame entre les vitrages des baies
    vitrées du DPE (double vitrage ou triple vitrage uniquement) (enum version BDNB)
    """

    type_generateur_chauffage: str
    """type de générateur de chauffage principal (enum version simplifiée BDNB)"""

    type_generateur_chauffage_anciennete: str
    """ancienneté du générateur de chauffage principal"""

    type_generateur_chauffage_anciennete_appoint: str
    """ancienneté du générateur de chauffage d'appoint"""

    type_generateur_chauffage_appoint: str
    """type de générateur de chauffage d'appoint (enum version simplifiée BDNB)"""

    type_generateur_climatisation: str
    """type de générateur de climatisation principal (enum version simplifiée BDNB)"""

    type_generateur_climatisation_anciennete: str
    """ancienneté du générateur de climatisation principal"""

    type_generateur_ecs: str
    """
    type de générateur d'eau chaude sanitaire (ECS) principal (enum version
    simplifiée BDNB)
    """

    type_generateur_ecs_anciennete: str
    """ancienneté du générateur d'eau chaude sanitaire (ECS) principal"""

    type_installation_chauffage: str
    """
    type d'installation de chauffage (collectif ou individuel) (enum version
    simplifiée BDNB)
    """

    type_installation_ecs: str
    """
    type d'installation d'eau chaude sanitaire (ECS) (collectif ou individuel) (enum
    version simplifiée BDNB)
    """

    type_isolation_mur_exterieur: str
    """
    type d'isolation principal des murs donnant sur l'extérieur pour le DPE (enum
    version BDNB)
    """

    type_isolation_plancher_bas: str
    """
    type d'isolation principal des planchers bas déperditifs pour le DPE (enum
    version BDNB)
    """

    type_isolation_plancher_haut: str
    """
    type d'isolation principal des planchers hauts déperditifs pour le DPE (enum
    version BDNB)
    """

    type_materiaux_menuiserie: str
    """
    type de matériaux principal des menuiseries des baies vitrées du DPE (enum
    version BDNB)
    """

    type_plancher_bas_deperditif: str
    """
    materiaux ou principe constructif principal des planchers bas (enum version
    BDNB)
    """

    type_plancher_haut_deperditif: str
    """
    materiaux ou principe constructif principal des planchers hauts (enum version
    BDNB)
    """

    type_production_energie_renouvelable: str
    """type de production ENR pour le DPE (enum version DPE 2021)"""

    type_ventilation: str
    """type de ventilation (enum version BDNB)"""

    type_vitrage: str
    """type de vitrage principal des baies vitrées du DPE (enum version BDNB)"""

    u_baie_vitree: str
    """
    Coefficient de transmission thermique moyen des baies vitrées en incluant le
    calcul de la résistance additionelle des fermetures (calcul Ujn) (W/mÂ²/K)
    """

    u_mur_exterieur: str
    """Coefficient de transmission thermique moyen des murs extérieurs (W/mÂ²/K)"""

    u_plancher_bas_final_deperditif: str
    """
    Coefficient de transmission thermique moyen des planchers bas en prenant en
    compte l'atténuation forfaitaire du U lorsqu'en contact avec le sol de la
    méthode 3CL(W/mÂ²/K)
    """

    u_plancher_haut_deperditif: str
    """Coefficient de transmission thermique moyen des planchers hauts (W/mÂ²/K)"""

    usage_niveau_1_txt: str
    """indicateurs d'usage simplifié du bâtiment (verbose)"""

    valeur_fonciere_etat_initial_incertitude: str
    """incertitude de l'estimation de la valeur fonciere avant renovation"""

    vitrage_vir: str
    """
    le vitrage a été traité avec un traitement à isolation renforcé ce qui le rend
    plus performant d'un point de vue thermique.
    """

    volume_brut: str
    """Volume brut du bâtiment [m3]"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
