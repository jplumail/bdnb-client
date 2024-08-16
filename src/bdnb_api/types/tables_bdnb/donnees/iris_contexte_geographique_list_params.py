# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["IrisContexteGeographiqueListParams"]


class IrisContexteGeographiqueListParams(TypedDict, total=False):
    action_coeur_ville_code_anct: str
    """Code anct des communes sÃ©lectionnÃ©es pour le programme Action cÅ“ur de ville"""

    action_coeur_ville_libelle: str
    """LibellÃ© des communes sÃ©lectionnÃ©es pour le programme Action cÅ“ur de ville"""

    aire_attraction_ville_catg: str
    """
    CatÃ©gorie de l'Aire d'Attraction urbaine des Villes (AAV2020) - recensement
    2020
    """

    aire_attraction_ville_catg_libelle: str
    """LibellÃ© de l'Aire d'Attraction urbaine des Villes (AAV2020) - recensement 2020"""

    aire_attraction_ville_code_insee: str
    """
    Code insee des Aires d'Attractions urbaines des Villes (AAV2020) - recensement
    2020
    """

    aire_attraction_ville_libelle: str
    """
    LibellÃ© des Aires d'Attractions urbaines des Villes (AAV2020) - recensement
    2020
    """

    aire_urbaine_fonctionnelle_eurostat: str
    """Code des cities et des aires urbaines fonctionnelles (FUA) - eurostat"""

    aire_urbaine_fonctionnelle_libelle: str
    """LibellÃ© des cities et des aires urbaines fonctionnelles (FUA) - eurostat"""

    bassin_vie_catg: str
    """CatÃ©gorie des bassins de vie 2022 (BV2022)"""

    bassin_vie_catg_libelle: str
    """LibellÃ© de la catÃ©gorie des bassins de vie 2022 (BV2022)"""

    bassin_vie_code_insee: str
    """Code insee des bassins de vie 2022 (BV2022)"""

    bassin_vie_libelle: str
    """LibellÃ© des bassins de vie 2022 (BV2022)"""

    code_departement_insee: str
    """Code departement INSEE"""

    code_iris: str
    """Code iris INSEE"""

    contrat_relance_trans_eco_code_anct: str
    """
    Code anct des iris dans le Contrat de relance et de transition Ã©cologique
    (CRTE)
    """

    contrat_relance_trans_eco_libelle: str
    """
    LibellÃ©s des communes/iris dans le Contrat de relance et de transition
    Ã©cologique (CRTE)
    """

    en_littoral: str
    """Iris situÃ© en littoral"""

    en_montagne: str
    """iris situÃ© en montagne"""

    geom_iris: str
    """GÃ©omÃ©trie de l'IRIS"""

    grille_communale_densite_catg: str
    """CatÃ©gorie de la Grille communale de densitÃ©"""

    grille_communale_densite_catg_libelle: str
    """LibellÃ© de la catÃ©gorie de la Grille communale de densitÃ©"""

    limit: str
    """Limiting and Pagination"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    petites_villes_demain_code_anct: str
    """Code anct des iris/comunes dans le programme petites villes de demain (PVD)"""

    select: str
    """Filtering Columns"""

    territoires_industrie_code_anct: str
    """Code anct - programme territoires d'industrie"""

    territoires_industrie_libelle: str
    """LibellÃ© - programme territoires d'industrie"""

    unite_urbaine_catg: str
    """CatÃ©gorie des unitÃ©s urbaines"""

    unite_urbaine_catg_libelle: str
    """LibellÃ© de la catÃ©gorie des unitÃ©s urbaines"""

    unite_urbaine_code_insee: str
    """Code INSEE des unitÃ©s urbaines"""

    unite_urbaine_libelle: str
    """LibellÃ© des unitÃ©s urbaines"""

    zone_aide_finalite_reg_catg: str
    """
    CatÃ©gorie des zones dâ€™aides Ã finalitÃ© rÃ©gionale (AFR) pour la pÃ©riode
    2022-2027
    """

    zone_aide_finalite_reg_code_anct: str
    """
    Code anct des zones dâ€™aides Ã finalitÃ© rÃ©gionale (AFR) pour la pÃ©riode
    2022-2027
    """

    zone_emploi_code_insee: str
    """Code insee des zones d'emploi"""

    zone_emploi_libelle: str
    """LibellÃ© des zones d'emploi"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
