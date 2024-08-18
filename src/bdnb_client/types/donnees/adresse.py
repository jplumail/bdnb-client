# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Adresse"]


class Adresse(BaseModel):
    cle_interop_adr: Optional[str] = None
    """Clé d'interopérabilité de l'adresse postale

    Note: This is a Primary Key.<pk/>
    """

    code_commune_insee: Optional[str] = None
    """Code INSEE de la commune"""

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    code_postal: Optional[str] = None
    """Code postal"""

    geom_adresse: Optional[str] = None
    """Géométrie de l'adresse (Lambert-93)"""

    libelle_adresse: Optional[str] = None
    """Libellé complet de l'adresse"""

    libelle_commune: Optional[str] = None
    """Libellé de la commune"""

    nom_voie: Optional[str] = None
    """Nom de la voie"""

    numero: Optional[int] = None
    """Numéro de l'adresse"""

    rep: Optional[str] = None
    """Indice de répétition du numéro de l'adresse"""

    source: Optional[str] = None
    """TODO"""

    type_voie: Optional[str] = None
    """Type de voie"""
