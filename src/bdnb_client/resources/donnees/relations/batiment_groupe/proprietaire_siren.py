# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, strip_not_given
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncDefault, AsyncDefault
from ....._base_client import AsyncPaginator, make_request_options
from .....types.donnees.relations.batiment_groupe import proprietaire_siren_list_params
from .....types.donnees.relations.batiment_groupe.rel_batiment_groupe_proprietaire_siren import (
    RelBatimentGroupeProprietaireSiren,
)

__all__ = ["ProprietaireSirenResource", "AsyncProprietaireSirenResource"]


class ProprietaireSirenResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProprietaireSirenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return ProprietaireSirenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProprietaireSirenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return ProprietaireSirenResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        bat_prop_denomination_proprietaire: str | NotGiven = NOT_GIVEN,
        dans_majic_pm: str | NotGiven = NOT_GIVEN,
        is_bailleur: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_locaux_open: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        siren: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[RelBatimentGroupeProprietaireSiren]:
        """
        Table de relation entre les propriétaires et les groupes de bâtiment (la version
        open filtre sur la colonne `dans_majic_pm)

        Args:
          bat_prop_denomination_proprietaire: TODO

          dans_majic_pm: (majic_pm) Ce propriétaire possède des bâtiments déclarés dans majic_pm

          is_bailleur: Vrai si le propriétaire est un bailleur social

          limit: Limiting and Pagination

          nb_locaux_open: (majic_pm) nombre de locaux déclarés dans majic_pm

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          siren: Numéro de SIREN de la personne morale (FF)

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
            "/donnees/rel_batiment_groupe_proprietaire_siren",
            page=SyncDefault[RelBatimentGroupeProprietaireSiren],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bat_prop_denomination_proprietaire": bat_prop_denomination_proprietaire,
                        "dans_majic_pm": dans_majic_pm,
                        "is_bailleur": is_bailleur,
                        "limit": limit,
                        "nb_locaux_open": nb_locaux_open,
                        "offset": offset,
                        "order": order,
                        "select": select,
                        "siren": siren,
                    },
                    proprietaire_siren_list_params.ProprietaireSirenListParams,
                ),
            ),
            model=RelBatimentGroupeProprietaireSiren,
        )


class AsyncProprietaireSirenResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProprietaireSirenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncProprietaireSirenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProprietaireSirenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncProprietaireSirenResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        bat_prop_denomination_proprietaire: str | NotGiven = NOT_GIVEN,
        dans_majic_pm: str | NotGiven = NOT_GIVEN,
        is_bailleur: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_locaux_open: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        siren: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[RelBatimentGroupeProprietaireSiren, AsyncDefault[RelBatimentGroupeProprietaireSiren]]:
        """
        Table de relation entre les propriétaires et les groupes de bâtiment (la version
        open filtre sur la colonne `dans_majic_pm)

        Args:
          bat_prop_denomination_proprietaire: TODO

          dans_majic_pm: (majic_pm) Ce propriétaire possède des bâtiments déclarés dans majic_pm

          is_bailleur: Vrai si le propriétaire est un bailleur social

          limit: Limiting and Pagination

          nb_locaux_open: (majic_pm) nombre de locaux déclarés dans majic_pm

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          siren: Numéro de SIREN de la personne morale (FF)

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
            "/donnees/rel_batiment_groupe_proprietaire_siren",
            page=AsyncDefault[RelBatimentGroupeProprietaireSiren],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bat_prop_denomination_proprietaire": bat_prop_denomination_proprietaire,
                        "dans_majic_pm": dans_majic_pm,
                        "is_bailleur": is_bailleur,
                        "limit": limit,
                        "nb_locaux_open": nb_locaux_open,
                        "offset": offset,
                        "order": order,
                        "select": select,
                        "siren": siren,
                    },
                    proprietaire_siren_list_params.ProprietaireSirenListParams,
                ),
            ),
            model=RelBatimentGroupeProprietaireSiren,
        )


class ProprietaireSirenResourceWithRawResponse:
    def __init__(self, proprietaire_siren: ProprietaireSirenResource) -> None:
        self._proprietaire_siren = proprietaire_siren

        self.list = to_raw_response_wrapper(
            proprietaire_siren.list,
        )


class AsyncProprietaireSirenResourceWithRawResponse:
    def __init__(self, proprietaire_siren: AsyncProprietaireSirenResource) -> None:
        self._proprietaire_siren = proprietaire_siren

        self.list = async_to_raw_response_wrapper(
            proprietaire_siren.list,
        )


class ProprietaireSirenResourceWithStreamingResponse:
    def __init__(self, proprietaire_siren: ProprietaireSirenResource) -> None:
        self._proprietaire_siren = proprietaire_siren

        self.list = to_streamed_response_wrapper(
            proprietaire_siren.list,
        )


class AsyncProprietaireSirenResourceWithStreamingResponse:
    def __init__(self, proprietaire_siren: AsyncProprietaireSirenResource) -> None:
        self._proprietaire_siren = proprietaire_siren

        self.list = async_to_streamed_response_wrapper(
            proprietaire_siren.list,
        )
