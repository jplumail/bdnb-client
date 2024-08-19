# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.donnees.batiment_groupe import wall_dict_list_params
from ....types.donnees.batiment_groupe.wall_dict_list_response import WallDictListResponse

__all__ = ["WallDictResource", "AsyncWallDictResource"]


class WallDictResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WallDictResourceWithRawResponse:
        return WallDictResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WallDictResourceWithStreamingResponse:
        return WallDictResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        wall_dict: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WallDictListResponse:
        """
        Table contenant les données de prétraitements de géométrie des groupes de
        bâtiments : liste des parois, orientations, surfaces, périmètres, adjacences et
        masques solaire

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          wall_dict: liste de toutes les parois extérieures constitutives d'un bâtiment (murs,
              planchers haut/bas). Collection de dictionnaires avec les clés suivantes

              - z0 : altitude au pied de la construction
              - azimuth : orientation de la paroi. (0 -> Sud)
              - hauteur : hauteur de la face (0 pour les parois horizontales)
              - inclination : 90-> vertical. 0 -> orienté vers le bas (sol). 180: orienté vers
                le haut (plancher haut)
              - cat_adj : Type d'adjacence de la paroi. "adjacent" : touche une autre paroi
                (mur mitoyen). "non_adjacent" : en contact avec l'ambiance extérieure
              - wall_type: floor | roof | vertical
              - wall_id : identifiant de la paroie
              - area: surface de la paroie
              - altitude : TODO
              - perimeter : périmètre de la face
              - shading_mask_36 (ARRAY): "Masque solaire : Elevation de l'occultation par
                tranche de 10Âº à partir de l'azimuth 0 (Sud)"

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
            "/donnees/batiment_groupe_wall_dict",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                        "wall_dict": wall_dict,
                    },
                    wall_dict_list_params.WallDictListParams,
                ),
            ),
            cast_to=WallDictListResponse,
        )


class AsyncWallDictResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWallDictResourceWithRawResponse:
        return AsyncWallDictResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWallDictResourceWithStreamingResponse:
        return AsyncWallDictResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        wall_dict: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WallDictListResponse:
        """
        Table contenant les données de prétraitements de géométrie des groupes de
        bâtiments : liste des parois, orientations, surfaces, périmètres, adjacences et
        masques solaire

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          wall_dict: liste de toutes les parois extérieures constitutives d'un bâtiment (murs,
              planchers haut/bas). Collection de dictionnaires avec les clés suivantes

              - z0 : altitude au pied de la construction
              - azimuth : orientation de la paroi. (0 -> Sud)
              - hauteur : hauteur de la face (0 pour les parois horizontales)
              - inclination : 90-> vertical. 0 -> orienté vers le bas (sol). 180: orienté vers
                le haut (plancher haut)
              - cat_adj : Type d'adjacence de la paroi. "adjacent" : touche une autre paroi
                (mur mitoyen). "non_adjacent" : en contact avec l'ambiance extérieure
              - wall_type: floor | roof | vertical
              - wall_id : identifiant de la paroie
              - area: surface de la paroie
              - altitude : TODO
              - perimeter : périmètre de la face
              - shading_mask_36 (ARRAY): "Masque solaire : Elevation de l'occultation par
                tranche de 10Âº à partir de l'azimuth 0 (Sud)"

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
            "/donnees/batiment_groupe_wall_dict",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                        "wall_dict": wall_dict,
                    },
                    wall_dict_list_params.WallDictListParams,
                ),
            ),
            cast_to=WallDictListResponse,
        )


class WallDictResourceWithRawResponse:
    def __init__(self, wall_dict: WallDictResource) -> None:
        self._wall_dict = wall_dict

        self.list = to_raw_response_wrapper(
            wall_dict.list,
        )


class AsyncWallDictResourceWithRawResponse:
    def __init__(self, wall_dict: AsyncWallDictResource) -> None:
        self._wall_dict = wall_dict

        self.list = async_to_raw_response_wrapper(
            wall_dict.list,
        )


class WallDictResourceWithStreamingResponse:
    def __init__(self, wall_dict: WallDictResource) -> None:
        self._wall_dict = wall_dict

        self.list = to_streamed_response_wrapper(
            wall_dict.list,
        )


class AsyncWallDictResourceWithStreamingResponse:
    def __init__(self, wall_dict: AsyncWallDictResource) -> None:
        self._wall_dict = wall_dict

        self.list = async_to_streamed_response_wrapper(
            wall_dict.list,
        )