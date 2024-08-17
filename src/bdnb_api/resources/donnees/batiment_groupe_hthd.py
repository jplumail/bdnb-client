# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.donnees import batiment_groupe_hthd_list_params
from ...types.donnees.batiment_groupe_hthd_list_response import BatimentGroupeHthdListResponse

__all__ = ["BatimentGroupeHthdResource", "AsyncBatimentGroupeHthdResource"]


class BatimentGroupeHthdResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatimentGroupeHthdResourceWithRawResponse:
        return BatimentGroupeHthdResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentGroupeHthdResourceWithStreamingResponse:
        return BatimentGroupeHthdResourceWithStreamingResponse(self)

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
    ) -> BatimentGroupeHthdListResponse:
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
        return self._get(
            "/donnees/batiment_groupe_hthd",
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
                    batiment_groupe_hthd_list_params.BatimentGroupeHthdListParams,
                ),
            ),
            cast_to=BatimentGroupeHthdListResponse,
        )


class AsyncBatimentGroupeHthdResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatimentGroupeHthdResourceWithRawResponse:
        return AsyncBatimentGroupeHthdResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentGroupeHthdResourceWithStreamingResponse:
        return AsyncBatimentGroupeHthdResourceWithStreamingResponse(self)

    async def list(
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
    ) -> BatimentGroupeHthdListResponse:
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
        return await self._get(
            "/donnees/batiment_groupe_hthd",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
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
                    batiment_groupe_hthd_list_params.BatimentGroupeHthdListParams,
                ),
            ),
            cast_to=BatimentGroupeHthdListResponse,
        )


class BatimentGroupeHthdResourceWithRawResponse:
    def __init__(self, batiment_groupe_hthd: BatimentGroupeHthdResource) -> None:
        self._batiment_groupe_hthd = batiment_groupe_hthd

        self.list = to_raw_response_wrapper(
            batiment_groupe_hthd.list,
        )


class AsyncBatimentGroupeHthdResourceWithRawResponse:
    def __init__(self, batiment_groupe_hthd: AsyncBatimentGroupeHthdResource) -> None:
        self._batiment_groupe_hthd = batiment_groupe_hthd

        self.list = async_to_raw_response_wrapper(
            batiment_groupe_hthd.list,
        )


class BatimentGroupeHthdResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_hthd: BatimentGroupeHthdResource) -> None:
        self._batiment_groupe_hthd = batiment_groupe_hthd

        self.list = to_streamed_response_wrapper(
            batiment_groupe_hthd.list,
        )


class AsyncBatimentGroupeHthdResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_hthd: AsyncBatimentGroupeHthdResource) -> None:
        self._batiment_groupe_hthd = batiment_groupe_hthd

        self.list = async_to_streamed_response_wrapper(
            batiment_groupe_hthd.list,
        )
