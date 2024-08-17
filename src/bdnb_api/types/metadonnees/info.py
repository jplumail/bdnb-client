# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Info"]


class Info(BaseModel):
    modifiee: Optional[str] = None
    """date de modification"""

    publication_schema: Optional[str] = None
    """schema de publication"""
