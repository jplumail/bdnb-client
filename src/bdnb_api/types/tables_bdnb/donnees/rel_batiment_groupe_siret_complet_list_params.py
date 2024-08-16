# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RelBatimentGroupeSiretCompletListParams"]


class RelBatimentGroupeSiretCompletListParams(TypedDict, total=False):
    activite_registre_metier: str
    """ActivitÃ© principale de l'Ã©tablissement au Registre des MÃ©tiers.

    Cette variable, complÃ©mentaire Ã l'activitÃ© principale de l'Ã©tablissement, ne
    concerne que les Ã©tablissements relevant de l'artisanat (artisans,
    artisans-commerÃ§ants et sociÃ©tÃ©s artisanales). Elle caractÃ©rise l'activitÃ©
    selon la Nomenclature d'ActivitÃ©s FranÃ§aise de l'Artisanat (NAFA). La variable
    n'est pas disponible au niveau unitÃ© lÃ©gale.
    """

    batiment_groupe_id: str
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    cle_interop_adr: str
    """ClÃ© d'interopÃ©rabilitÃ© de l'adresse postale"""

    code_activite_principale: str
    """
    Code de l'activitÃ© principale de l'Ã©tablissement, lors de son inscription au
    rÃ©pertoire APET. Il permet l'identification de la branche d'activitÃ©
    principale pour chaque Ã©tablissement.
    """

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    date_creation: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    La date de crÃ©ation de l'unitÃ© lÃ©gale - correspond Ã la date qui figure dans
    la dÃ©claration dÃ©posÃ©e au Centres de FormalitÃ©s des Entreprises (CFE)
    compÃ©tent.
    """

    date_dernier_traitement: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Date du dernier traitement de l'unitÃ© lÃ©gale dans le rÃ©pertoire Sirene."""

    denomination_etablissement: str
    """
    Cette variable dÃ©signe le nom sous lequel l'Ã©tablissement est connu du grand
    public (nom commercial de l'Ã©tablissement).
    """

    etat_administratif_actif: str
    """Ã‰tat administratif de l'Ã©tablissement.

    Si l'Ã©tablissement est signalÃ© comme actif alors la variable est indiquÃ©e
    comme 'Vrai'.
    """

    libelle_activite_principale: str
    """
    LibellÃ© de l'activitÃ© principale de l'Ã©tablissement, lors de son inscription
    au rÃ©pertoire APET.
    """

    limit: str
    """Limiting and Pagination"""

    nic: str
    """
    NumÃ©ro interne de classement (Nic) de l'Ã©tablissement siÃ¨ge de
    l'Ã©tablissement.
    """

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    siege_social: str
    """Indique si l'Ã©tablissement est le siÃ¨ge social"""

    siren: str
    """Siret de l'Ã©tablissement."""

    siret: str
    """Siret de l'Ã©tablissement."""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
