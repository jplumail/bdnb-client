# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RelBatimentGroupeQpvAPIExpert"]


class RelBatimentGroupeQpvAPIExpert(BaseModel):
    batiment_construction_id: Optional[str] = None
    """
    Identifiant unique du bÃ¢timent physique de la BDNB -> cleabs (ign) + index de
    sub-division (si construction sur plusieurs parcelles)
    """

    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Foreign Key to
    `batiment_groupe.batiment_groupe_id`.<fk table='batiment_groupe' column='batiment_groupe_id'/>
    """

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    qpv_code_qp: Optional[str] = None
    """identifiant de la table qpv"""
