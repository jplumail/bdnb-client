# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RelColonneJeuDeDonnees"]


class RelColonneJeuDeDonnees(BaseModel):
    denomination_serie: Optional[str] = None
    """DÃ©nomination du jeu de donnÃ©es"""

    millesime_jeu_de_donnees: Optional[str] = None
    """MillÃ©sime du jeu de donnÃ©es"""

    nom_colonne: Optional[str] = None
    """Nom de la colonne"""

    nom_table: Optional[str] = None
    """Nom de la table rattachÃ©e"""
