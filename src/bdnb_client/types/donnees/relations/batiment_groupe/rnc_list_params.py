# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["RncListParams"]


class RncListParams(TypedDict, total=False):
    adresse_brut: str
    """adresse brute envoyée au géocodeur"""

    adresse_geocodee: str
    """libelle de l'adresse retournée par le géocodeur"""

    batiment_groupe_id: str
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    cle_interop_adr: str
    """Clé d'interopérabilité de l'adresse postale"""

    code_departement_insee: str
    """Code département INSEE"""

    fiabilite_geocodage: str
    """fiabilité du géocodage"""

    fiabilite_globale: str
    """fiabilité du global du croisement"""

    limit: str
    """Limiting and Pagination"""

    numero_immat: str
    """identifiant de la table rnc"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    parcelle_id: str
    """
    (ffo:idpar) Identifiant de parcelle (Concaténation de ccodep, ccocom, ccopre,
    ccosec, dnupla)
    """

    select: str
    """Filtering Columns"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
