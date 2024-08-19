# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .rel_batiment_groupe_parcelle import RelBatimentGroupeParcelle

__all__ = ["ParcelleListResponse"]

ParcelleListResponse: TypeAlias = List[RelBatimentGroupeParcelle]
