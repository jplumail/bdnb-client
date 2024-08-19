# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .batiment_groupe_radon import BatimentGroupeRadon

__all__ = ["RadonListResponse"]

RadonListResponse: TypeAlias = List[BatimentGroupeRadon]
