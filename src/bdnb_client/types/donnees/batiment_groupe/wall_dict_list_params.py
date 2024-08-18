# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["WallDictListParams"]


class WallDictListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    code_departement_insee: str
    """Code département INSEE"""

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
    liste de toutes les parois extérieures constitutives d'un bâtiment (murs,
    planchers haut/bas). Collection de dictionnaires avec les clés suivantes

    - z0 : altitude au pied de la construction
    - azimuth : orientation de la paroi. (0 -> Sud)
    - hauteur : hauteur de la face (0 pour les parois horizontales)
    - inclination : 90-> vertical. 0 -> orienté vers le bas (sol). 180: orienté vers
      le haut (plancher haut)
    - cat_adj : Type d'adjacence de la paroi. "adjacent" : touche une autre paroi
      (mur mitoyen). "non_adjacent" : en contact avec l'ambiance extérieure
    - wall_type: floor | roof | vertical
    - wall_id : identifiant de la paroie
    - area: surface de la paroie
    - altitude : TODO
    - perimeter : périmètre de la face
    - shading_mask_36 (ARRAY): "Masque solaire : Elevation de l'occultation par
      tranche de 10Âº à partir de l'azimuth 0 (Sud)"
    """

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
