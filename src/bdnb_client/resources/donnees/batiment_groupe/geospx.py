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
from ....types.donnees.batiment_groupe import geospx_list_params
from ....types.donnees.batiment_groupe.batiment_groupe_geospx import BatimentGroupeGeospx

__all__ = ["GeospxResource", "AsyncGeospxResource"]


class GeospxResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GeospxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return GeospxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GeospxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return GeospxResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        croisement_geospx_reussi: str | NotGiven = NOT_GIVEN,
        fiabilite_adresse: str | NotGiven = NOT_GIVEN,
        fiabilite_emprise_sol: str | NotGiven = NOT_GIVEN,
        fiabilite_hauteur: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[BatimentGroupeGeospx]:
        """
        Métriques du bâtiment par rapport à son environnement géospatial.

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          croisement_geospx_reussi: le croisement géospatial entre la BDTOPO et les fichiers fonciers est considérée
              comme réussi

          fiabilite_adresse: Fiabilité des adresses du bâtiment : "vrai" si les Fichiers Fonciers et BDTOpo
              partagent au moins une màªme adresse BAN

          fiabilite_emprise_sol: Fiabilité de l'emprise au sol du bâtiment

          fiabilite_hauteur: Fiabilité de la hauteur du bâtiment

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

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
            "/donnees/batiment_groupe_geospx",
            page=SyncDefault[BatimentGroupeGeospx],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "croisement_geospx_reussi": croisement_geospx_reussi,
                        "fiabilite_adresse": fiabilite_adresse,
                        "fiabilite_emprise_sol": fiabilite_emprise_sol,
                        "fiabilite_hauteur": fiabilite_hauteur,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    geospx_list_params.GeospxListParams,
                ),
            ),
            model=BatimentGroupeGeospx,
        )


class AsyncGeospxResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGeospxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncGeospxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGeospxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncGeospxResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        croisement_geospx_reussi: str | NotGiven = NOT_GIVEN,
        fiabilite_adresse: str | NotGiven = NOT_GIVEN,
        fiabilite_emprise_sol: str | NotGiven = NOT_GIVEN,
        fiabilite_hauteur: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BatimentGroupeGeospx, AsyncDefault[BatimentGroupeGeospx]]:
        """
        Métriques du bâtiment par rapport à son environnement géospatial.

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          croisement_geospx_reussi: le croisement géospatial entre la BDTOPO et les fichiers fonciers est considérée
              comme réussi

          fiabilite_adresse: Fiabilité des adresses du bâtiment : "vrai" si les Fichiers Fonciers et BDTOpo
              partagent au moins une màªme adresse BAN

          fiabilite_emprise_sol: Fiabilité de l'emprise au sol du bâtiment

          fiabilite_hauteur: Fiabilité de la hauteur du bâtiment

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

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
            "/donnees/batiment_groupe_geospx",
            page=AsyncDefault[BatimentGroupeGeospx],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "croisement_geospx_reussi": croisement_geospx_reussi,
                        "fiabilite_adresse": fiabilite_adresse,
                        "fiabilite_emprise_sol": fiabilite_emprise_sol,
                        "fiabilite_hauteur": fiabilite_hauteur,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    geospx_list_params.GeospxListParams,
                ),
            ),
            model=BatimentGroupeGeospx,
        )


class GeospxResourceWithRawResponse:
    def __init__(self, geospx: GeospxResource) -> None:
        self._geospx = geospx

        self.list = to_raw_response_wrapper(
            geospx.list,
        )


class AsyncGeospxResourceWithRawResponse:
    def __init__(self, geospx: AsyncGeospxResource) -> None:
        self._geospx = geospx

        self.list = async_to_raw_response_wrapper(
            geospx.list,
        )


class GeospxResourceWithStreamingResponse:
    def __init__(self, geospx: GeospxResource) -> None:
        self._geospx = geospx

        self.list = to_streamed_response_wrapper(
            geospx.list,
        )


class AsyncGeospxResourceWithStreamingResponse:
    def __init__(self, geospx: AsyncGeospxResource) -> None:
        self._geospx = geospx

        self.list = async_to_streamed_response_wrapper(
            geospx.list,
        )
