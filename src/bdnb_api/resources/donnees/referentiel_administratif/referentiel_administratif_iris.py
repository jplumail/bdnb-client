# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    is_given,
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
from ....types.donnees.referentiel_administratif import referentiel_administratif_iris_list_params
from ....types.donnees.referentiel_administratif.referentiel_administratif_iris_list_response import (
    ReferentielAdministratifIrisListResponse,
)

__all__ = ["ReferentielAdministratifIrisResource", "AsyncReferentielAdministratifIrisResource"]


class ReferentielAdministratifIrisResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReferentielAdministratifIrisResourceWithRawResponse:
        return ReferentielAdministratifIrisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReferentielAdministratifIrisResourceWithStreamingResponse:
        return ReferentielAdministratifIrisResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        code_commune_insee: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        code_iris: str | NotGiven = NOT_GIVEN,
        geom_iris: str | NotGiven = NOT_GIVEN,
        libelle_iris: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        type_iris: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReferentielAdministratifIrisListResponse:
        """
        Données sur les IRIS Grande Echelle fournies par l'IGN pour le compte de l'INSEE

        Args:
          code_commune_insee: Code INSEE de la commune

          code_departement_insee: Code département INSEE

          code_iris: Code iris INSEE

          geom_iris: Géométrie de l'IRIS

          libelle_iris: Libellé de l'iris

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          type_iris: Type de l'IRIS

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
            "/donnees/referentiel_administratif_iris",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "code_commune_insee": code_commune_insee,
                        "code_departement_insee": code_departement_insee,
                        "code_iris": code_iris,
                        "geom_iris": geom_iris,
                        "libelle_iris": libelle_iris,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                        "type_iris": type_iris,
                    },
                    referentiel_administratif_iris_list_params.ReferentielAdministratifIrisListParams,
                ),
            ),
            cast_to=ReferentielAdministratifIrisListResponse,
        )


class AsyncReferentielAdministratifIrisResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReferentielAdministratifIrisResourceWithRawResponse:
        return AsyncReferentielAdministratifIrisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReferentielAdministratifIrisResourceWithStreamingResponse:
        return AsyncReferentielAdministratifIrisResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        code_commune_insee: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        code_iris: str | NotGiven = NOT_GIVEN,
        geom_iris: str | NotGiven = NOT_GIVEN,
        libelle_iris: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        type_iris: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReferentielAdministratifIrisListResponse:
        """
        Données sur les IRIS Grande Echelle fournies par l'IGN pour le compte de l'INSEE

        Args:
          code_commune_insee: Code INSEE de la commune

          code_departement_insee: Code département INSEE

          code_iris: Code iris INSEE

          geom_iris: Géométrie de l'IRIS

          libelle_iris: Libellé de l'iris

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          type_iris: Type de l'IRIS

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
            "/donnees/referentiel_administratif_iris",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "code_commune_insee": code_commune_insee,
                        "code_departement_insee": code_departement_insee,
                        "code_iris": code_iris,
                        "geom_iris": geom_iris,
                        "libelle_iris": libelle_iris,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                        "type_iris": type_iris,
                    },
                    referentiel_administratif_iris_list_params.ReferentielAdministratifIrisListParams,
                ),
            ),
            cast_to=ReferentielAdministratifIrisListResponse,
        )


class ReferentielAdministratifIrisResourceWithRawResponse:
    def __init__(self, referentiel_administratif_iris: ReferentielAdministratifIrisResource) -> None:
        self._referentiel_administratif_iris = referentiel_administratif_iris

        self.list = to_raw_response_wrapper(
            referentiel_administratif_iris.list,
        )


class AsyncReferentielAdministratifIrisResourceWithRawResponse:
    def __init__(self, referentiel_administratif_iris: AsyncReferentielAdministratifIrisResource) -> None:
        self._referentiel_administratif_iris = referentiel_administratif_iris

        self.list = async_to_raw_response_wrapper(
            referentiel_administratif_iris.list,
        )


class ReferentielAdministratifIrisResourceWithStreamingResponse:
    def __init__(self, referentiel_administratif_iris: ReferentielAdministratifIrisResource) -> None:
        self._referentiel_administratif_iris = referentiel_administratif_iris

        self.list = to_streamed_response_wrapper(
            referentiel_administratif_iris.list,
        )


class AsyncReferentielAdministratifIrisResourceWithStreamingResponse:
    def __init__(self, referentiel_administratif_iris: AsyncReferentielAdministratifIrisResource) -> None:
        self._referentiel_administratif_iris = referentiel_administratif_iris

        self.list = async_to_streamed_response_wrapper(
            referentiel_administratif_iris.list,
        )
