# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["BatimentGroupeComplet"]


class BatimentGroupeComplet(BaseModel):
    alea_argiles: Optional[str] = None
    """(argiles) Aléa du risque argiles"""

    alea_radon: Optional[str] = None
    """(radon) alea du risque radon"""

    altitude_sol_mean: Optional[int] = None
    """(ign) Altitude au sol moyenne [m]"""

    annee_construction: Optional[int] = None
    """Année de construction du bâtiment"""

    arrete_2021: Optional[bool] = None
    """
    précise si le DPE est un DPE qui est issu de la nouvelle réforme du DPE (arràªté
    du 31 mars 2021) ou s'il s'agit d'un DPE issu de la modification antérieure
    de 2012.
    """

    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    chauffage_solaire: Optional[bool] = None
    """présence de chauffage solaire"""

    classe_bilan_dpe: Optional[str] = None
    """
    Classe du DPE issu de la synthèse du double seuil sur les consommations énergie
    primaire et les émissions de CO2 sur les 5 usages
    (ecs/chauffage/climatisation/eclairage/auxiliaires). valable uniquement pour les
    DPE appliquant la méthode de l'arràªté du 31 mars 2021 (en vigueur actuellement)
    """

    classe_conso_energie_arrete_2012: Optional[str] = None
    """classe d'émission GES du DPE 3 usages (Chauffage, ECS, Climatisation).

    Valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    classe_inertie: Optional[str] = None
    """classe d'inertie du DPE (enum version BDNB)"""

    cle_interop_adr_principale_ban: Optional[str] = None
    """Clé d'interopérabilité de l'adresse principale (issue de la BAN)"""

    code_commune_insee: Optional[str] = None
    """Code INSEE de la commune"""

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    code_epci_insee: Optional[str] = None
    """Code de l'EPCI"""

    code_iris: Optional[str] = None
    """Code iris INSEE"""

    code_qp: Optional[str] = None
    """identifiant de la table qpv"""

    code_region_insee: Optional[str] = None
    """Code région INSEE"""

    conso_3_usages_ep_m2_arrete_2012: Optional[float] = None
    """
    consommation annuelle 3 usages énergie primaire rapportée au m2 (Chauffage, ECS
    , Climatisation). valable uniquement pour les DPE appliquant la méthode de
    l'arràªté du 8 février 2012
    """

    conso_5_usages_ep_m2: Optional[float] = None
    """
    consommation annuelle 5 usages
    (ecs/chauffage/climatisation/eclairage/auxiliaires) en énergie primaire (déduit
    de la production pv autoconsommée) (kWhep/mÂ²/an). valable uniquement pour les
    DPE appliquant la méthode de l'arràªté du 31 mars 2021 (en vigueur actuellement)
    """

    conso_pro_dle_elec_2020: Optional[float] = None
    """Consommation professionnelle électrique [kWh/an]"""

    conso_pro_dle_gaz_2020: Optional[float] = None
    """Consommation professionnelle gaz [kWh/an]"""

    conso_res_dle_elec_2020: Optional[float] = None
    """Consommation résidentielle électrique [kWh/an]"""

    conso_res_dle_gaz_2020: Optional[float] = None
    """Consommation résidentielle gaz [kWh/an]"""

    contient_fictive_geom_groupe: Optional[bool] = None
    """
    Vaut "vrai", si la géométrie du groupe de bâtiment est générée automatiquement
    et ne représente pas la géométrie du groupe de bâtiment.
    """

    croisement_geospx_reussi: Optional[bool] = None
    """
    le croisement géospatial entre la BDTOPO et les fichiers fonciers est considérée
    comme réussi
    """

    date_reception_dpe: Optional[str] = None
    """date de réception du DPE dans la base de données de l'ADEME"""

    difference_rel_valeur_fonciere_etat_initial_renove_categorie: Optional[str] = None
    """
    categorie de la difference relative de valeur fonciere avant et apres renovation
    (verbose)
    """

    distance_batiment_historique_plus_proche: Optional[int] = None
    """(mer) Distance au bâtiment historique le plus proche (si moins de 500m) [m]"""

    ecs_solaire: Optional[bool] = None
    """présence d'ecs solaire"""

    emission_ges_3_usages_ep_m2_arrete_2012: Optional[float] = None
    """
    emission GES totale 3 usages énergie primaire rapportée au m2 (Chauffage, ECS ,
    Climatisation). valable uniquement pour les DPE appliquant la méthode de
    l'arràªté du 8 février 2012 (kgCO2/m2/an).
    """

    emission_ges_5_usages_m2: Optional[float] = None
    """
    emission GES totale 5 usages rapportée au mÂ² (déduit de la production pv
    autoconsommée) (ecs/chauffage/climatisation/eclairage/auxiliaires)(kgCO2/m2/an).
    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 31 mars
    2021 (en vigueur actuellement)
    """

    epaisseur_lame: Optional[int] = None
    """
    epaisseur principale de la lame de gaz entre vitrages pour les baies vitrées du
    DPE.
    """

    etat_initial_consommation_energie_estim_inc: Optional[int] = None
    """
    Incertitude des estimations de consommation énergétique finale avant rénovation
    [kWh/m2/an]
    """

    etat_initial_consommation_energie_estim_lower: Optional[int] = None
    """
    Estimation basse de la consommation énergétique finale avant rénovation
    [kWh/m2/an]
    """

    etat_initial_consommation_energie_estim_mean: Optional[int] = None
    """
    Estimation moyenne de la consommation énergétique finale avant rénovation
    [kWh/m2/an]
    """

    etat_initial_consommation_energie_estim_upper: Optional[int] = None
    """
    Estimation haute de la consommation énergétique finale avant rénovation
    [kWh/m2/an]
    """

    etat_initial_consommation_energie_primaire_estim_lower: Optional[int] = None
    """
    Estimation basse de la consommation énergétique primaire avant rénovation
    [kWh/m2/an]
    """

    etat_initial_consommation_energie_primaire_estim_mean: Optional[int] = None
    """
    Estimation moyenne de la consommation énergétique primaire avant rénovation
    [kWh/m2/an]
    """

    etat_initial_consommation_energie_primaire_estim_upper: Optional[int] = None
    """
    Estimation haute de la consommation énergétique primaire avant rénovation
    [kWh/m2/an]
    """

    etat_initial_consommation_ges_estim_inc: Optional[int] = None
    """
    Incertitude sur l'estimation de consommation de GES avant rénovation
    [kgeqC02/m2/an]
    """

    etat_initial_ges_estim_lower: Optional[int] = None
    """Estimation basse de la consommation de GES avant rénovation [kgeqC02/m2/an]"""

    etat_initial_ges_estim_mean: Optional[int] = None
    """Estimation moyenne de la consommation de GES avant rénovation [kgeqC02/m2/an]"""

    etat_initial_ges_estim_upper: Optional[int] = None
    """Estimation haute de la consommation de GES avant rénovation [kgeqC02/m2/an]"""

    etat_initial_risque_canicule: Optional[int] = None
    """Estimation du risque canicule avant rénovation [1-5]"""

    etat_initial_risque_canicule_inc: Optional[int] = None
    """Incertitude de l'estimation du risque canicule avant rénovation [1-5]"""

    etat_renove_consommation_energie_estim_inc: Optional[int] = None
    """
    Incertitude sur les estimations des consommations énergétiques finales après un
    scénario de rénovation globale "standard" (isolation des principaux composants
    d'enveloppe et changement de système énergétique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_energie_estim_lower: Optional[int] = None
    """
    Estimation basse de la consommation énergétique finale après un scénario de
    rénovation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de système énergétique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_energie_estim_mean: Optional[int] = None
    """
    Estimation moyenne de la consommation énergétique finale après un scénario de
    rénovation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de système énergétique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_energie_estim_upper: Optional[int] = None
    """
    Estimation haute de la consommation énergétique finale après un scénario de
    rénovation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de système énergétique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_energie_primaire_estim_lower: Optional[int] = None
    """
    Estimation basse de la consommation d'énergie primaire après un scénario de
    rénovation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de système énergétique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_energie_primaire_estim_mean: Optional[int] = None
    """
    Estimation moyenne de la consommation d'énergie primaire après un scénario de
    rénovation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de système énergétique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_energie_primaire_estim_upper: Optional[int] = None
    """
    Estimation haute de la consommation d'énergie primaire après un scénario de
    rénovation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de système énergétique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_ges_estim_inc: Optional[int] = None
    """
    Incertitude sur l'estimation de consommation de GES après un scénario de
    rénovation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de système énergétique de chauffage) [kgeqC02/m2/an]
    """

    etat_renove_ges_estim_lower: Optional[int] = None
    """
    Estimation basse des émissions de GES après un scénario de rénovation globale
    "standard" (isolation des principaux composants d'enveloppe et changement de
    système énergétique de chauffage) [kWh/m2/an]
    """

    etat_renove_ges_estim_mean: Optional[int] = None
    """
    Estimation moyenne des émissions de GES après un scénario de rénovation globale
    "standard" (isolation des principaux composants d'enveloppe et changement de
    système énergétique de chauffage) [kWh/m2/an]
    """

    etat_renove_ges_estim_upper: Optional[int] = None
    """
    Estimation haute des émissions de GES après un scénario de rénovation globale
    "standard" (isolation des principaux composants d'enveloppe et changement de
    système énergétique de chauffage) [kWh/m2/an]
    """

    etat_renove_risque_canicule: Optional[int] = None
    """Estimation du risque canicule après rénovation [1-5]"""

    etat_renove_risque_canicule_inc: Optional[int] = None
    """Incertitude de l'estimation du risque canicule après rénovation [1-5]"""

    etiquette_dpe_initial_a: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette A dans le
    bâtiment pour l'état actuel du bâtiment
    """

    etiquette_dpe_initial_b: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette B dans le
    bâtiment pour l'état actuel du bâtiment
    """

    etiquette_dpe_initial_c: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette C dans le
    bâtiment pour l'état actuel du bâtiment
    """

    etiquette_dpe_initial_d: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette D dans le
    bâtiment pour l'état actuel du bâtiment
    """

    etiquette_dpe_initial_e: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette E dans le
    bâtiment pour l'état actuel du bâtiment
    """

    etiquette_dpe_initial_f: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette F dans le
    bâtiment pour l'état actuel du bâtiment
    """

    etiquette_dpe_initial_g: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette G dans le
    bâtiment pour l'état actuel du bâtiment
    """

    etiquette_dpe_initial_inc: Optional[float] = None
    """
    Classe d'incertitude de classe sur l'étiquette dpe avec la plus grande
    probabilité avant rénovation [1 à 5]. Cet indicateur se lit de 1 = peu fiable à
    5 = fiable.
    """

    etiquette_dpe_initial_map: Optional[str] = None
    """Etiquette ayant la plus grande probabilité pour l'état actuel du bâtiment"""

    etiquette_dpe_initial_map_2nd: Optional[str] = None
    """2 étiquettes ayant la plus grande probabilité pour l'état actuel du bâtiment.

    Si le champs vaut F-G alors F la première étiquette est l'étiquette la plus
    probable , G la seconde étiquette la plus probable.
    """

    etiquette_dpe_initial_map_2nd_prob: Optional[float] = None
    """
    Probabilité que le bâtiment ait une étiquette DPE parmi les 2 étiquettes ayant
    la plus grande probabilité pour l'état actuel du bâtiment. Si
    etiquette_dpe_initial_map_2nd = F-G et que etiquette_dpe_initial_map_2nd_prob =
    0.95 alors il y a 95% de chance que l'étiquette DPE de ce bâtiment soit classé F
    ou G.
    """

    etiquette_dpe_renove_a: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette A dans le
    bâtiment après un scénario de rénovation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de système énergétique de
    chauffage)
    """

    etiquette_dpe_renove_b: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette B dans le
    bâtiment après un scénario de rénovation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de système énergétique de
    chauffage)
    """

    etiquette_dpe_renove_c: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette C dans le
    bâtiment après un scénario de rénovation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de système énergétique de
    chauffage)
    """

    etiquette_dpe_renove_d: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette D dans le
    bâtiment après un scénario de rénovation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de système énergétique de
    chauffage)
    """

    etiquette_dpe_renove_e: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette E dans le
    bâtiment après un scénario de rénovation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de système énergétique de
    chauffage)
    """

    etiquette_dpe_renove_f: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette F dans le
    bâtiment après un scénario de rénovation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de système énergétique de
    chauffage)
    """

    etiquette_dpe_renove_g: Optional[float] = None
    """
    Estimation de la probabilité d'avoir des logements d'étiquette G dans le
    bâtiment après un scénario de rénovation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de système énergétique de
    chauffage)
    """

    etiquette_dpe_renove_inc: Optional[float] = None
    """
    Incertitude de classe sur l'étiquette dpe avec la plus grande probabilité après
    un scénario de rénovation globale "standard" (isolation des principaux
    composants d'enveloppe et changement de système énergétique de chauffage) [1-5]
    """

    etiquette_dpe_renove_map: Optional[str] = None
    """
    Etiquette ayant la plus grande probabilité après un scénario de rénovation
    globale "standard" (isolation des principaux composants d'enveloppe et
    changement de système énergétique de chauffage)
    """

    etiquette_dpe_renove_map_2nd: Optional[str] = None
    """
    2 étiquettes ayant la plus grande probabilité après un scénario de rénovation
    globale "standard" (isolation des principaux composants d'enveloppe et
    changement de système énergétique de chauffage)
    """

    etiquette_dpe_renove_map_2nd_prob: Optional[float] = None
    """
    Probabilité que le bâtiment ait une étiquette DPE parmi les 2 étiquettes ayant
    la plus grande probabilité après un scénario de rénovation globale "standard"
    (isolation des principaux composants d'enveloppe et changement de système
    énergétique de chauffage)
    """

    etiquette_dpe_synthese_particulier_simple: Optional[str] = None
    """Etiquette DPE selon l'arràªté 2021.

    Si un DPE existe, l'étiquette provient d'un DPE de l'AEDME, sinon, il s'agit
    d'une simulation.
    """

    etiquette_dpe_synthese_particulier_source: Optional[str] = None
    """TODO"""

    facteur_solaire_baie_vitree: Optional[float] = None
    """facteur de transmission du flux solaire par la baie vitrée.

    coefficient entre 0 et 1
    """

    fiabilite_cr_adr_niv_1: Optional[str] = None
    """
    Fiabilité des données croisées à l'adresse ('données croisées à l'adresse
    fiables', 'données croisées à l'adresse fiables à l'echelle de la parcelle
    unifiee', 'données croisées à l'adresse moyennement fiables', 'problème de
    géocodage')
    """

    fiabilite_cr_adr_niv_2: Optional[str] = None
    """Fiabilité détaillée des données croisées à l'adresse"""

    fiabilite_emprise_sol: Optional[str] = None
    """Fiabilité de l'emprise au sol du bâtiment"""

    fiabilite_hauteur: Optional[str] = None
    """Fiabilité de la hauteur du bâtiment"""

    geom_groupe: Optional[str] = None
    """Géométrie multipolygonale du groupe de bâtiment (Lambert-93)"""

    gisement_gain_conso_finale_total: Optional[int] = None
    """(cstb) Estimation du gisement de gain de consommation finale total (kWh/m2/an)"""

    gisement_gain_energetique_mean: Optional[int] = None
    """Estimation du gain énergétique moyen"""

    gisement_gain_ges_mean: Optional[int] = None
    """
    Estimation moyenne du gisement de gain sur les émissions de gaz à effets de
    serre
    """

    hauteur_mean: Optional[int] = None
    """(ign) Hauteur moyenne des bâtiments [m]"""

    identifiant_dpe: Optional[str] = None
    """identifiant de la table des DPE ademe"""

    l_cle_interop_adr: Optional[List[str]] = None
    """Liste de clés d'interopérabilité de l'adresse postale"""

    l_denomination_proprietaire: Optional[List[str]] = None
    """Liste de dénominations de propriétaires"""

    l_libelle_adr: Optional[List[str]] = None
    """Liste de libellé complet de l'adresse"""

    l_orientation_baie_vitree: Optional[List[str]] = None
    """liste des orientations des baies vitrées (enum version BDNB)"""

    l_parcelle_id: Optional[List[str]] = None
    """
    Liste d'identifiants de parcelle (Concaténation de ccodep, ccocom, ccopre,
    ccosec, dnupla)
    """

    l_siren: Optional[List[str]] = None
    """Liste d'identifiants siren"""

    l_type_generateur_chauffage: Optional[List[str]] = None
    """
    type de générateur de chauffage principal (enum version simplifiée BDNB)
    concaténé en liste pour tous les DPE
    """

    l_type_generateur_ecs: Optional[List[str]] = None
    """
    type de générateur d'ECS principal (enum version simplifiée BDNB) concaténé en
    liste pour tous les DPE
    """

    libelle_adr_principale_ban: Optional[str] = None
    """Libellé complet de l'adresse principale (issue de la BAN)"""

    libelle_commune_insee: Optional[str] = None
    """(insee) Libellé de la commune accueillant le groupe de bâtiment"""

    mat_mur_txt: Optional[str] = None
    """(ffo) Matériaux principal des murs extérieurs"""

    mat_toit_txt: Optional[str] = None
    """(ffo) Matériau principal des toitures"""

    materiaux_structure_mur_exterieur: Optional[str] = None
    """
    matériaux ou principe constructif principal utilisé pour les murs extérieurs
    (enum version BDNB)
    """

    materiaux_structure_mur_exterieur_simplifie: Optional[str] = None
    """materiaux principal utilié pour les murs extérieur simplifié.

    Cette information peut àªtre récupérée de différentes sources (Fichiers Fonciers
    ou DPE pour le moment)
    """

    materiaux_toiture_simplifie: Optional[str] = None
    """materiaux principal utilié pour la toiture simplifié.

    Cette information peut àªtre récupérée de différentes sources (Fichiers Fonciers
    ou DPE pour le moment)
    """

    nb_adresse_valid_ban: Optional[int] = None
    """
    Nombre d'adresses valides différentes provenant de la BAN qui desservent le
    groupe de bâtiment
    """

    nb_classe_bilan_dpe_a: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe A
    """

    nb_classe_bilan_dpe_b: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe B
    """

    nb_classe_bilan_dpe_c: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe C
    """

    nb_classe_bilan_dpe_d: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe D
    """

    nb_classe_bilan_dpe_e: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe E
    """

    nb_classe_bilan_dpe_f: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe F
    """

    nb_classe_bilan_dpe_g: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe G
    """

    nb_classe_conso_energie_arrete_2012_a: Optional[int] = None
    """(dpe) Nombre de DPE de la classe énergétique A.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_b: Optional[int] = None
    """(dpe) Nombre de DPE de la classe énergétique B.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_c: Optional[int] = None
    """(dpe) Nombre de DPE de la classe énergétique C.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_d: Optional[int] = None
    """(dpe) Nombre de DPE de la classe énergétique D.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_e: Optional[int] = None
    """(dpe) Nombre de DPE de la classe énergétique E.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_f: Optional[int] = None
    """(dpe) Nombre de DPE de la classe énergétique F.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_g: Optional[int] = None
    """(dpe) Nombre de DPE de la classe énergétique G.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_nc: Optional[int] = None
    """
    (dpe) Nombre de DPE n'ayant pas fait l'objet d'un calcul d'étiquette énergie
    (DPE dits vierges). valable uniquement pour les DPE appliquant la méthode de
    l'arràªté du 8 février 2012
    """

    nb_log: Optional[int] = None
    """(rnc) Nombre de logements"""

    nb_log_rnc: Optional[float] = None
    """(rnc) Nombre de logements"""

    nb_lot_garpark_rnc: Optional[float] = None
    """Nombre de lots de stationnement"""

    nb_lot_tertiaire_rnc: Optional[float] = None
    """Nombre de lots de type bureau et commerce"""

    nb_niveau: Optional[int] = None
    """(ffo) Nombre de niveau du bâtiment (ex: RDC = 1, R+1 = 2, etc..)"""

    nb_pdl_pro_dle_elec_2020: Optional[float] = None
    """Nombre de points de livraison électrique professionnels [kWh/an]"""

    nb_pdl_pro_dle_gaz_2020: Optional[float] = None
    """Nombre de points de livraison gaz professionnels [kWh/an]"""

    nb_pdl_res_dle_elec_2020: Optional[float] = None
    """Nombre de points de livraison électrique résidentiels [kWh/an]"""

    nb_pdl_res_dle_gaz_2020: Optional[float] = None
    """Nombre de points de livraison gaz résidentiels [kWh/an]"""

    nom_batiment_historique_plus_proche: Optional[str] = None
    """(mer:tico) nom du bâtiment historique le plus proche"""

    nom_qp: Optional[str] = None
    """Nom du quartier prioritaire dans lequel se trouve le bâtiment"""

    nom_quartier_qpv: Optional[str] = None
    """Nom du quartier prioritaire dans lequel se trouve le bâtiment"""

    numero_immat_principal: Optional[str] = None
    """numéro d'immatriculation principal associé au bâtiment groupe.

    (numéro d'immatriculation copropriété qui comporte le plus de lots)
    """

    pourcentage_surface_baie_vitree_exterieur: Optional[float] = None
    """pourcentage de surface de baies vitrées sur les murs extérieurs"""

    presence_balcon: Optional[bool] = None
    """
    présence de balcons identifiés par analyse des coefficients de masques solaires
    du DPE.
    """

    quartier_prioritaire: Optional[bool] = None
    """Est situé dans un quartier prioritaire"""

    s_geom_groupe: Optional[int] = None
    """Surface au sol de la géométrie du bâtiment groupe (geom_groupe)"""

    surface_emprise_sol: Optional[int] = None
    """Surface au sol de la géométrie du bâtiment groupe (geom_groupe)"""

    surface_facade_ext: Optional[int] = None
    """Estimation de la surface de faà§ade donnant sur l'exterieur [mÂ²]"""

    surface_facade_mitoyenne: Optional[int] = None
    """Estimation de la surface de faà§ade donnant sur un autre bâtiment [mÂ²]"""

    surface_facade_totale: Optional[int] = None
    """Estimation de la surface totale de faà§ade (murs + baies) [mÂ²]"""

    surface_facade_vitree: Optional[int] = None
    """Estimation de la surface de faà§ade vitrée [mÂ²]"""

    traversant: Optional[str] = None
    """indicateur du cà´té traversant du logement."""

    type_dpe: Optional[str] = None
    """type de DPE.

    Permet de préciser le type de DPE (arràªté 2012/arràªté 2021), son objet
    (logement, immeuble de logement, tertiaire) et la méthode de calcul utilisé (3CL
    conventionel,facture ou RT2012/RE2020)
    """

    type_energie_chauffage: Optional[str] = None
    """
    type d'énergie pour le générateur de chauffage principal (enum version
    simplifiée BDNB)
    """

    type_energie_chauffage_appoint: Optional[str] = None
    """
    type d'énergie pour le générateur de chauffage d'appoint (enum version
    simplifiée BDNB)
    """

    type_fermeture: Optional[str] = None
    """
    type de fermeture principale installée sur les baies vitrées du DPE
    (volet,persienne etc..) (enum version BDNB)
    """

    type_gaz_lame: Optional[str] = None
    """
    type de gaz injecté principalement dans la lame entre les vitrages des baies
    vitrées du DPE (double vitrage ou triple vitrage uniquement) (enum version BDNB)
    """

    type_generateur_chauffage: Optional[str] = None
    """type de générateur de chauffage principal (enum version simplifiée BDNB)"""

    type_generateur_chauffage_anciennete: Optional[str] = None
    """ancienneté du générateur de chauffage principal"""

    type_generateur_chauffage_anciennete_appoint: Optional[str] = None
    """ancienneté du générateur de chauffage d'appoint"""

    type_generateur_chauffage_appoint: Optional[str] = None
    """type de générateur de chauffage d'appoint (enum version simplifiée BDNB)"""

    type_generateur_climatisation: Optional[str] = None
    """type de générateur de climatisation principal (enum version simplifiée BDNB)"""

    type_generateur_climatisation_anciennete: Optional[str] = None
    """ancienneté du générateur de climatisation principal"""

    type_generateur_ecs: Optional[str] = None
    """
    type de générateur d'eau chaude sanitaire (ECS) principal (enum version
    simplifiée BDNB)
    """

    type_generateur_ecs_anciennete: Optional[str] = None
    """ancienneté du générateur d'eau chaude sanitaire (ECS) principal"""

    type_installation_chauffage: Optional[str] = None
    """
    type d'installation de chauffage (collectif ou individuel) (enum version
    simplifiée BDNB)
    """

    type_installation_ecs: Optional[str] = None
    """
    type d'installation d'eau chaude sanitaire (ECS) (collectif ou individuel) (enum
    version simplifiée BDNB)
    """

    type_isolation_mur_exterieur: Optional[str] = None
    """
    type d'isolation principal des murs donnant sur l'extérieur pour le DPE (enum
    version BDNB)
    """

    type_isolation_plancher_bas: Optional[str] = None
    """
    type d'isolation principal des planchers bas déperditifs pour le DPE (enum
    version BDNB)
    """

    type_isolation_plancher_haut: Optional[str] = None
    """
    type d'isolation principal des planchers hauts déperditifs pour le DPE (enum
    version BDNB)
    """

    type_materiaux_menuiserie: Optional[str] = None
    """
    type de matériaux principal des menuiseries des baies vitrées du DPE (enum
    version BDNB)
    """

    type_plancher_bas_deperditif: Optional[str] = None
    """
    materiaux ou principe constructif principal des planchers bas (enum version
    BDNB)
    """

    type_plancher_haut_deperditif: Optional[str] = None
    """
    materiaux ou principe constructif principal des planchers hauts (enum version
    BDNB)
    """

    type_production_energie_renouvelable: Optional[str] = None
    """type de production ENR pour le DPE (enum version DPE 2021)"""

    type_ventilation: Optional[str] = None
    """type de ventilation (enum version BDNB)"""

    type_vitrage: Optional[str] = None
    """type de vitrage principal des baies vitrées du DPE (enum version BDNB)"""

    u_baie_vitree: Optional[float] = None
    """
    Coefficient de transmission thermique moyen des baies vitrées en incluant le
    calcul de la résistance additionelle des fermetures (calcul Ujn) (W/mÂ²/K)
    """

    u_mur_exterieur: Optional[float] = None
    """Coefficient de transmission thermique moyen des murs extérieurs (W/mÂ²/K)"""

    u_plancher_bas_final_deperditif: Optional[float] = None
    """
    Coefficient de transmission thermique moyen des planchers bas en prenant en
    compte l'atténuation forfaitaire du U lorsqu'en contact avec le sol de la
    méthode 3CL(W/mÂ²/K)
    """

    u_plancher_haut_deperditif: Optional[float] = None
    """Coefficient de transmission thermique moyen des planchers hauts (W/mÂ²/K)"""

    usage_niveau_1_txt: Optional[str] = None
    """indicateurs d'usage simplifié du bâtiment (verbose)"""

    valeur_fonciere_etat_initial_incertitude: Optional[str] = None
    """incertitude de l'estimation de la valeur fonciere avant renovation"""

    vitrage_vir: Optional[bool] = None
    """
    le vitrage a été traité avec un traitement à isolation renforcé ce qui le rend
    plus performant d'un point de vue thermique.
    """

    volume_brut: Optional[int] = None
    """Volume brut du bâtiment [m3]"""
