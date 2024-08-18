# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["BatimentGroupeDpeStatistiqueLogement"]


class BatimentGroupeDpeStatistiqueLogement(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    nb_classe_bilan_dpe_a: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe A
    """

    nb_classe_bilan_dpe_b: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe B
    """

    nb_classe_bilan_dpe_c: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe C
    """

    nb_classe_bilan_dpe_d: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe D
    """

    nb_classe_bilan_dpe_e: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe E
    """

    nb_classe_bilan_dpe_f: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe F
    """

    nb_classe_bilan_dpe_g: Optional[int] = None
    """
    (dpe) Nombre de DPE avec une étiquette bilan DPE (double seuil énergie/ges) de
    classe G
    """

    nb_classe_conso_energie_arrete_2012_a: Optional[int] = None
    """(dpe) Nombre de DPE de la classe énergétique A.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_b: Optional[int] = None
    """(dpe) Nombre de DPE de la classe énergétique B.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_c: Optional[int] = None
    """(dpe) Nombre de DPE de la classe énergétique C.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_d: Optional[int] = None
    """(dpe) Nombre de DPE de la classe énergétique D.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_e: Optional[int] = None
    """(dpe) Nombre de DPE de la classe énergétique E.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_f: Optional[int] = None
    """(dpe) Nombre de DPE de la classe énergétique F.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_g: Optional[int] = None
    """(dpe) Nombre de DPE de la classe énergétique G.

    valable uniquement pour les DPE appliquant la méthode de l'arràªté du 8 février
    2012
    """

    nb_classe_conso_energie_arrete_2012_nc: Optional[int] = None
    """
    (dpe) Nombre de DPE n'ayant pas fait l'objet d'un calcul d'étiquette énergie
    (DPE dits vierges). valable uniquement pour les DPE appliquant la méthode de
    l'arràªté du 8 février 2012
    """
