# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["BatimentGroupeDelimitationEnveloppe"]


class BatimentGroupeDelimitationEnveloppe(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    delimitation_enveloppe_dict: Optional[str] = None
    """
    Liste de toutes les parois extérieures constitutives d''un bâtiment (murs,
    planchers haut/bas).
    """
