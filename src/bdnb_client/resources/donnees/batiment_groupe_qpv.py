# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, strip_not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDefault, AsyncDefault
from ..._base_client import AsyncPaginator, make_request_options
from ...types.donnees import batiment_groupe_qpv_list_params
from ...types.donnees.batiment_groupe_qpv import BatimentGroupeQpv

__all__ = ["BatimentGroupeQpvResource", "AsyncBatimentGroupeQpvResource"]


class BatimentGroupeQpvResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatimentGroupeQpvResourceWithRawResponse:
        return BatimentGroupeQpvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentGroupeQpvResourceWithStreamingResponse:
        return BatimentGroupeQpvResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nom_quartier: str | NotGiven = NOT_GIVEN,
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
    ) -> SyncDefault[BatimentGroupeQpv]:
        """
        Informations sur les Quartiers Prioritaires de la Ville agrégées à l'échelle du
        bâtiment

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          limit: Limiting and Pagination

          nom_quartier: Nom du quartier prioritaire dans lequel se trouve le bâtiment

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
            "/donnees/batiment_groupe_qpv",
            page=SyncDefault[BatimentGroupeQpv],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "limit": limit,
                        "nom_quartier": nom_quartier,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    batiment_groupe_qpv_list_params.BatimentGroupeQpvListParams,
                ),
            ),
            model=BatimentGroupeQpv,
        )


class AsyncBatimentGroupeQpvResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatimentGroupeQpvResourceWithRawResponse:
        return AsyncBatimentGroupeQpvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentGroupeQpvResourceWithStreamingResponse:
        return AsyncBatimentGroupeQpvResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nom_quartier: str | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[BatimentGroupeQpv, AsyncDefault[BatimentGroupeQpv]]:
        """
        Informations sur les Quartiers Prioritaires de la Ville agrégées à l'échelle du
        bâtiment

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          limit: Limiting and Pagination

          nom_quartier: Nom du quartier prioritaire dans lequel se trouve le bâtiment

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
            "/donnees/batiment_groupe_qpv",
            page=AsyncDefault[BatimentGroupeQpv],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "limit": limit,
                        "nom_quartier": nom_quartier,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    batiment_groupe_qpv_list_params.BatimentGroupeQpvListParams,
                ),
            ),
            model=BatimentGroupeQpv,
        )


class BatimentGroupeQpvResourceWithRawResponse:
    def __init__(self, batiment_groupe_qpv: BatimentGroupeQpvResource) -> None:
        self._batiment_groupe_qpv = batiment_groupe_qpv

        self.list = to_raw_response_wrapper(
            batiment_groupe_qpv.list,
        )


class AsyncBatimentGroupeQpvResourceWithRawResponse:
    def __init__(self, batiment_groupe_qpv: AsyncBatimentGroupeQpvResource) -> None:
        self._batiment_groupe_qpv = batiment_groupe_qpv

        self.list = async_to_raw_response_wrapper(
            batiment_groupe_qpv.list,
        )


class BatimentGroupeQpvResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_qpv: BatimentGroupeQpvResource) -> None:
        self._batiment_groupe_qpv = batiment_groupe_qpv

        self.list = to_streamed_response_wrapper(
            batiment_groupe_qpv.list,
        )


class AsyncBatimentGroupeQpvResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_qpv: AsyncBatimentGroupeQpvResource) -> None:
        self._batiment_groupe_qpv = batiment_groupe_qpv

        self.list = async_to_streamed_response_wrapper(
            batiment_groupe_qpv.list,
        )
