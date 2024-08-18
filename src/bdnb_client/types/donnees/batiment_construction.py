# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BatimentConstruction"]


class BatimentConstruction(BaseModel):
    altitude_sol: Optional[str] = None
    """(ign) Altitude moynne au pied du bâtiment physique [m]"""

    batiment_construction_id: Optional[str] = None
    """Identifiant unique de l'entrée batiment_construction."""

    batiment_groupe_id: Optional[str] = None
    """(bdnb) Clé d'Intéropérabilité du bâtiment dans la BDNB"""

    code_commune_insee: Optional[str] = None
    """Code INSEE de la commune"""

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    code_iris: Optional[str] = None
    """Code iris INSEE"""

    fictive_geom_cstr: Optional[str] = None
    """(ign) Booléen.

    Si 'True', la géométrie est fictive (et la surface au sol n'est pas réelle),
    sinon elle correspond à une emprise au sol réelle
    """

    geom_cstr: Optional[str] = None
    """(ign) Géométrie multipolygonale de l'enceinte du bâtiment (Lambert-93)"""

    hauteur: Optional[str] = None
    """(ign) Hauteur du bâtiment physique [m]:"""

    rnb_id: Optional[str] = None
    """Identifiant unique de l'entrée RNB.

    Dans le cas d'un double rnb_id pour un màªme bâtiment construction, celui
    appartenant au bâtiment construction avec le plus d'emprise au sol est pris en
    compte.:
    """

    s_geom_cstr: Optional[str] = None
    """(ign) Surface au sol de la géométrie de la construction [mÂ²]"""
