# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["BatimentGroupeDvfOpenRepresentatifAPIExpert"]


class BatimentGroupeDvfOpenRepresentatifAPIExpert(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    date_mutation: Optional[date] = None
    """(dv3f) date de la mutation"""

    id_opendata: Optional[str] = None
    """Identifiant open data de la mutation."""

    nb_appartement_mutee_mutation: Optional[int] = None
    """Nombre d'appartements ayant mutÃ©s lors de la mutation reprÃ©sentative."""

    nb_dependance_mutee_mutation: Optional[int] = None
    """Nombre de dÃ©pendances ayant mutÃ©es lors de la mutation reprÃ©sentative."""

    nb_locaux_mutee_mutation: Optional[int] = None
    """Nombre de locaux ayant mutÃ©s lors de la mutation reprÃ©sentative."""

    nb_locaux_tertiaire_mutee_mutation: Optional[int] = None
    """Nombre de locaux tertiaires ayant mutÃ©s lors de la mutation reprÃ©sentative."""

    nb_maison_mutee_mutation: Optional[int] = None
    """Nombre de maisons ayant mutÃ©es lors de la mutation reprÃ©sentative."""

    nb_piece_principale: Optional[int] = None
    """
    Nombre de piÃ¨ces principales de la rÃ©sidence individuelle ou collective ayant
    mutÃ©. Cet indicateur est disponible lorsqu'une unique rÃ©sidence individuelle
    ou collective a mutÃ©e.
    """

    prix_m2_local: Optional[float] = None
    """Prix au mÂ² de bÃ¢ti en euros lors de la mutation.

    Cet indicateur n'est disponible que pour des transactions dont uniquement les
    locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences collectives +
    dÃ©pendances) ont mutÃ©es [â‚¬]
    """

    prix_m2_terrain: Optional[float] = None
    """Prix au mÂ² du terrain en euros lors de la mutation.

    Cet indicateur n'est disponible que pour des transactions dont uniquement les
    locaux (rÃ©sidences individuelles + dÃ©pendances) ou (rÃ©sidences collectives +
    dÃ©pendances) ont mutÃ©es [â‚¬]
    """

    surface_bati_mutee_dependance: Optional[float] = None
    """
    Surface de bÃ¢ti associÃ©e Ã des dÃ©pendances ayant mutÃ©es lors de la mutation
    reprÃ©sentative [mÂ²].
    """

    surface_bati_mutee_residencielle_collective: Optional[float] = None
    """
    Surface de bÃ¢ti associÃ©e Ã des rÃ©sidences collectives ayant mutÃ©es lors de
    la mutation reprÃ©sentative [mÂ²].
    """

    surface_bati_mutee_residencielle_individuelle: Optional[float] = None
    """
    Surface de bÃ¢ti associÃ©e Ã des rÃ©sidences individuelles ayant mutÃ©es lors de
    la mutation reprÃ©sentative [mÂ²].
    """

    surface_bati_mutee_tertiaire: Optional[float] = None
    """
    Surface de bÃ¢ti associÃ©e Ã du tertiaire ayant mutÃ©es lors de la mutation
    reprÃ©sentative [mÂ²].
    """

    surface_terrain_mutee: Optional[float] = None
    """Surface de terrain ayant mutÃ© lors de la mutation reprÃ©sentative [mÂ²]."""

    valeur_fonciere: Optional[float] = None
    """Valeur fonciÃ¨re en euros de la mutation reprÃ©sentative. [â‚¬]"""
