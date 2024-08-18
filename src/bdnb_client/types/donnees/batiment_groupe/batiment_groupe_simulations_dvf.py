# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["BatimentGroupeSimulationsDvf"]


class BatimentGroupeSimulationsDvf(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    classe_dpe_conso_initial: Optional[str] = None
    """classe dpe a l'echelle bâtiment predit dans son etat initial"""

    classe_dpe_conso_renove: Optional[str] = None
    """classe dpe a l'echelle bâtiment predit dans son etat renove"""

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    difference_abs_valeur_fonciere_etat_initial_renove: Optional[float] = None
    """difference absolue entre la valeur foncière avant et apres renovation [â‚¬/mÂ²]"""

    difference_rel_valeur_fonciere_etat_initial_renove: Optional[float] = None
    """difference relative de valeur fonciere avant et apres renovation"""

    difference_rel_valeur_fonciere_etat_initial_renove_categorie: Optional[str] = None
    """
    categorie de la difference relative de valeur fonciere avant et apres renovation
    (verbose)
    """

    difference_rel_valeur_fonciere_initial_mean_iris: Optional[float] = None
    """
    difference relative de la valeur fonciere avant renovation par rapport à la
    moyenne à l'iris predite sans renovation
    """

    difference_rel_valeur_fonciere_renove_mean_iris: Optional[float] = None
    """
    difference relative de la valeur fonciere apres renovation par rapport à la
    moyenne à l'iris predite sans renovation
    """

    r2: Optional[float] = None
    """r2 du modele de simulation"""

    usage_niveau_1_txt: Optional[str] = None
    """indicateurs d'usage simplifié du bâtiment (verbose)"""

    valeur_fonciere_etat_initial_estim_lower: Optional[float] = None
    """Estimation basse de la valeur fonciere avant renovation [â‚¬/mÂ²]"""

    valeur_fonciere_etat_initial_estim_mean: Optional[float] = None
    """Estimation moyenne de la valeur fonciere avant renovation [â‚¬/mÂ²]"""

    valeur_fonciere_etat_initial_estim_upper: Optional[float] = None
    """Estimation haute de la valeur fonciere avant renovation [â‚¬/mÂ²]"""

    valeur_fonciere_etat_initial_incertitude: Optional[str] = None
    """incertitude de l'estimation de la valeur fonciere avant renovation"""

    valeur_fonciere_etat_renove_estim_lower: Optional[float] = None
    """Estimation basse de la valeur fonciere apres renovation [â‚¬/mÂ²]"""

    valeur_fonciere_etat_renove_estim_mean: Optional[float] = None
    """Estimation moyenne de la valeur fonciere apres renovation [â‚¬/mÂ²]"""

    valeur_fonciere_etat_renove_estim_upper: Optional[float] = None
    """Estimation haute de la valeur fonciere apres renovation [â‚¬/mÂ²]"""

    valeur_fonciere_etat_renove_incertitude: Optional[str] = None
    """incertitude de l'estimation de la valeur fonciere apres renovation"""
