# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .autocompletion_entites_texte import AutocompletionEntitesTexte

__all__ = ["AutocompletionListResponse"]

AutocompletionListResponse: TypeAlias = List[AutocompletionEntitesTexte]
