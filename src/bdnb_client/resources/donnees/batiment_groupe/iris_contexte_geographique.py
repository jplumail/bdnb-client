# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, strip_not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncDefault, AsyncDefault
from ...._base_client import AsyncPaginator, make_request_options
from ....types.donnees.batiment_groupe import iris_contexte_geographique_list_params
from ....types.donnees.batiment_groupe.iris_contexte_geographique import IrisContexteGeographique

__all__ = ["IrisContexteGeographiqueResource", "AsyncIrisContexteGeographiqueResource"]


class IrisContexteGeographiqueResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IrisContexteGeographiqueResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return IrisContexteGeographiqueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IrisContexteGeographiqueResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return IrisContexteGeographiqueResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        action_coeur_ville_code_anct: str | NotGiven = NOT_GIVEN,
        action_coeur_ville_libelle: str | NotGiven = NOT_GIVEN,
        aire_attraction_ville_catg: str | NotGiven = NOT_GIVEN,
        aire_attraction_ville_catg_libelle: str | NotGiven = NOT_GIVEN,
        aire_attraction_ville_code_insee: str | NotGiven = NOT_GIVEN,
        aire_attraction_ville_libelle: str | NotGiven = NOT_GIVEN,
        aire_urbaine_fonctionnelle_eurostat: str | NotGiven = NOT_GIVEN,
        aire_urbaine_fonctionnelle_libelle: str | NotGiven = NOT_GIVEN,
        bassin_vie_catg: str | NotGiven = NOT_GIVEN,
        bassin_vie_catg_libelle: str | NotGiven = NOT_GIVEN,
        bassin_vie_code_insee: str | NotGiven = NOT_GIVEN,
        bassin_vie_libelle: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        code_iris: str | NotGiven = NOT_GIVEN,
        contrat_relance_trans_eco_code_anct: str | NotGiven = NOT_GIVEN,
        contrat_relance_trans_eco_libelle: str | NotGiven = NOT_GIVEN,
        en_littoral: str | NotGiven = NOT_GIVEN,
        en_montagne: str | NotGiven = NOT_GIVEN,
        geom_iris: str | NotGiven = NOT_GIVEN,
        grille_communale_densite_catg: str | NotGiven = NOT_GIVEN,
        grille_communale_densite_catg_libelle: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        petites_villes_demain_code_anct: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        territoires_industrie_code_anct: str | NotGiven = NOT_GIVEN,
        territoires_industrie_libelle: str | NotGiven = NOT_GIVEN,
        unite_urbaine_catg: str | NotGiven = NOT_GIVEN,
        unite_urbaine_catg_libelle: str | NotGiven = NOT_GIVEN,
        unite_urbaine_code_insee: str | NotGiven = NOT_GIVEN,
        unite_urbaine_libelle: str | NotGiven = NOT_GIVEN,
        zone_aide_finalite_reg_catg: str | NotGiven = NOT_GIVEN,
        zone_aide_finalite_reg_code_anct: str | NotGiven = NOT_GIVEN,
        zone_emploi_code_insee: str | NotGiven = NOT_GIVEN,
        zone_emploi_libelle: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[IrisContexteGeographique]:
        """
        Contexte géographique des iris, comme par exemple leur situation géographique et
        la densité urbaine.

        Args:
          action_coeur_ville_code_anct: Code anct des communes sélectionnées pour le programme Action cÅ“ur de ville

          action_coeur_ville_libelle: Libellé des communes sélectionnées pour le programme Action cÅ“ur de ville

          aire_attraction_ville_catg: Catégorie de l'Aire d'Attraction urbaine des Villes (AAV2020) - recensement 2020

          aire_attraction_ville_catg_libelle: Libellé de l'Aire d'Attraction urbaine des Villes (AAV2020) - recensement 2020

          aire_attraction_ville_code_insee: Code insee des Aires d'Attractions urbaines des Villes (AAV2020) - recensement
              2020

          aire_attraction_ville_libelle: Libellé des Aires d'Attractions urbaines des Villes (AAV2020) - recensement 2020

          aire_urbaine_fonctionnelle_eurostat: Code des cities et des aires urbaines fonctionnelles (FUA) - eurostat

          aire_urbaine_fonctionnelle_libelle: Libellé des cities et des aires urbaines fonctionnelles (FUA) - eurostat

          bassin_vie_catg: Catégorie des bassins de vie 2022 (BV2022)

          bassin_vie_catg_libelle: Libellé de la catégorie des bassins de vie 2022 (BV2022)

          bassin_vie_code_insee: Code insee des bassins de vie 2022 (BV2022)

          bassin_vie_libelle: Libellé des bassins de vie 2022 (BV2022)

          code_departement_insee: Code departement INSEE

          code_iris: Code iris INSEE

          contrat_relance_trans_eco_code_anct: Code anct des iris dans le Contrat de relance et de transition écologique (CRTE)

          contrat_relance_trans_eco_libelle: Libellés des communes/iris dans le Contrat de relance et de transition
              écologique (CRTE)

          en_littoral: Iris situé en littoral

          en_montagne: iris situé en montagne

          geom_iris: Géométrie de l'IRIS

          grille_communale_densite_catg: Catégorie de la Grille communale de densité

          grille_communale_densite_catg_libelle: Libellé de la catégorie de la Grille communale de densité

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          petites_villes_demain_code_anct: Code anct des iris/comunes dans le programme petites villes de demain (PVD)

          select: Filtering Columns

          territoires_industrie_code_anct: Code anct - programme territoires d'industrie

          territoires_industrie_libelle: Libellé - programme territoires d'industrie

          unite_urbaine_catg: Catégorie des unités urbaines

          unite_urbaine_catg_libelle: Libellé de la catégorie des unités urbaines

          unite_urbaine_code_insee: Code INSEE des unités urbaines

          unite_urbaine_libelle: Libellé des unités urbaines

          zone_aide_finalite_reg_catg: Catégorie des zones dâ€™aides à finalité régionale (AFR) pour la période
              2022-2027

          zone_aide_finalite_reg_code_anct: Code anct des zones dâ€™aides à finalité régionale (AFR) pour la période
              2022-2027

          zone_emploi_code_insee: Code insee des zones d'emploi

          zone_emploi_libelle: Libellé des zones d'emploi

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get_api_list(
            "/donnees/iris_contexte_geographique",
            page=SyncDefault[IrisContexteGeographique],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action_coeur_ville_code_anct": action_coeur_ville_code_anct,
                        "action_coeur_ville_libelle": action_coeur_ville_libelle,
                        "aire_attraction_ville_catg": aire_attraction_ville_catg,
                        "aire_attraction_ville_catg_libelle": aire_attraction_ville_catg_libelle,
                        "aire_attraction_ville_code_insee": aire_attraction_ville_code_insee,
                        "aire_attraction_ville_libelle": aire_attraction_ville_libelle,
                        "aire_urbaine_fonctionnelle_eurostat": aire_urbaine_fonctionnelle_eurostat,
                        "aire_urbaine_fonctionnelle_libelle": aire_urbaine_fonctionnelle_libelle,
                        "bassin_vie_catg": bassin_vie_catg,
                        "bassin_vie_catg_libelle": bassin_vie_catg_libelle,
                        "bassin_vie_code_insee": bassin_vie_code_insee,
                        "bassin_vie_libelle": bassin_vie_libelle,
                        "code_departement_insee": code_departement_insee,
                        "code_iris": code_iris,
                        "contrat_relance_trans_eco_code_anct": contrat_relance_trans_eco_code_anct,
                        "contrat_relance_trans_eco_libelle": contrat_relance_trans_eco_libelle,
                        "en_littoral": en_littoral,
                        "en_montagne": en_montagne,
                        "geom_iris": geom_iris,
                        "grille_communale_densite_catg": grille_communale_densite_catg,
                        "grille_communale_densite_catg_libelle": grille_communale_densite_catg_libelle,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "petites_villes_demain_code_anct": petites_villes_demain_code_anct,
                        "select": select,
                        "territoires_industrie_code_anct": territoires_industrie_code_anct,
                        "territoires_industrie_libelle": territoires_industrie_libelle,
                        "unite_urbaine_catg": unite_urbaine_catg,
                        "unite_urbaine_catg_libelle": unite_urbaine_catg_libelle,
                        "unite_urbaine_code_insee": unite_urbaine_code_insee,
                        "unite_urbaine_libelle": unite_urbaine_libelle,
                        "zone_aide_finalite_reg_catg": zone_aide_finalite_reg_catg,
                        "zone_aide_finalite_reg_code_anct": zone_aide_finalite_reg_code_anct,
                        "zone_emploi_code_insee": zone_emploi_code_insee,
                        "zone_emploi_libelle": zone_emploi_libelle,
                    },
                    iris_contexte_geographique_list_params.IrisContexteGeographiqueListParams,
                ),
            ),
            model=IrisContexteGeographique,
        )


class AsyncIrisContexteGeographiqueResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIrisContexteGeographiqueResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncIrisContexteGeographiqueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIrisContexteGeographiqueResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncIrisContexteGeographiqueResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        action_coeur_ville_code_anct: str | NotGiven = NOT_GIVEN,
        action_coeur_ville_libelle: str | NotGiven = NOT_GIVEN,
        aire_attraction_ville_catg: str | NotGiven = NOT_GIVEN,
        aire_attraction_ville_catg_libelle: str | NotGiven = NOT_GIVEN,
        aire_attraction_ville_code_insee: str | NotGiven = NOT_GIVEN,
        aire_attraction_ville_libelle: str | NotGiven = NOT_GIVEN,
        aire_urbaine_fonctionnelle_eurostat: str | NotGiven = NOT_GIVEN,
        aire_urbaine_fonctionnelle_libelle: str | NotGiven = NOT_GIVEN,
        bassin_vie_catg: str | NotGiven = NOT_GIVEN,
        bassin_vie_catg_libelle: str | NotGiven = NOT_GIVEN,
        bassin_vie_code_insee: str | NotGiven = NOT_GIVEN,
        bassin_vie_libelle: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        code_iris: str | NotGiven = NOT_GIVEN,
        contrat_relance_trans_eco_code_anct: str | NotGiven = NOT_GIVEN,
        contrat_relance_trans_eco_libelle: str | NotGiven = NOT_GIVEN,
        en_littoral: str | NotGiven = NOT_GIVEN,
        en_montagne: str | NotGiven = NOT_GIVEN,
        geom_iris: str | NotGiven = NOT_GIVEN,
        grille_communale_densite_catg: str | NotGiven = NOT_GIVEN,
        grille_communale_densite_catg_libelle: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        petites_villes_demain_code_anct: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        territoires_industrie_code_anct: str | NotGiven = NOT_GIVEN,
        territoires_industrie_libelle: str | NotGiven = NOT_GIVEN,
        unite_urbaine_catg: str | NotGiven = NOT_GIVEN,
        unite_urbaine_catg_libelle: str | NotGiven = NOT_GIVEN,
        unite_urbaine_code_insee: str | NotGiven = NOT_GIVEN,
        unite_urbaine_libelle: str | NotGiven = NOT_GIVEN,
        zone_aide_finalite_reg_catg: str | NotGiven = NOT_GIVEN,
        zone_aide_finalite_reg_code_anct: str | NotGiven = NOT_GIVEN,
        zone_emploi_code_insee: str | NotGiven = NOT_GIVEN,
        zone_emploi_libelle: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[IrisContexteGeographique, AsyncDefault[IrisContexteGeographique]]:
        """
        Contexte géographique des iris, comme par exemple leur situation géographique et
        la densité urbaine.

        Args:
          action_coeur_ville_code_anct: Code anct des communes sélectionnées pour le programme Action cÅ“ur de ville

          action_coeur_ville_libelle: Libellé des communes sélectionnées pour le programme Action cÅ“ur de ville

          aire_attraction_ville_catg: Catégorie de l'Aire d'Attraction urbaine des Villes (AAV2020) - recensement 2020

          aire_attraction_ville_catg_libelle: Libellé de l'Aire d'Attraction urbaine des Villes (AAV2020) - recensement 2020

          aire_attraction_ville_code_insee: Code insee des Aires d'Attractions urbaines des Villes (AAV2020) - recensement
              2020

          aire_attraction_ville_libelle: Libellé des Aires d'Attractions urbaines des Villes (AAV2020) - recensement 2020

          aire_urbaine_fonctionnelle_eurostat: Code des cities et des aires urbaines fonctionnelles (FUA) - eurostat

          aire_urbaine_fonctionnelle_libelle: Libellé des cities et des aires urbaines fonctionnelles (FUA) - eurostat

          bassin_vie_catg: Catégorie des bassins de vie 2022 (BV2022)

          bassin_vie_catg_libelle: Libellé de la catégorie des bassins de vie 2022 (BV2022)

          bassin_vie_code_insee: Code insee des bassins de vie 2022 (BV2022)

          bassin_vie_libelle: Libellé des bassins de vie 2022 (BV2022)

          code_departement_insee: Code departement INSEE

          code_iris: Code iris INSEE

          contrat_relance_trans_eco_code_anct: Code anct des iris dans le Contrat de relance et de transition écologique (CRTE)

          contrat_relance_trans_eco_libelle: Libellés des communes/iris dans le Contrat de relance et de transition
              écologique (CRTE)

          en_littoral: Iris situé en littoral

          en_montagne: iris situé en montagne

          geom_iris: Géométrie de l'IRIS

          grille_communale_densite_catg: Catégorie de la Grille communale de densité

          grille_communale_densite_catg_libelle: Libellé de la catégorie de la Grille communale de densité

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          petites_villes_demain_code_anct: Code anct des iris/comunes dans le programme petites villes de demain (PVD)

          select: Filtering Columns

          territoires_industrie_code_anct: Code anct - programme territoires d'industrie

          territoires_industrie_libelle: Libellé - programme territoires d'industrie

          unite_urbaine_catg: Catégorie des unités urbaines

          unite_urbaine_catg_libelle: Libellé de la catégorie des unités urbaines

          unite_urbaine_code_insee: Code INSEE des unités urbaines

          unite_urbaine_libelle: Libellé des unités urbaines

          zone_aide_finalite_reg_catg: Catégorie des zones dâ€™aides à finalité régionale (AFR) pour la période
              2022-2027

          zone_aide_finalite_reg_code_anct: Code anct des zones dâ€™aides à finalité régionale (AFR) pour la période
              2022-2027

          zone_emploi_code_insee: Code insee des zones d'emploi

          zone_emploi_libelle: Libellé des zones d'emploi

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get_api_list(
            "/donnees/iris_contexte_geographique",
            page=AsyncDefault[IrisContexteGeographique],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action_coeur_ville_code_anct": action_coeur_ville_code_anct,
                        "action_coeur_ville_libelle": action_coeur_ville_libelle,
                        "aire_attraction_ville_catg": aire_attraction_ville_catg,
                        "aire_attraction_ville_catg_libelle": aire_attraction_ville_catg_libelle,
                        "aire_attraction_ville_code_insee": aire_attraction_ville_code_insee,
                        "aire_attraction_ville_libelle": aire_attraction_ville_libelle,
                        "aire_urbaine_fonctionnelle_eurostat": aire_urbaine_fonctionnelle_eurostat,
                        "aire_urbaine_fonctionnelle_libelle": aire_urbaine_fonctionnelle_libelle,
                        "bassin_vie_catg": bassin_vie_catg,
                        "bassin_vie_catg_libelle": bassin_vie_catg_libelle,
                        "bassin_vie_code_insee": bassin_vie_code_insee,
                        "bassin_vie_libelle": bassin_vie_libelle,
                        "code_departement_insee": code_departement_insee,
                        "code_iris": code_iris,
                        "contrat_relance_trans_eco_code_anct": contrat_relance_trans_eco_code_anct,
                        "contrat_relance_trans_eco_libelle": contrat_relance_trans_eco_libelle,
                        "en_littoral": en_littoral,
                        "en_montagne": en_montagne,
                        "geom_iris": geom_iris,
                        "grille_communale_densite_catg": grille_communale_densite_catg,
                        "grille_communale_densite_catg_libelle": grille_communale_densite_catg_libelle,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "petites_villes_demain_code_anct": petites_villes_demain_code_anct,
                        "select": select,
                        "territoires_industrie_code_anct": territoires_industrie_code_anct,
                        "territoires_industrie_libelle": territoires_industrie_libelle,
                        "unite_urbaine_catg": unite_urbaine_catg,
                        "unite_urbaine_catg_libelle": unite_urbaine_catg_libelle,
                        "unite_urbaine_code_insee": unite_urbaine_code_insee,
                        "unite_urbaine_libelle": unite_urbaine_libelle,
                        "zone_aide_finalite_reg_catg": zone_aide_finalite_reg_catg,
                        "zone_aide_finalite_reg_code_anct": zone_aide_finalite_reg_code_anct,
                        "zone_emploi_code_insee": zone_emploi_code_insee,
                        "zone_emploi_libelle": zone_emploi_libelle,
                    },
                    iris_contexte_geographique_list_params.IrisContexteGeographiqueListParams,
                ),
            ),
            model=IrisContexteGeographique,
        )


