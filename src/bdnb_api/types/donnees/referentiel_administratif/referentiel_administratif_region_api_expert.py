# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ReferentielAdministratifRegionAPIExpert"]


class ReferentielAdministratifRegionAPIExpert(BaseModel):
    code_region_insee: Optional[str] = None
    """Code région INSEE"""

    geom_region: Optional[str] = None
    """Géométrie de la région"""

    libelle_region: Optional[str] = None
    """Libellé de la région"""
