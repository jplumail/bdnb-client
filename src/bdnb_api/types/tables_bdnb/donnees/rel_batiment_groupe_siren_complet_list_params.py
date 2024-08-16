# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RelBatimentGroupeSirenCompletListParams"]


class RelBatimentGroupeSirenCompletListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """ClÃ© d'IntÃ©ropÃ©rabilitÃ© du bÃ¢timent dans la BDNB."""

    cat_org: str
    """CatÃ©gorie de l'organisation selon la base RPLS."""

    cat_org_simplifie: str
    """CatÃ©gorie de l'organisation - simplifiÃ©e"""

    code_departement_insee: str
    """(bdnb) Code dÃ©partement INSEE dans lequel se trouve le bÃ¢timent"""

    dans_majic_pm: str
    """(majic_pm) Ce propriÃ©taire possÃ¨de des bÃ¢timents dÃ©clarÃ©s dans majic_pm"""

    dans_majic_pm_ou_etablissement: str
    """
    IdentifiÃ© comme Ã©tablissement ou dans majic_pm - permet de filtrer les
    Ã©lÃ©ments en open data
    """

    date_creation: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    La date de crÃ©ation de l'unitÃ© lÃ©gale - correspond Ã la date qui figure dans
    la dÃ©claration dÃ©posÃ©e au Centres de FormalitÃ©s des Entreprises (CFE)
    compÃ©tent.
    """

    date_dernier_traitement: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Date du dernier traitement de l'unitÃ© lÃ©gale dans le rÃ©pertoire Sirene."""

    denomination_personne_morale: str
    """DÃ©nomination de la personne morale."""

    etablissement: str
    """IdentifiÃ© comme Ã©tablissement"""

    etat_administratif_actif: str
    """Ã‰tat administratif de l'unitÃ© lÃ©gale (siren).

    Si l'unitÃ© lÃ©gale est signalÃ©e comme active alors la variable est indiquÃ©e
    comme 'Vrai'.
    """

    limit: str
    """Limiting and Pagination"""

    nb_locaux_open: str
    """(majic_pm) Nombre de locaux dÃ©clarÃ©s dans majic_pm."""

    nb_siret_actifs: str
    """Nombre de siret actifs."""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    personne_type: str
    """Permet de diffÃ©rencier les personnes physiques des personnes morales."""

    proprietaire_open: str
    """Permet de filtrer les propriÃ©taires de type open"""

    select: str
    """Filtering Columns"""

    siren: str
    """Siren de la personne morale."""

    siren_dans_sirene: str
    """Le Siren est prÃ©sent dans la base sirene."""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
