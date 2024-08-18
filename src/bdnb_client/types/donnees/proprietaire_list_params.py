# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ProprietaireListParams"]


class ProprietaireListParams(TypedDict, total=False):
    code_departement_insee: str
    """Code département INSEE"""

    code_postal: str
    """Code postal"""

    dans_majic_pm: str
    """(majic_pm) Ce propriétaire possède des bâtiments déclarés dans majic_pm"""

    denomination: str
    """Dénomination du propriétaire (FF)"""

    forme_juridique: str
    """Forme juridique du propriétaire (FF)"""

    libelle_commune: str
    """Libellé de la commune"""

    limit: str
    """Limiting and Pagination"""

    nb_locaux_open: str
    """(majic_pm) nombre de locaux déclarés dans majic_pm"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    personne_id: str
    """
    Concaténation de code département et du numéro de personne Majic3 (FF) (appelé
    aussi NUMà‰RO PERSONNE PRESENT DANS Lâ€™APPLICATION MAJIC dans les fichiers des
    locaux des personnes morales)
    """

    select: str
    """Filtering Columns"""

    siren: str
    """Numéro de SIREN de la personne morale (FF)"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
