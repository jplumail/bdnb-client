# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AdresseAPIExpert"]


class AdresseAPIExpert(BaseModel):
    cle_interop_adr: Optional[str] = None
    """ClÃ© d'interopÃ©rabilitÃ© de l'adresse postale

    Note: This is a Primary Key.<pk/>
    """

    code_commune_insee: Optional[str] = None
    """Code INSEE de la commune"""

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    code_postal: Optional[str] = None
    """Code postal"""

    geom_adresse: Optional[str] = None
    """GÃ©omÃ©trie de l'adresse (Lambert-93)"""

    libelle_adresse: Optional[str] = None
    """LibellÃ© complet de l'adresse"""

    libelle_commune: Optional[str] = None
    """LibellÃ© de la commune"""

    nom_voie: Optional[str] = None
    """Nom de la voie"""

    numero: Optional[int] = None
    """NumÃ©ro de l'adresse"""

    rep: Optional[str] = None
    """Indice de rÃ©pÃ©tition du numÃ©ro de l'adresse"""

    source: Optional[str] = None
    """TODO"""

    type_voie: Optional[str] = None
    """Type de voie"""
