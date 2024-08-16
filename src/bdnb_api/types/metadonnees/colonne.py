# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Colonne"]


class Colonne(BaseModel):
    contrainte_acces: str
    """Contrainte d'accès à la données

    Note: This is a Primary Key.<pk/>
    """

    nom_colonne: str
    """Nom de la colonne

    Note: This is a Primary Key.<pk/>
    """

    nom_table: str
    """Nom de la table rattachée

    Note: This is a Primary Key.<pk/>
    """

    api_expert: Optional[bool] = None
    """Disponible pour les abonnés de l'API Expert"""

    api_open: Optional[bool] = None
    """Disponible sans souscription"""

    colonne_gorenove_legacy: Optional[str] = None
    """Nom de la colonne dans l'ancienne API gorenove /v2/gorenove/buildings"""

    description: Optional[str] = None
    """Description de la table dans la base postgres"""

    description_table: Optional[str] = None
    """Description de la table"""

    index: Optional[bool] = None
    """la colonne est indexée dans la table"""

    libelle_metier: Optional[str] = None
    """libelle à utiliser dans les application web"""

    route: Optional[str] = None
    """Chemin dans l'API"""

    type: Optional[str] = None
    """Type sql de la colonne"""

    unite: Optional[str] = None
    """Unité de la colonne"""
