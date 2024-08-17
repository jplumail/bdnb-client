# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ReferentielAdministratifDepartementAPIExpert"]


class ReferentielAdministratifDepartementAPIExpert(BaseModel):
    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    code_region_insee: Optional[str] = None
    """Code région INSEE"""

    geom_departement: Optional[str] = None
    """Géométrie du département"""

    libelle_departement: Optional[str] = None
    """Libellé département INSEE"""
