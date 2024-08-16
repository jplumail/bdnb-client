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
from ...types.metadonnees import rel_colonne_jeu_de_donnee_list_params
from ...types.metadonnees.rel_colonne_jeu_de_donnee_list_response import RelColonneJeuDeDonneeListResponse

__all__ = ["RelColonneJeuDeDonneesResource", "AsyncRelColonneJeuDeDonneesResource"]


class RelColonneJeuDeDonneesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RelColonneJeuDeDonneesResourceWithRawResponse:
        return RelColonneJeuDeDonneesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RelColonneJeuDeDonneesResourceWithStreamingResponse:
        return RelColonneJeuDeDonneesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        denomination_serie: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        millesime_jeu_de_donnees: str | NotGiven = NOT_GIVEN,
        nom_colonne: str | NotGiven = NOT_GIVEN,
        nom_table: str | NotGiven = NOT_GIVEN,
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
    ) -> RelColonneJeuDeDonneeListResponse:
        """
        Quels jeux de données ont servis à créer quelles colonnes ?

        Args:
          denomination_serie: Dénomination du jeu de données

          limit: Limiting and Pagination

          millesime_jeu_de_donnees: Millésime du jeu de données

          nom_colonne: Nom de la colonne

          nom_table: Nom de la table rattachée

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
            "/metadonnees/rel_colonne_jeu_de_donnees",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "denomination_serie": denomination_serie,
                        "limit": limit,
                        "millesime_jeu_de_donnees": millesime_jeu_de_donnees,
                        "nom_colonne": nom_colonne,
                        "nom_table": nom_table,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    rel_colonne_jeu_de_donnee_list_params.RelColonneJeuDeDonneeListParams,
                ),
            ),
            cast_to=RelColonneJeuDeDonneeListResponse,
        )


class AsyncRelColonneJeuDeDonneesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRelColonneJeuDeDonneesResourceWithRawResponse:
        return AsyncRelColonneJeuDeDonneesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRelColonneJeuDeDonneesResourceWithStreamingResponse:
        return AsyncRelColonneJeuDeDonneesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        denomination_serie: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        millesime_jeu_de_donnees: str | NotGiven = NOT_GIVEN,
        nom_colonne: str | NotGiven = NOT_GIVEN,
        nom_table: str | NotGiven = NOT_GIVEN,
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
    ) -> RelColonneJeuDeDonneeListResponse:
        """
        Quels jeux de données ont servis à créer quelles colonnes ?

        Args:
          denomination_serie: Dénomination du jeu de données

          limit: Limiting and Pagination

          millesime_jeu_de_donnees: Millésime du jeu de données

          nom_colonne: Nom de la colonne

          nom_table: Nom de la table rattachée

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
            "/metadonnees/rel_colonne_jeu_de_donnees",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "denomination_serie": denomination_serie,
                        "limit": limit,
                        "millesime_jeu_de_donnees": millesime_jeu_de_donnees,
                        "nom_colonne": nom_colonne,
                        "nom_table": nom_table,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    rel_colonne_jeu_de_donnee_list_params.RelColonneJeuDeDonneeListParams,
                ),
            ),
            cast_to=RelColonneJeuDeDonneeListResponse,
        )


class RelColonneJeuDeDonneesResourceWithRawResponse:
    def __init__(self, rel_colonne_jeu_de_donnees: RelColonneJeuDeDonneesResource) -> None:
        self._rel_colonne_jeu_de_donnees = rel_colonne_jeu_de_donnees

        self.list = to_raw_response_wrapper(
            rel_colonne_jeu_de_donnees.list,
        )


class AsyncRelColonneJeuDeDonneesResourceWithRawResponse:
    def __init__(self, rel_colonne_jeu_de_donnees: AsyncRelColonneJeuDeDonneesResource) -> None:
        self._rel_colonne_jeu_de_donnees = rel_colonne_jeu_de_donnees

        self.list = async_to_raw_response_wrapper(
            rel_colonne_jeu_de_donnees.list,
        )


class RelColonneJeuDeDonneesResourceWithStreamingResponse:
    def __init__(self, rel_colonne_jeu_de_donnees: RelColonneJeuDeDonneesResource) -> None:
        self._rel_colonne_jeu_de_donnees = rel_colonne_jeu_de_donnees

        self.list = to_streamed_response_wrapper(
            rel_colonne_jeu_de_donnees.list,
        )


class AsyncRelColonneJeuDeDonneesResourceWithStreamingResponse:
    def __init__(self, rel_colonne_jeu_de_donnees: AsyncRelColonneJeuDeDonneesResource) -> None:
        self._rel_colonne_jeu_de_donnees = rel_colonne_jeu_de_donnees

        self.list = async_to_streamed_response_wrapper(
            rel_colonne_jeu_de_donnees.list,
        )
