# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Proprietaire"]


class Proprietaire(BaseModel):
    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    code_postal: Optional[str] = None
    """Code postal"""

    dans_majic_pm: Optional[bool] = None
    """(majic_pm) Ce propriétaire possède des bâtiments déclarés dans majic_pm"""

    denomination: Optional[str] = None
    """Dénomination du propriétaire (FF)"""

    forme_juridique: Optional[str] = None
    """Forme juridique du propriétaire (FF)"""

    libelle_commune: Optional[str] = None
    """Libellé de la commune"""

    nb_locaux_open: Optional[int] = None
    """(majic_pm) nombre de locaux déclarés dans majic_pm"""

    personne_id: Optional[str] = None
    """
    Concaténation de code département et du numéro de personne Majic3 (FF) (appelé
    aussi NUMà‰RO PERSONNE PRESENT DANS Lâ€™APPLICATION MAJIC dans les fichiers des
    locaux des personnes morales)

    Note: This is a Primary Key.<pk/>
    """

    siren: Optional[str] = None
    """Numéro de SIREN de la personne morale (FF)"""
