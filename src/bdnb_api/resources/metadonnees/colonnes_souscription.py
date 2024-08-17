# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
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
from ...types.metadonnees import colonnes_souscription_list_params
from ...types.metadonnees.colonnes_souscription_list_response import ColonnesSouscriptionListResponse

__all__ = ["ColonnesSouscriptionResource", "AsyncColonnesSouscriptionResource"]


class ColonnesSouscriptionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ColonnesSouscriptionResourceWithRawResponse:
        return ColonnesSouscriptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ColonnesSouscriptionResourceWithStreamingResponse:
        return ColonnesSouscriptionResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        contrainte_acces: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        description_table: str | NotGiven = NOT_GIVEN,
        index: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nom_colonne: str | NotGiven = NOT_GIVEN,
        nom_table: str | NotGiven = NOT_GIVEN,
        nom_table_implementation: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        route: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        souscription: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        unite: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ColonnesSouscriptionListResponse:
        """Liste des colonnes de la base = attributs = modalités = champs des tables.

        Ces
        champs portent des droits d'accès

        Args:
          contrainte_acces: Contrainte d'accès à la données

          description: Description de la table dans la base postgres

          description_table: Description de la table

          index: la colonne est indexée dans la table

          limit: Limiting and Pagination

          nom_colonne: Nom de la colonne

          nom_table: Nom de la table rattachée

          nom_table_implementation: Nom de la table d'implémentation

          offset: Limiting and Pagination

          order: Ordering

          route: Chemin dans l'API

          select: Filtering Columns

          type: Type sql de la colonne

          unite: Unité de la colonne

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
        return self._get(
            "/metadonnees/colonne_souscription",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "contrainte_acces": contrainte_acces,
                        "description": description,
                        "description_table": description_table,
                        "index": index,
                        "limit": limit,
                        "nom_colonne": nom_colonne,
                        "nom_table": nom_table,
                        "nom_table_implementation": nom_table_implementation,
                        "offset": offset,
                        "order": order,
                        "route": route,
                        "select": select,
                        "souscription": souscription,
                        "type": type,
                        "unite": unite,
                    },
                    colonnes_souscription_list_params.ColonnesSouscriptionListParams,
                ),
            ),
            cast_to=ColonnesSouscriptionListResponse,
        )


class AsyncColonnesSouscriptionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncColonnesSouscriptionResourceWithRawResponse:
        return AsyncColonnesSouscriptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncColonnesSouscriptionResourceWithStreamingResponse:
        return AsyncColonnesSouscriptionResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        contrainte_acces: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        description_table: str | NotGiven = NOT_GIVEN,
        index: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nom_colonne: str | NotGiven = NOT_GIVEN,
        nom_table: str | NotGiven = NOT_GIVEN,
        nom_table_implementation: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        route: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        souscription: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        unite: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ColonnesSouscriptionListResponse:
        """Liste des colonnes de la base = attributs = modalités = champs des tables.

        Ces
        champs portent des droits d'accès

        Args:
          contrainte_acces: Contrainte d'accès à la données

          description: Description de la table dans la base postgres

          description_table: Description de la table

          index: la colonne est indexée dans la table

          limit: Limiting and Pagination

          nom_colonne: Nom de la colonne

          nom_table: Nom de la table rattachée

          nom_table_implementation: Nom de la table d'implémentation

          offset: Limiting and Pagination

          order: Ordering

          route: Chemin dans l'API

          select: Filtering Columns

          type: Type sql de la colonne

          unite: Unité de la colonne

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
        return await self._get(
            "/metadonnees/colonne_souscription",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "contrainte_acces": contrainte_acces,
                        "description": description,
                        "description_table": description_table,
                        "index": index,
                        "limit": limit,
                        "nom_colonne": nom_colonne,
                        "nom_table": nom_table,
                        "nom_table_implementation": nom_table_implementation,
                        "offset": offset,
                        "order": order,
                        "route": route,
                        "select": select,
                        "souscription": souscription,
                        "type": type,
                        "unite": unite,
                    },
                    colonnes_souscription_list_params.ColonnesSouscriptionListParams,
                ),
            ),
            cast_to=ColonnesSouscriptionListResponse,
        )


class ColonnesSouscriptionResourceWithRawResponse:
    def __init__(self, colonnes_souscription: ColonnesSouscriptionResource) -> None:
        self._colonnes_souscription = colonnes_souscription

        self.list = to_raw_response_wrapper(
            colonnes_souscription.list,
        )


class AsyncColonnesSouscriptionResourceWithRawResponse:
    def __init__(self, colonnes_souscription: AsyncColonnesSouscriptionResource) -> None:
        self._colonnes_souscription = colonnes_souscription

        self.list = async_to_raw_response_wrapper(
            colonnes_souscription.list,
        )


class ColonnesSouscriptionResourceWithStreamingResponse:
    def __init__(self, colonnes_souscription: ColonnesSouscriptionResource) -> None:
        self._colonnes_souscription = colonnes_souscription

        self.list = to_streamed_response_wrapper(
            colonnes_souscription.list,
        )


class AsyncColonnesSouscriptionResourceWithStreamingResponse:
    def __init__(self, colonnes_souscription: AsyncColonnesSouscriptionResource) -> None:
        self._colonnes_souscription = colonnes_souscription

        self.list = async_to_streamed_response_wrapper(
            colonnes_souscription.list,
        )
