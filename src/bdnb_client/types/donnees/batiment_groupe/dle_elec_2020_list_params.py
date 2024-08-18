# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DleElec2020ListParams"]


class DleElec2020ListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    code_departement_insee: str
    """Code département INSEE"""

    conso_pro: str
    """Consommation professionnelle [kWh/an]"""

    conso_pro_par_pdl: str
    """Consommation professionnelle par point de livraison [kWh/pdl.an]"""

    conso_res: str
    """Consommation résidentielle [kWh/an]"""

    conso_res_par_pdl: str
    """Consommation résidentielle par point de livraison [kWh/pdl.an]"""

    conso_tot: str
    """Consommation totale [kWh/an]"""

    conso_tot_par_pdl: str
    """Consommation totale par point de livraison [kWh/pdl.an]"""

    limit: str
    """Limiting and Pagination"""

    nb_pdl_pro: str
    """Nombre de points de livraisons professionel"""

    nb_pdl_res: str
    """Nombre de points de livraisons résidentiel"""

    nb_pdl_tot: str
    """Nombre total de points de livraisons"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
