# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BatimentsGroupesCompletListParams"]


class BatimentsGroupesCompletListParams(TypedDict, total=False):
    alea_argiles: str
    """(argiles) AlÃ©a du risque argiles"""

    alea_radon: str
    """(radon) alea du risque radon"""

    altitude_sol_mean: str
    """(ign) Altitude au sol moyenne [m]"""

    annee_construction: str
    """AnnÃ©e de construction du bÃ¢timent"""

    arrete_2021: str
    """
    prÃ©cise si le DPE est un DPE qui est issu de la nouvelle rÃ©forme du DPE
    (arrÃªtÃ© du 31 mars 2021) ou s'il s'agit d'un DPE issu de la modification
    antÃ©rieure de 2012.
    """

    batiment_groupe_id: str
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    chauffage_solaire: str
    """prÃ©sence de chauffage solaire"""

    classe_bilan_dpe: str
    """
    Classe du DPE issu de la synthÃ¨se du double seuil sur les consommations
    Ã©nergie primaire et les Ã©missions de CO2 sur les 5 usages
    (ecs/chauffage/climatisation/eclairage/auxiliaires). valable uniquement pour les
    DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en vigueur
    actuellement)
    """

    classe_conso_energie_arrete_2012: str
    """classe d'Ã©mission GES du DPE 3 usages (Chauffage, ECS, Climatisation).

    Valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    classe_inertie: str
    """classe d'inertie du DPE (enum version BDNB)"""

    cle_interop_adr_principale_ban: str
    """ClÃ© d'interopÃ©rabilitÃ© de l'adresse principale (issue de la BAN)"""

    code_commune_insee: str
    """Code INSEE de la commune"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    code_epci_insee: str
    """Code de l'EPCI"""

    code_iris: str
    """Code iris INSEE"""

    code_qp: str
    """identifiant de la table qpv"""

    code_region_insee: str
    """Code rÃ©gion INSEE"""

    conso_3_usages_ep_m2_arrete_2012: str
    """
    consommation annuelle 3 usages Ã©nergie primaire rapportÃ©e au m2 (Chauffage,
    ECS , Climatisation). valable uniquement pour les DPE appliquant la mÃ©thode de
    l'arrÃªtÃ© du 8 fÃ©vrier 2012
    """

    conso_5_usages_ep_m2: str
    """
    consommation annuelle 5 usages
    (ecs/chauffage/climatisation/eclairage/auxiliaires) en Ã©nergie primaire
    (dÃ©duit de la production pv autoconsommÃ©e) (kWhep/mÂ²/an). valable uniquement
    pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en vigueur
    actuellement)
    """

    conso_pro_dle_elec_2020: str
    """Consommation professionnelle Ã©lectrique [kWh/an]"""

    conso_pro_dle_gaz_2020: str
    """Consommation professionnelle gaz [kWh/an]"""

    conso_res_dle_elec_2020: str
    """Consommation rÃ©sidentielle Ã©lectrique [kWh/an]"""

    conso_res_dle_gaz_2020: str
    """Consommation rÃ©sidentielle gaz [kWh/an]"""

    contient_fictive_geom_groupe: str
    """
    Vaut "vrai", si la gÃ©omÃ©trie du groupe de bÃ¢timent est gÃ©nÃ©rÃ©e
    automatiquement et ne reprÃ©sente pas la gÃ©omÃ©trie du groupe de bÃ¢timent.
    """

    croisement_geospx_reussi: str
    """
    le croisement gÃ©ospatial entre la BDTOPO et les fichiers fonciers est
    considÃ©rÃ©e comme rÃ©ussi
    """

    date_reception_dpe: str
    """date de rÃ©ception du DPE dans la base de donnÃ©es de l'ADEME"""

    difference_rel_valeur_fonciere_etat_initial_renove_categorie: str
    """
    categorie de la difference relative de valeur fonciere avant et apres renovation
    (verbose)
    """

    distance_batiment_historique_plus_proche: str
    """(mer) Distance au bÃ¢timent historique le plus proche (si moins de 500m) [m]"""

    ecs_solaire: str
    """prÃ©sence d'ecs solaire"""

    emission_ges_3_usages_ep_m2_arrete_2012: str
    """
    emission GES totale 3 usages Ã©nergie primaire rapportÃ©e au m2 (Chauffage, ECS
    , Climatisation). valable uniquement pour les DPE appliquant la mÃ©thode de
    l'arrÃªtÃ© du 8 fÃ©vrier 2012 (kgCO2/m2/an).
    """

    emission_ges_5_usages_m2: str
    """
    emission GES totale 5 usages rapportÃ©e au mÂ² (dÃ©duit de la production pv
    autoconsommÃ©e)
    (ecs/chauffage/climatisation/eclairage/auxiliaires)(kgCO2/m2/an). valable
    uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 31 mars 2021 (en
    vigueur actuellement)
    """

    epaisseur_lame: str
    """
    epaisseur principale de la lame de gaz entre vitrages pour les baies vitrÃ©es du
    DPE.
    """

    etat_initial_consommation_energie_estim_inc: str
    """
    Incertitude des estimations de consommation Ã©nergÃ©tique finale avant
    rÃ©novation [kWh/m2/an]
    """

    etat_initial_consommation_energie_estim_lower: str
    """
    Estimation basse de la consommation Ã©nergÃ©tique finale avant rÃ©novation
    [kWh/m2/an]
    """

    etat_initial_consommation_energie_estim_mean: str
    """
    Estimation moyenne de la consommation Ã©nergÃ©tique finale avant rÃ©novation
    [kWh/m2/an]
    """

    etat_initial_consommation_energie_estim_upper: str
    """
    Estimation haute de la consommation Ã©nergÃ©tique finale avant rÃ©novation
    [kWh/m2/an]
    """

    etat_initial_consommation_energie_primaire_estim_lower: str
    """
    Estimation basse de la consommation Ã©nergÃ©tique primaire avant rÃ©novation
    [kWh/m2/an]
    """

    etat_initial_consommation_energie_primaire_estim_mean: str
    """
    Estimation moyenne de la consommation Ã©nergÃ©tique primaire avant rÃ©novation
    [kWh/m2/an]
    """

    etat_initial_consommation_energie_primaire_estim_upper: str
    """
    Estimation haute de la consommation Ã©nergÃ©tique primaire avant rÃ©novation
    [kWh/m2/an]
    """

    etat_initial_consommation_ges_estim_inc: str
    """
    Incertitude sur l'estimation de consommation de GES avant rÃ©novation
    [kgeqC02/m2/an]
    """

    etat_initial_ges_estim_lower: str
    """Estimation basse de la consommation de GES avant rÃ©novation [kgeqC02/m2/an]"""

    etat_initial_ges_estim_mean: str
    """Estimation moyenne de la consommation de GES avant rÃ©novation [kgeqC02/m2/an]"""

    etat_initial_ges_estim_upper: str
    """Estimation haute de la consommation de GES avant rÃ©novation [kgeqC02/m2/an]"""

    etat_initial_risque_canicule: str
    """Estimation du risque canicule avant rÃ©novation [1-5]"""

    etat_initial_risque_canicule_inc: str
    """Incertitude de l'estimation du risque canicule avant rÃ©novation [1-5]"""

    etat_renove_consommation_energie_estim_inc: str
    """
    Incertitude sur les estimations des consommations Ã©nergÃ©tiques finales aprÃ¨s
    un scÃ©nario de rÃ©novation globale "standard" (isolation des principaux
    composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de chauffage)
    [kWh/m2/an]
    """

    etat_renove_consommation_energie_estim_lower: str
    """
    Estimation basse de la consommation Ã©nergÃ©tique finale aprÃ¨s un scÃ©nario de
    rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_energie_estim_mean: str
    """
    Estimation moyenne de la consommation Ã©nergÃ©tique finale aprÃ¨s un scÃ©nario
    de rÃ©novation globale "standard" (isolation des principaux composants
    d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_energie_estim_upper: str
    """
    Estimation haute de la consommation Ã©nergÃ©tique finale aprÃ¨s un scÃ©nario de
    rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_energie_primaire_estim_lower: str
    """
    Estimation basse de la consommation d'Ã©nergie primaire aprÃ¨s un scÃ©nario de
    rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_energie_primaire_estim_mean: str
    """
    Estimation moyenne de la consommation d'Ã©nergie primaire aprÃ¨s un scÃ©nario de
    rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_energie_primaire_estim_upper: str
    """
    Estimation haute de la consommation d'Ã©nergie primaire aprÃ¨s un scÃ©nario de
    rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]
    """

    etat_renove_consommation_ges_estim_inc: str
    """
    Incertitude sur l'estimation de consommation de GES aprÃ¨s un scÃ©nario de
    rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kgeqC02/m2/an]
    """

    etat_renove_ges_estim_lower: str
    """
    Estimation basse des Ã©missions de GES aprÃ¨s un scÃ©nario de rÃ©novation
    globale "standard" (isolation des principaux composants d'enveloppe et
    changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]
    """

    etat_renove_ges_estim_mean: str
    """
    Estimation moyenne des Ã©missions de GES aprÃ¨s un scÃ©nario de rÃ©novation
    globale "standard" (isolation des principaux composants d'enveloppe et
    changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]
    """

    etat_renove_ges_estim_upper: str
    """
    Estimation haute des Ã©missions de GES aprÃ¨s un scÃ©nario de rÃ©novation
    globale "standard" (isolation des principaux composants d'enveloppe et
    changement de systÃ¨me Ã©nergÃ©tique de chauffage) [kWh/m2/an]
    """

    etat_renove_risque_canicule: str
    """Estimation du risque canicule aprÃ¨s rÃ©novation [1-5]"""

    etat_renove_risque_canicule_inc: str
    """Incertitude de l'estimation du risque canicule aprÃ¨s rÃ©novation [1-5]"""

    etiquette_dpe_initial_a: str
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette A dans le
    bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent
    """

    etiquette_dpe_initial_b: str
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette B dans le
    bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent
    """

    etiquette_dpe_initial_c: str
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette C dans le
    bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent
    """

    etiquette_dpe_initial_d: str
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette D dans le
    bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent
    """

    etiquette_dpe_initial_e: str
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette E dans le
    bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent
    """

    etiquette_dpe_initial_f: str
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette F dans le
    bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent
    """

    etiquette_dpe_initial_g: str
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette G dans le
    bÃ¢timent pour l'Ã©tat actuel du bÃ¢timent
    """

    etiquette_dpe_initial_inc: str
    """
    Classe d'incertitude de classe sur l'Ã©tiquette dpe avec la plus grande
    probabilitÃ© avant rÃ©novation [1 Ã 5]. Cet indicateur se lit de 1 = peu fiable
    Ã 5 = fiable.
    """

    etiquette_dpe_initial_map: str
    """Etiquette ayant la plus grande probabilitÃ© pour l'Ã©tat actuel du bÃ¢timent"""

    etiquette_dpe_initial_map_2nd: str
    """2 Ã©tiquettes ayant la plus grande probabilitÃ© pour l'Ã©tat actuel du
    bÃ¢timent.

    Si le champs vaut F-G alors F la premiÃ¨re Ã©tiquette est l'Ã©tiquette la plus
    probable , G la seconde Ã©tiquette la plus probable.
    """

    etiquette_dpe_initial_map_2nd_prob: str
    """
    ProbabilitÃ© que le bÃ¢timent ait une Ã©tiquette DPE parmi les 2 Ã©tiquettes
    ayant la plus grande probabilitÃ© pour l'Ã©tat actuel du bÃ¢timent. Si
    etiquette_dpe_initial_map_2nd = F-G et que etiquette_dpe_initial_map_2nd_prob =
    0.95 alors il y a 95% de chance que l'Ã©tiquette DPE de ce bÃ¢timent soit
    classÃ© F ou G.
    """

    etiquette_dpe_renove_a: str
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette A dans le
    bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
    chauffage)
    """

    etiquette_dpe_renove_b: str
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette B dans le
    bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
    chauffage)
    """

    etiquette_dpe_renove_c: str
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette C dans le
    bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
    chauffage)
    """

    etiquette_dpe_renove_d: str
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette D dans le
    bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
    chauffage)
    """

    etiquette_dpe_renove_e: str
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette E dans le
    bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
    chauffage)
    """

    etiquette_dpe_renove_f: str
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette F dans le
    bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
    chauffage)
    """

    etiquette_dpe_renove_g: str
    """
    Estimation de la probabilitÃ© d'avoir des logements d'Ã©tiquette G dans le
    bÃ¢timent aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des
    principaux composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de
    chauffage)
    """

    etiquette_dpe_renove_inc: str
    """
    Incertitude de classe sur l'Ã©tiquette dpe avec la plus grande probabilitÃ©
    aprÃ¨s un scÃ©nario de rÃ©novation globale "standard" (isolation des principaux
    composants d'enveloppe et changement de systÃ¨me Ã©nergÃ©tique de chauffage)
    [1-5]
    """

    etiquette_dpe_renove_map: str
    """
    Etiquette ayant la plus grande probabilitÃ© aprÃ¨s un scÃ©nario de rÃ©novation
    globale "standard" (isolation des principaux composants d'enveloppe et
    changement de systÃ¨me Ã©nergÃ©tique de chauffage)
    """

    etiquette_dpe_renove_map_2nd: str
    """
    2 Ã©tiquettes ayant la plus grande probabilitÃ© aprÃ¨s un scÃ©nario de
    rÃ©novation globale "standard" (isolation des principaux composants d'enveloppe
    et changement de systÃ¨me Ã©nergÃ©tique de chauffage)
    """

    etiquette_dpe_renove_map_2nd_prob: str
    """
    ProbabilitÃ© que le bÃ¢timent ait une Ã©tiquette DPE parmi les 2 Ã©tiquettes
    ayant la plus grande probabilitÃ© aprÃ¨s un scÃ©nario de rÃ©novation globale
    "standard" (isolation des principaux composants d'enveloppe et changement de
    systÃ¨me Ã©nergÃ©tique de chauffage)
    """

    etiquette_dpe_synthese_particulier_simple: str
    """Etiquette DPE selon l'arrÃªtÃ© 2021.

    Si un DPE existe, l'Ã©tiquette provient d'un DPE de l'AEDME, sinon, il s'agit
    d'une simulation.
    """

    etiquette_dpe_synthese_particulier_source: str
    """TODO"""

    facteur_solaire_baie_vitree: str
    """facteur de transmission du flux solaire par la baie vitrÃ©e.

    coefficient entre 0 et 1
    """

    fiabilite_cr_adr_niv_1: str
    """
    FiabilitÃ© des donnÃ©es croisÃ©es Ã l'adresse ('donnÃ©es croisÃ©es Ã l'adresse
    fiables', 'donnÃ©es croisÃ©es Ã l'adresse fiables Ã l'echelle de la parcelle
    unifiee', 'donnÃ©es croisÃ©es Ã l'adresse moyennement fiables', 'problÃ¨me de
    gÃ©ocodage')
    """

    fiabilite_cr_adr_niv_2: str
    """FiabilitÃ© dÃ©taillÃ©e des donnÃ©es croisÃ©es Ã l'adresse"""

    fiabilite_emprise_sol: str
    """FiabilitÃ© de l'emprise au sol du bÃ¢timent"""

    fiabilite_hauteur: str
    """FiabilitÃ© de la hauteur du bÃ¢timent"""

    geom_groupe: str
    """GÃ©omÃ©trie multipolygonale du groupe de bÃ¢timent (Lambert-93)"""

    gisement_gain_conso_finale_total: str
    """(cstb) Estimation du gisement de gain de consommation finale total (kWh/m2/an)"""

    gisement_gain_energetique_mean: str
    """Estimation du gain Ã©nergÃ©tique moyen"""

    gisement_gain_ges_mean: str
    """
    Estimation moyenne du gisement de gain sur les Ã©missions de gaz Ã effets de
    serre
    """

    hauteur_mean: str
    """(ign) Hauteur moyenne des bÃ¢timents [m]"""

    identifiant_dpe: str
    """identifiant de la table des DPE ademe"""

    indicateur_distance_au_reseau: str
    """
    Indication sur la distance entre le bÃ¢timent et le point au rÃ©seau de chaleur
    le plus proche en vue d'un potentiel raccordement au rÃ©seau.
    """

    l_cle_interop_adr: str
    """Liste de clÃ©s d'interopÃ©rabilitÃ© de l'adresse postale"""

    l_denomination_proprietaire: str
    """Liste de dÃ©nominations de propriÃ©taires"""

    l_libelle_adr: str
    """Liste de libellÃ© complet de l'adresse"""

    l_orientation_baie_vitree: str
    """liste des orientations des baies vitrÃ©es (enum version BDNB)"""

    l_parcelle_id: str
    """
    Liste d'identifiants de parcelle (ConcatÃ©nation de ccodep, ccocom, ccopre,
    ccosec, dnupla)
    """

    l_siren: str
    """Liste d'identifiants siren"""

    l_type_generateur_chauffage: str
    """
    type de gÃ©nÃ©rateur de chauffage principal (enum version simplifiÃ©e BDNB)
    concatÃ©nÃ© en liste pour tous les DPE
    """

    l_type_generateur_ecs: str
    """
    type de gÃ©nÃ©rateur d'ECS principal (enum version simplifiÃ©e BDNB) concatÃ©nÃ©
    en liste pour tous les DPE
    """

    libelle_adr_principale_ban: str
    """LibellÃ© complet de l'adresse principale (issue de la BAN)"""

    libelle_commune_insee: str
    """(insee) LibellÃ© de la commune accueillant le groupe de bÃ¢timent"""

    limit: str
    """Limiting and Pagination"""

    mat_mur_txt: str
    """(ffo) MatÃ©riaux principal des murs extÃ©rieurs"""

    mat_toit_txt: str
    """(ffo) MatÃ©riau principal des toitures"""

    materiaux_structure_mur_exterieur: str
    """
    matÃ©riaux ou principe constructif principal utilisÃ© pour les murs extÃ©rieurs
    (enum version BDNB)
    """

    materiaux_structure_mur_exterieur_simplifie: str
    """materiaux principal utiliÃ© pour les murs extÃ©rieur simplifiÃ©.

    Cette information peut Ãªtre rÃ©cupÃ©rÃ©e de diffÃ©rentes sources (Fichiers
    Fonciers ou DPE pour le moment)
    """

    materiaux_toiture_simplifie: str
    """materiaux principal utiliÃ© pour la toiture simplifiÃ©.

    Cette information peut Ãªtre rÃ©cupÃ©rÃ©e de diffÃ©rentes sources (Fichiers
    Fonciers ou DPE pour le moment)
    """

    nb_adresse_valid_ban: str
    """
    Nombre d'adresses valides diffÃ©rentes provenant de la BAN qui desservent le
    groupe de bÃ¢timent
    """

    nb_classe_bilan_dpe_a: str
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe A
    """

    nb_classe_bilan_dpe_b: str
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe B
    """

    nb_classe_bilan_dpe_c: str
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe C
    """

    nb_classe_bilan_dpe_d: str
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe D
    """

    nb_classe_bilan_dpe_e: str
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe E
    """

    nb_classe_bilan_dpe_f: str
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe F
    """

    nb_classe_bilan_dpe_g: str
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe G
    """

    nb_classe_conso_energie_arrete_2012_a: str
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique A.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_b: str
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique B.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_c: str
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique C.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_d: str
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique D.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_e: str
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique E.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_f: str
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique F.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_g: str
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique G.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_nc: str
    """
    (dpe) Nombre de DPE n'ayant pas fait l'objet d'un calcul d'Ã©tiquette Ã©nergie
    (DPE dits vierges). valable uniquement pour les DPE appliquant la mÃ©thode de
    l'arrÃªtÃ© du 8 fÃ©vrier 2012
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
    """(ffo) Nombre de niveau du bÃ¢timent (ex: RDC = 1, R+1 = 2, etc..)"""

    nb_pdl_pro_dle_elec_2020: str
    """Nombre de points de livraison Ã©lectrique professionnels [kWh/an]"""

    nb_pdl_pro_dle_gaz_2020: str
    """Nombre de points de livraison gaz professionnels [kWh/an]"""

    nb_pdl_res_dle_elec_2020: str
    """Nombre de points de livraison Ã©lectrique rÃ©sidentiels [kWh/an]"""

    nb_pdl_res_dle_gaz_2020: str
    """Nombre de points de livraison gaz rÃ©sidentiels [kWh/an]"""

    nom_batiment_historique_plus_proche: str
    """(mer:tico) nom du bÃ¢timent historique le plus proche"""

    nom_qp: str
    """Nom du quartier prioritaire dans lequel se trouve le bÃ¢timent"""

    nom_quartier_qpv: str
    """Nom du quartier prioritaire dans lequel se trouve le bÃ¢timent"""

    numero_immat_principal: str
    """numÃ©ro d'immatriculation principal associÃ© au bÃ¢timent groupe.

    (numÃ©ro d'immatriculation copropriÃ©tÃ© qui comporte le plus de lots)
    """

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    potentiel_raccordement_reseau_chaleur: str
    """Indicateur de potentiel de raccordement au rÃ©seau de chaleur.

    L'indicateur dÃ©pend de la distance entre le bÃ¢timent et le rÃ©seau et du type
    de circuit de chauffage existant du bÃ¢timent. Enfin, si le bÃ¢timent est dÃ©jÃ
    raccordÃ© alors il est indiquÃ© comme tel.
    """

    pourcentage_surface_baie_vitree_exterieur: str
    """pourcentage de surface de baies vitrÃ©es sur les murs extÃ©rieurs"""

    presence_balcon: str
    """
    prÃ©sence de balcons identifiÃ©s par analyse des coefficients de masques
    solaires du DPE.
    """

    quartier_prioritaire: str
    """Est situÃ© dans un quartier prioritaire"""

    s_geom_groupe: str
    """Surface au sol de la gÃ©omÃ©trie du bÃ¢timent groupe (geom_groupe)"""

    select: str
    """Filtering Columns"""

    surface_emprise_sol: str
    """Surface au sol de la gÃ©omÃ©trie du bÃ¢timent groupe (geom_groupe)"""

    surface_facade_ext: str
    """Estimation de la surface de faÃ§ade donnant sur l'exterieur [mÂ²]"""

    surface_facade_mitoyenne: str
    """Estimation de la surface de faÃ§ade donnant sur un autre bÃ¢timent [mÂ²]"""

    surface_facade_totale: str
    """Estimation de la surface totale de faÃ§ade (murs + baies) [mÂ²]"""

    surface_facade_vitree: str
    """Estimation de la surface de faÃ§ade vitrÃ©e [mÂ²]"""

    traversant: str
    """indicateur du cÃ´tÃ© traversant du logement."""

    type_dpe: str
    """type de DPE.

    Permet de prÃ©ciser le type de DPE (arrÃªtÃ© 2012/arrÃªtÃ© 2021), son objet
    (logement, immeuble de logement, tertiaire) et la mÃ©thode de calcul utilisÃ©
    (3CL conventionel,facture ou RT2012/RE2020)
    """

    type_energie_chauffage: str
    """
    type d'Ã©nergie pour le gÃ©nÃ©rateur de chauffage principal (enum version
    simplifiÃ©e BDNB)
    """

    type_energie_chauffage_appoint: str
    """
    type d'Ã©nergie pour le gÃ©nÃ©rateur de chauffage d'appoint (enum version
    simplifiÃ©e BDNB)
    """

    type_fermeture: str
    """
    type de fermeture principale installÃ©e sur les baies vitrÃ©es du DPE
    (volet,persienne etc..) (enum version BDNB)
    """

    type_gaz_lame: str
    """
    type de gaz injectÃ© principalement dans la lame entre les vitrages des baies
    vitrÃ©es du DPE (double vitrage ou triple vitrage uniquement) (enum version
    BDNB)
    """

    type_generateur_chauffage: str
    """type de gÃ©nÃ©rateur de chauffage principal (enum version simplifiÃ©e BDNB)"""

    type_generateur_chauffage_anciennete: str
    """anciennetÃ© du gÃ©nÃ©rateur de chauffage principal"""

    type_generateur_chauffage_anciennete_appoint: str
    """anciennetÃ© du gÃ©nÃ©rateur de chauffage d'appoint"""

    type_generateur_chauffage_appoint: str
    """type de gÃ©nÃ©rateur de chauffage d'appoint (enum version simplifiÃ©e BDNB)"""

    type_generateur_climatisation: str
    """type de gÃ©nÃ©rateur de climatisation principal (enum version simplifiÃ©e BDNB)"""

    type_generateur_climatisation_anciennete: str
    """anciennetÃ© du gÃ©nÃ©rateur de climatisation principal"""

    type_generateur_ecs: str
    """
    type de gÃ©nÃ©rateur d'eau chaude sanitaire (ECS) principal (enum version
    simplifiÃ©e BDNB)
    """

    type_generateur_ecs_anciennete: str
    """anciennetÃ© du gÃ©nÃ©rateur d'eau chaude sanitaire (ECS) principal"""

    type_installation_chauffage: str
    """
    type d'installation de chauffage (collectif ou individuel) (enum version
    simplifiÃ©e BDNB)
    """

    type_installation_ecs: str
    """
    type d'installation d'eau chaude sanitaire (ECS) (collectif ou individuel) (enum
    version simplifiÃ©e BDNB)
    """

    type_isolation_mur_exterieur: str
    """
    type d'isolation principal des murs donnant sur l'extÃ©rieur pour le DPE (enum
    version BDNB)
    """

    type_isolation_plancher_bas: str
    """
    type d'isolation principal des planchers bas dÃ©perditifs pour le DPE (enum
    version BDNB)
    """

    type_isolation_plancher_haut: str
    """
    type d'isolation principal des planchers hauts dÃ©perditifs pour le DPE (enum
    version BDNB)
    """

    type_materiaux_menuiserie: str
    """
    type de matÃ©riaux principal des menuiseries des baies vitrÃ©es du DPE (enum
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
    """type de vitrage principal des baies vitrÃ©es du DPE (enum version BDNB)"""

    u_baie_vitree: str
    """
    Coefficient de transmission thermique moyen des baies vitrÃ©es en incluant le
    calcul de la rÃ©sistance additionelle des fermetures (calcul Ujn) (W/mÂ²/K)
    """

    u_mur_exterieur: str
    """Coefficient de transmission thermique moyen des murs extÃ©rieurs (W/mÂ²/K)"""

    u_plancher_bas_final_deperditif: str
    """
    Coefficient de transmission thermique moyen des planchers bas en prenant en
    compte l'attÃ©nuation forfaitaire du U lorsqu'en contact avec le sol de la
    mÃ©thode 3CL(W/mÂ²/K)
    """

    u_plancher_haut_deperditif: str
    """Coefficient de transmission thermique moyen des planchers hauts (W/mÂ²/K)"""

    usage_niveau_1_txt: str
    """indicateurs d'usage simplifiÃ© du bÃ¢timent (verbose)"""

    valeur_fonciere_etat_initial_incertitude: str
    """incertitude de l'estimation de la valeur fonciere avant renovation"""

    vitrage_vir: str
    """
    le vitrage a Ã©tÃ© traitÃ© avec un traitement Ã isolation renforcÃ© ce qui le
    rend plus performant d'un point de vue thermique.
    """

    volume_brut: str
    """Volume brut du bÃ¢timent [m3]"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
