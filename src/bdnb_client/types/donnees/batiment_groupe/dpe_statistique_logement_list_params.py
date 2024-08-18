# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DpeStatistiqueLogementListParams"]


class DpeStatistiqueLogementListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    code_departement_insee: str
    """Code département INSEE"""

    limit: str
    """Limiting and Pagination"""

    nb_classe_bilan_dpe_a: str
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe A
    """

    nb_classe_bilan_dpe_b: str
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe B
    """

    nb_classe_bilan_dpe_c: str
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe C
    """

    nb_classe_bilan_dpe_d: str
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe D
    """

    nb_classe_bilan_dpe_e: str
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe E
    """

    nb_classe_bilan_dpe_f: str
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe F
    """

    nb_classe_bilan_dpe_g: str
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe G
    """

    nb_classe_conso_energie_arrete_2012_a: str
    """(dpe) Nombre de DPE de la classe énergétique A.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_b: str
    """(dpe) Nombre de DPE de la classe énergétique B.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_c: str
    """(dpe) Nombre de DPE de la classe énergétique C.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_d: str
    """(dpe) Nombre de DPE de la classe énergétique D.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_e: str
    """(dpe) Nombre de DPE de la classe énergétique E.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_f: str
    """(dpe) Nombre de DPE de la classe énergétique F.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_g: str
    """(dpe) Nombre de DPE de la classe énergétique G.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_nc: str
    """
    (dpe) Nombre de DPE n'ayant pas fait l'objet d'un calcul d'étiquette énergie
    (DPE dits vierges). valable uniquement pour les DPE appliquant la méthode de
    l'arràªté du 8 février 2012
    """

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
