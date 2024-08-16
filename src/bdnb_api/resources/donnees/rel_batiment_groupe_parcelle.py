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
from ...types.donnees import rel_batiment_groupe_parcelle_list_params
from ...types.donnees.rel_batiment_groupe_parcelle_list_response import RelBatimentGroupeParcelleListResponse

__all__ = ["RelBatimentGroupeParcelleResource", "AsyncRelBatimentGroupeParcelleResource"]


class RelBatimentGroupeParcelleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RelBatimentGroupeParcelleResourceWithRawResponse:
        return RelBatimentGroupeParcelleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RelBatimentGroupeParcelleResourceWithStreamingResponse:
        return RelBatimentGroupeParcelleResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        parcelle_id: str | NotGiven = NOT_GIVEN,
        parcelle_principale: str | NotGiven = NOT_GIVEN,
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
    ) -> RelBatimentGroupeParcelleListResponse:
        """
        Table de relation entre les groupes de bÃ¢timent et les parcelles (si
        ayant_droit_ffo, prÃ©fÃ©rer la table [parcelle_unifiee])

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          code_departement_insee: Code dÃ©partement INSEE

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          parcelle_id: (ffo:idpar) Identifiant de parcelle (ConcatÃ©nation de ccodep, ccocom, ccopre,
              ccosec, dnupla)

          parcelle_principale: BoolÃ©en renvoyant 'vrai' si la parcelle cadastrale est la plus grande
              intersectant le groupe de bÃ¢timent

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
            "/donnees/rel_batiment_groupe_parcelle",
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
                        "offset": offset,
                        "order": order,
                        "parcelle_id": parcelle_id,
                        "parcelle_principale": parcelle_principale,
                        "select": select,
                    },
                    rel_batiment_groupe_parcelle_list_params.RelBatimentGroupeParcelleListParams,
                ),
            ),
            cast_to=RelBatimentGroupeParcelleListResponse,
        )


class AsyncRelBatimentGroupeParcelleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRelBatimentGroupeParcelleResourceWithRawResponse:
        return AsyncRelBatimentGroupeParcelleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRelBatimentGroupeParcelleResourceWithStreamingResponse:
        return AsyncRelBatimentGroupeParcelleResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        parcelle_id: str | NotGiven = NOT_GIVEN,
        parcelle_principale: str | NotGiven = NOT_GIVEN,
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
    ) -> RelBatimentGroupeParcelleListResponse:
        """
        Table de relation entre les groupes de bÃ¢timent et les parcelles (si
        ayant_droit_ffo, prÃ©fÃ©rer la table [parcelle_unifiee])

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          code_departement_insee: Code dÃ©partement INSEE

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          parcelle_id: (ffo:idpar) Identifiant de parcelle (ConcatÃ©nation de ccodep, ccocom, ccopre,
              ccosec, dnupla)

          parcelle_principale: BoolÃ©en renvoyant 'vrai' si la parcelle cadastrale est la plus grande
              intersectant le groupe de bÃ¢timent

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
            "/donnees/rel_batiment_groupe_parcelle",
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
                        "offset": offset,
                        "order": order,
                        "parcelle_id": parcelle_id,
                        "parcelle_principale": parcelle_principale,
                        "select": select,
                    },
                    rel_batiment_groupe_parcelle_list_params.RelBatimentGroupeParcelleListParams,
                ),
            ),
            cast_to=RelBatimentGroupeParcelleListResponse,
        )


class RelBatimentGroupeParcelleResourceWithRawResponse:
    def __init__(self, rel_batiment_groupe_parcelle: RelBatimentGroupeParcelleResource) -> None:
        self._rel_batiment_groupe_parcelle = rel_batiment_groupe_parcelle

        self.list = to_raw_response_wrapper(
            rel_batiment_groupe_parcelle.list,
        )


class AsyncRelBatimentGroupeParcelleResourceWithRawResponse:
    def __init__(self, rel_batiment_groupe_parcelle: AsyncRelBatimentGroupeParcelleResource) -> None:
        self._rel_batiment_groupe_parcelle = rel_batiment_groupe_parcelle

        self.list = async_to_raw_response_wrapper(
            rel_batiment_groupe_parcelle.list,
        )


class RelBatimentGroupeParcelleResourceWithStreamingResponse:
    def __init__(self, rel_batiment_groupe_parcelle: RelBatimentGroupeParcelleResource) -> None:
        self._rel_batiment_groupe_parcelle = rel_batiment_groupe_parcelle

        self.list = to_streamed_response_wrapper(
            rel_batiment_groupe_parcelle.list,
        )


class AsyncRelBatimentGroupeParcelleResourceWithStreamingResponse:
    def __init__(self, rel_batiment_groupe_parcelle: AsyncRelBatimentGroupeParcelleResource) -> None:
        self._rel_batiment_groupe_parcelle = rel_batiment_groupe_parcelle

        self.list = async_to_streamed_response_wrapper(
            rel_batiment_groupe_parcelle.list,
        )
