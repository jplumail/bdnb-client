# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["AdresseListParams"]


class AdresseListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    classe: str
    """Classe de méthodologie de croisement à l'adresse (Fichiers_fonciers, Cadastre)"""

    cle_interop_adr: str
    """Clé d'interopérabilité de l'adresse postale"""

    code_departement_insee: str
    """Code département INSEE"""

    geom_bat_adresse: str
    """
    Géolocalisant du trait reliant le point adresse à la géométrie du bâtiment
    groupe (Lambert-93, SRID=2154)
    """

    lien_valide: str
    """
    [DEPRECIEE] (bdnb) un couple (batiment_groupe ; adresse) est considéré comme
    valide si l'adresse est une adresse ban et que le batiment_groupe est associé à
    des fichiers fonciers
    """

    limit: str
    """Limiting and Pagination"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    origine: str
    """Origine de l'entrée bâtiment.

    Elle provient soit des données foncières (Fichiers Fonciers), soit d'un
    croisement géospatial entre le Cadastre, la BDTopo et des bases de données
    métiers (ex: BPE ou Mérimée)
    """

    select: str
    """Filtering Columns"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
