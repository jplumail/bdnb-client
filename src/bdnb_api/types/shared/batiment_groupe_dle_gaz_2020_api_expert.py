# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BatimentGroupeDleGaz2020APIExpert"]


class BatimentGroupeDleGaz2020APIExpert(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    conso_pro: Optional[float] = None
    """Consommation professionnelle [kWh/an]"""

    conso_pro_par_pdl: Optional[float] = None
    """Consommation professionnelle par point de livraison [kWh/pdl.an]"""

    conso_res: Optional[float] = None
    """Consommation rÃ©sidentielle [kWh/an]"""

    conso_res_par_pdl: Optional[float] = None
    """Consommation rÃ©sidentielle par point de livraison [kWh/pdl.an]"""

    conso_tot: Optional[float] = None
    """Consommation totale [kWh/an]"""

    conso_tot_par_pdl: Optional[float] = None
    """Consommation totale par point de livraison [kWh/pdl.an]"""

    nb_pdl_pro: Optional[float] = None
    """Nombre de points de livraisons professionel"""

    nb_pdl_res: Optional[float] = None
    """Nombre de points de livraisons rÃ©sidentiel"""

    nb_pdl_tot: Optional[float] = None
    """Nombre total de points de livraisons"""
