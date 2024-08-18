# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["SirenCompletListParams"]


class SirenCompletListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Clé d'Intéropérabilité du bâtiment dans la BDNB."""

    cat_org: str
    """Catégorie de l'organisation selon la base RPLS."""

    cat_org_simplifie: str
    """Catégorie de l'organisation - simplifiée"""

    code_departement_insee: str
    """(bdnb) Code département INSEE dans lequel se trouve le bâtiment"""

    dans_majic_pm: str
    """(majic_pm) Ce propriétaire possède des bâtiments déclarés dans majic_pm"""

    dans_majic_pm_ou_etablissement: str
    """
    Identifié comme établissement ou dans majic_pm - permet de filtrer les éléments
    en open data
    """

    date_creation: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    La date de création de l'unité légale - correspond à la date qui figure dans la
    déclaration déposée au Centres de Formalités des Entreprises (CFE) compétent.
    """

    date_dernier_traitement: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Date du dernier traitement de l'unité légale dans le répertoire Sirene."""

    denomination_personne_morale: str
    """Dénomination de la personne morale."""

    etablissement: str
    """Identifié comme établissement"""

    etat_administratif_actif: str
    """à‰tat administratif de l'unité légale (siren).

    Si l'unité légale est signalée comme active alors la variable est indiquée comme
    'Vrai'.
    """

    limit: str
    """Limiting and Pagination"""

    nb_locaux_open: str
    """(majic_pm) Nombre de locaux déclarés dans majic_pm."""

    nb_siret_actifs: str
    """Nombre de siret actifs."""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    personne_type: str
    """Permet de différencier les personnes physiques des personnes morales."""

    proprietaire_open: str
    """Permet de filtrer les propriétaires de type open"""

    select: str
    """Filtering Columns"""

    siren: str
    """Siren de la personne morale."""

    siren_dans_sirene: str
    """Le Siren est présent dans la base sirene."""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
