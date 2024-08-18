# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DvfOpenStatistiqueListParams"]


class DvfOpenStatistiqueListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    code_departement_insee: str
    """Code département INSEE"""

    limit: str
    """Limiting and Pagination"""

    nb_appartement_mutee: str
    """
    Nombre d'appartements qui ont mutés sur le batiment_groupe (sur la période de
    référence des DVF).
    """

    nb_dependance_mutee: str
    """
    Nombre de dépendances qui ont mutées sur le batiment_groupe (sur la période de
    référence des DVF).
    """

    nb_locaux_mutee: str
    """
    Nombre de locaux qui ont mutés sur le batiment_groupe (sur la période de
    référence des DVF).
    """

    nb_locaux_tertiaire_mutee: str
    """
    Nombre de locaux tertiaires qui ont mutés sur le batiment_groupe (sur la période
    de référence des DVF).
    """

    nb_maisons_mutee: str
    """
    Nombre de maisons qui ont mutées sur le batiment_groupe (sur la période de
    référence des DVF).
    """

    nb_mutation: str
    """
    Nombre de mutations qui ont eu lieu sur le batiment_groupe (sur la période de
    référence des DVF).
    """

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    prix_m2_local_max: str
    """
    Prix maximale au m2 de bâti en euros calculé à partir des transactions dont
    uniquement des locaux (résidences individuelles + dépendances) ou (résidences
    collectives + dépendances) ont mutées
    """

    prix_m2_local_median: str
    """
    Prix médian au m2 de bâti en euros calculé à partir des transactions dont
    uniquement des locaux (résidences individuelles + dépendances) ou (résidences
    collectives + dépendances) ont mutées
    """

    prix_m2_local_min: str
    """
    Prix minimale au m2 de bâti en euros calculé à partir des transactions dont
    uniquement des locaux (résidences individuelles + dépendances) ou (résidences
    collectives + dépendances) ont mutées
    """

    prix_m2_local_moyen: str
    """
    Prix moyen au m2 de bâti en euros calculé à partir des transactions dont
    uniquement des locaux (résidences individuelles + dépendances) ou (résidences
    collectives + dépendances) ont mutées
    """

    prix_m2_terrain_max: str
    """
    Prix maximale au m2 de terrain en euros calculé à partir des transactions dont
    uniquement des locaux (résidences individuelles + dépendances) ou (résidences
    collectives + dépendances) ont mutées
    """

    prix_m2_terrain_median: str
    """
    Prix médian au m2 de terrain en euros calculé à partir des transactions dont
    uniquement des locaux (résidences individuelles + dépendances) ou (résidences
    collectives + dépendances) ont mutées
    """

    prix_m2_terrain_min: str
    """
    Prix minimale au m2 de terrain en euros calculé à partir des transactions dont
    uniquement des locaux (résidences individuelles + dépendances) ou (résidences
    collectives + dépendances) ont mutées
    """

    prix_m2_terrain_moyen: str
    """
    Prix moyen au m2 de terrain en euros calculé à partir des transactions dont
    uniquement des locaux (résidences individuelles + dépendances) ou (résidences
    collectives + dépendances) ont mutées
    """

    select: str
    """Filtering Columns"""

    valeur_fonciere_max: str
    """
    (dv3f) valeur foncière maximale parmi les locaux du bâtiment rapporté au mÂ²
    habitable (SHAB)[â‚¬/mÂ²]
    """

    valeur_fonciere_median: str
    """
    Valeur foncière médiane en euros calculée sur l'ensemble des mutations qui ont
    eu lieu sur le batiment_groupe.
    """

    valeur_fonciere_min: str
    """
    (dv3f) valeur foncière minimale parmi les locaux du bâtiment rapporté au mÂ²
    habitable (SHAB) [â‚¬/mÂ²]
    """

    valeur_fonciere_moyenne: str
    """
    Valeur foncière moyenne en euros calculée sur l'ensemble des mutations qui ont
    eu lieu sur le batiment_groupe.
    """

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
