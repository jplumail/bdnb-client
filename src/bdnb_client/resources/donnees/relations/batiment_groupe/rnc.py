# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.donnees.relations.batiment_groupe import rnc_list_params
from .....types.donnees.relations.batiment_groupe.rnc_list_response import RncListResponse

__all__ = ["RncResource", "AsyncRncResource"]


class RncResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RncResourceWithRawResponse:
        return RncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RncResourceWithStreamingResponse:
        return RncResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        adresse_brut: str | NotGiven = NOT_GIVEN,
        adresse_geocodee: str | NotGiven = NOT_GIVEN,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        cle_interop_adr: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        fiabilite_geocodage: str | NotGiven = NOT_GIVEN,
        fiabilite_globale: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        numero_immat: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        parcelle_id: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RncListResponse:
        """
        Table de relation entre les bâtiments de la BDNB et les éléments de la table RNC

        Args:
          adresse_brut: adresse brute envoyée au géocodeur

          adresse_geocodee: libelle de l'adresse retournée par le géocodeur

          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          cle_interop_adr: Clé d'interopérabilité de l'adresse postale

          code_departement_insee: Code département INSEE

          fiabilite_geocodage: fiabilité du géocodage

          fiabilite_globale: fiabilité du global du croisement

          limit: Limiting and Pagination

          numero_immat: identifiant de la table rnc

          offset: Limiting and Pagination

          order: Ordering

          parcelle_id: (ffo:idpar) Identifiant de parcelle (Concaténation de ccodep, ccocom, ccopre,
              ccosec, dnupla)

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
        return self._get(
            "/donnees/rel_batiment_groupe_rnc",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "adresse_brut": adresse_brut,
                        "adresse_geocodee": adresse_geocodee,
                        "batiment_groupe_id": batiment_groupe_id,
                        "cle_interop_adr": cle_interop_adr,
                        "code_departement_insee": code_departement_insee,
                        "fiabilite_geocodage": fiabilite_geocodage,
                        "fiabilite_globale": fiabilite_globale,
                        "limit": limit,
                        "numero_immat": numero_immat,
                        "offset": offset,
                        "order": order,
                        "parcelle_id": parcelle_id,
                        "select": select,
                    },
                    rnc_list_params.RncListParams,
                ),
            ),
            cast_to=RncListResponse,
        )


class AsyncRncResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRncResourceWithRawResponse:
        return AsyncRncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRncResourceWithStreamingResponse:
        return AsyncRncResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        adresse_brut: str | NotGiven = NOT_GIVEN,
        adresse_geocodee: str | NotGiven = NOT_GIVEN,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        cle_interop_adr: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        fiabilite_geocodage: str | NotGiven = NOT_GIVEN,
        fiabilite_globale: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        numero_immat: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        parcelle_id: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RncListResponse:
        """
        Table de relation entre les bâtiments de la BDNB et les éléments de la table RNC

        Args:
          adresse_brut: adresse brute envoyée au géocodeur

          adresse_geocodee: libelle de l'adresse retournée par le géocodeur

          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          cle_interop_adr: Clé d'interopérabilité de l'adresse postale

          code_departement_insee: Code département INSEE

          fiabilite_geocodage: fiabilité du géocodage

          fiabilite_globale: fiabilité du global du croisement

          limit: Limiting and Pagination

          numero_immat: identifiant de la table rnc

          offset: Limiting and Pagination

          order: Ordering

          parcelle_id: (ffo:idpar) Identifiant de parcelle (Concaténation de ccodep, ccocom, ccopre,
              ccosec, dnupla)

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
        return await self._get(
            "/donnees/rel_batiment_groupe_rnc",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "adresse_brut": adresse_brut,
                        "adresse_geocodee": adresse_geocodee,
                        "batiment_groupe_id": batiment_groupe_id,
                        "cle_interop_adr": cle_interop_adr,
                        "code_departement_insee": code_departement_insee,
                        "fiabilite_geocodage": fiabilite_geocodage,
                        "fiabilite_globale": fiabilite_globale,
                        "limit": limit,
                        "numero_immat": numero_immat,
                        "offset": offset,
                        "order": order,
                        "parcelle_id": parcelle_id,
                        "select": select,
                    },
                    rnc_list_params.RncListParams,
                ),
            ),
            cast_to=RncListResponse,
        )


class RncResourceWithRawResponse:
    def __init__(self, rnc: RncResource) -> None:
        self._rnc = rnc

        self.list = to_raw_response_wrapper(
            rnc.list,
        )


class AsyncRncResourceWithRawResponse:
    def __init__(self, rnc: AsyncRncResource) -> None:
        self._rnc = rnc

        self.list = async_to_raw_response_wrapper(
            rnc.list,
        )


class RncResourceWithStreamingResponse:
    def __init__(self, rnc: RncResource) -> None:
        self._rnc = rnc

        self.list = to_streamed_response_wrapper(
            rnc.list,
        )


class AsyncRncResourceWithStreamingResponse:
    def __init__(self, rnc: AsyncRncResource) -> None:
        self._rnc = rnc

        self.list = async_to_streamed_response_wrapper(
            rnc.list,
        )
