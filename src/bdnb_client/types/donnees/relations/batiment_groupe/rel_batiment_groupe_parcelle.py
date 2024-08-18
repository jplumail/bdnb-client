# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["RelBatimentGroupeParcelle"]


class RelBatimentGroupeParcelle(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB

    Note: This is a Foreign Key to
    `batiment_groupe.batiment_groupe_id`.<fk table='batiment_groupe' column='batiment_groupe_id'/>
    """

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    parcelle_id: Optional[str] = None
    """
    (ffo:idpar) Identifiant de parcelle (Concaténation de ccodep, ccocom, ccopre,
    ccosec, dnupla)
    """

    parcelle_principale: Optional[bool] = None
    """
    Booléen renvoyant 'vrai' si la parcelle cadastrale est la plus grande
    intersectant le groupe de bâtiment
    """
