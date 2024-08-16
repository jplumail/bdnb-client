# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["BatimentGroupeBpeAPIExpert"]


class BatimentGroupeBpeAPIExpert(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    l_type_equipement: Optional[List[str]] = None
    """(bpe) Liste des Ã©quipements recensÃ©s par la base BPE"""
