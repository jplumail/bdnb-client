# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
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
from ...types.stats import batiment_groupe_list_params
from ..._base_client import make_request_options
from ...types.stats.batiment_groupe_json_stats import BatimentGroupeJsonStats

__all__ = ["BatimentGroupeResource", "AsyncBatimentGroupeResource"]


class BatimentGroupeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatimentGroupeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return BatimentGroupeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentGroupeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return BatimentGroupeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        groupby: str,
        colonnes: str | NotGiven = NOT_GIVEN,
        epsg: int | NotGiven = NOT_GIVEN,
        filter: str | NotGiven = NOT_GIVEN,
        output_format: Literal["json", "geojson", "raw_query"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatimentGroupeJsonStats:
        """
        Agrégation et calcul de statistiques filtrées

        Args:
          groupby: colonnes de group by (agrégation)

          colonnes: colonnes pour lesquelles il faut calculer des statistiques (separées par
              virgules, pas d'espaces). Par default retourne toutes les colonnes ("\\**")

          epsg: EPSG de sortie pour les géométries. Exemple : 4326

          filter: filtre à appliquer à la population de bâtiments avec syntaxe PostgREST pour les
              operateurs

          output_format: type de sortie. valeurs possibles: json, geojson, raw_query raw_query retourne
              pas les données agrégées mais uniquement la requàªte SQL d'agrégation (pour
              débogage)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/stats/batiment_groupe",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "groupby": groupby,
                        "colonnes": colonnes,
                        "epsg": epsg,
                        "filter": filter,
                        "output_format": output_format,
                    },
                    batiment_groupe_list_params.BatimentGroupeListParams,
                ),
            ),
            cast_to=BatimentGroupeJsonStats,
        )


class AsyncBatimentGroupeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatimentGroupeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncBatimentGroupeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentGroupeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncBatimentGroupeResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        groupby: str,
        colonnes: str | NotGiven = NOT_GIVEN,
        epsg: int | NotGiven = NOT_GIVEN,
        filter: str | NotGiven = NOT_GIVEN,
        output_format: Literal["json", "geojson", "raw_query"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatimentGroupeJsonStats:
        """
        Agrégation et calcul de statistiques filtrées

        Args:
          groupby: colonnes de group by (agrégation)

          colonnes: colonnes pour lesquelles il faut calculer des statistiques (separées par
              virgules, pas d'espaces). Par default retourne toutes les colonnes ("\\**")

          epsg: EPSG de sortie pour les géométries. Exemple : 4326

          filter: filtre à appliquer à la population de bâtiments avec syntaxe PostgREST pour les
              operateurs

          output_format: type de sortie. valeurs possibles: json, geojson, raw_query raw_query retourne
              pas les données agrégées mais uniquement la requàªte SQL d'agrégation (pour
              débogage)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/stats/batiment_groupe",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "groupby": groupby,
                        "colonnes": colonnes,
                        "epsg": epsg,
                        "filter": filter,
                        "output_format": output_format,
                    },
                    batiment_groupe_list_params.BatimentGroupeListParams,
                ),
            ),
            cast_to=BatimentGroupeJsonStats,
        )


class BatimentGroupeResourceWithRawResponse:
    def __init__(self, batiment_groupe: BatimentGroupeResource) -> None:
        self._batiment_groupe = batiment_groupe

        self.list = to_raw_response_wrapper(
            batiment_groupe.list,
        )


class AsyncBatimentGroupeResourceWithRawResponse:
    def __init__(self, batiment_groupe: AsyncBatimentGroupeResource) -> None:
        self._batiment_groupe = batiment_groupe

        self.list = async_to_raw_response_wrapper(
            batiment_groupe.list,
        )


class BatimentGroupeResourceWithStreamingResponse:
    def __init__(self, batiment_groupe: BatimentGroupeResource) -> None:
        self._batiment_groupe = batiment_groupe

        self.list = to_streamed_response_wrapper(
            batiment_groupe.list,
        )


class AsyncBatimentGroupeResourceWithStreamingResponse:
    def __init__(self, batiment_groupe: AsyncBatimentGroupeResource) -> None:
        self._batiment_groupe = batiment_groupe

        self.list = async_to_streamed_response_wrapper(
            batiment_groupe.list,
        )
