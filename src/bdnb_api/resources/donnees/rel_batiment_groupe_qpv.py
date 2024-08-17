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
from ...types.donnees import rel_batiment_groupe_qpv_list_params
from ...types.donnees.rel_batiment_groupe_qpv_list_response import RelBatimentGroupeQpvListResponse

__all__ = ["RelBatimentGroupeQpvResource", "AsyncRelBatimentGroupeQpvResource"]


class RelBatimentGroupeQpvResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RelBatimentGroupeQpvResourceWithRawResponse:
        return RelBatimentGroupeQpvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RelBatimentGroupeQpvResourceWithStreamingResponse:
        return RelBatimentGroupeQpvResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_construction_id: str | NotGiven = NOT_GIVEN,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        qpv_code_qp: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RelBatimentGroupeQpvListResponse:
        """
        Table de relation entre les bâtiments de la BDNB et les éléments de la table QPV

        Args:
          batiment_construction_id: Identifiant unique du bâtiment physique de la BDNB -> cleabs (ign) + index de
              sub-division (si construction sur plusieurs parcelles)

          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          qpv_code_qp: identifiant de la table qpv

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
            "/donnees/rel_batiment_groupe_qpv",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_construction_id": batiment_construction_id,
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "qpv_code_qp": qpv_code_qp,
                        "select": select,
                    },
                    rel_batiment_groupe_qpv_list_params.RelBatimentGroupeQpvListParams,
                ),
            ),
            cast_to=RelBatimentGroupeQpvListResponse,
        )


class AsyncRelBatimentGroupeQpvResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRelBatimentGroupeQpvResourceWithRawResponse:
        return AsyncRelBatimentGroupeQpvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRelBatimentGroupeQpvResourceWithStreamingResponse:
        return AsyncRelBatimentGroupeQpvResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        batiment_construction_id: str | NotGiven = NOT_GIVEN,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        qpv_code_qp: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RelBatimentGroupeQpvListResponse:
        """
        Table de relation entre les bâtiments de la BDNB et les éléments de la table QPV

        Args:
          batiment_construction_id: Identifiant unique du bâtiment physique de la BDNB -> cleabs (ign) + index de
              sub-division (si construction sur plusieurs parcelles)

          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          qpv_code_qp: identifiant de la table qpv

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
            "/donnees/rel_batiment_groupe_qpv",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "batiment_construction_id": batiment_construction_id,
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "qpv_code_qp": qpv_code_qp,
                        "select": select,
                    },
                    rel_batiment_groupe_qpv_list_params.RelBatimentGroupeQpvListParams,
                ),
            ),
            cast_to=RelBatimentGroupeQpvListResponse,
        )


class RelBatimentGroupeQpvResourceWithRawResponse:
    def __init__(self, rel_batiment_groupe_qpv: RelBatimentGroupeQpvResource) -> None:
        self._rel_batiment_groupe_qpv = rel_batiment_groupe_qpv

        self.list = to_raw_response_wrapper(
            rel_batiment_groupe_qpv.list,
        )


class AsyncRelBatimentGroupeQpvResourceWithRawResponse:
    def __init__(self, rel_batiment_groupe_qpv: AsyncRelBatimentGroupeQpvResource) -> None:
        self._rel_batiment_groupe_qpv = rel_batiment_groupe_qpv

        self.list = async_to_raw_response_wrapper(
            rel_batiment_groupe_qpv.list,
        )


class RelBatimentGroupeQpvResourceWithStreamingResponse:
    def __init__(self, rel_batiment_groupe_qpv: RelBatimentGroupeQpvResource) -> None:
        self._rel_batiment_groupe_qpv = rel_batiment_groupe_qpv

        self.list = to_streamed_response_wrapper(
            rel_batiment_groupe_qpv.list,
        )


class AsyncRelBatimentGroupeQpvResourceWithStreamingResponse:
    def __init__(self, rel_batiment_groupe_qpv: AsyncRelBatimentGroupeQpvResource) -> None:
        self._rel_batiment_groupe_qpv = rel_batiment_groupe_qpv

        self.list = async_to_streamed_response_wrapper(
            rel_batiment_groupe_qpv.list,
        )
