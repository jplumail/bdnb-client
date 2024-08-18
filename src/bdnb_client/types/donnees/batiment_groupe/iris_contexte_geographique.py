# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["IrisContexteGeographique"]


class IrisContexteGeographique(BaseModel):
    action_coeur_ville_code_anct: Optional[str] = None
    """Code anct des communes sélectionnées pour le programme Action cÅ“ur de ville"""

    action_coeur_ville_libelle: Optional[str] = None
    """Libellé des communes sélectionnées pour le programme Action cÅ“ur de ville"""

    aire_attraction_ville_catg: Optional[str] = None
    """
    Catégorie de l'Aire d'Attraction urbaine des Villes (AAV2020) - recensement 2020
    """

    aire_attraction_ville_catg_libelle: Optional[str] = None
    """Libellé de l'Aire d'Attraction urbaine des Villes (AAV2020) - recensement 2020"""

    aire_attraction_ville_code_insee: Optional[str] = None
    """
    Code insee des Aires d'Attractions urbaines des Villes (AAV2020) - recensement
    2020
    """

    aire_attraction_ville_libelle: Optional[str] = None
    """
    Libellé des Aires d'Attractions urbaines des Villes (AAV2020) - recensement 2020
    """

    aire_urbaine_fonctionnelle_eurostat: Optional[str] = None
    """Code des cities et des aires urbaines fonctionnelles (FUA) - eurostat"""

    aire_urbaine_fonctionnelle_libelle: Optional[str] = None
    """Libellé des cities et des aires urbaines fonctionnelles (FUA) - eurostat"""

    bassin_vie_catg: Optional[str] = None
    """Catégorie des bassins de vie 2022 (BV2022)"""

    bassin_vie_catg_libelle: Optional[str] = None
    """Libellé de la catégorie des bassins de vie 2022 (BV2022)"""

    bassin_vie_code_insee: Optional[str] = None
    """Code insee des bassins de vie 2022 (BV2022)"""

    bassin_vie_libelle: Optional[str] = None
    """Libellé des bassins de vie 2022 (BV2022)"""

    code_departement_insee: Optional[str] = None
    """Code departement INSEE"""

    code_iris: Optional[str] = None
    """Code iris INSEE"""

    contrat_relance_trans_eco_code_anct: Optional[str] = None
    """
    Code anct des iris dans le Contrat de relance et de transition écologique (CRTE)
    """

    contrat_relance_trans_eco_libelle: Optional[str] = None
    """
    Libellés des communes/iris dans le Contrat de relance et de transition
    écologique (CRTE)
    """

    en_littoral: Optional[str] = None
    """Iris situé en littoral"""

    en_montagne: Optional[str] = None
    """iris situé en montagne"""

    geom_iris: Optional[str] = None
    """Géométrie de l'IRIS"""

    grille_communale_densite_catg: Optional[str] = None
    """Catégorie de la Grille communale de densité"""

    grille_communale_densite_catg_libelle: Optional[str] = None
    """Libellé de la catégorie de la Grille communale de densité"""

    petites_villes_demain_code_anct: Optional[str] = None
    """Code anct des iris/comunes dans le programme petites villes de demain (PVD)"""

    territoires_industrie_code_anct: Optional[str] = None
    """Code anct - programme territoires d'industrie"""

    territoires_industrie_libelle: Optional[str] = None
    """Libellé - programme territoires d'industrie"""

    unite_urbaine_catg: Optional[str] = None
    """Catégorie des unités urbaines"""

    unite_urbaine_catg_libelle: Optional[str] = None
    """Libellé de la catégorie des unités urbaines"""

    unite_urbaine_code_insee: Optional[str] = None
    """Code INSEE des unités urbaines"""

    unite_urbaine_libelle: Optional[str] = None
    """Libellé des unités urbaines"""

    zone_aide_finalite_reg_catg: Optional[str] = None
    """
    Catégorie des zones dâ€™aides à finalité régionale (AFR) pour la période
    2022-2027
    """

    zone_aide_finalite_reg_code_anct: Optional[str] = None
    """
    Code anct des zones dâ€™aides à finalité régionale (AFR) pour la période
    2022-2027
    """

    zone_emploi_code_insee: Optional[str] = None
    """Code insee des zones d'emploi"""

    zone_emploi_libelle: Optional[str] = None
    """Libellé des zones d'emploi"""
