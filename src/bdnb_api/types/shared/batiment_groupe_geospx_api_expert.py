# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BatimentGroupeGeospxAPIExpert"]


class BatimentGroupeGeospxAPIExpert(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    croisement_geospx_reussi: Optional[bool] = None
    """
    le croisement gÃ©ospatial entre la BDTOPO et les fichiers fonciers est
    considÃ©rÃ©e comme rÃ©ussi
    """

    fiabilite_adresse: Optional[str] = None
    """
    FiabilitÃ© des adresses du bÃ¢timent : "vrai" si les Fichiers Fonciers et BDTOpo
    partagent au moins une mÃªme adresse BAN
    """

    fiabilite_emprise_sol: Optional[str] = None
    """FiabilitÃ© de l'emprise au sol du bÃ¢timent"""

    fiabilite_hauteur: Optional[str] = None
    """FiabilitÃ© de la hauteur du bÃ¢timent"""
