# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ReferentielAdministratifDepartementAPIExpert"]


class ReferentielAdministratifDepartementAPIExpert(BaseModel):
    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    code_region_insee: Optional[str] = None
    """Code rÃ©gion INSEE"""

    geom_departement: Optional[str] = None
    """GÃ©omÃ©trie du dÃ©partement"""

    libelle_departement: Optional[str] = None
    """LibellÃ© dÃ©partement INSEE"""
