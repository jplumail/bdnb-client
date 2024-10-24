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
from ....types.donnees.batiment_groupe import delimitation_enveloppe_list_params
from ....types.donnees.batiment_groupe.batiment_groupe_delimitation_enveloppe import BatimentGroupeDelimitationEnveloppe

__all__ = ["DelimitationEnveloppeResource", "AsyncDelimitationEnveloppeResource"]


class DelimitationEnveloppeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DelimitationEnveloppeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return DelimitationEnveloppeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DelimitationEnveloppeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return DelimitationEnveloppeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        delimitation_enveloppe_dict: str | NotGiven = NOT_GIVEN,
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
    ) -> SyncDefault[BatimentGroupeDelimitationEnveloppe]:
        """
        Table contenant les données de prétraitements de géométrie des groupes de
        bâtiments : liste des parois, orientations, surfaces, périmètres, adjacences et
        masques solaire

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          delimitation_enveloppe_dict: Liste de toutes les parois extérieures constitutives d''un bâtiment (murs,
              planchers haut/bas).

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
            "/donnees/batiment_groupe_delimitation_enveloppe",
            page=SyncDefault[BatimentGroupeDelimitationEnveloppe],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "delimitation_enveloppe_dict": delimitation_enveloppe_dict,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    delimitation_enveloppe_list_params.DelimitationEnveloppeListParams,
                ),
            ),
            model=BatimentGroupeDelimitationEnveloppe,
        )


class AsyncDelimitationEnveloppeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDelimitationEnveloppeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncDelimitationEnveloppeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDelimitationEnveloppeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncDelimitationEnveloppeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        delimitation_enveloppe_dict: str | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[BatimentGroupeDelimitationEnveloppe, AsyncDefault[BatimentGroupeDelimitationEnveloppe]]:
        """
        Table contenant les données de prétraitements de géométrie des groupes de
        bâtiments : liste des parois, orientations, surfaces, périmètres, adjacences et
        masques solaire

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          delimitation_enveloppe_dict: Liste de toutes les parois extérieures constitutives d''un bâtiment (murs,
              planchers haut/bas).

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
            "/donnees/batiment_groupe_delimitation_enveloppe",
            page=AsyncDefault[BatimentGroupeDelimitationEnveloppe],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "delimitation_enveloppe_dict": delimitation_enveloppe_dict,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    delimitation_enveloppe_list_params.DelimitationEnveloppeListParams,
                ),
            ),
            model=BatimentGroupeDelimitationEnveloppe,
        )


class DelimitationEnveloppeResourceWithRawResponse:
    def __init__(self, delimitation_enveloppe: DelimitationEnveloppeResource) -> None:
        self._delimitation_enveloppe = delimitation_enveloppe

        self.list = to_raw_response_wrapper(
            delimitation_enveloppe.list,
        )


class AsyncDelimitationEnveloppeResourceWithRawResponse:
    def __init__(self, delimitation_enveloppe: AsyncDelimitationEnveloppeResource) -> None:
        self._delimitation_enveloppe = delimitation_enveloppe

        self.list = async_to_raw_response_wrapper(
            delimitation_enveloppe.list,
        )


class DelimitationEnveloppeResourceWithStreamingResponse:
    def __init__(self, delimitation_enveloppe: DelimitationEnveloppeResource) -> None:
        self._delimitation_enveloppe = delimitation_enveloppe

        self.list = to_streamed_response_wrapper(
            delimitation_enveloppe.list,
        )


class AsyncDelimitationEnveloppeResourceWithStreamingResponse:
    def __init__(self, delimitation_enveloppe: AsyncDelimitationEnveloppeResource) -> None:
        self._delimitation_enveloppe = delimitation_enveloppe

        self.list = async_to_streamed_response_wrapper(
            delimitation_enveloppe.list,
        )
