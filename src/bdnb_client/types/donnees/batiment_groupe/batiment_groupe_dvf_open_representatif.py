# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ...._models import BaseModel

__all__ = ["BatimentGroupeDvfOpenRepresentatif"]


class BatimentGroupeDvfOpenRepresentatif(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    date_mutation: Optional[date] = None
    """(dv3f) date de la mutation"""

    id_opendata: Optional[str] = None
    """Identifiant open data de la mutation."""

    nb_appartement_mutee_mutation: Optional[int] = None
    """Nombre d'appartements ayant mutés lors de la mutation représentative."""

    nb_dependance_mutee_mutation: Optional[int] = None
    """Nombre de dépendances ayant mutées lors de la mutation représentative."""

    nb_locaux_mutee_mutation: Optional[int] = None
    """Nombre de locaux ayant mutés lors de la mutation représentative."""

    nb_locaux_tertiaire_mutee_mutation: Optional[int] = None
    """Nombre de locaux tertiaires ayant mutés lors de la mutation représentative."""

    nb_maison_mutee_mutation: Optional[int] = None
    """Nombre de maisons ayant mutées lors de la mutation représentative."""

    nb_piece_principale: Optional[int] = None
    """
    Nombre de pièces principales de la résidence individuelle ou collective ayant
    muté. Cet indicateur est disponible lorsqu'une unique résidence individuelle ou
    collective a mutée.
    """

    prix_m2_local: Optional[float] = None
    """Prix au mÂ² de bâti en euros lors de la mutation.

    Cet indicateur n'est disponible que pour des transactions dont uniquement les
    locaux (résidences individuelles + dépendances) ou (résidences collectives +
    dépendances) ont mutées [â‚¬]
    """

    prix_m2_terrain: Optional[float] = None
    """Prix au mÂ² du terrain en euros lors de la mutation.

    Cet indicateur n'est disponible que pour des transactions dont uniquement les
    locaux (résidences individuelles + dépendances) ou (résidences collectives +
    dépendances) ont mutées [â‚¬]
    """

    surface_bati_mutee_dependance: Optional[float] = None
    """
    Surface de bâti associée à des dépendances ayant mutées lors de la mutation
    représentative [mÂ²].
    """

    surface_bati_mutee_residencielle_collective: Optional[float] = None
    """
    Surface de bâti associée à des résidences collectives ayant mutées lors de la
    mutation représentative [mÂ²].
    """

    surface_bati_mutee_residencielle_individuelle: Optional[float] = None
    """
    Surface de bâti associée à des résidences individuelles ayant mutées lors de la
    mutation représentative [mÂ²].
    """

    surface_bati_mutee_tertiaire: Optional[float] = None
    """
    Surface de bâti associée à du tertiaire ayant mutées lors de la mutation
    représentative [mÂ²].
    """

    surface_terrain_mutee: Optional[float] = None
    """Surface de terrain ayant muté lors de la mutation représentative [mÂ²]."""

    valeur_fonciere: Optional[float] = None
    """Valeur foncière en euros de la mutation représentative. [â‚¬]"""
