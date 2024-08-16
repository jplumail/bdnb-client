# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ReferentielAdministratifEpciAPIExpert"]


class ReferentielAdministratifEpciAPIExpert(BaseModel):
    code_epci_insee: Optional[str] = None
    """Code de l'EPCI"""

    geom_epci: Optional[str] = None
    """Géométrie de l'EPCI"""

    libelle_epci: Optional[str] = None
    """Libellé de l'EPCI"""

    nature_epci: Optional[str] = None
    """Type d'EPCI"""
