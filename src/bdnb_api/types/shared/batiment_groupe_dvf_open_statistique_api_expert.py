# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BatimentGroupeDvfOpenStatistiqueAPIExpert"]


class BatimentGroupeDvfOpenStatistiqueAPIExpert(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    nb_appartement_mutee: Optional[int] = None
    """
    Nombre d'appartements qui ont mutÃ©s sur le batiment_groupe (sur la pÃ©riode de
    rÃ©fÃ©rence des DVF).
    """

    nb_dependance_mutee: Optional[int] = None
    """
    Nombre de dÃ©pendances qui ont mutÃ©es sur le batiment_groupe (sur la pÃ©riode
    de rÃ©fÃ©rence des DVF).
    """

    nb_locaux_mutee: Optional[int] = None
    """
    Nombre de locaux qui ont mutÃ©s sur le batiment_groupe (sur la pÃ©riode de
    rÃ©fÃ©rence des DVF).
    """

    nb_locaux_tertiaire_mutee: Optional[int] = None
    """
    Nombre de locaux tertiaires qui ont mutÃ©s sur le batiment_groupe (sur la
    pÃ©riode de rÃ©fÃ©rence des DVF).
    """

    nb_maisons_mutee: Optional[int] = None
    """
    Nombre de maisons qui ont mutÃ©es sur le batiment_groupe (sur la pÃ©riode de
    rÃ©fÃ©rence des DVF).
    """

    nb_mutation: Optional[int] = None
    """
    Nombre de mutations qui ont eu lieu sur le batiment_groupe (sur la pÃ©riode de
    rÃ©fÃ©rence des DVF).
    """

    prix_m2_local_max: Optional[float] = None
    """
    Prix maximale au m2 de bÃ¢ti en euros calculÃ© Ã partir des transactions dont
    uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
    collectives + dÃ©pendances) ont mutÃ©es
    """

    prix_m2_local_median: Optional[float] = None
    """
    Prix mÃ©dian au m2 de bÃ¢ti en euros calculÃ© Ã partir des transactions dont
    uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
    collectives + dÃ©pendances) ont mutÃ©es
    """

    prix_m2_local_min: Optional[float] = None
    """
    Prix minimale au m2 de bÃ¢ti en euros calculÃ© Ã partir des transactions dont
    uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
    collectives + dÃ©pendances) ont mutÃ©es
    """

    prix_m2_local_moyen: Optional[float] = None
    """
    Prix moyen au m2 de bÃ¢ti en euros calculÃ© Ã partir des transactions dont
    uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
    collectives + dÃ©pendances) ont mutÃ©es
    """

    prix_m2_terrain_max: Optional[float] = None
    """
    Prix maximale au m2 de terrain en euros calculÃ© Ã partir des transactions dont
    uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
    collectives + dÃ©pendances) ont mutÃ©es
    """

    prix_m2_terrain_median: Optional[float] = None
    """
    Prix mÃ©dian au m2 de terrain en euros calculÃ© Ã partir des transactions dont
    uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
    collectives + dÃ©pendances) ont mutÃ©es
    """

    prix_m2_terrain_min: Optional[float] = None
    """
    Prix minimale au m2 de terrain en euros calculÃ© Ã partir des transactions dont
    uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
    collectives + dÃ©pendances) ont mutÃ©es
    """

    prix_m2_terrain_moyen: Optional[float] = None
    """
    Prix moyen au m2 de terrain en euros calculÃ© Ã partir des transactions dont
    uniquement des locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences
    collectives + dÃ©pendances) ont mutÃ©es
    """

    valeur_fonciere_max: Optional[float] = None
    """
    (dv3f) valeur fonciÃ¨re maximale parmi les locaux du bÃ¢timent rapportÃ© au mÂ²
    habitable (SHAB)[â‚¬/mÂ²]
    """

    valeur_fonciere_median: Optional[float] = None
    """
    Valeur fonciÃ¨re mÃ©diane en euros calculÃ©e sur l'ensemble des mutations qui
    ont eu lieu sur le batiment_groupe.
    """

    valeur_fonciere_min: Optional[float] = None
    """
    (dv3f) valeur fonciÃ¨re minimale parmi les locaux du bÃ¢timent rapportÃ© au mÂ²
    habitable (SHAB) [â‚¬/mÂ²]
    """

    valeur_fonciere_moyenne: Optional[float] = None
    """
    Valeur fonciÃ¨re moyenne en euros calculÃ©e sur l'ensemble des mutations qui ont
    eu lieu sur le batiment_groupe.
    """
