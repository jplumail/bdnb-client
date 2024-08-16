# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RelBatimentGroupeRncListParams"]


class RelBatimentGroupeRncListParams(TypedDict, total=False):
    adresse_brut: str
    """adresse brute envoyÃ©e au gÃ©ocodeur"""

    adresse_geocodee: str
    """libelle de l'adresse retournÃ©e par le gÃ©ocodeur"""

    batiment_groupe_id: str
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    cle_interop_adr: str
    """ClÃ© d'interopÃ©rabilitÃ© de l'adresse postale"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    fiabilite_geocodage: str
    """fiabilitÃ© du gÃ©ocodage"""

    fiabilite_globale: str
    """fiabilitÃ© du global du croisement"""

    limit: str
    """Limiting and Pagination"""

    numero_immat: str
    """identifiant de la table rnc"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    parcelle_id: str
    """
    (ffo:idpar) Identifiant de parcelle (ConcatÃ©nation de ccodep, ccocom, ccopre,
    ccosec, dnupla)
    """

    select: str
    """Filtering Columns"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
