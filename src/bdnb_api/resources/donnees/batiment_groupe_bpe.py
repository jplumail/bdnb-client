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
from ...types.donnees import batiment_groupe_bpe_list_params
from ...types.shared.batiment_groupe_bpe_api_expert import BatimentGroupeBpeAPIExpert

__all__ = ["BatimentGroupeBpeResource", "AsyncBatimentGroupeBpeResource"]


class BatimentGroupeBpeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatimentGroupeBpeResourceWithRawResponse:
        return BatimentGroupeBpeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentGroupeBpeResourceWithStreamingResponse:
        return BatimentGroupeBpeResourceWithStreamingResponse(self)

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
    ) -> SyncDefault[BatimentGroupeBpeAPIExpert]:
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
            page=SyncDefault[BatimentGroupeBpeAPIExpert],
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
                    batiment_groupe_bpe_list_params.BatimentGroupeBpeListParams,
                ),
            ),
            model=BatimentGroupeBpeAPIExpert,
        )


class AsyncBatimentGroupeBpeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatimentGroupeBpeResourceWithRawResponse:
        return AsyncBatimentGroupeBpeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentGroupeBpeResourceWithStreamingResponse:
        return AsyncBatimentGroupeBpeResourceWithStreamingResponse(self)

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
    ) -> AsyncPaginator[BatimentGroupeBpeAPIExpert, AsyncDefault[BatimentGroupeBpeAPIExpert]]:
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
            page=AsyncDefault[BatimentGroupeBpeAPIExpert],
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
                    batiment_groupe_bpe_list_params.BatimentGroupeBpeListParams,
                ),
            ),
            model=BatimentGroupeBpeAPIExpert,
        )


class BatimentGroupeBpeResourceWithRawResponse:
    def __init__(self, batiment_groupe_bpe: BatimentGroupeBpeResource) -> None:
        self._batiment_groupe_bpe = batiment_groupe_bpe

        self.list = to_raw_response_wrapper(
            batiment_groupe_bpe.list,
        )


class AsyncBatimentGroupeBpeResourceWithRawResponse:
    def __init__(self, batiment_groupe_bpe: AsyncBatimentGroupeBpeResource) -> None:
        self._batiment_groupe_bpe = batiment_groupe_bpe

        self.list = async_to_raw_response_wrapper(
            batiment_groupe_bpe.list,
        )


class BatimentGroupeBpeResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_bpe: BatimentGroupeBpeResource) -> None:
        self._batiment_groupe_bpe = batiment_groupe_bpe

        self.list = to_streamed_response_wrapper(
            batiment_groupe_bpe.list,
        )


class AsyncBatimentGroupeBpeResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_bpe: AsyncBatimentGroupeBpeResource) -> None:
        self._batiment_groupe_bpe = batiment_groupe_bpe

        self.list = async_to_streamed_response_wrapper(
            batiment_groupe_bpe.list,
        )
