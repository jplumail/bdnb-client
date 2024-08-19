# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.donnees.batiment_groupe import qpv_list_params
from ....types.donnees.batiment_groupe.qpv_list_response import QpvListResponse

__all__ = ["QpvResource", "AsyncQpvResource"]


class QpvResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QpvResourceWithRawResponse:
        return QpvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QpvResourceWithStreamingResponse:
        return QpvResourceWithStreamingResponse(self)

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
    ) -> QpvListResponse:
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
        return self._get(
            "/donnees/batiment_groupe_qpv",
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
                    qpv_list_params.QpvListParams,
                ),
            ),
            cast_to=QpvListResponse,
        )


class AsyncQpvResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQpvResourceWithRawResponse:
        return AsyncQpvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQpvResourceWithStreamingResponse:
        return AsyncQpvResourceWithStreamingResponse(self)

    async def list(
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
    ) -> QpvListResponse:
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
        return await self._get(
            "/donnees/batiment_groupe_qpv",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "limit": limit,
                        "nom_quartier": nom_quartier,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    qpv_list_params.QpvListParams,
                ),
            ),
            cast_to=QpvListResponse,
        )


class QpvResourceWithRawResponse:
    def __init__(self, qpv: QpvResource) -> None:
        self._qpv = qpv

        self.list = to_raw_response_wrapper(
            qpv.list,
        )


class AsyncQpvResourceWithRawResponse:
    def __init__(self, qpv: AsyncQpvResource) -> None:
        self._qpv = qpv

        self.list = async_to_raw_response_wrapper(
            qpv.list,
        )


class QpvResourceWithStreamingResponse:
    def __init__(self, qpv: QpvResource) -> None:
        self._qpv = qpv

        self.list = to_streamed_response_wrapper(
            qpv.list,
        )


class AsyncQpvResourceWithStreamingResponse:
    def __init__(self, qpv: AsyncQpvResource) -> None:
        self._qpv = qpv

        self.list = async_to_streamed_response_wrapper(
            qpv.list,
        )
