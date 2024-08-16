# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["BatimentGroupeRncAPIExpert"]


class BatimentGroupeRncAPIExpert(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    copro_dans_pvd: Optional[bool] = None
    """
    (rnc) au moins une des coproprietÃ©s est dans le programme petites villes de
    demain
    """

    l_annee_construction: Optional[List[str]] = None
    """Liste des annÃ©es de construction"""

    l_nom_copro: Optional[List[str]] = None
    """(rnc) liste des noms des copropriÃ©tÃ©s"""

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
    """numÃ©ro d'immatriculation principal associÃ© au bÃ¢timent groupe.

    (numÃ©ro d'immatriculation copropriÃ©tÃ© qui comporte le plus de lots)
    """

    periode_construction_max: Optional[str] = None
    """(rnc) PÃ©riode de construction du local le plus rÃ©cent"""
