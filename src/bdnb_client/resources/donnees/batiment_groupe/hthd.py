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
from ....types.donnees.batiment_groupe import hthd_list_params
from ....types.donnees.batiment_groupe.batiment_groupe_hthd import BatimentGroupeHthd

__all__ = ["HthdResource", "AsyncHthdResource"]


class HthdResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HthdResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return HthdResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HthdResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return HthdResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        l_nom_pdl: str | NotGiven = NOT_GIVEN,
        l_type_pdl: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_pdl: str | NotGiven = NOT_GIVEN,
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
    ) -> SyncDefault[BatimentGroupeHthd]:
        """
        Données issues de la base Arcep agrégées à l'échelle du bâtiment

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          l_nom_pdl: (hthd) Liste des noms des points de livraisons centraux

          l_type_pdl: (hthd) Liste de type de bâtiment desservis par les PDL

          limit: Limiting and Pagination

          nb_pdl: (hthd) Nombre total de PDL Arcep

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
            "/donnees/batiment_groupe_hthd",
            page=SyncDefault[BatimentGroupeHthd],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "l_nom_pdl": l_nom_pdl,
                        "l_type_pdl": l_type_pdl,
                        "limit": limit,
                        "nb_pdl": nb_pdl,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    hthd_list_params.HthdListParams,
                ),
            ),
            model=BatimentGroupeHthd,
        )


class AsyncHthdResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHthdResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncHthdResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHthdResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncHthdResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        l_nom_pdl: str | NotGiven = NOT_GIVEN,
        l_type_pdl: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_pdl: str | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[BatimentGroupeHthd, AsyncDefault[BatimentGroupeHthd]]:
        """
        Données issues de la base Arcep agrégées à l'échelle du bâtiment

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          l_nom_pdl: (hthd) Liste des noms des points de livraisons centraux

          l_type_pdl: (hthd) Liste de type de bâtiment desservis par les PDL

          limit: Limiting and Pagination

          nb_pdl: (hthd) Nombre total de PDL Arcep

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
            "/donnees/batiment_groupe_hthd",
            page=AsyncDefault[BatimentGroupeHthd],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "l_nom_pdl": l_nom_pdl,
                        "l_type_pdl": l_type_pdl,
                        "limit": limit,
                        "nb_pdl": nb_pdl,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    hthd_list_params.HthdListParams,
                ),
            ),
            model=BatimentGroupeHthd,
        )


class HthdResourceWithRawResponse:
    def __init__(self, hthd: HthdResource) -> None:
        self._hthd = hthd

        self.list = to_raw_response_wrapper(
            hthd.list,
        )


class AsyncHthdResourceWithRawResponse:
    def __init__(self, hthd: AsyncHthdResource) -> None:
        self._hthd = hthd

        self.list = async_to_raw_response_wrapper(
            hthd.list,
        )


class HthdResourceWithStreamingResponse:
    def __init__(self, hthd: HthdResource) -> None:
        self._hthd = hthd

        self.list = to_streamed_response_wrapper(
            hthd.list,
        )


class AsyncHthdResourceWithStreamingResponse:
    def __init__(self, hthd: AsyncHthdResource) -> None:
        self._hthd = hthd

        self.list = async_to_streamed_response_wrapper(
            hthd.list,
        )
