# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["BatimentGroupeGeospx"]


class BatimentGroupeGeospx(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    croisement_geospx_reussi: Optional[bool] = None
    """
    le croisement géospatial entre la BDTOPO et les fichiers fonciers est considérée
    comme réussi
    """

    fiabilite_adresse: Optional[str] = None
    """
    Fiabilité des adresses du bâtiment : "vrai" si les Fichiers Fonciers et BDTOpo
    partagent au moins une màªme adresse BAN
    """

    fiabilite_emprise_sol: Optional[str] = None
    """Fiabilité de l'emprise au sol du bâtiment"""

    fiabilite_hauteur: Optional[str] = None
    """Fiabilité de la hauteur du bâtiment"""
