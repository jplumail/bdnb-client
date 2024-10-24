# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, strip_not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDefault, AsyncDefault
from ..._base_client import AsyncPaginator, make_request_options
from ...types.donnees import batiment_construction_list_params
from ...types.donnees.batiment_construction import BatimentConstruction

__all__ = ["BatimentConstructionResource", "AsyncBatimentConstructionResource"]


class BatimentConstructionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatimentConstructionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return BatimentConstructionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentConstructionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return BatimentConstructionResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        altitude_sol: str | NotGiven = NOT_GIVEN,
        batiment_construction_id: str | NotGiven = NOT_GIVEN,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_commune_insee: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        code_iris: str | NotGiven = NOT_GIVEN,
        fictive_geom_cstr: str | NotGiven = NOT_GIVEN,
        geom_cstr: str | NotGiven = NOT_GIVEN,
        hauteur: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        rnb_id: str | NotGiven = NOT_GIVEN,
        s_geom_cstr: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[BatimentConstruction]:
        """
        Enceinte physique des différentes géométries qui composent le groupe de bâtiment
        ainsi que l'identifiant rnb.

        Args:
          altitude_sol: (ign) Altitude moynne au pied du bâtiment physique [m]

          batiment_construction_id: Identifiant unique de l'entrée batiment_construction.

          batiment_groupe_id: (bdnb) Clé d'Intéropérabilité du bâtiment dans la BDNB

          code_commune_insee: Code INSEE de la commune

          code_departement_insee: Code département INSEE

          code_iris: Code iris INSEE

          fictive_geom_cstr: (ign) Booléen. Si 'True', la géométrie est fictive (et la surface au sol n'est
              pas réelle), sinon elle correspond à une emprise au sol réelle

          geom_cstr: (ign) Géométrie multipolygonale de l'enceinte du bâtiment (Lambert-93)

          hauteur: (ign) Hauteur du bâtiment physique [m]

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          rnb_id: Identifiant unique de l'entrée RNB. Dans le cas d'un double rnb_id pour un màªme
              bâtiment construction, celui appartenant au bâtiment construction avec le plus
              d'emprise au sol est pris en compte.

          s_geom_cstr: (ign) Surface au sol de la géométrie de la construction [mÂ²]

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
            "/donnees/batiment_construction",
            page=SyncDefault[BatimentConstruction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "altitude_sol": altitude_sol,
                        "batiment_construction_id": batiment_construction_id,
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_commune_insee": code_commune_insee,
                        "code_departement_insee": code_departement_insee,
                        "code_iris": code_iris,
                        "fictive_geom_cstr": fictive_geom_cstr,
                        "geom_cstr": geom_cstr,
                        "hauteur": hauteur,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "rnb_id": rnb_id,
                        "s_geom_cstr": s_geom_cstr,
                        "select": select,
                    },
                    batiment_construction_list_params.BatimentConstructionListParams,
                ),
            ),
            model=BatimentConstruction,
        )


class AsyncBatimentConstructionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatimentConstructionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncBatimentConstructionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentConstructionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncBatimentConstructionResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        altitude_sol: str | NotGiven = NOT_GIVEN,
        batiment_construction_id: str | NotGiven = NOT_GIVEN,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_commune_insee: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        code_iris: str | NotGiven = NOT_GIVEN,
        fictive_geom_cstr: str | NotGiven = NOT_GIVEN,
        geom_cstr: str | NotGiven = NOT_GIVEN,
        hauteur: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        rnb_id: str | NotGiven = NOT_GIVEN,
        s_geom_cstr: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BatimentConstruction, AsyncDefault[BatimentConstruction]]:
        """
        Enceinte physique des différentes géométries qui composent le groupe de bâtiment
        ainsi que l'identifiant rnb.

        Args:
          altitude_sol: (ign) Altitude moynne au pied du bâtiment physique [m]

          batiment_construction_id: Identifiant unique de l'entrée batiment_construction.

          batiment_groupe_id: (bdnb) Clé d'Intéropérabilité du bâtiment dans la BDNB

          code_commune_insee: Code INSEE de la commune

          code_departement_insee: Code département INSEE

          code_iris: Code iris INSEE

          fictive_geom_cstr: (ign) Booléen. Si 'True', la géométrie est fictive (et la surface au sol n'est
              pas réelle), sinon elle correspond à une emprise au sol réelle

          geom_cstr: (ign) Géométrie multipolygonale de l'enceinte du bâtiment (Lambert-93)

          hauteur: (ign) Hauteur du bâtiment physique [m]

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          rnb_id: Identifiant unique de l'entrée RNB. Dans le cas d'un double rnb_id pour un màªme
              bâtiment construction, celui appartenant au bâtiment construction avec le plus
              d'emprise au sol est pris en compte.

          s_geom_cstr: (ign) Surface au sol de la géométrie de la construction [mÂ²]

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
            "/donnees/batiment_construction",
            page=AsyncDefault[BatimentConstruction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "altitude_sol": altitude_sol,
                        "batiment_construction_id": batiment_construction_id,
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_commune_insee": code_commune_insee,
                        "code_departement_insee": code_departement_insee,
                        "code_iris": code_iris,
                        "fictive_geom_cstr": fictive_geom_cstr,
                        "geom_cstr": geom_cstr,
                        "hauteur": hauteur,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "rnb_id": rnb_id,
                        "s_geom_cstr": s_geom_cstr,
                        "select": select,
                    },
                    batiment_construction_list_params.BatimentConstructionListParams,
                ),
            ),
            model=BatimentConstruction,
        )


class BatimentConstructionResourceWithRawResponse:
    def __init__(self, batiment_construction: BatimentConstructionResource) -> None:
        self._batiment_construction = batiment_construction

        self.list = to_raw_response_wrapper(
            batiment_construction.list,
        )


class AsyncBatimentConstructionResourceWithRawResponse:
    def __init__(self, batiment_construction: AsyncBatimentConstructionResource) -> None:
        self._batiment_construction = batiment_construction

        self.list = async_to_raw_response_wrapper(
            batiment_construction.list,
        )


class BatimentConstructionResourceWithStreamingResponse:
    def __init__(self, batiment_construction: BatimentConstructionResource) -> None:
        self._batiment_construction = batiment_construction

        self.list = to_streamed_response_wrapper(
            batiment_construction.list,
        )


class AsyncBatimentConstructionResourceWithStreamingResponse:
    def __init__(self, batiment_construction: AsyncBatimentConstructionResource) -> None:
        self._batiment_construction = batiment_construction

        self.list = async_to_streamed_response_wrapper(
            batiment_construction.list,
        )
