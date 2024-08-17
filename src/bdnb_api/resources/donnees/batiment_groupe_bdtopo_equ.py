# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    is_given,
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
from ...types.donnees import batiment_groupe_bdtopo_equ_list_params
from ...types.donnees.batiment_groupe_bdtopo_equ_list_response import BatimentGroupeBdtopoEquListResponse

__all__ = ["BatimentGroupeBdtopoEquResource", "AsyncBatimentGroupeBdtopoEquResource"]


class BatimentGroupeBdtopoEquResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatimentGroupeBdtopoEquResourceWithRawResponse:
        return BatimentGroupeBdtopoEquResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentGroupeBdtopoEquResourceWithStreamingResponse:
        return BatimentGroupeBdtopoEquResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        l_nature: str | NotGiven = NOT_GIVEN,
        l_nature_detaillee: str | NotGiven = NOT_GIVEN,
        l_toponyme: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatimentGroupeBdtopoEquListResponse:
        """
        Informations de la BDTopo, couche équipement, agrégées à l'échelle du bâtiment

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          l_nature: (ign) Catégorie de nature du bâtiment

          l_nature_detaillee: (ign) Catégorie détaillée de nature de l'équipement

          l_toponyme: (ign) Toponymie de l'équipement

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
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/donnees/batiment_groupe_bdtopo_equ",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "l_nature": l_nature,
                        "l_nature_detaillee": l_nature_detaillee,
                        "l_toponyme": l_toponyme,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    batiment_groupe_bdtopo_equ_list_params.BatimentGroupeBdtopoEquListParams,
                ),
            ),
            cast_to=BatimentGroupeBdtopoEquListResponse,
        )


class AsyncBatimentGroupeBdtopoEquResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatimentGroupeBdtopoEquResourceWithRawResponse:
        return AsyncBatimentGroupeBdtopoEquResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentGroupeBdtopoEquResourceWithStreamingResponse:
        return AsyncBatimentGroupeBdtopoEquResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        l_nature: str | NotGiven = NOT_GIVEN,
        l_nature_detaillee: str | NotGiven = NOT_GIVEN,
        l_toponyme: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatimentGroupeBdtopoEquListResponse:
        """
        Informations de la BDTopo, couche équipement, agrégées à l'échelle du bâtiment

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          l_nature: (ign) Catégorie de nature du bâtiment

          l_nature_detaillee: (ign) Catégorie détaillée de nature de l'équipement

          l_toponyme: (ign) Toponymie de l'équipement

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
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            "/donnees/batiment_groupe_bdtopo_equ",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "l_nature": l_nature,
                        "l_nature_detaillee": l_nature_detaillee,
                        "l_toponyme": l_toponyme,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    batiment_groupe_bdtopo_equ_list_params.BatimentGroupeBdtopoEquListParams,
                ),
            ),
            cast_to=BatimentGroupeBdtopoEquListResponse,
        )


class BatimentGroupeBdtopoEquResourceWithRawResponse:
    def __init__(self, batiment_groupe_bdtopo_equ: BatimentGroupeBdtopoEquResource) -> None:
        self._batiment_groupe_bdtopo_equ = batiment_groupe_bdtopo_equ

        self.list = to_raw_response_wrapper(
            batiment_groupe_bdtopo_equ.list,
        )


class AsyncBatimentGroupeBdtopoEquResourceWithRawResponse:
    def __init__(self, batiment_groupe_bdtopo_equ: AsyncBatimentGroupeBdtopoEquResource) -> None:
        self._batiment_groupe_bdtopo_equ = batiment_groupe_bdtopo_equ

        self.list = async_to_raw_response_wrapper(
            batiment_groupe_bdtopo_equ.list,
        )


class BatimentGroupeBdtopoEquResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_bdtopo_equ: BatimentGroupeBdtopoEquResource) -> None:
        self._batiment_groupe_bdtopo_equ = batiment_groupe_bdtopo_equ

        self.list = to_streamed_response_wrapper(
            batiment_groupe_bdtopo_equ.list,
        )


class AsyncBatimentGroupeBdtopoEquResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_bdtopo_equ: AsyncBatimentGroupeBdtopoEquResource) -> None:
        self._batiment_groupe_bdtopo_equ = batiment_groupe_bdtopo_equ

        self.list = async_to_streamed_response_wrapper(
            batiment_groupe_bdtopo_equ.list,
        )