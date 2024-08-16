# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RelBatimentGroupeProprietaireSirenOpenAPIExpert"]


class RelBatimentGroupeProprietaireSirenOpenAPIExpert(BaseModel):
    bat_prop_denomination_proprietaire: Optional[str] = None
    """TODO"""

    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Foreign Key to
    `batiment_groupe.batiment_groupe_id`.<fk table='batiment_groupe' column='batiment_groupe_id'/>
    """

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    dans_majic_pm: Optional[bool] = None
    """(majic_pm) Ce propriÃ©taire possÃ¨de des bÃ¢timents dÃ©clarÃ©s dans majic_pm"""

    is_bailleur: Optional[bool] = None
    """Vrai si le propriÃ©taire est un bailleur social"""

    nb_locaux_open: Optional[int] = None
    """(majic_pm) nombre de locaux dÃ©clarÃ©s dans majic_pm"""

    siren: Optional[str] = None
    """NumÃ©ro de SIREN de la personne morale (FF)"""
