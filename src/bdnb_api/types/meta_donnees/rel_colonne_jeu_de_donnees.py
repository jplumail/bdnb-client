# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RelColonneJeuDeDonnees"]


class RelColonneJeuDeDonnees(BaseModel):
    denomination_serie: Optional[str] = None
    """Dénomination du jeu de données"""

    millesime_jeu_de_donnees: Optional[str] = None
    """Millésime du jeu de données"""

    nom_colonne: Optional[str] = None
    """Nom de la colonne"""

    nom_table: Optional[str] = None
    """Nom de la table rattachée"""
