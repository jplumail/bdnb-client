# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AdresseListParams"]


class AdresseListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    cle_interop_adr_principale_ban: str
    """Clé d'interopérabilité de l'adresse principale (issue de la BAN)"""

    code_departement_insee: str
    """Code département INSEE"""

    fiabilite_cr_adr_niv_1: str
    """
    Fiabilité des données croisées à l'adresse ('données croisées à l'adresse
    fiables', 'données croisées à l'adresse fiables à l'echelle de la parcelle
    unifiee', 'données croisées à l'adresse moyennement fiables', 'problème de
    géocodage')
    """

    fiabilite_cr_adr_niv_2: str
    """Fiabilité détaillée des données croisées à l'adresse"""

    libelle_adr_principale_ban: str
    """Libellé complet de l'adresse principale (issue de la BAN)"""

    limit: str
    """Limiting and Pagination"""

    nb_adresse_valid_ban: str
    """
    Nombre d'adresses valides différentes provenant de la BAN qui desservent le
    groupe de bâtiment
    """

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
