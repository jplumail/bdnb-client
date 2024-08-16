# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BatimentGroupeWallDictListParams"]


class BatimentGroupeWallDictListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    limit: str
    """Limiting and Pagination"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    wall_dict: str
    """
    liste de toutes les parois extÃ©rieures constitutives d'un bÃ¢timent (murs,
    planchers haut/bas). Collection de dictionnaires avec les clÃ©s suivantes

    - z0 : altitude au pied de la construction
    - azimuth : orientation de la paroi. (0 -> Sud)
    - hauteur : hauteur de la face (0 pour les parois horizontales)
    - inclination : 90-> vertical. 0 -> orientÃ© vers le bas (sol). 180: orientÃ©
      vers le haut (plancher haut)
    - cat_adj : Type d'adjacence de la paroi. "adjacent" : touche une autre paroi
      (mur mitoyen). "non_adjacent" : en contact avec l'ambiance extÃ©rieure
    - wall_type: floor | roof | vertical
    - wall_id : identifiant de la paroie
    - area: surface de la paroie
    - altitude : TODO
    - perimeter : pÃ©rimÃ¨tre de la face
    - shading_mask_36 (ARRAY): "Masque solaire : Elevation de l'occultation par
      tranche de 10Âº Ã partir de l'azimuth 0 (Sud)"
    """

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
