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
from ...types.donnees import referentiel_administratif_region_list_params
from ...types.donnees.referentiel_administratif_region_list_response import ReferentielAdministratifRegionListResponse

__all__ = ["ReferentielAdministratifRegionResource", "AsyncReferentielAdministratifRegionResource"]


class ReferentielAdministratifRegionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReferentielAdministratifRegionResourceWithRawResponse:
        return ReferentielAdministratifRegionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReferentielAdministratifRegionResourceWithStreamingResponse:
        return ReferentielAdministratifRegionResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        code_region_insee: str | NotGiven = NOT_GIVEN,
        geom_region: str | NotGiven = NOT_GIVEN,
        libelle_region: str | NotGiven = NOT_GIVEN,
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
    ) -> ReferentielAdministratifRegionListResponse:
        """
        DonnÃ©es sur contours des rÃ©gions, issues de l'agrÃ©gation des IRIS Grande
        Echelle fournies par l'IGN pour le compte de l'INSEE

        Args:
          code_region_insee: Code rÃ©gion INSEE

          geom_region: GÃ©omÃ©trie de la rÃ©gion

          libelle_region: LibellÃ© de la rÃ©gion

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
            "/donnees/referentiel_administratif_region",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "code_region_insee": code_region_insee,
                        "geom_region": geom_region,
                        "libelle_region": libelle_region,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    referentiel_administratif_region_list_params.ReferentielAdministratifRegionListParams,
                ),
            ),
            cast_to=ReferentielAdministratifRegionListResponse,
        )


class AsyncReferentielAdministratifRegionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReferentielAdministratifRegionResourceWithRawResponse:
        return AsyncReferentielAdministratifRegionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReferentielAdministratifRegionResourceWithStreamingResponse:
        return AsyncReferentielAdministratifRegionResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        code_region_insee: str | NotGiven = NOT_GIVEN,
        geom_region: str | NotGiven = NOT_GIVEN,
        libelle_region: str | NotGiven = NOT_GIVEN,
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
    ) -> ReferentielAdministratifRegionListResponse:
        """
        DonnÃ©es sur contours des rÃ©gions, issues de l'agrÃ©gation des IRIS Grande
        Echelle fournies par l'IGN pour le compte de l'INSEE

        Args:
          code_region_insee: Code rÃ©gion INSEE

          geom_region: GÃ©omÃ©trie de la rÃ©gion

          libelle_region: LibellÃ© de la rÃ©gion

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
            "/donnees/referentiel_administratif_region",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "code_region_insee": code_region_insee,
                        "geom_region": geom_region,
                        "libelle_region": libelle_region,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    referentiel_administratif_region_list_params.ReferentielAdministratifRegionListParams,
                ),
            ),
            cast_to=ReferentielAdministratifRegionListResponse,
        )


class ReferentielAdministratifRegionResourceWithRawResponse:
    def __init__(self, referentiel_administratif_region: ReferentielAdministratifRegionResource) -> None:
        self._referentiel_administratif_region = referentiel_administratif_region

        self.list = to_raw_response_wrapper(
            referentiel_administratif_region.list,
        )


class AsyncReferentielAdministratifRegionResourceWithRawResponse:
    def __init__(self, referentiel_administratif_region: AsyncReferentielAdministratifRegionResource) -> None:
        self._referentiel_administratif_region = referentiel_administratif_region

        self.list = async_to_raw_response_wrapper(
            referentiel_administratif_region.list,
        )


class ReferentielAdministratifRegionResourceWithStreamingResponse:
    def __init__(self, referentiel_administratif_region: ReferentielAdministratifRegionResource) -> None:
        self._referentiel_administratif_region = referentiel_administratif_region

        self.list = to_streamed_response_wrapper(
            referentiel_administratif_region.list,
        )


class AsyncReferentielAdministratifRegionResourceWithStreamingResponse:
    def __init__(self, referentiel_administratif_region: AsyncReferentielAdministratifRegionResource) -> None:
        self._referentiel_administratif_region = referentiel_administratif_region

        self.list = async_to_streamed_response_wrapper(
            referentiel_administratif_region.list,
        )
