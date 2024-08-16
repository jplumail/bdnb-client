# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ExtBatimentGroupeLBdtopoBatCleabsAPIExpert"]


class ExtBatimentGroupeLBdtopoBatCleabsAPIExpert(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    l_bdtopo_bat_cleabs: Optional[List[str]] = None
    """Liste d'identifiants de la table bÃ¢timent de la BDTOPO"""
