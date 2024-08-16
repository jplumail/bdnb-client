# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BatimentGroupeDpeStatistiqueLogementAPIExpert"]


class BatimentGroupeDpeStatistiqueLogementAPIExpert(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    nb_classe_bilan_dpe_a: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe A
    """

    nb_classe_bilan_dpe_b: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe B
    """

    nb_classe_bilan_dpe_c: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe C
    """

    nb_classe_bilan_dpe_d: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe D
    """

    nb_classe_bilan_dpe_e: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe E
    """

    nb_classe_bilan_dpe_f: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe F
    """

    nb_classe_bilan_dpe_g: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe G
    """

    nb_classe_conso_energie_arrete_2012_a: Optional[int] = None
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique A.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_b: Optional[int] = None
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique B.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_c: Optional[int] = None
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique C.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_d: Optional[int] = None
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique D.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_e: Optional[int] = None
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique E.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_f: Optional[int] = None
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique F.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_g: Optional[int] = None
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique G.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_nc: Optional[int] = None
    """
    (dpe) Nombre de DPE n'ayant pas fait l'objet d'un calcul d'Ã©tiquette Ã©nergie
    (DPE dits vierges). valable uniquement pour les DPE appliquant la mÃ©thode de
    l'arrÃªtÃ© du 8 fÃ©vrier 2012
    """
