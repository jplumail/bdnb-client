# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BatimentGroupeSimulationsDvfListParams"]


class BatimentGroupeSimulationsDvfListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    classe_dpe_conso_initial: str
    """classe dpe a l'echelle bÃ¢timent predit dans son etat initial"""

    classe_dpe_conso_renove: str
    """classe dpe a l'echelle bÃ¢timent predit dans son etat renove"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    difference_abs_valeur_fonciere_etat_initial_renove: str
    """
    difference absolue entre la valeur fonciÃ¨re avant et apres renovation [â‚¬/mÂ²]
    """

    difference_rel_valeur_fonciere_etat_initial_renove: str
    """difference relative de valeur fonciere avant et apres renovation"""

    difference_rel_valeur_fonciere_etat_initial_renove_categorie: str
    """
    categorie de la difference relative de valeur fonciere avant et apres renovation
    (verbose)
    """

    difference_rel_valeur_fonciere_initial_mean_iris: str
    """
    difference relative de la valeur fonciere avant renovation par rapport Ã la
    moyenne Ã l'iris predite sans renovation
    """

    difference_rel_valeur_fonciere_renove_mean_iris: str
    """
    difference relative de la valeur fonciere apres renovation par rapport Ã la
    moyenne Ã l'iris predite sans renovation
    """

    limit: str
    """Limiting and Pagination"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    r2: str
    """r2 du modele de simulation"""

    select: str
    """Filtering Columns"""

    usage_niveau_1_txt: str
    """indicateurs d'usage simplifiÃ© du bÃ¢timent (verbose)"""

    valeur_fonciere_etat_initial_estim_lower: str
    """Estimation basse de la valeur fonciere avant renovation [â‚¬/mÂ²]"""

    valeur_fonciere_etat_initial_estim_mean: str
    """Estimation moyenne de la valeur fonciere avant renovation [â‚¬/mÂ²]"""

    valeur_fonciere_etat_initial_estim_upper: str
    """Estimation haute de la valeur fonciere avant renovation [â‚¬/mÂ²]"""

    valeur_fonciere_etat_initial_incertitude: str
    """incertitude de l'estimation de la valeur fonciere avant renovation"""

    valeur_fonciere_etat_renove_estim_lower: str
    """Estimation basse de la valeur fonciere apres renovation [â‚¬/mÂ²]"""

    valeur_fonciere_etat_renove_estim_mean: str
    """Estimation moyenne de la valeur fonciere apres renovation [â‚¬/mÂ²]"""

    valeur_fonciere_etat_renove_estim_upper: str
    """Estimation haute de la valeur fonciere apres renovation [â‚¬/mÂ²]"""

    valeur_fonciere_etat_renove_incertitude: str
    """incertitude de l'estimation de la valeur fonciere apres renovation"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
