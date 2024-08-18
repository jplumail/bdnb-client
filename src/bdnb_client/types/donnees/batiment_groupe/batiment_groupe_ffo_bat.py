# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["BatimentGroupeFfoBat"]


class BatimentGroupeFfoBat(BaseModel):
    annee_construction: Optional[int] = None
    """Année de construction du bâtiment"""

    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    mat_mur_txt: Optional[str] = None
    """(ffo) Matériaux principal des murs extérieurs"""

    mat_toit_txt: Optional[str] = None
    """(ffo) Matériau principal des toitures"""

    nb_log: Optional[int] = None
    """(rnc) Nombre de logements"""

    nb_niveau: Optional[int] = None
    """(ffo) Nombre de niveau du bâtiment (ex: RDC = 1, R+1 = 2, etc..)"""

    usage_niveau_1_txt: Optional[str] = None
    """indicateurs d'usage simplifié du bâtiment (verbose)"""
