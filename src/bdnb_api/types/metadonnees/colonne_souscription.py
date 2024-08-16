# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ColonneSouscription"]


class ColonneSouscription(BaseModel):
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

    nom_table_implementation: str
    """Nom de la table d'implémentation

    Note: This is a Primary Key.<pk/>
    """

    souscription: str
    """Note: This is a Primary Key.<pk/>"""

    description: Optional[str] = None
    """Description de la table dans la base postgres"""

    description_table: Optional[str] = None
    """Description de la table"""

    index: Optional[bool] = None
    """la colonne est indexée dans la table"""

    route: Optional[str] = None
    """Chemin dans l'API"""

    type: Optional[str] = None
    """Type sql de la colonne"""

    unite: Optional[str] = None
    """Unité de la colonne"""
