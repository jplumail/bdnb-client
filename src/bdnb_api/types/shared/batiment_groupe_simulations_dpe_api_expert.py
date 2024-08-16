# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BatimentGroupeSimulationsDpeAPIExpert"]


class BatimentGroupeSimulationsDpeAPIExpert(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

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

    etiquette_dpe_initial_error: Optional[float] = None
    """Erreur sur la simulation de DPE pour l'Ã©tat actuel du bÃ¢timent"""

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

    etiquette_dpe_initial_map_prob: Optional[float] = None
    """
    ProbabilitÃ© que le bÃ¢timent ait une Ã©tiquette DPE Ã©gale Ã l'Ã©tiquette ayant
    la plus grande probabilitÃ© pour l'Ã©tat actuel du bÃ¢timent. C'est la
    probabilitÃ© d'avoir pour ce bÃ¢timent l'Ã©tiquette etiquette_dpe_initial_map.
    Si etiquette_dpe_initial_map = F et que etiquette_dpe_initial_map_prob = 0.64
    alors il y a 64% de chance que l'Ã©tiquette DPE de ce bÃ¢timent soit classÃ© F
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

    etiquette_dpe_renove_error: Optional[float] = None
    """Erreur sur la simulation de DPE avant rÃ©novation"""

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

    etiquette_dpe_renove_map_prob: Optional[float] = None
    """
    ProbabilitÃ© que le bÃ¢timent ait une Ã©tiquette DPE Ã©gale Ã l'Ã©tiquette ayant
    la plus grande probabilitÃ© aprÃ¨s un scÃ©nario de rÃ©novation globale
    "standard" (isolation des principaux composants d'enveloppe et changement de
    systÃ¨me Ã©nergÃ©tique de chauffage)
    """

    gisement_gain_conso_finale_total: Optional[int] = None
    """Estimation du gisement de gain de consommation finale total"""

    gisement_gain_energetique_mean: Optional[int] = None
    """Estimation du gain Ã©nergÃ©tique moyen"""

    gisement_gain_ges_mean: Optional[int] = None
    """
    Estimation moyenne du gisement de gain sur les Ã©missions de gaz Ã effets de
    serre
    """

    indecence_energetique_initial: Optional[float] = None
    """
    probabilitÃ© du bÃ¢timent d'Ãªtre en indÃ©cence Ã©nergÃ©tique dans son Ã©tat
    initial
    """

    indecence_energetique_renove: Optional[float] = None
    """
    probabilitÃ© du bÃ¢timent d'Ãªtre en indÃ©cence Ã©nergÃ©tique dans son Ã©tat
    rÃ©novÃ© (rÃ©novation globale)
    """

    surface_deperditive: Optional[int] = None
    """Estimation de la surface dÃ©perditive du bÃ¢timent [mÂ²]"""

    surface_deperditive_verticale: Optional[int] = None
    """Estimation de la surface dÃ©perditive verticale du bÃ¢timent [mÂ²]"""

    surface_enveloppe: Optional[int] = None
    """Estimation de la surface de l'enveloppe [mÂ²]"""

    surface_facade_ext: Optional[int] = None
    """Estimation de la surface de faÃ§ade donnant sur l'exterieur [mÂ²]"""

    surface_facade_mitoyenne: Optional[int] = None
    """Estimation de la surface de faÃ§ade donnant sur un autre bÃ¢timent [mÂ²]"""

    surface_facade_totale: Optional[int] = None
    """Estimation de la surface totale de faÃ§ade (murs + baies) [mÂ²]"""

    surface_facade_vitree: Optional[int] = None
    """Estimation de la surface de faÃ§ade vitrÃ©e [mÂ²]"""

    surface_toiture: Optional[int] = None
    """Estimation de la surface de toiture du bÃ¢timent [mÂ²]"""

    surface_verticale: Optional[int] = None
    """Estimation de la surface verticale du bÃ¢timent [mÂ²]"""

    volume_brut: Optional[int] = None
    """Volume brut du bÃ¢timent [m3]"""
