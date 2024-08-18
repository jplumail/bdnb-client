# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ....._models import BaseModel

__all__ = ["RelBatimentGroupeSirenComplet"]


class RelBatimentGroupeSirenComplet(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Clé d'Intéropérabilité du bâtiment dans la BDNB."""

    cat_org: Optional[str] = None
    """Catégorie de l'organisation selon la base RPLS."""

    cat_org_simplifie: Optional[str] = None
    """Catégorie de l'organisation - simplifiée"""

    code_departement_insee: Optional[str] = None
    """(bdnb) Code département INSEE dans lequel se trouve le bâtiment"""

    dans_majic_pm: Optional[str] = None
    """(majic_pm) Ce propriétaire possède des bâtiments déclarés dans majic_pm"""

    dans_majic_pm_ou_etablissement: Optional[str] = None
    """
    Identifié comme établissement ou dans majic_pm - permet de filtrer les éléments
    en open data
    """

    date_creation: Optional[date] = None
    """
    La date de création de l'unité légale - correspond à la date qui figure dans la
    déclaration déposée au Centres de Formalités des Entreprises (CFE) compétent.
    """

    date_dernier_traitement: Optional[date] = None
    """Date du dernier traitement de l'unité légale dans le répertoire Sirene."""

    denomination_personne_morale: Optional[str] = None
    """Dénomination de la personne morale."""

    etablissement: Optional[str] = None
    """Identifié comme établissement"""

    etat_administratif_actif: Optional[str] = None
    """à‰tat administratif de l'unité légale (siren).

    Si l'unité légale est signalée comme active alors la variable est indiquée comme
    'Vrai'.
    """

    nb_locaux_open: Optional[str] = None
    """(majic_pm) Nombre de locaux déclarés dans majic_pm."""

    nb_siret_actifs: Optional[str] = None
    """Nombre de siret actifs."""

    personne_type: Optional[str] = None
    """Permet de différencier les personnes physiques des personnes morales."""

    proprietaire_open: Optional[str] = None
    """Permet de filtrer les propriétaires de type open"""

    siren: Optional[str] = None
    """Siren de la personne morale."""

    siren_dans_sirene: Optional[str] = None
    """Le Siren est présent dans la base sirene."""
