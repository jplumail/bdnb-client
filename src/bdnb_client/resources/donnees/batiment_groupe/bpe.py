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
from ....types.donnees.batiment_groupe import bpe_list_params
from ....types.donnees.batiment_groupe.batiment_groupe_bpe import BatimentGroupeBpe

__all__ = ["BpeResource", "AsyncBpeResource"]


class BpeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BpeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return BpeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BpeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return BpeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        l_type_equipement: str | NotGiven = NOT_GIVEN,
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
    ) -> SyncDefault[BatimentGroupeBpe]:
        """
        Informations provenant de la base permanente des équipements (BPE) de l'INSEE
        agrégées à l'échelle du bâtiment

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          l_type_equipement: (bpe) Liste des équipements recensés par la base BPE

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
            "/donnees/batiment_groupe_bpe",
            page=SyncDefault[BatimentGroupeBpe],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "l_type_equipement": l_type_equipement,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    bpe_list_params.BpeListParams,
                ),
            ),
            model=BatimentGroupeBpe,
        )


class AsyncBpeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBpeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncBpeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBpeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncBpeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        l_type_equipement: str | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[BatimentGroupeBpe, AsyncDefault[BatimentGroupeBpe]]:
        """
        Informations provenant de la base permanente des équipements (BPE) de l'INSEE
        agrégées à l'échelle du bâtiment

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          l_type_equipement: (bpe) Liste des équipements recensés par la base BPE

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
            "/donnees/batiment_groupe_bpe",
            page=AsyncDefault[BatimentGroupeBpe],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "l_type_equipement": l_type_equipement,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    bpe_list_params.BpeListParams,
                ),
            ),
            model=BatimentGroupeBpe,
        )


class BpeResourceWithRawResponse:
    def __init__(self, bpe: BpeResource) -> None:
        self._bpe = bpe

        self.list = to_raw_response_wrapper(
            bpe.list,
        )


class AsyncBpeResourceWithRawResponse:
    def __init__(self, bpe: AsyncBpeResource) -> None:
        self._bpe = bpe

        self.list = async_to_raw_response_wrapper(
            bpe.list,
        )


class BpeResourceWithStreamingResponse:
    def __init__(self, bpe: BpeResource) -> None:
        self._bpe = bpe

        self.list = to_streamed_response_wrapper(
            bpe.list,
        )


class AsyncBpeResourceWithStreamingResponse:
    def __init__(self, bpe: AsyncBpeResource) -> None:
        self._bpe = bpe

        self.list = async_to_streamed_response_wrapper(
            bpe.list,
        )
