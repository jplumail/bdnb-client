# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .batiment_groupe_indicateur_reseau_chaud_froid_api_expert import BatimentGroupeIndicateurReseauChaudFroidAPIExpert

__all__ = ["BatimentGroupeIndicateurReseauChaudFroidListResponse"]

BatimentGroupeIndicateurReseauChaudFroidListResponse: TypeAlias = List[
    BatimentGroupeIndicateurReseauChaudFroidAPIExpert
]
