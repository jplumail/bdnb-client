# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["RelBatimentGroupeSirenAPIExpert"]


class RelBatimentGroupeSirenAPIExpert(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """ClÃ© d'IntÃ©ropÃ©rabilitÃ© du bÃ¢timent dans la BDNB."""

    cat_org: Optional[str] = None
    """CatÃ©gorie de l'organisation selon la base RPLS."""

    cat_org_simplifie: Optional[str] = None
    """CatÃ©gorie de l'organisation - simplifiÃ©e"""

    code_departement_insee: Optional[str] = None
    """(bdnb) Code dÃ©partement INSEE dans lequel se trouve le bÃ¢timent"""

    dans_majic_pm: Optional[str] = None
    """(majic_pm) Ce propriÃ©taire possÃ¨de des bÃ¢timents dÃ©clarÃ©s dans majic_pm"""

    dans_majic_pm_ou_etablissement: Optional[str] = None
    """
    IdentifiÃ© comme Ã©tablissement ou dans majic_pm - permet de filtrer les
    Ã©lÃ©ments en open data
    """

    date_creation: Optional[date] = None
    """
    La date de crÃ©ation de l'unitÃ© lÃ©gale - correspond Ã la date qui figure dans
    la dÃ©claration dÃ©posÃ©e au Centres de FormalitÃ©s des Entreprises (CFE)
    compÃ©tent.
    """

    date_dernier_traitement: Optional[date] = None
    """Date du dernier traitement de l'unitÃ© lÃ©gale dans le rÃ©pertoire Sirene."""

    denomination_personne_morale: Optional[str] = None
    """DÃ©nomination de la personne morale."""

    etablissement: Optional[str] = None
    """IdentifiÃ© comme Ã©tablissement"""

    etat_administratif_actif: Optional[str] = None
    """Ã‰tat administratif de l'unitÃ© lÃ©gale (siren).

    Si l'unitÃ© lÃ©gale est signalÃ©e comme active alors la variable est indiquÃ©e
    comme 'Vrai'.
    """

    nb_locaux_open: Optional[str] = None
    """(majic_pm) Nombre de locaux dÃ©clarÃ©s dans majic_pm."""

    nb_siret_actifs: Optional[str] = None
    """Nombre de siret actifs."""

    personne_type: Optional[str] = None
    """Permet de diffÃ©rencier les personnes physiques des personnes morales."""

    proprietaire_open: Optional[str] = None
    """Permet de filtrer les propriÃ©taires de type open"""

    siren: Optional[str] = None
    """Siren de la personne morale."""

    siren_dans_sirene: Optional[str] = None
    """Le Siren est prÃ©sent dans la base sirene."""
