# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["ReferentielAdministratifRegionListResponse", "ReferentielAdministratifRegionListResponseItem"]


class ReferentielAdministratifRegionListResponseItem(BaseModel):
    code_region_insee: Optional[str] = None
    """Code rÃ©gion INSEE"""

    geom_region: Optional[str] = None
    """GÃ©omÃ©trie de la rÃ©gion"""

    libelle_region: Optional[str] = None
    """LibellÃ© de la rÃ©gion"""


ReferentielAdministratifRegionListResponse: TypeAlias = List[ReferentielAdministratifRegionListResponseItem]
