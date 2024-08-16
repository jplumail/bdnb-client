# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["BatimentGroupeCompletParcelleAPIExpert"]


class BatimentGroupeCompletParcelleAPIExpert(BaseModel):
    alea_argiles: Optional[str] = None

    alea_radon: Optional[str] = None

    altitude_sol_mean: Optional[int] = None

    annee_construction: Optional[int] = None

    arrete_2021: Optional[bool] = None
    """
    prÃ©cise si le DPE est un DPE qui est issu de la nouvelle rÃ©forme du DPE
    (arrÃªtÃ© du 31 mars 2021) ou s'il s'agit d'un DPE issu de la modification
    antÃ©rieure de 2012.
    """

    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    chauffage_solaire: Optional[bool] = None

    classe_bilan_dpe: Optional[str] = None
    """
    Classe du DPE issu de la synthÃ¨se du double seuil sur les consommations
    Ã©nergie primaire et les Ã©missions de CO2 sur les 5 usages
    (ecs/chauffage/climatisation/eclairage/auxiliaires). valable uniquement pour les
    DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en vigueur
    actuellement)
    """

    classe_conso_energie_arrete_2012: Optional[str] = None
    """classe d'Ã©mission GES du DPE 3 usages (Chauffage, ECS, Climatisation).

    Valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    classe_inertie: Optional[str] = None

    cle_interop_adr_principale_ban: Optional[str] = None
    """ClÃ© d'interopÃ©rabilitÃ© de l'adresse principale (issue de la BAN)"""

    code_commune_insee: Optional[str] = None
    """Code INSEE de la commune"""

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    code_epci_insee: Optional[str] = None

    code_iris: Optional[str] = None
    """Code iris INSEE"""

    code_qp: Optional[str] = None
    """identifiant de la table qpv"""

    code_region_insee: Optional[str] = None
    """Code rÃ©gion INSEE"""

    conso_3_usages_ep_m2_arrete_2012: Optional[float] = None
    """
    consommation annuelle 3 usages Ã©nergie primaire rapportÃ©e au m2 (Chauffage,
    ECS , Climatisation). valable uniquement pour les DPE appliquant la mÃ©thode de
    l'arrÃªtÃ© du 8 fÃ©vrier 2012
    """

    conso_5_usages_ep_m2: Optional[float] = None
    """
    consommation annuelle 5 usages
    (ecs/chauffage/climatisation/eclairage/auxiliaires) en Ã©nergie primaire
    (dÃ©duit de la production pv autoconsommÃ©e) (kWhep/mÂ²/an). valable uniquement
    pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en vigueur
    actuellement)
    """

    conso_pro_dle_elec_2020: Optional[float] = None
    """Consommation professionnelle Ã©lectrique [kWh/an]"""

    conso_pro_dle_gaz_2020: Optional[float] = None
    """Consommation professionnelle gaz [kWh/an]"""

    conso_res_dle_elec_2020: Optional[float] = None
    """Consommation rÃ©sidentielle Ã©lectrique [kWh/an]"""

    conso_res_dle_gaz_2020: Optional[float] = None
    """Consommation rÃ©sidentielle gaz [kWh/an]"""

    contient_fictive_geom_groupe: Optional[bool] = None

    croisement_geospx_reussi: Optional[bool] = None

    date_reception_dpe: Optional[str] = None
    """date de rÃ©ception du DPE dans la base de donnÃ©es de l'ADEME"""

    difference_rel_valeur_fonciere_etat_initial_renove_categorie: Optional[str] = None
    """
    categorie de la difference relative de valeur fonciere avant et apres renovation
    (verbose)
    """

    distance_batiment_historique_plus_proche: Optional[int] = None

    ecs_solaire: Optional[bool] = None

    emission_ges_3_usages_ep_m2_arrete_2012: Optional[float] = None
    """
    emission GES totale 3 usages Ã©nergie primaire rapportÃ©e au m2 (Chauffage, ECS
    , Climatisation). valable uniquement pour les DPE appliquant la mÃ©thode de
    l'arrÃªtÃ© du 8 fÃ©vrier 2012 (kgCO2/m2/an).
    """

    emission_ges_5_usages_m2: Optional[float] = None
    """
    emission GES totale 5 usages rapportÃ©e au mÂ² (dÃ©duit de la production pv
    autoconsommÃ©e)
    (ecs/chauffage/climatisation/eclairage/auxiliaires)(kgCO2/m2/an). valable
    uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en
    vigueur actuellement)
    """

    epaisseur_lame: Optional[int] = None
    """
    epaisseur principale de la lame de gaz entre vitrages pour les baies vitrÃ©es du
    DPE.
    """

    etat_initial_consommation_energie_estim_inc: Optional[int] = None
    """
    Incertitude des estimations de consommation Ã©nergÃ©tique finale avant
    rÃ©novation [kWh/m2/an]
    """

    etat_initial_consommation_energie_estim_lower: Optional[int] = None
    """
    Estimation basse de la consommation Ã©nergÃ©tique finale avant rÃ©novation
    [kWh/m2/an]
    """

    etat_initial_consommation_energie_estim_mean: Optional[int] = None
    """
    Estimation moyenne de la consommation Ã©nergÃ©tique finale avant rÃ©novation
    [kWh/m2/an]
    """

    etat_initial_consommation_energie_estim_upper: Optional[int] = None
    """
    Estimation haute de la consommation Ã©nergÃ©tique finale avant rÃ©novation
    [kWh/m2/an]
    """

    etat_initial_consommation_energie_primaire_estim_lower: Optional[int] = None
    """
    Estimation basse de la consommation Ã©nergÃ©tique primaire avant rÃ©novation
    [kWh/m2/an]
    """

    etat_initial_consommation_energie_primaire_estim_mean: Optional[int] = None
    """
    Estimation moyenne de la consommation Ã©nergÃ©tique primaire avant rÃ©novation
    [kWh/m2/an]
    """

    etat_initial_consommation_energie_primaire_estim_upper: Optional[int] = None
    """
    Estimation haute de la consommation Ã©nergÃ©tique primaire avant rÃ©novation
    [kWh/m2/an]
    """

    etat_initial_consommation_ges_estim_inc: Optional[int] = None
    """
    Incertitude sur l'estimation de consommation de GES avant rÃ©novation
    [kgeqC02/m2/an]
    """

    etat_initial_ges_estim_lower: Optional[int] = None
    """Estimation basse de la consommation de GES avant rÃ©novation [kgeqC02/m2/an]"""

    etat_initial_ges_estim_mean: Optional[int] = None
    """Estimation moyenne de la consommation de GES avant rÃ©novation [kgeqC02/m2/an]"""

    etat_initial_ges_estim_upper: Optional[int] = None
    """Estimation haute de la consommation de GES avant rÃ©novation [kgeqC02/m2/an]"""

    etat_initial_risque_canicule: Optional[int] = None
    """Estimation du risque canicule avant rÃ©novation [1-5]"""

    etat_initial_risque_canicule_inc: Optional[int] = None
    """Incertitude de l'estimation du risque canicule avant rÃ©novation [1-5]"""

    etat_renove_consommation_energie_estim_inc: Optional[int] = None
    """
    Incertitude sur les estimations des consommations Ã©nergÃ©tiques finales aprÃ¨s
    un scÃ©nario de rÃ©novation globale "standard" (isolation des principaux
    composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de chauffage)
    [kWh/m2/an]
    """

    etat_renove_consommation_energie_estim_lower: Optional[int] = None
    """
    Estimation basse de la consommation Ã©nergÃ©tique finale aprÃ¨s un scÃ©nario de
    rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_energie_estim_mean: Optional[int] = None
    """
    Estimation moyenne de la consommation Ã©nergÃ©tique finale aprÃ¨s un scÃ©nario
    de rÃ©novation globale "standard" (isolation des principaux composants
    d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_energie_estim_upper: Optional[int] = None
    """
    Estimation haute de la consommation Ã©nergÃ©tique finale aprÃ¨s un scÃ©nario de
    rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_energie_primaire_estim_lower: Optional[int] = None
    """
    Estimation basse de la consommation d'Ã©nergie primaire aprÃ¨s un scÃ©nario de
    rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_energie_primaire_estim_mean: Optional[int] = None
    """
    Estimation moyenne de la consommation d'Ã©nergie primaire aprÃ¨s un scÃ©nario de
    rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_energie_primaire_estim_upper: Optional[int] = None
    """
    Estimation haute de la consommation d'Ã©nergie primaire aprÃ¨s un scÃ©nario de
    rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_ges_estim_inc: Optional[int] = None
    """
    Incertitude sur l'estimation de consommation de GES aprÃ¨s un scÃ©nario de
    rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kgeqC02/m2/an]
    """

    etat_renove_ges_estim_lower: Optional[int] = None
    """
    Estimation basse des Ã©missions de GES aprÃ¨s un scÃ©nario de rÃ©novation
    globale "standard" (isolation des principaux composants d'enveloppe et
    changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]
    """

    etat_renove_ges_estim_mean: Optional[int] = None
    """
    Estimation moyenne des Ã©missions de GES aprÃ¨s un scÃ©nario de rÃ©novation
    globale "standard" (isolation des principaux composants d'enveloppe et
    changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]
    """

    etat_renove_ges_estim_upper: Optional[int] = None
    """
    Estimation haute des Ã©missions de GES aprÃ¨s un scÃ©nario de rÃ©novation
    globale "standard" (isolation des principaux composants d'enveloppe et
    changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]
    """

    etat_renove_risque_canicule: Optional[int] = None
    """Estimation du risque canicule aprÃ¨s rÃ©novation [1-5]"""

    etat_renove_risque_canicule_inc: Optional[int] = None
    """Incertitude de l'estimation du risque canicule aprÃ¨s rÃ©novation [1-5]"""

    etiquette_dpe_initial_a: Optional[float] = None
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette A dans le
    bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent
    """

    etiquette_dpe_initial_b: Optional[float] = None
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette B dans le
    bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent
    """

    etiquette_dpe_initial_c: Optional[float] = None
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette C dans le
    bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent
    """

    etiquette_dpe_initial_d: Optional[float] = None
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette D dans le
    bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent
    """

    etiquette_dpe_initial_e: Optional[float] = None
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette E dans le
    bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent
    """

    etiquette_dpe_initial_f: Optional[float] = None
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette F dans le
    bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent
    """

    etiquette_dpe_initial_g: Optional[float] = None
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette G dans le
    bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent
    """

    etiquette_dpe_initial_inc: Optional[float] = None
    """
    Classe d'incertitude de classe sur l'Ã©tiquette dpe avec la plus grande
    probabilitÃ© avant rÃ©novation [1 Ã 5]. Cet indicateur se lit de 1 = peu fiable
    Ã 5 = fiable.
    """

    etiquette_dpe_initial_map: Optional[str] = None
    """Etiquette ayant la plus grande probabilitÃ© pour l'Ã©tat actuel du bÃ¢timent"""

    etiquette_dpe_initial_map_2nd: Optional[str] = None
    """2 Ã©tiquettes ayant la plus grande probabilitÃ© pour l'Ã©tat actuel du
    bÃ¢timent.

    Si le champs vaut F-G alors F la premiÃ¨re Ã©tiquette est l'Ã©tiquette la plus
    probable , G la seconde Ã©tiquette la plus probable.
    """

    etiquette_dpe_initial_map_2nd_prob: Optional[float] = None
    """
    ProbabilitÃ© que le bÃ¢timent ait une Ã©tiquette DPE parmi les 2 Ã©tiquettes
    ayant la plus grande probabilitÃ© pour l'Ã©tat actuel du bÃ¢timent. Si
    etiquette_dpe_initial_map_2nd = F-G et que etiquette_dpe_initial_map_2nd_prob =
    0.95 alors il y a 95% de chance que l'Ã©tiquette DPE de ce bÃ¢timent soit
    classÃ© F ou G.
    """

    etiquette_dpe_renove_a: Optional[float] = None
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette A dans le
    bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
    chauffage)
    """

    etiquette_dpe_renove_b: Optional[float] = None
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette B dans le
    bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
    chauffage)
    """

    etiquette_dpe_renove_c: Optional[float] = None
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette C dans le
    bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
    chauffage)
    """

    etiquette_dpe_renove_d: Optional[float] = None
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette D dans le
    bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
    chauffage)
    """

    etiquette_dpe_renove_e: Optional[float] = None
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette E dans le
    bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
    chauffage)
    """

    etiquette_dpe_renove_f: Optional[float] = None
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette F dans le
    bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
    chauffage)
    """

    etiquette_dpe_renove_g: Optional[float] = None
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette G dans le
    bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
    chauffage)
    """

    etiquette_dpe_renove_inc: Optional[float] = None
    """
    Incertitude de classe sur l'Ã©tiquette dpe avec la plus grande probabilitÃ©
    aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des principaux
    composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de chauffage)
    [1-5]
    """

    etiquette_dpe_renove_map: Optional[str] = None
    """
    Etiquette ayant la plus grande probabilitÃ© aprÃ¨s un scÃ©nario de rÃ©novation
    globale "standard" (isolation des principaux composants d'enveloppe et
    changement de systÃ¨me Ã©nergÃ©tique de chauffage)
    """

    etiquette_dpe_renove_map_2nd: Optional[str] = None
    """
    2 Ã©tiquettes ayant la plus grande probabilitÃ© aprÃ¨s un scÃ©nario de
    rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de systÃ¨me Ã©nergÃ©tique de chauffage)
    """

    etiquette_dpe_renove_map_2nd_prob: Optional[float] = None
    """
    ProbabilitÃ© que le bÃ¢timent ait une Ã©tiquette DPE parmi les 2 Ã©tiquettes
    ayant la plus grande probabilitÃ© aprÃ¨s un scÃ©nario de rÃ©novation globale
    "standard" (isolation des principaux composants d'enveloppe et changement de
    systÃ¨me Ã©nergÃ©tique de chauffage)
    """

    etiquette_dpe_synthese_particulier_simple: Optional[str] = None
    """Etiquette DPE selon l'arrÃªtÃ© 2021.

    Si un DPE existe, l'Ã©tiquette provient d'un DPE de l'AEDME, sinon, il s'agit
    d'une simulation.
    """

    etiquette_dpe_synthese_particulier_source: Optional[str] = None
    """TODO"""

    facteur_solaire_baie_vitree: Optional[float] = None
    """facteur de transmission du flux solaire par la baie vitrÃ©e.

    coefficient entre 0 et 1
    """

    fiabilite_cr_adr_niv_1: Optional[str] = None

    fiabilite_cr_adr_niv_2: Optional[str] = None

    fiabilite_emprise_sol: Optional[str] = None

    fiabilite_hauteur: Optional[str] = None

    geom_groupe: Optional[str] = None

    gisement_gain_conso_finale_total: Optional[int] = None
    """Estimation du gisement de gain de consommation finale total"""

    gisement_gain_energetique_mean: Optional[int] = None
    """Estimation du gain Ã©nergÃ©tique moyen"""

    gisement_gain_ges_mean: Optional[int] = None
    """
    Estimation moyenne du gisement de gain sur les Ã©missions de gaz Ã effets de
    serre
    """

    hauteur_mean: Optional[int] = None

    identifiant_dpe: Optional[str] = None
    """identifiant de la table des DPE ademe"""

    l_cle_interop_adr: Optional[List[str]] = None
    """Liste de clÃ©s d'interopÃ©rabilitÃ© de l'adresse postale"""

    l_denomination_proprietaire: Optional[List[str]] = None
    """Liste de dÃ©nominations de propriÃ©taires"""

    l_libelle_adr: Optional[List[str]] = None
    """Liste de libellÃ© complet de l'adresse"""

    l_orientation_baie_vitree: Optional[List[str]] = None
    """liste des orientations des baies vitrÃ©es (enum version BDNB)"""

    l_parcelle_id: Optional[List[str]] = None
    """
    Liste d'identifiants de parcelle (ConcatÃ©nation de ccodep, ccocom, ccopre,
    ccosec, dnupla)
    """

    l_siren: Optional[List[str]] = None
    """Liste d'identifiants siren"""

    l_type_generateur_chauffage: Optional[List[str]] = None

    l_type_generateur_ecs: Optional[List[str]] = None

    libelle_adr_principale_ban: Optional[str] = None
    """LibellÃ© complet de l'adresse principale (issue de la BAN)"""

    libelle_commune_insee: Optional[str] = None
    """(insee) LibellÃ© de la commune accueillant le groupe de bÃ¢timent"""

    mat_mur_txt: Optional[str] = None

    mat_toit_txt: Optional[str] = None

    materiaux_structure_mur_exterieur: Optional[str] = None
    """
    matÃ©riaux ou principe constructif principal utilisÃ© pour les murs extÃ©rieurs
    (enum version BDNB)
    """

    materiaux_structure_mur_exterieur_simplifie: Optional[str] = None
    """materiaux principal utiliÃ© pour les murs extÃ©rieur simplifiÃ©.

    Cette information peut Ãªtre rÃ©cupÃ©rÃ©e de diffÃ©rentes sources (Fichiers
    Fonciers ou DPE pour le moment)
    """

    materiaux_toiture_simplifie: Optional[str] = None

    nb_adresse_valid_ban: Optional[int] = None
    """
    Nombre d'adresses valides diffÃ©rentes provenant de la BAN qui desservent le
    groupe de bÃ¢timent
    """

    nb_classe_bilan_dpe_a: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe A
    """

    nb_classe_bilan_dpe_b: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe B
    """

    nb_classe_bilan_dpe_c: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe C
    """

    nb_classe_bilan_dpe_d: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe D
    """

    nb_classe_bilan_dpe_e: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe E
    """

    nb_classe_bilan_dpe_f: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe F
    """

    nb_classe_bilan_dpe_g: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe G
    """

    nb_classe_conso_energie_arrete_2012_a: Optional[int] = None
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique A.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_b: Optional[int] = None
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique B.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_c: Optional[int] = None
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique C.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_d: Optional[int] = None
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique D.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_e: Optional[int] = None
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique E.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_f: Optional[int] = None
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique F.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_g: Optional[int] = None
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique G.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_nc: Optional[int] = None
    """
    (dpe) Nombre de DPE n'ayant pas fait l'objet d'un calcul d'Ã©tiquette Ã©nergie
    (DPE dits vierges). valable uniquement pour les DPE appliquant la mÃ©thode de
    l'arrÃªtÃ© du 8 fÃ©vrier 2012
    """

    nb_log: Optional[int] = None
    """(rnc) Nombre de logements"""

    nb_log_rnc: Optional[float] = None

    nb_lot_garpark_rnc: Optional[float] = None

    nb_lot_tertiaire_rnc: Optional[float] = None

    nb_niveau: Optional[int] = None
    """(ffo) Nombre de niveau du bÃ¢timent (ex: RDC = 1, R+1 = 2, etc..)"""

    nb_pdl_pro_dle_elec_2020: Optional[float] = None
    """Nombre de points de livraison Ã©lectrique professionnels [kWh/an]"""

    nb_pdl_pro_dle_gaz_2020: Optional[float] = None
    """Nombre de points de livraison gaz professionnels [kWh/an]"""

    nb_pdl_res_dle_elec_2020: Optional[float] = None
    """Nombre de points de livraison Ã©lectrique rÃ©sidentiels [kWh/an]"""

    nb_pdl_res_dle_gaz_2020: Optional[float] = None
    """Nombre de points de livraison gaz rÃ©sidentiels [kWh/an]"""

    nom_batiment_historique_plus_proche: Optional[str] = None

    nom_qp: Optional[str] = None
    """Nom du quartier prioritaire dans lequel se trouve le bÃ¢timent"""

    nom_quartier_qpv: Optional[str] = None

    numero_immat_principal: Optional[str] = None

    parcelle_id: Optional[str] = None
    """
    (ffo:idpar) Identifiant de parcelle (ConcatÃ©nation de ccodep, ccocom, ccopre,
    ccosec, dnupla)
    """

    pourcentage_surface_baie_vitree_exterieur: Optional[float] = None
    """pourcentage de surface de baies vitrÃ©es sur les murs extÃ©rieurs"""

    presence_balcon: Optional[bool] = None
    """
    prÃ©sence de balcons identifiÃ©s par analyse des coefficients de masques
    solaires du DPE.
    """

    quartier_prioritaire: Optional[bool] = None
    """Est situÃ© dans un quartier prioritaire"""

    s_geom_groupe: Optional[int] = None
    """Surface au sol de la gÃ©omÃ©trie du bÃ¢timent groupe (geom_groupe)"""

    surface_emprise_sol: Optional[int] = None
    """Surface au sol de la gÃ©omÃ©trie du bÃ¢timent groupe (geom_groupe)"""

    surface_facade_ext: Optional[int] = None
    """Estimation de la surface de faÃ§ade donnant sur l'exterieur [mÂ²]"""

    surface_facade_mitoyenne: Optional[int] = None
    """Estimation de la surface de faÃ§ade donnant sur un autre bÃ¢timent [mÂ²]"""

    surface_facade_totale: Optional[int] = None
    """Estimation de la surface totale de faÃ§ade (murs + baies) [mÂ²]"""

    surface_facade_vitree: Optional[int] = None
    """Estimation de la surface de faÃ§ade vitrÃ©e [mÂ²]"""

    traversant: Optional[str] = None
    """indicateur du cÃ´tÃ© traversant du logement."""

    type_dpe: Optional[str] = None
    """type de DPE.

    Permet de prÃ©ciser le type de DPE (arrÃªtÃ© 2012/arrÃªtÃ© 2021), son objet
    (logement, immeuble de logement, tertiaire) et la mÃ©thode de calcul utilisÃ©
    (3CL conventionel,facture ou RT2012/RE2020)
    """

    type_energie_chauffage: Optional[str] = None

    type_energie_chauffage_appoint: Optional[str] = None

    type_fermeture: Optional[str] = None
    """
    type de fermeture principale installÃ©e sur les baies vitrÃ©es du DPE
    (volet,persienne etc..) (enum version BDNB)
    """

    type_gaz_lame: Optional[str] = None
    """
    type de gaz injectÃ© principalement dans la lame entre les vitrages des baies
    vitrÃ©es du DPE (double vitrage ou triple vitrage uniquement) (enum version
    BDNB)
    """

    type_generateur_chauffage: Optional[str] = None

    type_generateur_chauffage_anciennete: Optional[str] = None

    type_generateur_chauffage_anciennete_appoint: Optional[str] = None

    type_generateur_chauffage_appoint: Optional[str] = None

    type_generateur_climatisation: Optional[str] = None

    type_generateur_climatisation_anciennete: Optional[str] = None

    type_generateur_ecs: Optional[str] = None

    type_generateur_ecs_anciennete: Optional[str] = None

    type_installation_chauffage: Optional[str] = None

    type_installation_ecs: Optional[str] = None

    type_isolation_mur_exterieur: Optional[str] = None
    """
    type d'isolation principal des murs donnant sur l'extÃ©rieur pour le DPE (enum
    version BDNB)
    """

    type_isolation_plancher_bas: Optional[str] = None
    """
    type d'isolation principal des planchers bas dÃ©perditifs pour le DPE (enum
    version BDNB)
    """

    type_isolation_plancher_haut: Optional[str] = None
    """
    type d'isolation principal des planchers hauts dÃ©perditifs pour le DPE (enum
    version BDNB)
    """

    type_materiaux_menuiserie: Optional[str] = None
    """
    type de matÃ©riaux principal des menuiseries des baies vitrÃ©es du DPE (enum
    version BDNB)
    """

    type_plancher_bas_deperditif: Optional[str] = None
    """
    materiaux ou principe constructif principal des planchers bas (enum version
    BDNB)
    """

    type_plancher_haut_deperditif: Optional[str] = None

    type_production_energie_renouvelable: Optional[str] = None

    type_ventilation: Optional[str] = None

    type_vitrage: Optional[str] = None
    """type de vitrage principal des baies vitrÃ©es du DPE (enum version BDNB)"""

    u_baie_vitree: Optional[float] = None
    """
    Coefficient de transmission thermique moyen des baies vitrÃ©es en incluant le
    calcul de la rÃ©sistance additionelle des fermetures (calcul Ujn) (W/mÂ²/K)
    """

    u_mur_exterieur: Optional[float] = None
    """Coefficient de transmission thermique moyen des murs extÃ©rieurs (W/mÂ²/K)"""

    u_plancher_bas_final_deperditif: Optional[float] = None
    """
    Coefficient de transmission thermique moyen des planchers bas en prenant en
    compte l'attÃ©nuation forfaitaire du U lorsqu'en contact avec le sol de la
    mÃ©thode 3CL(W/mÂ²/K)
    """

    u_plancher_haut_deperditif: Optional[float] = None

    usage_niveau_1_txt: Optional[str] = None

    valeur_fonciere_etat_initial_incertitude: Optional[str] = None
    """incertitude de l'estimation de la valeur fonciere avant renovation"""

    vitrage_vir: Optional[bool] = None
    """
    le vitrage a Ã©tÃ© traitÃ© avec un traitement Ã isolation renforcÃ© ce qui le
    rend plus performant d'un point de vue thermique.
    """

    volume_brut: Optional[int] = None
    """Volume brut du bÃ¢timent [m3]"""
