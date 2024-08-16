# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AutocompletionEntitesTexteAPIExpert"]


class AutocompletionEntitesTexteAPIExpert(BaseModel):
    code: Optional[str] = None
    """code de l'entitÃ©"""

    geom: Optional[str] = None
    """geometrie de l'entitÃ© s'il y en a une"""

    nom: Optional[str] = None
    """nom d'entitÃ©"""

    nom_unaccent: Optional[str] = None
    """nom d'entitÃ© sans accent"""

    origine_code: Optional[str] = None
    """nom de la table de la colonne d'origine du code"""

    origine_nom: Optional[str] = None
    """nom de la table de la colonne d'origine du nom"""

    type_entite: Optional[str] = None
    """type de l'entitÃ©"""
