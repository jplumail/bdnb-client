# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["RelBatimentGroupeSiretCompletAPIExpert"]


class RelBatimentGroupeSiretCompletAPIExpert(BaseModel):
    activite_registre_metier: Optional[str] = None
    """ActivitÃ© principale de l'Ã©tablissement au Registre des MÃ©tiers.

    Cette variable, complÃ©mentaire Ã l'activitÃ© principale de l'Ã©tablissement, ne
    concerne que les Ã©tablissements relevant de l'artisanat (artisans,
    artisans-commerÃ§ants et sociÃ©tÃ©s artisanales). Elle caractÃ©rise l'activitÃ©
    selon la Nomenclature d'ActivitÃ©s FranÃ§aise de l'Artisanat (NAFA). La variable
    n'est pas disponible au niveau unitÃ© lÃ©gale.
    """

    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB."""

    cle_interop_adr: Optional[str] = None
    """ClÃ© d'interopÃ©rabilitÃ© de l'adresse postale."""

    code_activite_principale: Optional[str] = None
    """
    Code de l'activitÃ© principale de l'Ã©tablissement, lors de son inscription au
    rÃ©pertoire APET. Il permet l'identification de la branche d'activitÃ©
    principale pour chaque Ã©tablissement.
    """

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE."""

    date_creation: Optional[date] = None
    """
    La date de crÃ©ation de l'unitÃ© lÃ©gale - correspond Ã la date qui figure dans
    la dÃ©claration dÃ©posÃ©e au Centres de FormalitÃ©s des Entreprises (CFE)
    compÃ©tent.
    """

    date_dernier_traitement: Optional[date] = None
    """Date du dernier traitement de l'unitÃ© lÃ©gale dans le rÃ©pertoire Sirene."""

    denomination_etablissement: Optional[str] = None
    """
    Cette variable dÃ©signe le nom sous lequel l'Ã©tablissement est connu du grand
    public (nom commercial de l'Ã©tablissement).
    """

    etat_administratif_actif: Optional[str] = None
    """Ã‰tat administratif de l'Ã©tablissement.

    Si l'Ã©tablissement est signalÃ© comme actif alors la variable est indiquÃ©e
    comme 'Vrai'.
    """

    libelle_activite_principale: Optional[str] = None
    """
    LibellÃ© de l'activitÃ© principale de l'Ã©tablissement, lors de son inscription
    au rÃ©pertoire APET.
    """

    nic: Optional[str] = None
    """
    NumÃ©ro interne de classement (Nic) de l'Ã©tablissement siÃ¨ge de
    l'Ã©tablissement.
    """

    siege_social: Optional[str] = None
    """Indique si l'Ã©tablissement est le siÃ¨ge social."""

    siren: Optional[str] = None
    """Siret de l'Ã©tablissement."""

    siret: Optional[str] = None
    """Siret de l'Ã©tablissement."""
