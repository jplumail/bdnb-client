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
from ...types.donnees import batiment_groupe_radon_list_params
from ...types.donnees.batiment_groupe_radon_api_expert import BatimentGroupeRadonAPIExpert

__all__ = ["BatimentGroupeRadonResource", "AsyncBatimentGroupeRadonResource"]


class BatimentGroupeRadonResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatimentGroupeRadonResourceWithRawResponse:
        return BatimentGroupeRadonResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentGroupeRadonResourceWithStreamingResponse:
        return BatimentGroupeRadonResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        alea: str | NotGiven = NOT_GIVEN,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
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
    ) -> SyncDefault[BatimentGroupeRadonAPIExpert]:
        """
        Informations sur l'aléa Radon à l'échelle du bâtiment

        Args:
          alea: (radon) alea du risque radon

          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

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
            "/donnees/batiment_groupe_radon",
            page=SyncDefault[BatimentGroupeRadonAPIExpert],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "alea": alea,
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    batiment_groupe_radon_list_params.BatimentGroupeRadonListParams,
                ),
            ),
            model=BatimentGroupeRadonAPIExpert,
        )


class AsyncBatimentGroupeRadonResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatimentGroupeRadonResourceWithRawResponse:
        return AsyncBatimentGroupeRadonResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentGroupeRadonResourceWithStreamingResponse:
        return AsyncBatimentGroupeRadonResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        alea: str | NotGiven = NOT_GIVEN,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[BatimentGroupeRadonAPIExpert, AsyncDefault[BatimentGroupeRadonAPIExpert]]:
        """
        Informations sur l'aléa Radon à l'échelle du bâtiment

        Args:
          alea: (radon) alea du risque radon

          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

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
            "/donnees/batiment_groupe_radon",
            page=AsyncDefault[BatimentGroupeRadonAPIExpert],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "alea": alea,
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    batiment_groupe_radon_list_params.BatimentGroupeRadonListParams,
                ),
            ),
            model=BatimentGroupeRadonAPIExpert,
        )


class BatimentGroupeRadonResourceWithRawResponse:
    def __init__(self, batiment_groupe_radon: BatimentGroupeRadonResource) -> None:
        self._batiment_groupe_radon = batiment_groupe_radon

        self.list = to_raw_response_wrapper(
            batiment_groupe_radon.list,
        )


class AsyncBatimentGroupeRadonResourceWithRawResponse:
    def __init__(self, batiment_groupe_radon: AsyncBatimentGroupeRadonResource) -> None:
        self._batiment_groupe_radon = batiment_groupe_radon

        self.list = async_to_raw_response_wrapper(
            batiment_groupe_radon.list,
        )


class BatimentGroupeRadonResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_radon: BatimentGroupeRadonResource) -> None:
        self._batiment_groupe_radon = batiment_groupe_radon

        self.list = to_streamed_response_wrapper(
            batiment_groupe_radon.list,
        )


class AsyncBatimentGroupeRadonResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_radon: AsyncBatimentGroupeRadonResource) -> None:
        self._batiment_groupe_radon = batiment_groupe_radon

        self.list = async_to_streamed_response_wrapper(
            batiment_groupe_radon.list,
        )
