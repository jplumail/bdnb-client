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
from ...types.tables_bdnb import adresse_list_params
from ...types.tables_bdnb.adresse_list_response import AdresseListResponse

__all__ = ["AdresseResource", "AsyncAdresseResource"]


class AdresseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdresseResourceWithRawResponse:
        return AdresseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdresseResourceWithStreamingResponse:
        return AdresseResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cle_interop_adr: str | NotGiven = NOT_GIVEN,
        code_commune_insee: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        code_postal: str | NotGiven = NOT_GIVEN,
        geom_adresse: str | NotGiven = NOT_GIVEN,
        libelle_adresse: str | NotGiven = NOT_GIVEN,
        libelle_commune: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nom_voie: str | NotGiven = NOT_GIVEN,
        numero: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        rep: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        source: str | NotGiven = NOT_GIVEN,
        type_voie: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdresseListResponse:
        """Table de description des adresses.

        Les adresses dans la BDNB sont un
        sous-ensemble des adresses BAN de type `housenumber` (adressage au numÃ©ro) et
        uniquement localisÃ© en France hexagonale et Corse. Des adresses ARCEP viennent
        complÃ©ter les adresses BAN quand ces adresses n'existent pas dans la BAN. Les
        gÃ©olocalisants ponctuels sont au format Lambert-93 (ESPG:2154).

        Args:
          cle_interop_adr: ClÃ© d'interopÃ©rabilitÃ© de l'adresse postale

          code_commune_insee: Code INSEE de la commune

          code_departement_insee: Code dÃ©partement INSEE

          code_postal: Code postal

          geom_adresse: GÃ©omÃ©trie de l'adresse (Lambert-93)

          libelle_adresse: LibellÃ© complet de l'adresse

          libelle_commune: LibellÃ© de la commune

          limit: Limiting and Pagination

          nom_voie: Nom de la voie

          numero: NumÃ©ro de l'adresse

          offset: Limiting and Pagination

          order: Ordering

          rep: Indice de rÃ©pÃ©tition du numÃ©ro de l'adresse

          select: Filtering Columns

          source: TODO

          type_voie: Type de voie

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
            "/donnees/adresse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cle_interop_adr": cle_interop_adr,
                        "code_commune_insee": code_commune_insee,
                        "code_departement_insee": code_departement_insee,
                        "code_postal": code_postal,
                        "geom_adresse": geom_adresse,
                        "libelle_adresse": libelle_adresse,
                        "libelle_commune": libelle_commune,
                        "limit": limit,
                        "nom_voie": nom_voie,
                        "numero": numero,
                        "offset": offset,
                        "order": order,
                        "rep": rep,
                        "select": select,
                        "source": source,
                        "type_voie": type_voie,
                    },
                    adresse_list_params.AdresseListParams,
                ),
            ),
            cast_to=AdresseListResponse,
        )


class AsyncAdresseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdresseResourceWithRawResponse:
        return AsyncAdresseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdresseResourceWithStreamingResponse:
        return AsyncAdresseResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cle_interop_adr: str | NotGiven = NOT_GIVEN,
        code_commune_insee: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        code_postal: str | NotGiven = NOT_GIVEN,
        geom_adresse: str | NotGiven = NOT_GIVEN,
        libelle_adresse: str | NotGiven = NOT_GIVEN,
        libelle_commune: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nom_voie: str | NotGiven = NOT_GIVEN,
        numero: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        rep: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        source: str | NotGiven = NOT_GIVEN,
        type_voie: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdresseListResponse:
        """Table de description des adresses.

        Les adresses dans la BDNB sont un
        sous-ensemble des adresses BAN de type `housenumber` (adressage au numÃ©ro) et
        uniquement localisÃ© en France hexagonale et Corse. Des adresses ARCEP viennent
        complÃ©ter les adresses BAN quand ces adresses n'existent pas dans la BAN. Les
        gÃ©olocalisants ponctuels sont au format Lambert-93 (ESPG:2154).

        Args:
          cle_interop_adr: ClÃ© d'interopÃ©rabilitÃ© de l'adresse postale

          code_commune_insee: Code INSEE de la commune

          code_departement_insee: Code dÃ©partement INSEE

          code_postal: Code postal

          geom_adresse: GÃ©omÃ©trie de l'adresse (Lambert-93)

          libelle_adresse: LibellÃ© complet de l'adresse

          libelle_commune: LibellÃ© de la commune

          limit: Limiting and Pagination

          nom_voie: Nom de la voie

          numero: NumÃ©ro de l'adresse

          offset: Limiting and Pagination

          order: Ordering

          rep: Indice de rÃ©pÃ©tition du numÃ©ro de l'adresse

          select: Filtering Columns

          source: TODO

          type_voie: Type de voie

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
            "/donnees/adresse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cle_interop_adr": cle_interop_adr,
                        "code_commune_insee": code_commune_insee,
                        "code_departement_insee": code_departement_insee,
                        "code_postal": code_postal,
                        "geom_adresse": geom_adresse,
                        "libelle_adresse": libelle_adresse,
                        "libelle_commune": libelle_commune,
                        "limit": limit,
                        "nom_voie": nom_voie,
                        "numero": numero,
                        "offset": offset,
                        "order": order,
                        "rep": rep,
                        "select": select,
                        "source": source,
                        "type_voie": type_voie,
                    },
                    adresse_list_params.AdresseListParams,
                ),
            ),
            cast_to=AdresseListResponse,
        )


class AdresseResourceWithRawResponse:
    def __init__(self, adresse: AdresseResource) -> None:
        self._adresse = adresse

        self.list = to_raw_response_wrapper(
            adresse.list,
        )


class AsyncAdresseResourceWithRawResponse:
    def __init__(self, adresse: AsyncAdresseResource) -> None:
        self._adresse = adresse

        self.list = async_to_raw_response_wrapper(
            adresse.list,
        )


class AdresseResourceWithStreamingResponse:
    def __init__(self, adresse: AdresseResource) -> None:
        self._adresse = adresse

        self.list = to_streamed_response_wrapper(
            adresse.list,
        )


class AsyncAdresseResourceWithStreamingResponse:
    def __init__(self, adresse: AsyncAdresseResource) -> None:
        self._adresse = adresse

        self.list = async_to_streamed_response_wrapper(
            adresse.list,
        )
