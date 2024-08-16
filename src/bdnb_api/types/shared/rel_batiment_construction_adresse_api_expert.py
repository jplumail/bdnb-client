# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RelBatimentConstructionAdresseAPIExpert"]


class RelBatimentConstructionAdresseAPIExpert(BaseModel):
    adresse_principale: Optional[bool] = None
    """
    BoolÃ©en prÃ©cisant si l'adresse courante est l'une des adresses principales de
    la construction ou non. Une relation est taguÃ©e comme `principale` si l'adresse
    qui la compose obtient le score de fiabilitÃ© le plus important parmi toutes les
    adresses desservant une mÃªme construction. Il se peut, par consÃ©quent, qu'une
    construction ait plusieurs adresses principales : toutes celles ayant le score
    de fiabilitÃ© le plus haut pour cette construction.
    """

    batiment_construction_id: Optional[str] = None
    """
    Identifiant unique du bÃ¢timent physique de la BDNB -> cleabs (ign) + index de
    sub-division (si construction sur plusieurs parcelles)
    """

    cle_interop_adr: Optional[str] = None
    """ClÃ© d'interopÃ©rabilitÃ© de l'adresse postale"""

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    distance_batiment_construction_adresse: Optional[int] = None
    """Distance entre le gÃ©olocalisant adresse et la gÃ©omÃ©trie de bÃ¢timent"""

    fiabilite: Optional[int] = None
    """Niveau de fiabilitÃ©"""
