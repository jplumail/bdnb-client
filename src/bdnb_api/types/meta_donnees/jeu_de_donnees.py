# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["JeuDeDonnees"]


class JeuDeDonnees(BaseModel):
    contrainte_acces: Optional[str] = None
    """Dénomination de la contrainte d'accès associée

    Note: This is a Foreign Key to
    `contrainte_acces.contrainte_acces`.<fk table='contrainte_acces' column='contrainte_acces'/>
    """

    couverture_spatiale: Optional[str] = None
    """Couverture spatiale du jeu de données"""

    couverture_temporelle: Optional[str] = None
    """Couverture temporelle du jeu de données"""

    date_publication: Optional[str] = None
    """Date de publication du jeu de données"""

    denomination_serie: Optional[str] = None
    """Dénomination du jeu de données"""

    description: Optional[str] = None
    """Description du jeu de données"""

    millesime_jeu_de_donnees: Optional[str] = None
    """Millésime du jeu de données"""
