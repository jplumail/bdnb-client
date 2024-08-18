# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RncListParams"]


class RncListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    code_departement_insee: str
    """Code département INSEE"""

    copro_dans_pvd: str
    """
    (rnc) au moins une des coproprietés est dans le programme petites villes de
    demain
    """

    l_annee_construction: str
    """Liste des années de construction"""

    l_nom_copro: str
    """(rnc) liste des noms des copropriétés"""

    l_siret: str
    """liste de siret"""

    limit: str
    """Limiting and Pagination"""

    nb_log: str
    """(rnc) Nombre de logements"""

    nb_lot_garpark: str
    """Nombre de lots de stationnement"""

    nb_lot_tertiaire: str
    """Nombre de lots de type bureau et commerce"""

    nb_lot_tot: str
    """Nombre total de lots"""

    numero_immat_principal: str
    """numéro d'immatriculation principal associé au bâtiment groupe.

    (numéro d'immatriculation copropriété qui comporte le plus de lots)
    """

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    periode_construction_max: str
    """(rnc) Période de construction du local le plus récent"""

    select: str
    """Filtering Columns"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
