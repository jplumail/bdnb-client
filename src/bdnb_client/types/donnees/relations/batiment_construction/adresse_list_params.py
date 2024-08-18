# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["AdresseListParams"]


class AdresseListParams(TypedDict, total=False):
    adresse_principale: str
    """
    Booléen précisant si l'adresse courante est l'une des adresses principales de la
    construction ou non. Une relation est taguée comme `principale` si l'adresse qui
    la compose obtient le score de fiabilité le plus important parmi toutes les
    adresses desservant une màªme construction. Il se peut, par conséquent, qu'une
    construction ait plusieurs adresses principales : toutes celles ayant le score
    de fiabilité le plus haut pour cette construction.
    """

    batiment_construction_id: str
    """
    Identifiant unique du bâtiment physique de la BDNB -> cleabs (ign) + index de
    sub-division (si construction sur plusieurs parcelles)
    """

    cle_interop_adr: str
    """Clé d'interopérabilité de l'adresse postale"""

    code_departement_insee: str
    """Code département INSEE"""

    distance_batiment_construction_adresse: str
    """Distance entre le géolocalisant adresse et la géométrie de bâtiment"""

    fiabilite: str
    """Niveau de fiabilité"""

    limit: str
    """Limiting and Pagination"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
