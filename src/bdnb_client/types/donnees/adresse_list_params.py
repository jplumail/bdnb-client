# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AdresseListParams"]


class AdresseListParams(TypedDict, total=False):
    cle_interop_adr: str
    """Clé d'interopérabilité de l'adresse postale"""

    code_commune_insee: str
    """Code INSEE de la commune"""

    code_departement_insee: str
    """Code département INSEE"""

    code_postal: str
    """Code postal"""

    geom_adresse: str
    """Géométrie de l'adresse (Lambert-93)"""

    libelle_adresse: str
    """Libellé complet de l'adresse"""

    libelle_commune: str
    """Libellé de la commune"""

    limit: str
    """Limiting and Pagination"""

    nom_voie: str
    """Nom de la voie"""

    numero: str
    """Numéro de l'adresse"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    rep: str
    """Indice de répétition du numéro de l'adresse"""

    select: str
    """Filtering Columns"""

    source: str
    """TODO"""

    type_voie: str
    """Type de voie"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
