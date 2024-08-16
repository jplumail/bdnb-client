# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TablesBdnbRetrieveBatimentGroupeDvfOpenStatistiqueParams"]


class TablesBdnbRetrieveBatimentGroupeDvfOpenStatistiqueParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    limit: str
    """Limiting and Pagination"""

    nb_appartement_mutee: str
    """
    Nombre d'appartements qui ont mutÃ©s sur le batiment_groupe (sur la pÃ©riode de
    rÃ©fÃ©rence des DVF).
    """

    nb_dependance_mutee: str
    """
    Nombre de dÃ©pendances qui ont mutÃ©es sur le batiment_groupe (sur la pÃ©riode
    de rÃ©fÃ©rence des DVF).
    """

    nb_locaux_mutee: str
    """
    Nombre de locaux qui ont mutÃ©s sur le batiment_groupe (sur la pÃ©riode de
    rÃ©fÃ©rence des DVF).
    """

    nb_locaux_tertiaire_mutee: str
    """
    Nombre de locaux tertiaires qui ont mutÃ©s sur le batiment_groupe (sur la
    pÃ©riode de rÃ©fÃ©rence des DVF).
    """

    nb_maisons_mutee: str
    """
    Nombre de maisons qui ont mutÃ©es sur le batiment_groupe (sur la pÃ©riode de
    rÃ©fÃ©rence des DVF).
    """

    nb_mutation: str
    """
    Nombre de mutations qui ont eu lieu sur le batiment_groupe (sur la pÃ©riode de
    rÃ©fÃ©rence des DVF).
    """

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    prix_m2_local_max: str
    """
    Prix maximale au m2 de bÃ¢ti en euros calculÃ© Ã partir des transactions dont
    uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
    collectives + dÃ©pendances) ont mutÃ©es
    """

    prix_m2_local_median: str
    """
    Prix mÃ©dian au m2 de bÃ¢ti en euros calculÃ© Ã partir des transactions dont
    uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
    collectives + dÃ©pendances) ont mutÃ©es
    """

    prix_m2_local_min: str
    """
    Prix minimale au m2 de bÃ¢ti en euros calculÃ© Ã partir des transactions dont
    uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
    collectives + dÃ©pendances) ont mutÃ©es
    """

    prix_m2_local_moyen: str
    """
    Prix moyen au m2 de bÃ¢ti en euros calculÃ© Ã partir des transactions dont
    uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
    collectives + dÃ©pendances) ont mutÃ©es
    """

    prix_m2_terrain_max: str
    """
    Prix maximale au m2 de terrain en euros calculÃ© Ã partir des transactions dont
    uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
    collectives + dÃ©pendances) ont mutÃ©es
    """

    prix_m2_terrain_median: str
    """
    Prix mÃ©dian au m2 de terrain en euros calculÃ© Ã partir des transactions dont
    uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
    collectives + dÃ©pendances) ont mutÃ©es
    """

    prix_m2_terrain_min: str
    """
    Prix minimale au m2 de terrain en euros calculÃ© Ã partir des transactions dont
    uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
    collectives + dÃ©pendances) ont mutÃ©es
    """

    prix_m2_terrain_moyen: str
    """
    Prix moyen au m2 de terrain en euros calculÃ© Ã partir des transactions dont
    uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
    collectives + dÃ©pendances) ont mutÃ©es
    """

    select: str
    """Filtering Columns"""

    valeur_fonciere_max: str
    """
    (dv3f) valeur fonciÃ¨re maximale parmi les locaux du bÃ¢timent rapportÃ© au mÂ²
    habitable (SHAB)[â‚¬/mÂ²]
    """

    valeur_fonciere_median: str
    """
    Valeur fonciÃ¨re mÃ©diane en euros calculÃ©e sur l'ensemble des mutations qui
    ont eu lieu sur le batiment_groupe.
    """

    valeur_fonciere_min: str
    """
    (dv3f) valeur fonciÃ¨re minimale parmi les locaux du bÃ¢timent rapportÃ© au mÂ²
    habitable (SHAB) [â‚¬/mÂ²]
    """

    valeur_fonciere_moyenne: str
    """
    Valeur fonciÃ¨re moyenne en euros calculÃ©e sur l'ensemble des mutations qui ont
    eu lieu sur le batiment_groupe.
    """

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
