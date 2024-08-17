# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Table"]


class Table(BaseModel):
    nom_table: str
    """Nom de la table"""

    description: Optional[str] = None
    """Commentaire de la table"""

    external_pk: Optional[str] = None

    quality_elements: Optional[str] = None
