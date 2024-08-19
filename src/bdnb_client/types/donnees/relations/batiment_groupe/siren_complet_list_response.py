# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .rel_batiment_groupe_siren_complet import RelBatimentGroupeSirenComplet

__all__ = ["SirenCompletListResponse"]

SirenCompletListResponse: TypeAlias = List[RelBatimentGroupeSirenComplet]
