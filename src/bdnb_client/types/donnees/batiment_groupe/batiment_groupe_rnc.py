# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["BatimentGroupeRnc"]


class BatimentGroupeRnc(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code département INSEE"""

    copro_dans_pvd: Optional[bool] = None
    """
    (rnc) au moins une des coproprietés est dans le programme petites villes de
    demain
    """

    l_annee_construction: Optional[List[str]] = None
    """Liste des années de construction"""

    l_nom_copro: Optional[List[str]] = None
    """(rnc) liste des noms des copropriétés"""

    l_siret: Optional[List[str]] = None
    """liste de siret"""

    nb_log: Optional[float] = None
    """(rnc) Nombre de logements"""

    nb_lot_garpark: Optional[float] = None
    """Nombre de lots de stationnement"""

    nb_lot_tertiaire: Optional[float] = None
    """Nombre de lots de type bureau et commerce"""

    nb_lot_tot: Optional[float] = None
    """Nombre total de lots"""

    numero_immat_principal: Optional[str] = None
    """numéro d'immatriculation principal associé au bâtiment groupe.

    (numéro d'immatriculation copropriété qui comporte le plus de lots)
    """

    periode_construction_max: Optional[str] = None
    """(rnc) Période de construction du local le plus récent"""
