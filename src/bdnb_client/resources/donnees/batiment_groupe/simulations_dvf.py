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
from ....types.donnees.batiment_groupe import simulations_dvf_list_params
from ....types.donnees.batiment_groupe.batiment_groupe_simulations_dvf import BatimentGroupeSimulationsDvf

__all__ = ["SimulationsDvfResource", "AsyncSimulationsDvfResource"]


class SimulationsDvfResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimulationsDvfResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return SimulationsDvfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulationsDvfResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return SimulationsDvfResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        classe_dpe_conso_initial: str | NotGiven = NOT_GIVEN,
        classe_dpe_conso_renove: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        difference_abs_valeur_fonciere_etat_initial_renove: str | NotGiven = NOT_GIVEN,
        difference_rel_valeur_fonciere_etat_initial_renove: str | NotGiven = NOT_GIVEN,
        difference_rel_valeur_fonciere_etat_initial_renove_categorie: str | NotGiven = NOT_GIVEN,
        difference_rel_valeur_fonciere_initial_mean_iris: str | NotGiven = NOT_GIVEN,
        difference_rel_valeur_fonciere_renove_mean_iris: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        r2: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        usage_niveau_1_txt: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_initial_estim_lower: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_initial_estim_mean: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_initial_estim_upper: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_initial_incertitude: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_renove_estim_lower: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_renove_estim_mean: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_renove_estim_upper: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_renove_incertitude: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[BatimentGroupeSimulationsDvf]:
        """
        Simulations des valeurs foncières des bâtiments

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          classe_dpe_conso_initial: classe dpe a l'echelle bâtiment predit dans son etat initial

          classe_dpe_conso_renove: classe dpe a l'echelle bâtiment predit dans son etat renove

          code_departement_insee: Code département INSEE

          difference_abs_valeur_fonciere_etat_initial_renove: difference absolue entre la valeur foncière avant et apres renovation [â‚¬/mÂ²]

          difference_rel_valeur_fonciere_etat_initial_renove: difference relative de valeur fonciere avant et apres renovation

          difference_rel_valeur_fonciere_etat_initial_renove_categorie: categorie de la difference relative de valeur fonciere avant et apres renovation
              (verbose)

          difference_rel_valeur_fonciere_initial_mean_iris: difference relative de la valeur fonciere avant renovation par rapport à la
              moyenne à l'iris predite sans renovation

          difference_rel_valeur_fonciere_renove_mean_iris: difference relative de la valeur fonciere apres renovation par rapport à la
              moyenne à l'iris predite sans renovation

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          r2: r2 du modele de simulation

          select: Filtering Columns

          usage_niveau_1_txt: indicateurs d'usage simplifié du bâtiment (verbose)

          valeur_fonciere_etat_initial_estim_lower: Estimation basse de la valeur fonciere avant renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_initial_estim_mean: Estimation moyenne de la valeur fonciere avant renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_initial_estim_upper: Estimation haute de la valeur fonciere avant renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_initial_incertitude: incertitude de l'estimation de la valeur fonciere avant renovation

          valeur_fonciere_etat_renove_estim_lower: Estimation basse de la valeur fonciere apres renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_renove_estim_mean: Estimation moyenne de la valeur fonciere apres renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_renove_estim_upper: Estimation haute de la valeur fonciere apres renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_renove_incertitude: incertitude de l'estimation de la valeur fonciere apres renovation

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
            "/donnees/batiment_groupe_simulations_dvf",
            page=SyncDefault[BatimentGroupeSimulationsDvf],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "classe_dpe_conso_initial": classe_dpe_conso_initial,
                        "classe_dpe_conso_renove": classe_dpe_conso_renove,
                        "code_departement_insee": code_departement_insee,
                        "difference_abs_valeur_fonciere_etat_initial_renove": difference_abs_valeur_fonciere_etat_initial_renove,
                        "difference_rel_valeur_fonciere_etat_initial_renove": difference_rel_valeur_fonciere_etat_initial_renove,
                        "difference_rel_valeur_fonciere_etat_initial_renove_categorie": difference_rel_valeur_fonciere_etat_initial_renove_categorie,
                        "difference_rel_valeur_fonciere_initial_mean_iris": difference_rel_valeur_fonciere_initial_mean_iris,
                        "difference_rel_valeur_fonciere_renove_mean_iris": difference_rel_valeur_fonciere_renove_mean_iris,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "r2": r2,
                        "select": select,
                        "usage_niveau_1_txt": usage_niveau_1_txt,
                        "valeur_fonciere_etat_initial_estim_lower": valeur_fonciere_etat_initial_estim_lower,
                        "valeur_fonciere_etat_initial_estim_mean": valeur_fonciere_etat_initial_estim_mean,
                        "valeur_fonciere_etat_initial_estim_upper": valeur_fonciere_etat_initial_estim_upper,
                        "valeur_fonciere_etat_initial_incertitude": valeur_fonciere_etat_initial_incertitude,
                        "valeur_fonciere_etat_renove_estim_lower": valeur_fonciere_etat_renove_estim_lower,
                        "valeur_fonciere_etat_renove_estim_mean": valeur_fonciere_etat_renove_estim_mean,
                        "valeur_fonciere_etat_renove_estim_upper": valeur_fonciere_etat_renove_estim_upper,
                        "valeur_fonciere_etat_renove_incertitude": valeur_fonciere_etat_renove_incertitude,
                    },
                    simulations_dvf_list_params.SimulationsDvfListParams,
                ),
            ),
            model=BatimentGroupeSimulationsDvf,
        )


class AsyncSimulationsDvfResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimulationsDvfResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncSimulationsDvfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulationsDvfResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncSimulationsDvfResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        classe_dpe_conso_initial: str | NotGiven = NOT_GIVEN,
        classe_dpe_conso_renove: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        difference_abs_valeur_fonciere_etat_initial_renove: str | NotGiven = NOT_GIVEN,
        difference_rel_valeur_fonciere_etat_initial_renove: str | NotGiven = NOT_GIVEN,
        difference_rel_valeur_fonciere_etat_initial_renove_categorie: str | NotGiven = NOT_GIVEN,
        difference_rel_valeur_fonciere_initial_mean_iris: str | NotGiven = NOT_GIVEN,
        difference_rel_valeur_fonciere_renove_mean_iris: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        r2: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        usage_niveau_1_txt: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_initial_estim_lower: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_initial_estim_mean: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_initial_estim_upper: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_initial_incertitude: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_renove_estim_lower: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_renove_estim_mean: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_renove_estim_upper: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_renove_incertitude: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BatimentGroupeSimulationsDvf, AsyncDefault[BatimentGroupeSimulationsDvf]]:
        """
        Simulations des valeurs foncières des bâtiments

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          classe_dpe_conso_initial: classe dpe a l'echelle bâtiment predit dans son etat initial

          classe_dpe_conso_renove: classe dpe a l'echelle bâtiment predit dans son etat renove

          code_departement_insee: Code département INSEE

          difference_abs_valeur_fonciere_etat_initial_renove: difference absolue entre la valeur foncière avant et apres renovation [â‚¬/mÂ²]

          difference_rel_valeur_fonciere_etat_initial_renove: difference relative de valeur fonciere avant et apres renovation

          difference_rel_valeur_fonciere_etat_initial_renove_categorie: categorie de la difference relative de valeur fonciere avant et apres renovation
              (verbose)

          difference_rel_valeur_fonciere_initial_mean_iris: difference relative de la valeur fonciere avant renovation par rapport à la
              moyenne à l'iris predite sans renovation

          difference_rel_valeur_fonciere_renove_mean_iris: difference relative de la valeur fonciere apres renovation par rapport à la
              moyenne à l'iris predite sans renovation

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          r2: r2 du modele de simulation

          select: Filtering Columns

          usage_niveau_1_txt: indicateurs d'usage simplifié du bâtiment (verbose)

          valeur_fonciere_etat_initial_estim_lower: Estimation basse de la valeur fonciere avant renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_initial_estim_mean: Estimation moyenne de la valeur fonciere avant renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_initial_estim_upper: Estimation haute de la valeur fonciere avant renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_initial_incertitude: incertitude de l'estimation de la valeur fonciere avant renovation

          valeur_fonciere_etat_renove_estim_lower: Estimation basse de la valeur fonciere apres renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_renove_estim_mean: Estimation moyenne de la valeur fonciere apres renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_renove_estim_upper: Estimation haute de la valeur fonciere apres renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_renove_incertitude: incertitude de l'estimation de la valeur fonciere apres renovation

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
            "/donnees/batiment_groupe_simulations_dvf",
            page=AsyncDefault[BatimentGroupeSimulationsDvf],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "classe_dpe_conso_initial": classe_dpe_conso_initial,
                        "classe_dpe_conso_renove": classe_dpe_conso_renove,
                        "code_departement_insee": code_departement_insee,
                        "difference_abs_valeur_fonciere_etat_initial_renove": difference_abs_valeur_fonciere_etat_initial_renove,
                        "difference_rel_valeur_fonciere_etat_initial_renove": difference_rel_valeur_fonciere_etat_initial_renove,
                        "difference_rel_valeur_fonciere_etat_initial_renove_categorie": difference_rel_valeur_fonciere_etat_initial_renove_categorie,
                        "difference_rel_valeur_fonciere_initial_mean_iris": difference_rel_valeur_fonciere_initial_mean_iris,
                        "difference_rel_valeur_fonciere_renove_mean_iris": difference_rel_valeur_fonciere_renove_mean_iris,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "r2": r2,
                        "select": select,
                        "usage_niveau_1_txt": usage_niveau_1_txt,
                        "valeur_fonciere_etat_initial_estim_lower": valeur_fonciere_etat_initial_estim_lower,
                        "valeur_fonciere_etat_initial_estim_mean": valeur_fonciere_etat_initial_estim_mean,
                        "valeur_fonciere_etat_initial_estim_upper": valeur_fonciere_etat_initial_estim_upper,
                        "valeur_fonciere_etat_initial_incertitude": valeur_fonciere_etat_initial_incertitude,
                        "valeur_fonciere_etat_renove_estim_lower": valeur_fonciere_etat_renove_estim_lower,
                        "valeur_fonciere_etat_renove_estim_mean": valeur_fonciere_etat_renove_estim_mean,
                        "valeur_fonciere_etat_renove_estim_upper": valeur_fonciere_etat_renove_estim_upper,
                        "valeur_fonciere_etat_renove_incertitude": valeur_fonciere_etat_renove_incertitude,
                    },
                    simulations_dvf_list_params.SimulationsDvfListParams,
                ),
            ),
            model=BatimentGroupeSimulationsDvf,
        )


class SimulationsDvfResourceWithRawResponse:
    def __init__(self, simulations_dvf: SimulationsDvfResource) -> None:
        self._simulations_dvf = simulations_dvf

        self.list = to_raw_response_wrapper(
            simulations_dvf.list,
        )


class AsyncSimulationsDvfResourceWithRawResponse:
    def __init__(self, simulations_dvf: AsyncSimulationsDvfResource) -> None:
        self._simulations_dvf = simulations_dvf

        self.list = async_to_raw_response_wrapper(
            simulations_dvf.list,
        )


class SimulationsDvfResourceWithStreamingResponse:
    def __init__(self, simulations_dvf: SimulationsDvfResource) -> None:
        self._simulations_dvf = simulations_dvf

        self.list = to_streamed_response_wrapper(
            simulations_dvf.list,
        )


class AsyncSimulationsDvfResourceWithStreamingResponse:
    def __init__(self, simulations_dvf: AsyncSimulationsDvfResource) -> None:
        self._simulations_dvf = simulations_dvf

        self.list = async_to_streamed_response_wrapper(
            simulations_dvf.list,
        )
