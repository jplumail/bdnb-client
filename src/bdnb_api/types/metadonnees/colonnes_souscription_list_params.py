# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ColonnesSouscriptionListParams"]


class ColonnesSouscriptionListParams(TypedDict, total=False):
    contrainte_acces: str
    """Contrainte d'accès à la données"""

    description: str
    """Description de la table dans la base postgres"""

    description_table: str
    """Description de la table"""

    index: str
    """la colonne est indexée dans la table"""

    limit: str
    """Limiting and Pagination"""

    nom_colonne: str
    """Nom de la colonne"""

    nom_table: str
    """Nom de la table rattachée"""

    nom_table_implementation: str
    """Nom de la table d'implémentation"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    route: str
    """Chemin dans l'API"""

    select: str
    """Filtering Columns"""

    souscription: str

    type: str
    """Type sql de la colonne"""

    unite: str
    """Unité de la colonne"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
