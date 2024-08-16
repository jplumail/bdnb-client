# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BatimentGroupeSimulationsDpeListParams"]


class BatimentGroupeSimulationsDpeListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

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

    etiquette_dpe_initial_error: str
    """Erreur sur la simulation de DPE pour l'Ã©tat actuel du bÃ¢timent"""

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

    etiquette_dpe_initial_map_prob: str
    """
    ProbabilitÃ© que le bÃ¢timent ait une Ã©tiquette DPE Ã©gale Ã l'Ã©tiquette ayant
    la plus grande probabilitÃ© pour l'Ã©tat actuel du bÃ¢timent. C'est la
    probabilitÃ© d'avoir pour ce bÃ¢timent l'Ã©tiquette etiquette_dpe_initial_map.
    Si etiquette_dpe_initial_map = F et que etiquette_dpe_initial_map_prob = 0.64
    alors il y a 64% de chance que l'Ã©tiquette DPE de ce bÃ¢timent soit classÃ© F
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

    etiquette_dpe_renove_error: str
    """Erreur sur la simulation de DPE avant rÃ©novation"""

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

    etiquette_dpe_renove_map_prob: str
    """
    ProbabilitÃ© que le bÃ¢timent ait une Ã©tiquette DPE Ã©gale Ã l'Ã©tiquette ayant
    la plus grande probabilitÃ© aprÃ¨s un scÃ©nario de rÃ©novation globale
    "standard" (isolation des principaux composants d'enveloppe et changement de
    systÃ¨me Ã©nergÃ©tique de chauffage)
    """

    gisement_gain_conso_finale_total: str
    """Estimation du gisement de gain de consommation finale total"""

    gisement_gain_energetique_mean: str
    """Estimation du gain Ã©nergÃ©tique moyen"""

    gisement_gain_ges_mean: str
    """
    Estimation moyenne du gisement de gain sur les Ã©missions de gaz Ã effets de
    serre
    """

    indecence_energetique_initial: str
    """
    probabilitÃ© du bÃ¢timent d'Ãªtre en indÃ©cence Ã©nergÃ©tique dans son Ã©tat
    initial
    """

    indecence_energetique_renove: str
    """
    probabilitÃ© du bÃ¢timent d'Ãªtre en indÃ©cence Ã©nergÃ©tique dans son Ã©tat
    rÃ©novÃ© (rÃ©novation globale)
    """

    limit: str
    """Limiting and Pagination"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    surface_deperditive: str
    """Estimation de la surface dÃ©perditive du bÃ¢timent [mÂ²]"""

    surface_deperditive_verticale: str
    """Estimation de la surface dÃ©perditive verticale du bÃ¢timent [mÂ²]"""

    surface_enveloppe: str
    """Estimation de la surface de l'enveloppe [mÂ²]"""

    surface_facade_ext: str
    """Estimation de la surface de faÃ§ade donnant sur l'exterieur [mÂ²]"""

    surface_facade_mitoyenne: str
    """Estimation de la surface de faÃ§ade donnant sur un autre bÃ¢timent [mÂ²]"""

    surface_facade_totale: str
    """Estimation de la surface totale de faÃ§ade (murs + baies) [mÂ²]"""

    surface_facade_vitree: str
    """Estimation de la surface de faÃ§ade vitrÃ©e [mÂ²]"""

    surface_toiture: str
    """Estimation de la surface de toiture du bÃ¢timent [mÂ²]"""

    surface_verticale: str
    """Estimation de la surface verticale du bÃ¢timent [mÂ²]"""

    volume_brut: str
    """Volume brut du bÃ¢timent [m3]"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
