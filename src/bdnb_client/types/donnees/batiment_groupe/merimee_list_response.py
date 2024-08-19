# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .batiment_groupe_merimee import BatimentGroupeMerimee

__all__ = ["MerimeeListResponse"]

MerimeeListResponse: TypeAlias = List[BatimentGroupeMerimee]