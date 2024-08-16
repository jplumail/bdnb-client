# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BatimentGroupeArgilesAPIExpert"]


class BatimentGroupeArgilesAPIExpert(BaseModel):
    alea: Optional[str] = None
    """(argiles) AlÃ©a du risque argiles"""

    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""
