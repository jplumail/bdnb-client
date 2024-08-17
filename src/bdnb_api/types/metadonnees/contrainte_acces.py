# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ContrainteAcces"]


class ContrainteAcces(BaseModel):
    contrainte_acces: str
    """Dénomination de la contrainte d'accès

    Note: This is a Primary Key.<pk/>
    """

    description: Optional[str] = None
    """Description de la série de données"""
