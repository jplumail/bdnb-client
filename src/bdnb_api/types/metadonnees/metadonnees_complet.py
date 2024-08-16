# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MetadonneesComplet"]


class MetadonneesComplet(BaseModel):
    api_expert: Optional[bool] = None
    """Disponible pour les abonnÃ©s de l'API Expert"""

    api_open: Optional[bool] = None
    """Disponible sans souscription"""

    colonne_gorenove_legacy: Optional[str] = None
    """Nom de la colonne dans l'ancienne API gorenove /v2/gorenove/buildings"""

    contrainte_acces: Optional[str] = None
    """Contrainte d'accÃ¨s de la colonne"""

    contrainte_acces_table: Optional[str] = None
    """Contrainte d'accÃ¨s de la table"""

    couverture_spatiale: Optional[str] = None
    """Couverture spatiale du jeu de donnÃ©es"""

    couverture_temporelle: Optional[str] = None
    """Couverture temporelle du jeu de donnÃ©es"""

    date_publication: Optional[str] = None
    """Date de publication du jeu de donnÃ©es"""

    denomination_serie: Optional[str] = None
    """DÃ©nomination du jeu de donnÃ©es"""

    description: Optional[str] = None
    """Description de la table"""

    description_jeu_de_donnees: Optional[str] = None
    """Description du jeu de donnÃ©es"""

    description_table: Optional[str] = None

    index: Optional[bool] = None
    """la colonne est indexÃ©e dans la table"""

    libelle_metier: Optional[str] = None
    """libelle Ã utiliser dans les applications web"""

    millesime_jeu_de_donnees: Optional[str] = None
    """MillÃ©sime du jeu de donnÃ©es"""

    nom_colonne: Optional[str] = None
    """Nom de la colonne"""

    nom_table: Optional[str] = None
    """Nom de la table rattachÃ©e"""

    route: Optional[str] = None

    row_number: Optional[int] = None

    type: Optional[str] = None
    """Type de la colonne"""

    unite: Optional[str] = None
    """UnitÃ© de la colonne"""
