# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Colonne"]


class Colonne(BaseModel):
    contrainte_acces: str
    """Contrainte d'accÃ¨s Ã la donnÃ©es

    Note: This is a Primary Key.<pk/>
    """

    nom_colonne: str
    """Nom de la colonne

    Note: This is a Primary Key.<pk/>
    """

    nom_table: str
    """Nom de la table rattachÃ©e

    Note: This is a Primary Key.<pk/>
    """

    api_expert: Optional[bool] = None
    """Disponible pour les abonnÃ©s de l'API Expert"""

    api_open: Optional[bool] = None
    """Disponible sans souscription"""

    colonne_gorenove_legacy: Optional[str] = None
    """Nom de la colonne dans l'ancienne API gorenove /v2/gorenove/buildings"""

    description: Optional[str] = None
    """Description de la table dans la base postgres"""

    description_table: Optional[str] = None
    """Description de la table"""

    index: Optional[bool] = None
    """la colonne est indexÃ©e dans la table"""

    libelle_metier: Optional[str] = None
    """libelle Ã utiliser dans les application web"""

    route: Optional[str] = None
    """Chemin dans l'API"""

    type: Optional[str] = None
    """Type sql de la colonne"""

    unite: Optional[str] = None
    """UnitÃ© de la colonne"""
