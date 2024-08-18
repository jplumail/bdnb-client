# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DvfOpenRepresentatifListParams"]


class DvfOpenRepresentatifListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    code_departement_insee: str
    """Code département INSEE"""

    date_mutation: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """(dv3f) date de la mutation"""

    id_opendata: str
    """Identifiant open data de la mutation."""

    limit: str
    """Limiting and Pagination"""

    nb_appartement_mutee_mutation: str
    """Nombre d'appartements ayant mutés lors de la mutation représentative."""

    nb_dependance_mutee_mutation: str
    """Nombre de dépendances ayant mutées lors de la mutation représentative."""

    nb_locaux_mutee_mutation: str
    """Nombre de locaux ayant mutés lors de la mutation représentative."""

    nb_locaux_tertiaire_mutee_mutation: str
    """Nombre de locaux tertiaires ayant mutés lors de la mutation représentative."""

    nb_maison_mutee_mutation: str
    """Nombre de maisons ayant mutées lors de la mutation représentative."""

    nb_piece_principale: str
    """
    Nombre de pièces principales de la résidence individuelle ou collective ayant
    muté. Cet indicateur est disponible lorsqu'une unique résidence individuelle ou
    collective a mutée.
    """

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    prix_m2_local: str
    """Prix au mÂ² de bâti en euros lors de la mutation.

    Cet indicateur n'est disponible que pour des transactions dont uniquement les
    locaux (résidences individuelles + dépendances) ou (résidences collectives +
    dépendances) ont mutées [â‚¬]
    """

    prix_m2_terrain: str
    """Prix au mÂ² du terrain en euros lors de la mutation.

    Cet indicateur n'est disponible que pour des transactions dont uniquement les
    locaux (résidences individuelles + dépendances) ou (résidences collectives +
    dépendances) ont mutées [â‚¬]
    """

    select: str
    """Filtering Columns"""

    surface_bati_mutee_dependance: str
    """
    Surface de bâti associée à des dépendances ayant mutées lors de la mutation
    représentative [mÂ²].
    """

    surface_bati_mutee_residencielle_collective: str
    """
    Surface de bâti associée à des résidences collectives ayant mutées lors de la
    mutation représentative [mÂ²].
    """

    surface_bati_mutee_residencielle_individuelle: str
    """
    Surface de bâti associée à des résidences individuelles ayant mutées lors de la
    mutation représentative [mÂ²].
    """

    surface_bati_mutee_tertiaire: str
    """
    Surface de bâti associée à du tertiaire ayant mutées lors de la mutation
    représentative [mÂ²].
    """

    surface_terrain_mutee: str
    """Surface de terrain ayant muté lors de la mutation représentative [mÂ²]."""

    valeur_fonciere: str
    """Valeur foncière en euros de la mutation représentative. [â‚¬]"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
