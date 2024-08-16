# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BatimentGroupeFfoBatAPIExpert"]


class BatimentGroupeFfoBatAPIExpert(BaseModel):
    annee_construction: Optional[int] = None
    """AnnÃ©e de construction du bÃ¢timent"""

    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    mat_mur_txt: Optional[str] = None
    """(ffo) MatÃ©riaux principal des murs extÃ©rieurs"""

    mat_toit_txt: Optional[str] = None
    """(ffo) MatÃ©riau principal des toitures"""

    nb_log: Optional[int] = None
    """(rnc) Nombre de logements"""

    nb_niveau: Optional[int] = None
    """(ffo) Nombre de niveau du bÃ¢timent (ex: RDC = 1, R+1 = 2, etc..)"""

    usage_niveau_1_txt: Optional[str] = None
    """indicateurs d'usage simplifiÃ© du bÃ¢timent (verbose)"""
