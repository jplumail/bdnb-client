# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["JeuDeDonnees"]


class JeuDeDonnees(BaseModel):
    contrainte_acces: Optional[str] = None
    """DÃ©nomination de la contrainte d'accÃ¨s associÃ©e

    Note: This is a Foreign Key to
    `contrainte_acces.contrainte_acces`.<fk table='contrainte_acces' column='contrainte_acces'/>
    """

    couverture_spatiale: Optional[str] = None
    """Couverture spatiale du jeu de donnÃ©es"""

    couverture_temporelle: Optional[str] = None
    """Couverture temporelle du jeu de donnÃ©es"""

    date_publication: Optional[str] = None
    """Date de publication du jeu de donnÃ©es"""

    denomination_serie: Optional[str] = None
    """DÃ©nomination du jeu de donnÃ©es"""

    description: Optional[str] = None
    """Description du jeu de donnÃ©es"""

    millesime_jeu_de_donnees: Optional[str] = None
    """MillÃ©sime du jeu de donnÃ©es"""
