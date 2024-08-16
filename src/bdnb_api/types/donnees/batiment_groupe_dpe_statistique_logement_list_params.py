# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BatimentGroupeDpeStatistiqueLogementListParams"]


class BatimentGroupeDpeStatistiqueLogementListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    limit: str
    """Limiting and Pagination"""

    nb_classe_bilan_dpe_a: str
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe A
    """

    nb_classe_bilan_dpe_b: str
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe B
    """

    nb_classe_bilan_dpe_c: str
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe C
    """

    nb_classe_bilan_dpe_d: str
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe D
    """

    nb_classe_bilan_dpe_e: str
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe E
    """

    nb_classe_bilan_dpe_f: str
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe F
    """

    nb_classe_bilan_dpe_g: str
    """
    (dpe) Nombre de DPE avec une Ã©tiquette bilan DPE (double seuil Ã©nergie/ges) de
    classe G
    """

    nb_classe_conso_energie_arrete_2012_a: str
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique A.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_b: str
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique B.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_c: str
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique C.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_d: str
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique D.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_e: str
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique E.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_f: str
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique F.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_g: str
    """(dpe) Nombre de DPE de la classe Ã©nergÃ©tique G.

    valable uniquement pour les DPE appliquant la mÃ©thode de l'arrÃªtÃ© du 8
    fÃ©vrier 2012
    """

    nb_classe_conso_energie_arrete_2012_nc: str
    """
    (dpe) Nombre de DPE n'ayant pas fait l'objet d'un calcul d'Ã©tiquette Ã©nergie
    (DPE dits vierges). valable uniquement pour les DPE appliquant la mÃ©thode de
    l'arrÃªtÃ© du 8 fÃ©vrier 2012
    """

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
