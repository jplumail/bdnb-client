# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AdresseListParams"]


class AdresseListParams(TypedDict, total=False):
    cle_interop_adr: str
    """ClÃ© d'interopÃ©rabilitÃ© de l'adresse postale"""

    code_commune_insee: str
    """Code INSEE de la commune"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    code_postal: str
    """Code postal"""

    geom_adresse: str
    """GÃ©omÃ©trie de l'adresse (Lambert-93)"""

    libelle_adresse: str
    """LibellÃ© complet de l'adresse"""

    libelle_commune: str
    """LibellÃ© de la commune"""

    limit: str
    """Limiting and Pagination"""

    nom_voie: str
    """Nom de la voie"""

    numero: str
    """NumÃ©ro de l'adresse"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    rep: str
    """Indice de rÃ©pÃ©tition du numÃ©ro de l'adresse"""

    select: str
    """Filtering Columns"""

    source: str
    """TODO"""

    type_voie: str
    """Type de voie"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
