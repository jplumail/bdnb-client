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
from ....types.donnees.referentiel_administratif import epci_list_params
from ....types.donnees.referentiel_administratif.referentiel_administratif_epci import ReferentielAdministratifEpci

__all__ = ["EpciResource", "AsyncEpciResource"]


class EpciResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EpciResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return EpciResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EpciResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return EpciResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        code_epci_insee: str | NotGiven = NOT_GIVEN,
        geom_epci: str | NotGiven = NOT_GIVEN,
        libelle_epci: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nature_epci: str | NotGiven = NOT_GIVEN,
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
    ) -> SyncDefault[ReferentielAdministratifEpci]:
        """
        Données sur contours des EPCI, issues de l'agrégation des IRIS Grande Echelle
        fournies par l'IGN pour le compte de l'INSEE

        Args:
          code_epci_insee: Code de l'EPCI

          geom_epci: Géométrie de l'EPCI

          libelle_epci: Libellé de l'EPCI

          limit: Limiting and Pagination

          nature_epci: Type d'EPCI

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
            "/donnees/referentiel_administratif_epci",
            page=SyncDefault[ReferentielAdministratifEpci],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "code_epci_insee": code_epci_insee,
                        "geom_epci": geom_epci,
                        "libelle_epci": libelle_epci,
                        "limit": limit,
                        "nature_epci": nature_epci,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    epci_list_params.EpciListParams,
                ),
            ),
            model=ReferentielAdministratifEpci,
        )


class AsyncEpciResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEpciResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncEpciResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEpciResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncEpciResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        code_epci_insee: str | NotGiven = NOT_GIVEN,
        geom_epci: str | NotGiven = NOT_GIVEN,
        libelle_epci: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nature_epci: str | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[ReferentielAdministratifEpci, AsyncDefault[ReferentielAdministratifEpci]]:
        """
        Données sur contours des EPCI, issues de l'agrégation des IRIS Grande Echelle
        fournies par l'IGN pour le compte de l'INSEE

        Args:
          code_epci_insee: Code de l'EPCI

          geom_epci: Géométrie de l'EPCI

          libelle_epci: Libellé de l'EPCI

          limit: Limiting and Pagination

          nature_epci: Type d'EPCI

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
            "/donnees/referentiel_administratif_epci",
            page=AsyncDefault[ReferentielAdministratifEpci],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "code_epci_insee": code_epci_insee,
                        "geom_epci": geom_epci,
                        "libelle_epci": libelle_epci,
                        "limit": limit,
                        "nature_epci": nature_epci,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    epci_list_params.EpciListParams,
                ),
            ),
            model=ReferentielAdministratifEpci,
        )


class EpciResourceWithRawResponse:
    def __init__(self, epci: EpciResource) -> None:
        self._epci = epci

        self.list = to_raw_response_wrapper(
            epci.list,
        )


class AsyncEpciResourceWithRawResponse:
    def __init__(self, epci: AsyncEpciResource) -> None:
        self._epci = epci

        self.list = async_to_raw_response_wrapper(
            epci.list,
        )


class EpciResourceWithStreamingResponse:
    def __init__(self, epci: EpciResource) -> None:
        self._epci = epci

        self.list = to_streamed_response_wrapper(
            epci.list,
        )


class AsyncEpciResourceWithStreamingResponse:
    def __init__(self, epci: AsyncEpciResource) -> None:
        self._epci = epci

        self.list = async_to_streamed_response_wrapper(
            epci.list,
        )
