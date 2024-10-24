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
from ....types.donnees.referentiel_administratif import departement_list_params
from ....types.donnees.referentiel_administratif.referentiel_administratif_departement import (
    ReferentielAdministratifDepartement,
)

__all__ = ["DepartementResource", "AsyncDepartementResource"]


class DepartementResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DepartementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return DepartementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DepartementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return DepartementResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        code_region_insee: str | NotGiven = NOT_GIVEN,
        geom_departement: str | NotGiven = NOT_GIVEN,
        libelle_departement: str | NotGiven = NOT_GIVEN,
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
    ) -> SyncDefault[ReferentielAdministratifDepartement]:
        """
        Données sur contours des départements, issues de l'agrégation des IRIS Grande
        Echelle fournies par l'IGN pour le compte de l'INSEE

        Args:
          code_departement_insee: Code département INSEE

          code_region_insee: Code région INSEE

          geom_departement: Géométrie du département

          libelle_departement: Libellé département INSEE

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
            "/donnees/referentiel_administratif_departement",
            page=SyncDefault[ReferentielAdministratifDepartement],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "code_departement_insee": code_departement_insee,
                        "code_region_insee": code_region_insee,
                        "geom_departement": geom_departement,
                        "libelle_departement": libelle_departement,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    departement_list_params.DepartementListParams,
                ),
            ),
            model=ReferentielAdministratifDepartement,
        )


class AsyncDepartementResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDepartementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncDepartementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDepartementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncDepartementResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        code_region_insee: str | NotGiven = NOT_GIVEN,
        geom_departement: str | NotGiven = NOT_GIVEN,
        libelle_departement: str | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[ReferentielAdministratifDepartement, AsyncDefault[ReferentielAdministratifDepartement]]:
        """
        Données sur contours des départements, issues de l'agrégation des IRIS Grande
        Echelle fournies par l'IGN pour le compte de l'INSEE

        Args:
          code_departement_insee: Code département INSEE

          code_region_insee: Code région INSEE

          geom_departement: Géométrie du département

          libelle_departement: Libellé département INSEE

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
            "/donnees/referentiel_administratif_departement",
            page=AsyncDefault[ReferentielAdministratifDepartement],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "code_departement_insee": code_departement_insee,
                        "code_region_insee": code_region_insee,
                        "geom_departement": geom_departement,
                        "libelle_departement": libelle_departement,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    departement_list_params.DepartementListParams,
                ),
            ),
            model=ReferentielAdministratifDepartement,
        )


class DepartementResourceWithRawResponse:
    def __init__(self, departement: DepartementResource) -> None:
        self._departement = departement

        self.list = to_raw_response_wrapper(
            departement.list,
        )


class AsyncDepartementResourceWithRawResponse:
    def __init__(self, departement: AsyncDepartementResource) -> None:
        self._departement = departement

        self.list = async_to_raw_response_wrapper(
            departement.list,
        )


class DepartementResourceWithStreamingResponse:
    def __init__(self, departement: DepartementResource) -> None:
        self._departement = departement

        self.list = to_streamed_response_wrapper(
            departement.list,
        )


class AsyncDepartementResourceWithStreamingResponse:
    def __init__(self, departement: AsyncDepartementResource) -> None:
        self._departement = departement

        self.list = async_to_streamed_response_wrapper(
            departement.list,
        )
