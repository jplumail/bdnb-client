# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ....._models import BaseModel

__all__ = ["RelBatimentGroupeSiretComplet"]


class RelBatimentGroupeSiretComplet(BaseModel):
    activite_registre_metier: Optional[str] = None
    """Activité principale de l'établissement au Registre des Métiers.

    Cette variable, complémentaire à l'activité principale de l'établissement, ne
    concerne que les établissements relevant de l'artisanat (artisans,
    artisans-commerà§ants et sociétés artisanales). Elle caractérise l'activité
    selon la Nomenclature d'Activités Franà§aise de l'Artisanat (NAFA). La variable
    n'est pas disponible au niveau unité légale.
    """

    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bâtiment au sens de la BDNB."""

    cle_interop_adr: Optional[str] = None
    """Clé d'interopérabilité de l'adresse postale."""

    code_activite_principale: Optional[str] = None
    """
    Code de l'activité principale de l'établissement, lors de son inscription au
    répertoire APET. Il permet l'identification de la branche d'activité principale
    pour chaque établissement.
    """

    code_departement_insee: Optional[str] = None
    """Code département INSEE."""

    date_creation: Optional[date] = None
    """
    La date de création de l'unité légale - correspond à la date qui figure dans la
    déclaration déposée au Centres de Formalités des Entreprises (CFE) compétent.
    """

    date_dernier_traitement: Optional[date] = None
    """Date du dernier traitement de l'unité légale dans le répertoire Sirene."""

    denomination_etablissement: Optional[str] = None
    """
    Cette variable désigne le nom sous lequel l'établissement est connu du grand
    public (nom commercial de l'établissement).
    """

    etat_administratif_actif: Optional[str] = None
    """à‰tat administratif de l'établissement.

    Si l'établissement est signalé comme actif alors la variable est indiquée comme
    'Vrai'.
    """

    libelle_activite_principale: Optional[str] = None
    """
    Libellé de l'activité principale de l'établissement, lors de son inscription au
    répertoire APET.
    """

    nic: Optional[str] = None
    """Numéro interne de classement (Nic) de l'établissement siège de l'établissement."""

    siege_social: Optional[str] = None
    """Indique si l'établissement est le siège social."""

    siren: Optional[str] = None
    """Siret de l'établissement."""

    siret: Optional[str] = None
    """Siret de l'établissement."""
