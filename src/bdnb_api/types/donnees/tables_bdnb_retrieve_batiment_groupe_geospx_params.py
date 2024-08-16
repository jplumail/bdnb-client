# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TablesBdnbRetrieveBatimentGroupeGeospxParams"]


class TablesBdnbRetrieveBatimentGroupeGeospxParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    croisement_geospx_reussi: str
    """
    le croisement gÃ©ospatial entre la BDTOPO et les fichiers fonciers est
    considÃ©rÃ©e comme rÃ©ussi
    """

    fiabilite_adresse: str
    """
    FiabilitÃ© des adresses du bÃ¢timent : "vrai" si les Fichiers Fonciers et BDTOpo
    partagent au moins une mÃªme adresse BAN
    """

    fiabilite_emprise_sol: str
    """FiabilitÃ© de l'emprise au sol du bÃ¢timent"""

    fiabilite_hauteur: str
    """FiabilitÃ© de la hauteur du bÃ¢timent"""

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
