# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import autocompletion_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, strip_not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncDefault, AsyncDefault
from .._base_client import AsyncPaginator, make_request_options
from ..types.autocompletion_entites_texte import AutocompletionEntitesTexte

__all__ = ["AutocompletionResource", "AsyncAutocompletionResource"]


class AutocompletionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutocompletionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AutocompletionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutocompletionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AutocompletionResourceWithStreamingResponse(self)

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
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[AutocompletionEntitesTexte]:
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
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get_api_list(
            "/autocompletion_entites_texte",
            page=SyncDefault[AutocompletionEntitesTexte],
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
                    autocompletion_list_params.AutocompletionListParams,
                ),
            ),
            model=AutocompletionEntitesTexte,
        )


class AsyncAutocompletionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutocompletionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncAutocompletionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutocompletionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncAutocompletionResourceWithStreamingResponse(self)

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
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AutocompletionEntitesTexte, AsyncDefault[AutocompletionEntitesTexte]]:
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
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get_api_list(
            "/autocompletion_entites_texte",
            page=AsyncDefault[AutocompletionEntitesTexte],
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
                    autocompletion_list_params.AutocompletionListParams,
                ),
            ),
            model=AutocompletionEntitesTexte,
        )


class AutocompletionResourceWithRawResponse:
    def __init__(self, autocompletion: AutocompletionResource) -> None:
        self._autocompletion = autocompletion

        self.list = to_raw_response_wrapper(
            autocompletion.list,
        )


class AsyncAutocompletionResourceWithRawResponse:
    def __init__(self, autocompletion: AsyncAutocompletionResource) -> None:
        self._autocompletion = autocompletion

        self.list = async_to_raw_response_wrapper(
            autocompletion.list,
        )


class AutocompletionResourceWithStreamingResponse:
    def __init__(self, autocompletion: AutocompletionResource) -> None:
        self._autocompletion = autocompletion

        self.list = to_streamed_response_wrapper(
            autocompletion.list,
        )


class AsyncAutocompletionResourceWithStreamingResponse:
    def __init__(self, autocompletion: AsyncAutocompletionResource) -> None:
        self._autocompletion = autocompletion

        self.list = async_to_streamed_response_wrapper(
            autocompletion.list,
        )
