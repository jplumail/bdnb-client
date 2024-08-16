# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .batiment_groupe_radon_api_expert import BatimentGroupeRadonAPIExpert

__all__ = ["BatimentGroupeRadonListResponse"]

BatimentGroupeRadonListResponse: TypeAlias = List[BatimentGroupeRadonAPIExpert]
