# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ReferentielAdministratifIris"]


class ReferentielAdministratifIris(BaseModel):
    code_commune_insee: Optional[str] = None
    """Code INSEE de la commune"""

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    code_iris: Optional[str] = None
    """Code iris INSEE"""

    geom_iris: Optional[str] = None
    """Géométrie de l'IRIS"""

    libelle_iris: Optional[str] = None
    """Libellé de l'iris"""

    type_iris: Optional[str] = None
    """Type de l'IRIS"""
