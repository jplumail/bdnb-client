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
from ....types.donnees.batiment_groupe import iris_simulations_valeur_verte_list_params
from ....types.donnees.batiment_groupe.iris_simulations_valeur_verte import IrisSimulationsValeurVerte

__all__ = ["IrisSimulationsValeurVerteResource", "AsyncIrisSimulationsValeurVerteResource"]


class IrisSimulationsValeurVerteResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IrisSimulationsValeurVerteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return IrisSimulationsValeurVerteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IrisSimulationsValeurVerteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return IrisSimulationsValeurVerteResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        gain_classe_b_vers_a: float | NotGiven = NOT_GIVEN,
        gain_classe_c_vers_a: object | NotGiven = NOT_GIVEN,
        gain_classe_c_vers_b: object | NotGiven = NOT_GIVEN,
        gain_classe_d_vers_a: object | NotGiven = NOT_GIVEN,
        gain_classe_d_vers_b: object | NotGiven = NOT_GIVEN,
        gain_classe_d_vers_c: object | NotGiven = NOT_GIVEN,
        gain_classe_e_vers_a: object | NotGiven = NOT_GIVEN,
        gain_classe_e_vers_b: object | NotGiven = NOT_GIVEN,
        gain_classe_e_vers_c: object | NotGiven = NOT_GIVEN,
        gain_classe_e_vers_d: object | NotGiven = NOT_GIVEN,
        gain_classe_f_vers_a: object | NotGiven = NOT_GIVEN,
        gain_classe_f_vers_b: object | NotGiven = NOT_GIVEN,
        gain_classe_f_vers_c: object | NotGiven = NOT_GIVEN,
        gain_classe_f_vers_d: object | NotGiven = NOT_GIVEN,
        gain_classe_f_vers_e: object | NotGiven = NOT_GIVEN,
        gain_classe_g_vers_a: object | NotGiven = NOT_GIVEN,
        gain_classe_g_vers_b: object | NotGiven = NOT_GIVEN,
        gain_classe_g_vers_c: object | NotGiven = NOT_GIVEN,
        gain_classe_g_vers_d: object | NotGiven = NOT_GIVEN,
        gain_classe_g_vers_e: object | NotGiven = NOT_GIVEN,
        gain_classe_g_vers_f: object | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        renovation: float | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[IrisSimulationsValeurVerte]:
        """
        Simulation des gains en valeur foncière liés à un potentiel changement de classe
        DPE pour un logement du bâtiment (en valeur relative)

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          gain_classe_b_vers_a: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE B vers A.

          gain_classe_c_vers_a: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE C vers A.

          gain_classe_c_vers_b: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE C vers B.

          gain_classe_d_vers_a: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE D vers A.

          gain_classe_d_vers_b: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE D vers B.

          gain_classe_d_vers_c: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE D vers C.

          gain_classe_e_vers_a: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE E vers A.

          gain_classe_e_vers_b: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE E vers B.

          gain_classe_e_vers_c: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE E vers C.

          gain_classe_e_vers_d: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE E vers D.

          gain_classe_f_vers_a: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE F vers A.

          gain_classe_f_vers_b: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE F vers B.

          gain_classe_f_vers_c: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE F vers C.

          gain_classe_f_vers_d: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE F vers D.

          gain_classe_f_vers_e: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE F vers E.

          gain_classe_g_vers_a: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE G vers A.

          gain_classe_g_vers_b: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE G vers B.

          gain_classe_g_vers_c: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE G vers C.

          gain_classe_g_vers_d: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE G vers D.

          gain_classe_g_vers_e: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE G vers E.

          gain_classe_g_vers_f: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE G vers F.

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          renovation: (simulations) gain en % de la valeur immobilière lorsqu'on simule une
              rénovation.

          select: Filtering Columns

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
            "/donnees/iris_simulations_valeur_verte",
            page=SyncDefault[IrisSimulationsValeurVerte],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "gain_classe_b_vers_a": gain_classe_b_vers_a,
                        "gain_classe_c_vers_a": gain_classe_c_vers_a,
                        "gain_classe_c_vers_b": gain_classe_c_vers_b,
                        "gain_classe_d_vers_a": gain_classe_d_vers_a,
                        "gain_classe_d_vers_b": gain_classe_d_vers_b,
                        "gain_classe_d_vers_c": gain_classe_d_vers_c,
                        "gain_classe_e_vers_a": gain_classe_e_vers_a,
                        "gain_classe_e_vers_b": gain_classe_e_vers_b,
                        "gain_classe_e_vers_c": gain_classe_e_vers_c,
                        "gain_classe_e_vers_d": gain_classe_e_vers_d,
                        "gain_classe_f_vers_a": gain_classe_f_vers_a,
                        "gain_classe_f_vers_b": gain_classe_f_vers_b,
                        "gain_classe_f_vers_c": gain_classe_f_vers_c,
                        "gain_classe_f_vers_d": gain_classe_f_vers_d,
                        "gain_classe_f_vers_e": gain_classe_f_vers_e,
                        "gain_classe_g_vers_a": gain_classe_g_vers_a,
                        "gain_classe_g_vers_b": gain_classe_g_vers_b,
                        "gain_classe_g_vers_c": gain_classe_g_vers_c,
                        "gain_classe_g_vers_d": gain_classe_g_vers_d,
                        "gain_classe_g_vers_e": gain_classe_g_vers_e,
                        "gain_classe_g_vers_f": gain_classe_g_vers_f,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "renovation": renovation,
                        "select": select,
                    },
                    iris_simulations_valeur_verte_list_params.IrisSimulationsValeurVerteListParams,
                ),
            ),
            model=IrisSimulationsValeurVerte,
        )


class AsyncIrisSimulationsValeurVerteResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIrisSimulationsValeurVerteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncIrisSimulationsValeurVerteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIrisSimulationsValeurVerteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncIrisSimulationsValeurVerteResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        gain_classe_b_vers_a: float | NotGiven = NOT_GIVEN,
        gain_classe_c_vers_a: object | NotGiven = NOT_GIVEN,
        gain_classe_c_vers_b: object | NotGiven = NOT_GIVEN,
        gain_classe_d_vers_a: object | NotGiven = NOT_GIVEN,
        gain_classe_d_vers_b: object | NotGiven = NOT_GIVEN,
        gain_classe_d_vers_c: object | NotGiven = NOT_GIVEN,
        gain_classe_e_vers_a: object | NotGiven = NOT_GIVEN,
        gain_classe_e_vers_b: object | NotGiven = NOT_GIVEN,
        gain_classe_e_vers_c: object | NotGiven = NOT_GIVEN,
        gain_classe_e_vers_d: object | NotGiven = NOT_GIVEN,
        gain_classe_f_vers_a: object | NotGiven = NOT_GIVEN,
        gain_classe_f_vers_b: object | NotGiven = NOT_GIVEN,
        gain_classe_f_vers_c: object | NotGiven = NOT_GIVEN,
        gain_classe_f_vers_d: object | NotGiven = NOT_GIVEN,
        gain_classe_f_vers_e: object | NotGiven = NOT_GIVEN,
        gain_classe_g_vers_a: object | NotGiven = NOT_GIVEN,
        gain_classe_g_vers_b: object | NotGiven = NOT_GIVEN,
        gain_classe_g_vers_c: object | NotGiven = NOT_GIVEN,
        gain_classe_g_vers_d: object | NotGiven = NOT_GIVEN,
        gain_classe_g_vers_e: object | NotGiven = NOT_GIVEN,
        gain_classe_g_vers_f: object | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        renovation: float | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[IrisSimulationsValeurVerte, AsyncDefault[IrisSimulationsValeurVerte]]:
        """
        Simulation des gains en valeur foncière liés à un potentiel changement de classe
        DPE pour un logement du bâtiment (en valeur relative)

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          gain_classe_b_vers_a: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE B vers A.

          gain_classe_c_vers_a: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE C vers A.

          gain_classe_c_vers_b: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE C vers B.

          gain_classe_d_vers_a: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE D vers A.

          gain_classe_d_vers_b: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE D vers B.

          gain_classe_d_vers_c: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE D vers C.

          gain_classe_e_vers_a: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE E vers A.

          gain_classe_e_vers_b: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE E vers B.

          gain_classe_e_vers_c: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE E vers C.

          gain_classe_e_vers_d: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE E vers D.

          gain_classe_f_vers_a: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE F vers A.

          gain_classe_f_vers_b: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE F vers B.

          gain_classe_f_vers_c: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE F vers C.

          gain_classe_f_vers_d: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE F vers D.

          gain_classe_f_vers_e: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE F vers E.

          gain_classe_g_vers_a: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE G vers A.

          gain_classe_g_vers_b: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE G vers B.

          gain_classe_g_vers_c: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE G vers C.

          gain_classe_g_vers_d: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE G vers D.

          gain_classe_g_vers_e: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE G vers E.

          gain_classe_g_vers_f: (simulations) gain en % de la valeur immobilière lorsqu'on simule le changement
              de DPE G vers F.

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          renovation: (simulations) gain en % de la valeur immobilière lorsqu'on simule une
              rénovation.

          select: Filtering Columns

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
            "/donnees/iris_simulations_valeur_verte",
            page=AsyncDefault[IrisSimulationsValeurVerte],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "gain_classe_b_vers_a": gain_classe_b_vers_a,
                        "gain_classe_c_vers_a": gain_classe_c_vers_a,
                        "gain_classe_c_vers_b": gain_classe_c_vers_b,
                        "gain_classe_d_vers_a": gain_classe_d_vers_a,
                        "gain_classe_d_vers_b": gain_classe_d_vers_b,
                        "gain_classe_d_vers_c": gain_classe_d_vers_c,
                        "gain_classe_e_vers_a": gain_classe_e_vers_a,
                        "gain_classe_e_vers_b": gain_classe_e_vers_b,
                        "gain_classe_e_vers_c": gain_classe_e_vers_c,
                        "gain_classe_e_vers_d": gain_classe_e_vers_d,
                        "gain_classe_f_vers_a": gain_classe_f_vers_a,
                        "gain_classe_f_vers_b": gain_classe_f_vers_b,
                        "gain_classe_f_vers_c": gain_classe_f_vers_c,
                        "gain_classe_f_vers_d": gain_classe_f_vers_d,
                        "gain_classe_f_vers_e": gain_classe_f_vers_e,
                        "gain_classe_g_vers_a": gain_classe_g_vers_a,
                        "gain_classe_g_vers_b": gain_classe_g_vers_b,
                        "gain_classe_g_vers_c": gain_classe_g_vers_c,
                        "gain_classe_g_vers_d": gain_classe_g_vers_d,
                        "gain_classe_g_vers_e": gain_classe_g_vers_e,
                        "gain_classe_g_vers_f": gain_classe_g_vers_f,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "renovation": renovation,
                        "select": select,
                    },
                    iris_simulations_valeur_verte_list_params.IrisSimulationsValeurVerteListParams,
                ),
            ),
            model=IrisSimulationsValeurVerte,
        )


