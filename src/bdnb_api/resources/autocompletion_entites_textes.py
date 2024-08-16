# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import autocompletion_entites_texte_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    is_given,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.autocompletion_entites_texte_list_response import AutocompletionEntitesTexteListResponse

__all__ = ["AutocompletionEntitesTextesResource", "AsyncAutocompletionEntitesTextesResource"]


class AutocompletionEntitesTextesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutocompletionEntitesTextesResourceWithRawResponse:
        return AutocompletionEntitesTextesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutocompletionEntitesTextesResourceWithStreamingResponse:
        return AutocompletionEntitesTextesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        code: str | NotGiven = NOT_GIVEN,
        geom: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nom: str | NotGiven = NOT_GIVEN,
        nom_unaccent: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        origine_code: str | NotGiven = NOT_GIVEN,
        origine_nom: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        type_entite: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutocompletionEntitesTexteListResponse:
        """
        table utilisée pour l'autocomplétion de champs textuelles des entités dans la
        base

        Args:
          code: code de l'entité

          geom: geometrie de l'entité s'il y en a une

          limit: Limiting and Pagination

          nom: nom d'entité

          nom_unaccent: nom d'entité sans accent

          offset: Limiting and Pagination

          order: Ordering

          origine_code: nom de la table de la colonne d'origine du code

          origine_nom: nom de la table de la colonne d'origine du nom

          select: Filtering Columns

          type_entite: type de l'entité

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
            "/autocompletion_entites_texte",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "code": code,
                        "geom": geom,
                        "limit": limit,
                        "nom": nom,
                        "nom_unaccent": nom_unaccent,
                        "offset": offset,
                        "order": order,
                        "origine_code": origine_code,
                        "origine_nom": origine_nom,
                        "select": select,
                        "type_entite": type_entite,
                    },
                    autocompletion_entites_texte_list_params.AutocompletionEntitesTexteListParams,
                ),
            ),
            cast_to=AutocompletionEntitesTexteListResponse,
        )


class AsyncAutocompletionEntitesTextesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutocompletionEntitesTextesResourceWithRawResponse:
        return AsyncAutocompletionEntitesTextesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutocompletionEntitesTextesResourceWithStreamingResponse:
        return AsyncAutocompletionEntitesTextesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        code: str | NotGiven = NOT_GIVEN,
        geom: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nom: str | NotGiven = NOT_GIVEN,
        nom_unaccent: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        origine_code: str | NotGiven = NOT_GIVEN,
        origine_nom: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        type_entite: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutocompletionEntitesTexteListResponse:
        """
        table utilisée pour l'autocomplétion de champs textuelles des entités dans la
        base

        Args:
          code: code de l'entité

          geom: geometrie de l'entité s'il y en a une

          limit: Limiting and Pagination

          nom: nom d'entité

          nom_unaccent: nom d'entité sans accent

          offset: Limiting and Pagination

          order: Ordering

          origine_code: nom de la table de la colonne d'origine du code

          origine_nom: nom de la table de la colonne d'origine du nom

          select: Filtering Columns

          type_entite: type de l'entité

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
            "/autocompletion_entites_texte",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "code": code,
                        "geom": geom,
                        "limit": limit,
                        "nom": nom,
                        "nom_unaccent": nom_unaccent,
                        "offset": offset,
                        "order": order,
                        "origine_code": origine_code,
                        "origine_nom": origine_nom,
                        "select": select,
                        "type_entite": type_entite,
                    },
                    autocompletion_entites_texte_list_params.AutocompletionEntitesTexteListParams,
                ),
            ),
            cast_to=AutocompletionEntitesTexteListResponse,
        )


class AutocompletionEntitesTextesResourceWithRawResponse:
    def __init__(self, autocompletion_entites_textes: AutocompletionEntitesTextesResource) -> None:
        self._autocompletion_entites_textes = autocompletion_entites_textes

        self.list = to_raw_response_wrapper(
            autocompletion_entites_textes.list,
        )


class AsyncAutocompletionEntitesTextesResourceWithRawResponse:
    def __init__(self, autocompletion_entites_textes: AsyncAutocompletionEntitesTextesResource) -> None:
        self._autocompletion_entites_textes = autocompletion_entites_textes

        self.list = async_to_raw_response_wrapper(
            autocompletion_entites_textes.list,
        )


class AutocompletionEntitesTextesResourceWithStreamingResponse:
    def __init__(self, autocompletion_entites_textes: AutocompletionEntitesTextesResource) -> None:
        self._autocompletion_entites_textes = autocompletion_entites_textes

        self.list = to_streamed_response_wrapper(
            autocompletion_entites_textes.list,
        )


class AsyncAutocompletionEntitesTextesResourceWithStreamingResponse:
    def __init__(self, autocompletion_entites_textes: AsyncAutocompletionEntitesTextesResource) -> None:
        self._autocompletion_entites_textes = autocompletion_entites_textes

        self.list = async_to_streamed_response_wrapper(
            autocompletion_entites_textes.list,
        )
