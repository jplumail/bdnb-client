# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TablesBdnbRetrieveRelBatimentConstructionAdresseParams"]


class TablesBdnbRetrieveRelBatimentConstructionAdresseParams(TypedDict, total=False):
    adresse_principale: str
    """
    BoolÃ©en prÃ©cisant si l'adresse courante est l'une des adresses principales de
    la construction ou non. Une relation est taguÃ©e comme `principale` si l'adresse
    qui la compose obtient le score de fiabilitÃ© le plus important parmi toutes les
    adresses desservant une mÃªme construction. Il se peut, par consÃ©quent, qu'une
    construction ait plusieurs adresses principales : toutes celles ayant le score
    de fiabilitÃ© le plus haut pour cette construction.
    """

    batiment_construction_id: str
    """
    Identifiant unique du bÃ¢timent physique de la BDNB -> cleabs (ign) + index de
    sub-division (si construction sur plusieurs parcelles)
    """

    cle_interop_adr: str
    """ClÃ© d'interopÃ©rabilitÃ© de l'adresse postale"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    distance_batiment_construction_adresse: str
    """Distance entre le gÃ©olocalisant adresse et la gÃ©omÃ©trie de bÃ¢timent"""

    fiabilite: str
    """Niveau de fiabilitÃ©"""

    limit: str
    """Limiting and Pagination"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
