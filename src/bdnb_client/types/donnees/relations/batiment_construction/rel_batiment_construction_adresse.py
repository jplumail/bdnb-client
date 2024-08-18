# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["RelBatimentConstructionAdresse"]


class RelBatimentConstructionAdresse(BaseModel):
    adresse_principale: Optional[bool] = None
    """
    Booléen précisant si l'adresse courante est l'une des adresses principales de la
    construction ou non. Une relation est taguée comme `principale` si l'adresse qui
    la compose obtient le score de fiabilité le plus important parmi toutes les
    adresses desservant une màªme construction. Il se peut, par conséquent, qu'une
    construction ait plusieurs adresses principales : toutes celles ayant le score
    de fiabilité le plus haut pour cette construction.
    """

    batiment_construction_id: Optional[str] = None
    """
    Identifiant unique du bâtiment physique de la BDNB -> cleabs (ign) + index de
    sub-division (si construction sur plusieurs parcelles)
    """

    cle_interop_adr: Optional[str] = None
    """Clé d'interopérabilité de l'adresse postale"""

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    distance_batiment_construction_adresse: Optional[int] = None
    """Distance entre le géolocalisant adresse et la géométrie de bâtiment"""

    fiabilite: Optional[int] = None
    """Niveau de fiabilité"""
