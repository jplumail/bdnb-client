# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BatimentGroupeIndicateurReseauChaudFroidListParams"]


class BatimentGroupeIndicateurReseauChaudFroidListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """(bdnb) ClÃ© d'IntÃ©ropÃ©rabilitÃ© du bÃ¢timent dans la BDNB"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    consommation_chaleur_par_rapport_distance_au_reseau: str
    """Indication sur la consommation de chaleur du bÃ¢timent et sa distance au
    rÃ©seau.

    Plus un bÃ¢timent consomme plus celui-ci peut Ãªtre Ã©loignÃ© du rÃ©seau et
    malgrÃ© tout Ãªtre raccordÃ©. Ici, si la distance entre le bÃ¢timent et le
    rÃ©seau est suffisamment proche par rapport Ã sa consommation, la consommation
    est notÃ© 'suffisante', sinon elle est notÃ©e 'trop faible'.
    """

    id_reseau: str
    """(France chaleur urbaine) Identifiant national du rÃ©seau."""

    id_reseau_bdnb: str
    """
    Identifiant BDNB, liÃ© au rÃ©seau de chaleur, car des donnÃ©es sources ne
    disposent pas d'identifiant unique pour chacune des entrÃ©es (traces et points).
    """

    indicateur_distance_au_reseau: str
    """
    Indication sur la distance entre le bÃ¢timent et le point au rÃ©seau de chaleur
    le plus proche en vue d'un potentiel raccordement au rÃ©seau.
    """

    indicateur_systeme_chauffage: str

    limit: str
    """Limiting and Pagination"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    potentiel_obligation_raccordement: str
    """
    Indique si le bÃ¢timent est Ã©ventuellement dans l'obligation de se raccorder
    lors de certains travaux de rÃ©novation. Pour que
    potentiel_obligation_raccordement soit possible, le bÃ¢timent doit Ãªtre situÃ©
    Ã moins de 100m d'un rÃ©seau classÃ© et son systÃ¨me de chauffage indiquÃ© comme
    collectif. Attention, cet indicateur n'est qu'Ã titre d'information.
    """

    potentiel_raccordement_reseau_chaleur: str
    """Indicateur de potentiel de raccordement au rÃ©seau de chaleur.

    L'indicateur dÃ©pend de la distance entre le bÃ¢timent et le rÃ©seau et du type
    de circuit de chauffage existant du bÃ¢timent. Enfin, si le bÃ¢timent est dÃ©jÃ
    raccordÃ© alors il est indiquÃ© comme tel.
    """

    select: str
    """Filtering Columns"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
