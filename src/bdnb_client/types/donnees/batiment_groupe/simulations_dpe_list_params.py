# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SimulationsDpeListParams"]


class SimulationsDpeListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    code_departement_insee: str
    """Code département INSEE"""

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

    etiquette_dpe_initial_error: str
    """Erreur sur la simulation de DPE pour l'état actuel du bâtiment"""

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

    etiquette_dpe_initial_map_prob: str
    """
    Probabilité que le bâtiment ait une étiquette DPE égale à l'étiquette ayant la
    plus grande probabilité pour l'état actuel du bâtiment. C'est la probabilité
    d'avoir pour ce bâtiment l'étiquette etiquette_dpe_initial_map. Si
    etiquette_dpe_initial_map = F et que etiquette_dpe_initial_map_prob = 0.64 alors
    il y a 64% de chance que l'étiquette DPE de ce bâtiment soit classé F
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

    etiquette_dpe_renove_error: str
    """Erreur sur la simulation de DPE avant rénovation"""

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

    etiquette_dpe_renove_map_prob: str
    """
    Probabilité que le bâtiment ait une étiquette DPE égale à l'étiquette ayant la
    plus grande probabilité après un scénario de rénovation globale "standard"
    (isolation des principaux composants d'enveloppe et changement de système
    énergétique de chauffage)
    """

    gisement_gain_conso_finale_total: str
    """Estimation du gisement de gain de consommation finale total"""

    gisement_gain_energetique_mean: str
    """Estimation du gain énergétique moyen"""

    gisement_gain_ges_mean: str
    """
    Estimation moyenne du gisement de gain sur les émissions de gaz à effets de
    serre
    """

    indecence_energetique_initial: str
    """probabilité du bâtiment d'àªtre en indécence énergétique dans son état initial"""

    indecence_energetique_renove: str
    """
    probabilité du bâtiment d'àªtre en indécence énergétique dans son état rénové
    (rénovation globale)
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
    """Estimation de la surface déperditive du bâtiment [mÂ²]"""

    surface_deperditive_verticale: str
    """Estimation de la surface déperditive verticale du bâtiment [mÂ²]"""

    surface_enveloppe: str
    """Estimation de la surface de l'enveloppe [mÂ²]"""

    surface_facade_ext: str
    """Estimation de la surface de faà§ade donnant sur l'exterieur [mÂ²]"""

    surface_facade_mitoyenne: str
    """Estimation de la surface de faà§ade donnant sur un autre bâtiment [mÂ²]"""

    surface_facade_totale: str
    """Estimation de la surface totale de faà§ade (murs + baies) [mÂ²]"""

    surface_facade_vitree: str
    """Estimation de la surface de faà§ade vitrée [mÂ²]"""

    surface_toiture: str
    """Estimation de la surface de toiture du bâtiment [mÂ²]"""

    surface_verticale: str
    """Estimation de la surface verticale du bâtiment [mÂ²]"""

    volume_brut: str
    """Volume brut du bâtiment [m3]"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
