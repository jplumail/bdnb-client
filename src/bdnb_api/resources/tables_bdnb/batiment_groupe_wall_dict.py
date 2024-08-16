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
from ...types.tables_bdnb import batiment_groupe_wall_dict_list_params
from ...types.tables_bdnb.batiment_groupe_wall_dict_list_response import BatimentGroupeWallDictListResponse

__all__ = ["BatimentGroupeWallDictResource", "AsyncBatimentGroupeWallDictResource"]


class BatimentGroupeWallDictResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatimentGroupeWallDictResourceWithRawResponse:
        return BatimentGroupeWallDictResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentGroupeWallDictResourceWithStreamingResponse:
        return BatimentGroupeWallDictResourceWithStreamingResponse(self)

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
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatimentGroupeWallDictListResponse:
        """
        Table contenant les donnÃ©es de prÃ©traitements de gÃ©omÃ©trie des groupes de
        bÃ¢timents : liste des parois, orientations, surfaces, pÃ©rimÃ¨tres, adjacences
        et masques solaire

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          code_departement_insee: Code dÃ©partement INSEE

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          wall_dict: liste de toutes les parois extÃ©rieures constitutives d'un bÃ¢timent (murs,
              planchers haut/bas). Collection de dictionnaires avec les clÃ©s suivantes

              - z0 : altitude au pied de la construction
              - azimuth : orientation de la paroi. (0 -> Sud)
              - hauteur : hauteur de la face (0 pour les parois horizontales)
              - inclination : 90-> vertical. 0 -> orientÃ© vers le bas (sol). 180: orientÃ©
                vers le haut (plancher haut)
              - cat_adj : Type d'adjacence de la paroi. "adjacent" : touche une autre paroi
                (mur mitoyen). "non_adjacent" : en contact avec l'ambiance extÃ©rieure
              - wall_type: floor | roof | vertical
              - wall_id : identifiant de la paroie
              - area: surface de la paroie
              - altitude : TODO
              - perimeter : pÃ©rimÃ¨tre de la face
              - shading_mask_36 (ARRAY): "Masque solaire : Elevation de l'occultation par
                tranche de 10Âº Ã partir de l'azimuth 0 (Sud)"

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
                    batiment_groupe_wall_dict_list_params.BatimentGroupeWallDictListParams,
                ),
            ),
            cast_to=BatimentGroupeWallDictListResponse,
        )


class AsyncBatimentGroupeWallDictResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatimentGroupeWallDictResourceWithRawResponse:
        return AsyncBatimentGroupeWallDictResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentGroupeWallDictResourceWithStreamingResponse:
        return AsyncBatimentGroupeWallDictResourceWithStreamingResponse(self)

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
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatimentGroupeWallDictListResponse:
        """
        Table contenant les donnÃ©es de prÃ©traitements de gÃ©omÃ©trie des groupes de
        bÃ¢timents : liste des parois, orientations, surfaces, pÃ©rimÃ¨tres, adjacences
        et masques solaire

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          code_departement_insee: Code dÃ©partement INSEE

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          wall_dict: liste de toutes les parois extÃ©rieures constitutives d'un bÃ¢timent (murs,
              planchers haut/bas). Collection de dictionnaires avec les clÃ©s suivantes

              - z0 : altitude au pied de la construction
              - azimuth : orientation de la paroi. (0 -> Sud)
              - hauteur : hauteur de la face (0 pour les parois horizontales)
              - inclination : 90-> vertical. 0 -> orientÃ© vers le bas (sol). 180: orientÃ©
                vers le haut (plancher haut)
              - cat_adj : Type d'adjacence de la paroi. "adjacent" : touche une autre paroi
                (mur mitoyen). "non_adjacent" : en contact avec l'ambiance extÃ©rieure
              - wall_type: floor | roof | vertical
              - wall_id : identifiant de la paroie
              - area: surface de la paroie
              - altitude : TODO
              - perimeter : pÃ©rimÃ¨tre de la face
              - shading_mask_36 (ARRAY): "Masque solaire : Elevation de l'occultation par
                tranche de 10Âº Ã partir de l'azimuth 0 (Sud)"

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
                    batiment_groupe_wall_dict_list_params.BatimentGroupeWallDictListParams,
                ),
            ),
            cast_to=BatimentGroupeWallDictListResponse,
        )


class BatimentGroupeWallDictResourceWithRawResponse:
    def __init__(self, batiment_groupe_wall_dict: BatimentGroupeWallDictResource) -> None:
        self._batiment_groupe_wall_dict = batiment_groupe_wall_dict

        self.list = to_raw_response_wrapper(
            batiment_groupe_wall_dict.list,
        )


class AsyncBatimentGroupeWallDictResourceWithRawResponse:
    def __init__(self, batiment_groupe_wall_dict: AsyncBatimentGroupeWallDictResource) -> None:
        self._batiment_groupe_wall_dict = batiment_groupe_wall_dict

        self.list = async_to_raw_response_wrapper(
            batiment_groupe_wall_dict.list,
        )


class BatimentGroupeWallDictResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_wall_dict: BatimentGroupeWallDictResource) -> None:
        self._batiment_groupe_wall_dict = batiment_groupe_wall_dict

        self.list = to_streamed_response_wrapper(
            batiment_groupe_wall_dict.list,
        )


class AsyncBatimentGroupeWallDictResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_wall_dict: AsyncBatimentGroupeWallDictResource) -> None:
        self._batiment_groupe_wall_dict = batiment_groupe_wall_dict

        self.list = async_to_streamed_response_wrapper(
            batiment_groupe_wall_dict.list,
        )
