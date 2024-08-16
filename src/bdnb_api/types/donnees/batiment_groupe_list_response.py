# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .tables_bdnb.batiment_groupe_api_expert import BatimentGroupeAPIExpert

__all__ = ["BatimentGroupeListResponse"]

BatimentGroupeListResponse: TypeAlias = List[BatimentGroupeAPIExpert]
