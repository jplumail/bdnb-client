# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ColonneListParams"]


class ColonneListParams(TypedDict, total=False):
    api_expert: str
    """Disponible pour les abonnÃ©s de l'API Expert"""

    api_open: str
    """Disponible sans souscription"""

    colonne_gorenove_legacy: str
    """Nom de la colonne dans l'ancienne API gorenove /v2/gorenove/buildings"""

    contrainte_acces: str
    """Contrainte d'accÃ¨s Ã la donnÃ©es"""

    description: str
    """Description de la table dans la base postgres"""

    description_table: str
    """Description de la table"""

    index: str
    """la colonne est indexÃ©e dans la table"""

    libelle_metier: str
    """libelle Ã utiliser dans les application web"""

    limit: str
    """Limiting and Pagination"""

    nom_colonne: str
    """Nom de la colonne"""

    nom_table: str
    """Nom de la table rattachÃ©e"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    route: str
    """Chemin dans l'API"""

    select: str
    """Filtering Columns"""

    type: str
    """Type sql de la colonne"""

    unite: str
    """UnitÃ© de la colonne"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
