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
from ...types.donnees import rel_batiment_groupe_merimee_list_params
from ...types.shared.rel_batiment_groupe_merimee_api_expert import RelBatimentGroupeMerimeeAPIExpert

__all__ = ["RelBatimentGroupeMerimeeResource", "AsyncRelBatimentGroupeMerimeeResource"]


class RelBatimentGroupeMerimeeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RelBatimentGroupeMerimeeResourceWithRawResponse:
        return RelBatimentGroupeMerimeeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RelBatimentGroupeMerimeeResourceWithStreamingResponse:
        return RelBatimentGroupeMerimeeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        distance_batiment_historique: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        merimee_ref: str | NotGiven = NOT_GIVEN,
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
    ) -> SyncDefault[RelBatimentGroupeMerimeeAPIExpert]:
        """
        Table de relation entre les bâtiments de la BDNB et les éléments de la table
        merimee

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          distance_batiment_historique: (mer) Distance entre le batiment_historique et le batiment_construction (si
              moins de 500m) [m]

          limit: Limiting and Pagination

          merimee_ref: identifiant de la table merimee

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
            "/donnees/rel_batiment_groupe_merimee",
            page=SyncDefault[RelBatimentGroupeMerimeeAPIExpert],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "distance_batiment_historique": distance_batiment_historique,
                        "limit": limit,
                        "merimee_ref": merimee_ref,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    rel_batiment_groupe_merimee_list_params.RelBatimentGroupeMerimeeListParams,
                ),
            ),
            model=RelBatimentGroupeMerimeeAPIExpert,
        )


class AsyncRelBatimentGroupeMerimeeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRelBatimentGroupeMerimeeResourceWithRawResponse:
        return AsyncRelBatimentGroupeMerimeeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRelBatimentGroupeMerimeeResourceWithStreamingResponse:
        return AsyncRelBatimentGroupeMerimeeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        distance_batiment_historique: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        merimee_ref: str | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[RelBatimentGroupeMerimeeAPIExpert, AsyncDefault[RelBatimentGroupeMerimeeAPIExpert]]:
        """
        Table de relation entre les bâtiments de la BDNB et les éléments de la table
        merimee

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          distance_batiment_historique: (mer) Distance entre le batiment_historique et le batiment_construction (si
              moins de 500m) [m]

          limit: Limiting and Pagination

          merimee_ref: identifiant de la table merimee

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
            "/donnees/rel_batiment_groupe_merimee",
            page=AsyncDefault[RelBatimentGroupeMerimeeAPIExpert],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "distance_batiment_historique": distance_batiment_historique,
                        "limit": limit,
                        "merimee_ref": merimee_ref,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    rel_batiment_groupe_merimee_list_params.RelBatimentGroupeMerimeeListParams,
                ),
            ),
            model=RelBatimentGroupeMerimeeAPIExpert,
        )


class RelBatimentGroupeMerimeeResourceWithRawResponse:
    def __init__(self, rel_batiment_groupe_merimee: RelBatimentGroupeMerimeeResource) -> None:
        self._rel_batiment_groupe_merimee = rel_batiment_groupe_merimee

        self.list = to_raw_response_wrapper(
            rel_batiment_groupe_merimee.list,
        )


class AsyncRelBatimentGroupeMerimeeResourceWithRawResponse:
    def __init__(self, rel_batiment_groupe_merimee: AsyncRelBatimentGroupeMerimeeResource) -> None:
        self._rel_batiment_groupe_merimee = rel_batiment_groupe_merimee

        self.list = async_to_raw_response_wrapper(
            rel_batiment_groupe_merimee.list,
        )


class RelBatimentGroupeMerimeeResourceWithStreamingResponse:
    def __init__(self, rel_batiment_groupe_merimee: RelBatimentGroupeMerimeeResource) -> None:
        self._rel_batiment_groupe_merimee = rel_batiment_groupe_merimee

        self.list = to_streamed_response_wrapper(
            rel_batiment_groupe_merimee.list,
        )


class AsyncRelBatimentGroupeMerimeeResourceWithStreamingResponse:
    def __init__(self, rel_batiment_groupe_merimee: AsyncRelBatimentGroupeMerimeeResource) -> None:
        self._rel_batiment_groupe_merimee = rel_batiment_groupe_merimee

        self.list = async_to_streamed_response_wrapper(
            rel_batiment_groupe_merimee.list,
        )
