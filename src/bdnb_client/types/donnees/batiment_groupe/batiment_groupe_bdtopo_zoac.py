# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["BatimentGroupeBdtopoZoac"]


class BatimentGroupeBdtopoZoac(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    l_nature: Optional[List[str]] = None
    """(ign) Catégorie de nature du bâtiment"""

    l_nature_detaillee: Optional[List[str]] = None
    """(ign) Catégorie détaillée de nature de l'équipement"""

    l_toponyme: Optional[List[str]] = None
    """(ign) Toponymie de l'équipement"""
