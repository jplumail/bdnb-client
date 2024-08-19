# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .rel_batiment_groupe_merimee import RelBatimentGroupeMerimee

__all__ = ["MerimeeListResponse"]

MerimeeListResponse: TypeAlias = List[RelBatimentGroupeMerimee]
