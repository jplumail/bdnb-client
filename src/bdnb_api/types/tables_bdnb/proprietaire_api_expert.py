# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ProprietaireAPIExpert"]


class ProprietaireAPIExpert(BaseModel):
    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    code_postal: Optional[str] = None
    """Code postal"""

    dans_majic_pm: Optional[bool] = None
    """(majic_pm) Ce propriÃ©taire possÃ¨de des bÃ¢timents dÃ©clarÃ©s dans majic_pm"""

    denomination: Optional[str] = None
    """DÃ©nomination du propriÃ©taire (FF)"""

    forme_juridique: Optional[str] = None
    """Forme juridique du propriÃ©taire (FF)"""

    libelle_commune: Optional[str] = None
    """LibellÃ© de la commune"""

    nb_locaux_open: Optional[int] = None
    """(majic_pm) nombre de locaux dÃ©clarÃ©s dans majic_pm"""

    personne_id: Optional[str] = None
    """
    ConcatÃ©nation de code dÃ©partement et du numÃ©ro de personne Majic3 (FF)
    (appelÃ© aussi NUMÃ‰RO PERSONNE PRESENT DANS Lâ€™APPLICATION MAJIC dans les
    fichiers des locaux des personnes morales)

    Note: This is a Primary Key.<pk/>
    """

    siren: Optional[str] = None
    """NumÃ©ro de SIREN de la personne morale (FF)"""
