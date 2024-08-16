# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BatimentGroupeAdresseListParams"]


class BatimentGroupeAdresseListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    cle_interop_adr_principale_ban: str
    """ClÃ© d'interopÃ©rabilitÃ© de l'adresse principale (issue de la BAN)"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    fiabilite_cr_adr_niv_1: str
    """
    FiabilitÃ© des donnÃ©es croisÃ©es Ã l'adresse ('donnÃ©es croisÃ©es Ã l'adresse
    fiables', 'donnÃ©es croisÃ©es Ã l'adresse fiables Ã l'echelle de la parcelle
    unifiee', 'donnÃ©es croisÃ©es Ã l'adresse moyennement fiables', 'problÃ¨me de
    gÃ©ocodage')
    """

    fiabilite_cr_adr_niv_2: str
    """FiabilitÃ© dÃ©taillÃ©e des donnÃ©es croisÃ©es Ã l'adresse"""

    libelle_adr_principale_ban: str
    """LibellÃ© complet de l'adresse principale (issue de la BAN)"""

    limit: str
    """Limiting and Pagination"""

    nb_adresse_valid_ban: str
    """
    Nombre d'adresses valides diffÃ©rentes provenant de la BAN qui desservent le
    groupe de bÃ¢timent
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
