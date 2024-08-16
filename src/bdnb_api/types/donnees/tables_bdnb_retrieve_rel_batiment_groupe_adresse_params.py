# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TablesBdnbRetrieveRelBatimentGroupeAdresseParams"]


class TablesBdnbRetrieveRelBatimentGroupeAdresseParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    classe: str
    """Classe de mÃ©thodologie de croisement Ã l'adresse (Fichiers_fonciers, Cadastre)"""

    cle_interop_adr: str
    """ClÃ© d'interopÃ©rabilitÃ© de l'adresse postale"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    geom_bat_adresse: str
    """
    GÃ©olocalisant du trait reliant le point adresse Ã la gÃ©omÃ©trie du bÃ¢timent
    groupe (Lambert-93, SRID=2154)
    """

    lien_valide: str
    """
    [DEPRECIEE] (bdnb) un couple (batiment_groupe ; adresse) est considÃ©rÃ© comme
    valide si l'adresse est une adresse ban et que le batiment_groupe est associÃ© Ã
    des fichiers fonciers
    """

    limit: str
    """Limiting and Pagination"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    origine: str
    """Origine de l'entrÃ©e bÃ¢timent.

    Elle provient soit des donnÃ©es fonciÃ¨res (Fichiers Fonciers), soit d'un
    croisement gÃ©ospatial entre le Cadastre, la BDTopo et des bases de donnÃ©es
    mÃ©tiers (ex: BPE ou MÃ©rimÃ©e)
    """

    select: str
    """Filtering Columns"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