class IrisContexteGeographiqueResourceWithRawResponse:
    def __init__(self, iris_contexte_geographique: IrisContexteGeographiqueResource) -> None:
        self._iris_contexte_geographique = iris_contexte_geographique

        self.list = to_raw_response_wrapper(
            iris_contexte_geographique.list,
        )


class AsyncIrisContexteGeographiqueResourceWithRawResponse:
    def __init__(self, iris_contexte_geographique: AsyncIrisContexteGeographiqueResource) -> None:
        self._iris_contexte_geographique = iris_contexte_geographique

        self.list = async_to_raw_response_wrapper(
            iris_contexte_geographique.list,
        )


class IrisContexteGeographiqueResourceWithStreamingResponse:
    def __init__(self, iris_contexte_geographique: IrisContexteGeographiqueResource) -> None:
        self._iris_contexte_geographique = iris_contexte_geographique

        self.list = to_streamed_response_wrapper(
            iris_contexte_geographique.list,
        )


class AsyncIrisContexteGeographiqueResourceWithStreamingResponse:
    def __init__(self, iris_contexte_geographique: AsyncIrisContexteGeographiqueResource) -> None:
        self._iris_contexte_geographique = iris_contexte_geographique

        self.list = async_to_streamed_response_wrapper(
            iris_contexte_geographique.list,
        )
