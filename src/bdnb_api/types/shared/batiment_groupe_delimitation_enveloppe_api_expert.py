# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BatimentGroupeDelimitationEnveloppeAPIExpert"]


class BatimentGroupeDelimitationEnveloppeAPIExpert(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    delimitation_enveloppe_dict: Optional[str] = None
    """
    Liste de toutes les parois extÃ©rieures constitutives d''un bÃ¢timent (murs,
    planchers haut/bas).
    """
