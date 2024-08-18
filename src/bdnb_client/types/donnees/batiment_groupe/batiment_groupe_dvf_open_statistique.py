# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["BatimentGroupeDvfOpenStatistique"]


class BatimentGroupeDvfOpenStatistique(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    nb_appartement_mutee: Optional[int] = None
    """
    Nombre d'appartements qui ont mutés sur le batiment_groupe (sur la période de
    référence des DVF).
    """

    nb_dependance_mutee: Optional[int] = None
    """
    Nombre de dépendances qui ont mutées sur le batiment_groupe (sur la période de
    référence des DVF).
    """

    nb_locaux_mutee: Optional[int] = None
    """
    Nombre de locaux qui ont mutés sur le batiment_groupe (sur la période de
    référence des DVF).
    """

    nb_locaux_tertiaire_mutee: Optional[int] = None
    """
    Nombre de locaux tertiaires qui ont mutés sur le batiment_groupe (sur la période
    de référence des DVF).
    """

    nb_maisons_mutee: Optional[int] = None
    """
    Nombre de maisons qui ont mutées sur le batiment_groupe (sur la période de
    référence des DVF).
    """

    nb_mutation: Optional[int] = None
    """
    Nombre de mutations qui ont eu lieu sur le batiment_groupe (sur la période de
    référence des DVF).
    """

    prix_m2_local_max: Optional[float] = None
    """
    Prix maximale au m2 de bâti en euros calculé à partir des transactions dont
    uniquement des locaux (résidences individuelles + dépendances) ou (résidences
    collectives + dépendances) ont mutées
    """

    prix_m2_local_median: Optional[float] = None
    """
    Prix médian au m2 de bâti en euros calculé à partir des transactions dont
    uniquement des locaux (résidences individuelles + dépendances) ou (résidences
    collectives + dépendances) ont mutées
    """

    prix_m2_local_min: Optional[float] = None
    """
    Prix minimale au m2 de bâti en euros calculé à partir des transactions dont
    uniquement des locaux (résidences individuelles + dépendances) ou (résidences
    collectives + dépendances) ont mutées
    """

    prix_m2_local_moyen: Optional[float] = None
    """
    Prix moyen au m2 de bâti en euros calculé à partir des transactions dont
    uniquement des locaux (résidences individuelles + dépendances) ou (résidences
    collectives + dépendances) ont mutées
    """

    prix_m2_terrain_max: Optional[float] = None
    """
    Prix maximale au m2 de terrain en euros calculé à partir des transactions dont
    uniquement des locaux (résidences individuelles + dépendances) ou (résidences
    collectives + dépendances) ont mutées
    """

    prix_m2_terrain_median: Optional[float] = None
    """
    Prix médian au m2 de terrain en euros calculé à partir des transactions dont
    uniquement des locaux (résidences individuelles + dépendances) ou (résidences
    collectives + dépendances) ont mutées
    """

    prix_m2_terrain_min: Optional[float] = None
    """
    Prix minimale au m2 de terrain en euros calculé à partir des transactions dont
    uniquement des locaux (résidences individuelles + dépendances) ou (résidences
    collectives + dépendances) ont mutées
    """

    prix_m2_terrain_moyen: Optional[float] = None
    """
    Prix moyen au m2 de terrain en euros calculé à partir des transactions dont
    uniquement des locaux (résidences individuelles + dépendances) ou (résidences
    collectives + dépendances) ont mutées
    """

    valeur_fonciere_max: Optional[float] = None
    """
    (dv3f) valeur foncière maximale parmi les locaux du bâtiment rapporté au mÂ²
    habitable (SHAB)[â‚¬/mÂ²]
    """

    valeur_fonciere_median: Optional[float] = None
    """
    Valeur foncière médiane en euros calculée sur l'ensemble des mutations qui ont
    eu lieu sur le batiment_groupe.
    """

    valeur_fonciere_min: Optional[float] = None
    """
    (dv3f) valeur foncière minimale parmi les locaux du bâtiment rapporté au mÂ²
    habitable (SHAB) [â‚¬/mÂ²]
    """

    valeur_fonciere_moyenne: Optional[float] = None
    """
    Valeur foncière moyenne en euros calculée sur l'ensemble des mutations qui ont
    eu lieu sur le batiment_groupe.
    """
