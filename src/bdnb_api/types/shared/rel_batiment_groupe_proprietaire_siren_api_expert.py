# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RelBatimentGroupeProprietaireSirenAPIExpert"]


class RelBatimentGroupeProprietaireSirenAPIExpert(BaseModel):
    bat_prop_denomination_proprietaire: Optional[str] = None
    """TODO"""

    dans_majic_pm: Optional[bool] = None
    """(majic_pm) Ce propriÃ©taire possÃ¨de des bÃ¢timents dÃ©clarÃ©s dans majic_pm"""

    is_bailleur: Optional[bool] = None
    """Vrai si le propriÃ©taire est un bailleur social"""

    nb_locaux_open: Optional[int] = None
    """(majic_pm) nombre de locaux dÃ©clarÃ©s dans majic_pm"""

    siren: Optional[str] = None
    """NumÃ©ro de SIREN de la personne morale (FF)"""
