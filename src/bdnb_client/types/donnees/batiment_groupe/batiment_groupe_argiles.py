# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["BatimentGroupeArgiles"]


class BatimentGroupeArgiles(BaseModel):
    alea: Optional[str] = None
    """(argiles) Aléa du risque argiles"""

    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""
