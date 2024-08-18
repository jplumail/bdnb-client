# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["BatimentGroupeWallDict"]


class BatimentGroupeWallDict(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB

    Note: This is a Foreign Key to
    `batiment_groupe.batiment_groupe_id`.<fk table='batiment_groupe' column='batiment_groupe_id'/>
    """

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    wall_dict: Optional[str] = None
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
