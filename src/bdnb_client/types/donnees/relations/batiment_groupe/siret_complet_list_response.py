# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .rel_batiment_groupe_siret_complet import RelBatimentGroupeSiretComplet

__all__ = ["SiretCompletListResponse"]

SiretCompletListResponse: TypeAlias = List[RelBatimentGroupeSiretComplet]
