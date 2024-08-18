# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["BatimentGroupeSimulationsDpe"]


class BatimentGroupeSimulationsDpe(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

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

    etiquette_dpe_initial_error: Optional[float] = None
    """Erreur sur la simulation de DPE pour l'état actuel du bâtiment"""

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

    etiquette_dpe_initial_map_prob: Optional[float] = None
    """
    Probabilité que le bâtiment ait une étiquette DPE égale à l'étiquette ayant la
    plus grande probabilité pour l'état actuel du bâtiment. C'est la probabilité
    d'avoir pour ce bâtiment l'étiquette etiquette_dpe_initial_map. Si
    etiquette_dpe_initial_map = F et que etiquette_dpe_initial_map_prob = 0.64 alors
    il y a 64% de chance que l'étiquette DPE de ce bâtiment soit classé F
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

    etiquette_dpe_renove_error: Optional[float] = None
    """Erreur sur la simulation de DPE avant rénovation"""

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

    etiquette_dpe_renove_map_prob: Optional[float] = None
    """
    Probabilité que le bâtiment ait une étiquette DPE égale à l'étiquette ayant la
    plus grande probabilité après un scénario de rénovation globale "standard"
    (isolation des principaux composants d'enveloppe et changement de système
    énergétique de chauffage)
    """

    gisement_gain_conso_finale_total: Optional[int] = None
    """Estimation du gisement de gain de consommation finale total"""

    gisement_gain_energetique_mean: Optional[int] = None
    """Estimation du gain énergétique moyen"""

    gisement_gain_ges_mean: Optional[int] = None
    """
    Estimation moyenne du gisement de gain sur les émissions de gaz à effets de
    serre
    """

    indecence_energetique_initial: Optional[float] = None
    """probabilité du bâtiment d'àªtre en indécence énergétique dans son état initial"""

    indecence_energetique_renove: Optional[float] = None
    """
    probabilité du bâtiment d'àªtre en indécence énergétique dans son état rénové
    (rénovation globale)
    """

    surface_deperditive: Optional[int] = None
    """Estimation de la surface déperditive du bâtiment [mÂ²]"""

    surface_deperditive_verticale: Optional[int] = None
    """Estimation de la surface déperditive verticale du bâtiment [mÂ²]"""

    surface_enveloppe: Optional[int] = None
    """Estimation de la surface de l'enveloppe [mÂ²]"""

    surface_facade_ext: Optional[int] = None
    """Estimation de la surface de faà§ade donnant sur l'exterieur [mÂ²]"""

    surface_facade_mitoyenne: Optional[int] = None
    """Estimation de la surface de faà§ade donnant sur un autre bâtiment [mÂ²]"""

    surface_facade_totale: Optional[int] = None
    """Estimation de la surface totale de faà§ade (murs + baies) [mÂ²]"""

    surface_facade_vitree: Optional[int] = None
    """Estimation de la surface de faà§ade vitrée [mÂ²]"""

    surface_toiture: Optional[int] = None
    """Estimation de la surface de toiture du bâtiment [mÂ²]"""

    surface_verticale: Optional[int] = None
    """Estimation de la surface verticale du bâtiment [mÂ²]"""

    volume_brut: Optional[int] = None
    """Volume brut du bâtiment [m3]"""
