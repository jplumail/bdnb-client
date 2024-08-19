# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .batiment_groupe_ffo_bat import BatimentGroupeFfoBat

__all__ = ["FfoBatListResponse"]

FfoBatListResponse: TypeAlias = List[BatimentGroupeFfoBat]