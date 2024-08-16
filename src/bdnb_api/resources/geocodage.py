# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import geocodage_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
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

__all__ = ["GeocodageResource", "AsyncGeocodageResource"]


class GeocodageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GeocodageResourceWithRawResponse:
        return GeocodageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GeocodageResourceWithStreamingResponse:
        return GeocodageResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        q: str,
        autocomplete: int | NotGiven = NOT_GIVEN,
        citycode: str | NotGiven = NOT_GIVEN,
        lat: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        lon: str | NotGiven = NOT_GIVEN,
        postcode: str | NotGiven = NOT_GIVEN,
        type: Literal["street", "housenumber", "locality", "municipality"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Service de géocodage.

        Prend en entrée un chaà®ne de caractère et retourne des
        coordonnées géographiques. Permet l'autocomplétion dans une barre de saisie

        Args:
          q: Adresse texte

          autocomplete: Avec autocomplete on peut désactiver les traitements dâ€™auto-complétion
              autocomplete=0

          citycode: Limite du nombre de réponses

          lat: latitude. Avec lat et lon on peut donner une priorité géographique

          limit: Limite du nombre de réponses

          lon: longitude. Avec lat et lon on peut donner une priorité géographique

          postcode: Limite du nombre de réponses

          type: Limite du nombre de réponses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/geocodage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "autocomplete": autocomplete,
                        "citycode": citycode,
                        "lat": lat,
                        "limit": limit,
                        "lon": lon,
                        "postcode": postcode,
                        "type": type,
                    },
                    geocodage_list_params.GeocodageListParams,
                ),
            ),
            cast_to=object,
        )


class AsyncGeocodageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGeocodageResourceWithRawResponse:
        return AsyncGeocodageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGeocodageResourceWithStreamingResponse:
        return AsyncGeocodageResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        q: str,
        autocomplete: int | NotGiven = NOT_GIVEN,
        citycode: str | NotGiven = NOT_GIVEN,
        lat: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        lon: str | NotGiven = NOT_GIVEN,
        postcode: str | NotGiven = NOT_GIVEN,
        type: Literal["street", "housenumber", "locality", "municipality"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Service de géocodage.

        Prend en entrée un chaà®ne de caractère et retourne des
        coordonnées géographiques. Permet l'autocomplétion dans une barre de saisie

        Args:
          q: Adresse texte

          autocomplete: Avec autocomplete on peut désactiver les traitements dâ€™auto-complétion
              autocomplete=0

          citycode: Limite du nombre de réponses

          lat: latitude. Avec lat et lon on peut donner une priorité géographique

          limit: Limite du nombre de réponses

          lon: longitude. Avec lat et lon on peut donner une priorité géographique

          postcode: Limite du nombre de réponses

          type: Limite du nombre de réponses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/geocodage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "autocomplete": autocomplete,
                        "citycode": citycode,
                        "lat": lat,
                        "limit": limit,
                        "lon": lon,
                        "postcode": postcode,
                        "type": type,
                    },
                    geocodage_list_params.GeocodageListParams,
                ),
            ),
            cast_to=object,
        )


class GeocodageResourceWithRawResponse:
    def __init__(self, geocodage: GeocodageResource) -> None:
        self._geocodage = geocodage

        self.list = to_raw_response_wrapper(
            geocodage.list,
        )


class AsyncGeocodageResourceWithRawResponse:
    def __init__(self, geocodage: AsyncGeocodageResource) -> None:
        self._geocodage = geocodage

        self.list = async_to_raw_response_wrapper(
            geocodage.list,
        )


class GeocodageResourceWithStreamingResponse:
    def __init__(self, geocodage: GeocodageResource) -> None:
        self._geocodage = geocodage

        self.list = to_streamed_response_wrapper(
            geocodage.list,
        )


class AsyncGeocodageResourceWithStreamingResponse:
    def __init__(self, geocodage: AsyncGeocodageResource) -> None:
        self._geocodage = geocodage

        self.list = async_to_streamed_response_wrapper(
            geocodage.list,
        )