class IrisSimulationsValeurVerteResourceWithRawResponse:
    def __init__(self, iris_simulations_valeur_verte: IrisSimulationsValeurVerteResource) -> None:
        self._iris_simulations_valeur_verte = iris_simulations_valeur_verte

        self.list = to_raw_response_wrapper(
            iris_simulations_valeur_verte.list,
        )


class AsyncIrisSimulationsValeurVerteResourceWithRawResponse:
    def __init__(self, iris_simulations_valeur_verte: AsyncIrisSimulationsValeurVerteResource) -> None:
        self._iris_simulations_valeur_verte = iris_simulations_valeur_verte

        self.list = async_to_raw_response_wrapper(
            iris_simulations_valeur_verte.list,
        )


class IrisSimulationsValeurVerteResourceWithStreamingResponse:
    def __init__(self, iris_simulations_valeur_verte: IrisSimulationsValeurVerteResource) -> None:
        self._iris_simulations_valeur_verte = iris_simulations_valeur_verte

        self.list = to_streamed_response_wrapper(
            iris_simulations_valeur_verte.list,
        )


class AsyncIrisSimulationsValeurVerteResourceWithStreamingResponse:
    def __init__(self, iris_simulations_valeur_verte: AsyncIrisSimulationsValeurVerteResource) -> None:
        self._iris_simulations_valeur_verte = iris_simulations_valeur_verte

        self.list = async_to_streamed_response_wrapper(
            iris_simulations_valeur_verte.list,
        )
