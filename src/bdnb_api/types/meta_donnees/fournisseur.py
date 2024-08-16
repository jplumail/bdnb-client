# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Fournisseur"]


class Fournisseur(BaseModel):
    denomination_fournisseur: str
    """Dénomination du fournisseur de données

    Note: This is a Primary Key.<pk/>
    """

    acronyme: Optional[str] = None
    """Acronyme du fournisseur de données"""

    description: Optional[str] = None
    """Description du fournisseur de données"""
