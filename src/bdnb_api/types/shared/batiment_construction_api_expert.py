# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BatimentConstructionAPIExpert"]


class BatimentConstructionAPIExpert(BaseModel):
    altitude_sol: Optional[str] = None
    """(ign) Altitude moynne au pied du bÃ¢timent physique [m]"""

    batiment_construction_id: Optional[str] = None
    """Identifiant unique de l'entrÃ©e batiment_construction."""

    batiment_groupe_id: Optional[str] = None
    """(bdnb) ClÃ© d'IntÃ©ropÃ©rabilitÃ© du bÃ¢timent dans la BDNB"""

    code_commune_insee: Optional[str] = None
    """Code INSEE de la commune"""

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    code_iris: Optional[str] = None
    """Code iris INSEE"""

    fictive_geom_cstr: Optional[str] = None
    """(ign) BoolÃ©en.

    Si 'True', la gÃ©omÃ©trie est fictive (et la surface au sol n'est pas rÃ©elle),
    sinon elle correspond Ã une emprise au sol rÃ©elle
    """

    geom_cstr: Optional[str] = None
    """(ign) GÃ©omÃ©trie multipolygonale de l'enceinte du bÃ¢timent (Lambert-93)"""

    hauteur: Optional[str] = None
    """(ign) Hauteur du bÃ¢timent physique [m]:"""

    rnb_id: Optional[str] = None
    """Identifiant unique de l'entrÃ©e RNB.

    Dans le cas d'un double rnb_id pour un mÃªme bÃ¢timent construction, celui
    appartenant au bÃ¢timent construction avec le plus d'emprise au sol est pris en
    compte.:
    """

    s_geom_cstr: Optional[str] = None
    """(ign) Surface au sol de la gÃ©omÃ©trie de la construction [mÂ²]"""
