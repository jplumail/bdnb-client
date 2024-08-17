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
from ...types.metadonnees import colonne_list_params
from ...types.metadonnees.colonne_list_response import ColonneListResponse

__all__ = ["ColonnesResource", "AsyncColonnesResource"]


class ColonnesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ColonnesResourceWithRawResponse:
        return ColonnesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ColonnesResourceWithStreamingResponse:
        return ColonnesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        api_expert: str | NotGiven = NOT_GIVEN,
        api_open: str | NotGiven = NOT_GIVEN,
        colonne_gorenove_legacy: str | NotGiven = NOT_GIVEN,
        contrainte_acces: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        description_table: str | NotGiven = NOT_GIVEN,
        index: str | NotGiven = NOT_GIVEN,
        libelle_metier: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nom_colonne: str | NotGiven = NOT_GIVEN,
        nom_table: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        route: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        unite: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ColonneListResponse:
        """Liste des colonnes de la base = attributs = modalités = champs des tables.

        Ces
        champs portent des droits d'accès

        Args:
          api_expert: Disponible pour les abonnés de l'API Expert

          api_open: Disponible sans souscription

          colonne_gorenove_legacy: Nom de la colonne dans l'ancienne API gorenove /v2/gorenove/buildings

          contrainte_acces: Contrainte d'accès à la données

          description: Description de la table dans la base postgres

          description_table: Description de la table

          index: la colonne est indexée dans la table

          libelle_metier: libelle à utiliser dans les application web

          limit: Limiting and Pagination

          nom_colonne: Nom de la colonne

          nom_table: Nom de la table rattachée

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
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/metadonnees/colonne",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "api_expert": api_expert,
                        "api_open": api_open,
                        "colonne_gorenove_legacy": colonne_gorenove_legacy,
                        "contrainte_acces": contrainte_acces,
                        "description": description,
                        "description_table": description_table,
                        "index": index,
                        "libelle_metier": libelle_metier,
                        "limit": limit,
                        "nom_colonne": nom_colonne,
                        "nom_table": nom_table,
                        "offset": offset,
                        "order": order,
                        "route": route,
                        "select": select,
                        "type": type,
                        "unite": unite,
                    },
                    colonne_list_params.ColonneListParams,
                ),
            ),
            cast_to=ColonneListResponse,
        )


class AsyncColonnesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncColonnesResourceWithRawResponse:
        return AsyncColonnesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncColonnesResourceWithStreamingResponse:
        return AsyncColonnesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        api_expert: str | NotGiven = NOT_GIVEN,
        api_open: str | NotGiven = NOT_GIVEN,
        colonne_gorenove_legacy: str | NotGiven = NOT_GIVEN,
        contrainte_acces: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        description_table: str | NotGiven = NOT_GIVEN,
        index: str | NotGiven = NOT_GIVEN,
        libelle_metier: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nom_colonne: str | NotGiven = NOT_GIVEN,
        nom_table: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        route: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        unite: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ColonneListResponse:
        """Liste des colonnes de la base = attributs = modalités = champs des tables.

        Ces
        champs portent des droits d'accès

        Args:
          api_expert: Disponible pour les abonnés de l'API Expert

          api_open: Disponible sans souscription

          colonne_gorenove_legacy: Nom de la colonne dans l'ancienne API gorenove /v2/gorenove/buildings

          contrainte_acces: Contrainte d'accès à la données

          description: Description de la table dans la base postgres

          description_table: Description de la table

          index: la colonne est indexée dans la table

          libelle_metier: libelle à utiliser dans les application web

          limit: Limiting and Pagination

          nom_colonne: Nom de la colonne

          nom_table: Nom de la table rattachée

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
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            "/metadonnees/colonne",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "api_expert": api_expert,
                        "api_open": api_open,
                        "colonne_gorenove_legacy": colonne_gorenove_legacy,
                        "contrainte_acces": contrainte_acces,
                        "description": description,
                        "description_table": description_table,
                        "index": index,
                        "libelle_metier": libelle_metier,
                        "limit": limit,
                        "nom_colonne": nom_colonne,
                        "nom_table": nom_table,
                        "offset": offset,
                        "order": order,
                        "route": route,
                        "select": select,
                        "type": type,
                        "unite": unite,
                    },
                    colonne_list_params.ColonneListParams,
                ),
            ),
            cast_to=ColonneListResponse,
        )


class ColonnesResourceWithRawResponse:
    def __init__(self, colonnes: ColonnesResource) -> None:
        self._colonnes = colonnes

        self.list = to_raw_response_wrapper(
            colonnes.list,
        )


class AsyncColonnesResourceWithRawResponse:
    def __init__(self, colonnes: AsyncColonnesResource) -> None:
        self._colonnes = colonnes

        self.list = async_to_raw_response_wrapper(
            colonnes.list,
        )


class ColonnesResourceWithStreamingResponse:
    def __init__(self, colonnes: ColonnesResource) -> None:
        self._colonnes = colonnes

        self.list = to_streamed_response_wrapper(
            colonnes.list,
        )


class AsyncColonnesResourceWithStreamingResponse:
    def __init__(self, colonnes: AsyncColonnesResource) -> None:
        self._colonnes = colonnes

        self.list = async_to_streamed_response_wrapper(
            colonnes.list,
        )