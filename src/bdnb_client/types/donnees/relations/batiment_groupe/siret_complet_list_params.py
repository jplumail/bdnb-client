# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["SiretCompletListParams"]


class SiretCompletListParams(TypedDict, total=False):
    activite_registre_metier: str
    """Activité principale de l'établissement au Registre des Métiers.

    Cette variable, complémentaire à l'activité principale de l'établissement, ne
    concerne que les établissements relevant de l'artisanat (artisans,
    artisans-commerà§ants et sociétés artisanales). Elle caractérise l'activité
    selon la Nomenclature d'Activités Franà§aise de l'Artisanat (NAFA). La variable
    n'est pas disponible au niveau unité légale.
    """

    batiment_groupe_id: str
    """Identifiant du groupe de bâtiment au sens de la BDNB"""

    cle_interop_adr: str
    """Clé d'interopérabilité de l'adresse postale"""

    code_activite_principale: str
    """
    Code de l'activité principale de l'établissement, lors de son inscription au
    répertoire APET. Il permet l'identification de la branche d'activité principale
    pour chaque établissement.
    """

    code_departement_insee: str
    """Code département INSEE"""

    date_creation: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    La date de création de l'unité légale - correspond à la date qui figure dans la
    déclaration déposée au Centres de Formalités des Entreprises (CFE) compétent.
    """

    date_dernier_traitement: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Date du dernier traitement de l'unité légale dans le répertoire Sirene."""

    denomination_etablissement: str
    """
    Cette variable désigne le nom sous lequel l'établissement est connu du grand
    public (nom commercial de l'établissement).
    """

    etat_administratif_actif: str
    """à‰tat administratif de l'établissement.

    Si l'établissement est signalé comme actif alors la variable est indiquée comme
    'Vrai'.
    """

    libelle_activite_principale: str
    """
    Libellé de l'activité principale de l'établissement, lors de son inscription au
    répertoire APET.
    """

    limit: str
    """Limiting and Pagination"""

    nic: str
    """Numéro interne de classement (Nic) de l'établissement siège de l'établissement."""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    siege_social: str
    """Indique si l'établissement est le siège social"""

    siren: str
    """Siret de l'établissement."""

    siret: str
    """Siret de l'établissement."""

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
