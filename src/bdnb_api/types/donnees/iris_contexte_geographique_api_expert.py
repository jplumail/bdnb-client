# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["IrisContexteGeographiqueAPIExpert"]


class IrisContexteGeographiqueAPIExpert(BaseModel):
    action_coeur_ville_code_anct: Optional[str] = None
    """Code anct des communes sÃ©lectionnÃ©es pour le programme Action cÅ“ur de ville"""

    action_coeur_ville_libelle: Optional[str] = None
    """LibellÃ© des communes sÃ©lectionnÃ©es pour le programme Action cÅ“ur de ville"""

    aire_attraction_ville_catg: Optional[str] = None
    """
    CatÃ©gorie de l'Aire d'Attraction urbaine des Villes (AAV2020) - recensement
    2020
    """

    aire_attraction_ville_catg_libelle: Optional[str] = None
    """LibellÃ© de l'Aire d'Attraction urbaine des Villes (AAV2020) - recensement 2020"""

    aire_attraction_ville_code_insee: Optional[str] = None
    """
    Code insee des Aires d'Attractions urbaines des Villes (AAV2020) - recensement
    2020
    """

    aire_attraction_ville_libelle: Optional[str] = None
    """
    LibellÃ© des Aires d'Attractions urbaines des Villes (AAV2020) - recensement
    2020
    """

    aire_urbaine_fonctionnelle_eurostat: Optional[str] = None
    """Code des cities et des aires urbaines fonctionnelles (FUA) - eurostat"""

    aire_urbaine_fonctionnelle_libelle: Optional[str] = None
    """LibellÃ© des cities et des aires urbaines fonctionnelles (FUA) - eurostat"""

    bassin_vie_catg: Optional[str] = None
    """CatÃ©gorie des bassins de vie 2022 (BV2022)"""

    bassin_vie_catg_libelle: Optional[str] = None
    """LibellÃ© de la catÃ©gorie des bassins de vie 2022 (BV2022)"""

    bassin_vie_code_insee: Optional[str] = None
    """Code insee des bassins de vie 2022 (BV2022)"""

    bassin_vie_libelle: Optional[str] = None
    """LibellÃ© des bassins de vie 2022 (BV2022)"""

    code_departement_insee: Optional[str] = None
    """Code departement INSEE"""

    code_iris: Optional[str] = None
    """Code iris INSEE"""

    contrat_relance_trans_eco_code_anct: Optional[str] = None
    """
    Code anct des iris dans le Contrat de relance et de transition Ã©cologique
    (CRTE)
    """

    contrat_relance_trans_eco_libelle: Optional[str] = None
    """
    LibellÃ©s des communes/iris dans le Contrat de relance et de transition
    Ã©cologique (CRTE)
    """

    en_littoral: Optional[str] = None
    """Iris situÃ© en littoral"""

    en_montagne: Optional[str] = None
    """iris situÃ© en montagne"""

    geom_iris: Optional[str] = None
    """GÃ©omÃ©trie de l'IRIS"""

    grille_communale_densite_catg: Optional[str] = None
    """CatÃ©gorie de la Grille communale de densitÃ©"""

    grille_communale_densite_catg_libelle: Optional[str] = None
    """LibellÃ© de la catÃ©gorie de la Grille communale de densitÃ©"""

    petites_villes_demain_code_anct: Optional[str] = None
    """Code anct des iris/comunes dans le programme petites villes de demain (PVD)"""

    territoires_industrie_code_anct: Optional[str] = None
    """Code anct - programme territoires d'industrie"""

    territoires_industrie_libelle: Optional[str] = None
    """LibellÃ© - programme territoires d'industrie"""

    unite_urbaine_catg: Optional[str] = None
    """CatÃ©gorie des unitÃ©s urbaines"""

    unite_urbaine_catg_libelle: Optional[str] = None
    """LibellÃ© de la catÃ©gorie des unitÃ©s urbaines"""

    unite_urbaine_code_insee: Optional[str] = None
    """Code INSEE des unitÃ©s urbaines"""

    unite_urbaine_libelle: Optional[str] = None
    """LibellÃ© des unitÃ©s urbaines"""

    zone_aide_finalite_reg_catg: Optional[str] = None
    """
    CatÃ©gorie des zones dâ€™aides Ã finalitÃ© rÃ©gionale (AFR) pour la pÃ©riode
    2022-2027
    """

    zone_aide_finalite_reg_code_anct: Optional[str] = None
    """
    Code anct des zones dâ€™aides Ã finalitÃ© rÃ©gionale (AFR) pour la pÃ©riode
    2022-2027
    """

    zone_emploi_code_insee: Optional[str] = None
    """Code insee des zones d'emploi"""

    zone_emploi_libelle: Optional[str] = None
    """LibellÃ© des zones d'emploi"""
