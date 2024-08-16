# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BatimentGroupeDvfOpenRepresentatifListParams"]


class BatimentGroupeDvfOpenRepresentatifListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    date_mutation: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """(dv3f) date de la mutation"""

    id_opendata: str
    """Identifiant open data de la mutation."""

    limit: str
    """Limiting and Pagination"""

    nb_appartement_mutee_mutation: str
    """Nombre d'appartements ayant mutÃ©s lors de la mutation reprÃ©sentative."""

    nb_dependance_mutee_mutation: str
    """Nombre de dÃ©pendances ayant mutÃ©es lors de la mutation reprÃ©sentative."""

    nb_locaux_mutee_mutation: str
    """Nombre de locaux ayant mutÃ©s lors de la mutation reprÃ©sentative."""

    nb_locaux_tertiaire_mutee_mutation: str
    """Nombre de locaux tertiaires ayant mutÃ©s lors de la mutation reprÃ©sentative."""

    nb_maison_mutee_mutation: str
    """Nombre de maisons ayant mutÃ©es lors de la mutation reprÃ©sentative."""

    nb_piece_principale: str
    """
    Nombre de piÃ¨ces principales de la rÃ©sidence individuelle ou collective ayant
    mutÃ©. Cet indicateur est disponible lorsqu'une unique rÃ©sidence individuelle
    ou collective a mutÃ©e.
    """

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    prix_m2_local: str
    """Prix au mÂ² de bÃ¢ti en euros lors de la mutation.

    Cet indicateur n'est disponible que pour des transactions dont uniquement les
    locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences collectives +
    dÃ©pendances) ont mutÃ©es [â‚¬]
    """

    prix_m2_terrain: str
    """Prix au mÂ² du terrain en euros lors de la mutation.

    Cet indicateur n'est disponible que pour des transactions dont uniquement les
    locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences collectives +
    dÃ©pendances) ont mutÃ©es [â‚¬]
    """

    select: str
    """Filtering Columns"""

    surface_bati_mutee_dependance: str
    """
    Surface de bÃ¢ti associÃ©e Ã des dÃ©pendances ayant mutÃ©es lors de la mutation
    reprÃ©sentative [mÂ²].
    """

    surface_bati_mutee_residencielle_collective: str
    """
    Surface de bÃ¢ti associÃ©e Ã des rÃ©sidences collectives ayant mutÃ©es lors de
    la mutation reprÃ©sentative [mÂ²].
    """

    surface_bati_mutee_residencielle_individuelle: str
    """
    Surface de bÃ¢ti associÃ©e Ã des rÃ©sidences individuelles ayant mutÃ©es lors de
    la mutation reprÃ©sentative [mÂ²].
    """

    surface_bati_mutee_tertiaire: str
    """
    Surface de bÃ¢ti associÃ©e Ã du tertiaire ayant mutÃ©es lors de la mutation
    reprÃ©sentative [mÂ²].
    """

    surface_terrain_mutee: str
    """Surface de terrain ayant mutÃ© lors de la mutation reprÃ©sentative [mÂ²]."""

    valeur_fonciere: str
    """Valeur fonciÃ¨re en euros de la mutation reprÃ©sentative. [â‚¬]"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
