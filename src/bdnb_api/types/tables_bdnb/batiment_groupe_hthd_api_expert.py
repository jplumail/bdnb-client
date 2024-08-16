# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["BatimentGroupeHthdAPIExpert"]


class BatimentGroupeHthdAPIExpert(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    l_nom_pdl: Optional[List[str]] = None
    """(hthd) Liste des noms des points de livraisons centraux"""

    l_type_pdl: Optional[List[str]] = None
    """(hthd) Liste de type de bÃ¢timent desservis par les PDL"""

    nb_pdl: Optional[float] = None
    """(hthd) Nombre total de PDL Arcep"""
