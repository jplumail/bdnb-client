# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
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
from ...types.donnees import rel_batiment_construction_adresse_list_params
from ...types.donnees.rel_batiment_construction_adresse_list_response import RelBatimentConstructionAdresseListResponse

__all__ = ["RelBatimentConstructionAdresseResource", "AsyncRelBatimentConstructionAdresseResource"]


class RelBatimentConstructionAdresseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RelBatimentConstructionAdresseResourceWithRawResponse:
        return RelBatimentConstructionAdresseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RelBatimentConstructionAdresseResourceWithStreamingResponse:
        return RelBatimentConstructionAdresseResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        adresse_principale: str | NotGiven = NOT_GIVEN,
        batiment_construction_id: str | NotGiven = NOT_GIVEN,
        cle_interop_adr: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        distance_batiment_construction_adresse: str | NotGiven = NOT_GIVEN,
        fiabilite: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RelBatimentConstructionAdresseListResponse:
        """
        Table de relation entre les adresses postales BAN/Arcep et les entrées de la
        table [batiment_construction]. Pour plus d'informations voir la méthodologie
        détaillée d'association des adresses aux bâtiments, publiée sur le site de la
        BDNB.

        Args:
          adresse_principale: Booléen précisant si l'adresse courante est l'une des adresses principales de la
              construction ou non. Une relation est taguée comme `principale` si l'adresse qui
              la compose obtient le score de fiabilité le plus important parmi toutes les
              adresses desservant une màªme construction. Il se peut, par conséquent, qu'une
              construction ait plusieurs adresses principales : toutes celles ayant le score
              de fiabilité le plus haut pour cette construction.

          batiment_construction_id: Identifiant unique du bâtiment physique de la BDNB -> cleabs (ign) + index de
              sub-division (si construction sur plusieurs parcelles)

          cle_interop_adr: Clé d'interopérabilité de l'adresse postale

          code_departement_insee: Code département INSEE

          distance_batiment_construction_adresse: Distance entre le géolocalisant adresse et la géométrie de bâtiment

          fiabilite: Niveau de fiabilité

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

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
            "/donnees/rel_batiment_construction_adresse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "adresse_principale": adresse_principale,
                        "batiment_construction_id": batiment_construction_id,
                        "cle_interop_adr": cle_interop_adr,
                        "code_departement_insee": code_departement_insee,
                        "distance_batiment_construction_adresse": distance_batiment_construction_adresse,
                        "fiabilite": fiabilite,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    rel_batiment_construction_adresse_list_params.RelBatimentConstructionAdresseListParams,
                ),
            ),
            cast_to=RelBatimentConstructionAdresseListResponse,
        )


class AsyncRelBatimentConstructionAdresseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRelBatimentConstructionAdresseResourceWithRawResponse:
        return AsyncRelBatimentConstructionAdresseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRelBatimentConstructionAdresseResourceWithStreamingResponse:
        return AsyncRelBatimentConstructionAdresseResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        adresse_principale: str | NotGiven = NOT_GIVEN,
        batiment_construction_id: str | NotGiven = NOT_GIVEN,
        cle_interop_adr: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        distance_batiment_construction_adresse: str | NotGiven = NOT_GIVEN,
        fiabilite: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RelBatimentConstructionAdresseListResponse:
        """
        Table de relation entre les adresses postales BAN/Arcep et les entrées de la
        table [batiment_construction]. Pour plus d'informations voir la méthodologie
        détaillée d'association des adresses aux bâtiments, publiée sur le site de la
        BDNB.

        Args:
          adresse_principale: Booléen précisant si l'adresse courante est l'une des adresses principales de la
              construction ou non. Une relation est taguée comme `principale` si l'adresse qui
              la compose obtient le score de fiabilité le plus important parmi toutes les
              adresses desservant une màªme construction. Il se peut, par conséquent, qu'une
              construction ait plusieurs adresses principales : toutes celles ayant le score
              de fiabilité le plus haut pour cette construction.

          batiment_construction_id: Identifiant unique du bâtiment physique de la BDNB -> cleabs (ign) + index de
              sub-division (si construction sur plusieurs parcelles)

          cle_interop_adr: Clé d'interopérabilité de l'adresse postale

          code_departement_insee: Code département INSEE

          distance_batiment_construction_adresse: Distance entre le géolocalisant adresse et la géométrie de bâtiment

          fiabilite: Niveau de fiabilité

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

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
            "/donnees/rel_batiment_construction_adresse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "adresse_principale": adresse_principale,
                        "batiment_construction_id": batiment_construction_id,
                        "cle_interop_adr": cle_interop_adr,
                        "code_departement_insee": code_departement_insee,
                        "distance_batiment_construction_adresse": distance_batiment_construction_adresse,
                        "fiabilite": fiabilite,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    rel_batiment_construction_adresse_list_params.RelBatimentConstructionAdresseListParams,
                ),
            ),
            cast_to=RelBatimentConstructionAdresseListResponse,
        )


class RelBatimentConstructionAdresseResourceWithRawResponse:
    def __init__(self, rel_batiment_construction_adresse: RelBatimentConstructionAdresseResource) -> None:
        self._rel_batiment_construction_adresse = rel_batiment_construction_adresse

        self.list = to_raw_response_wrapper(
            rel_batiment_construction_adresse.list,
        )


class AsyncRelBatimentConstructionAdresseResourceWithRawResponse:
    def __init__(self, rel_batiment_construction_adresse: AsyncRelBatimentConstructionAdresseResource) -> None:
        self._rel_batiment_construction_adresse = rel_batiment_construction_adresse

        self.list = async_to_raw_response_wrapper(
            rel_batiment_construction_adresse.list,
        )


class RelBatimentConstructionAdresseResourceWithStreamingResponse:
    def __init__(self, rel_batiment_construction_adresse: RelBatimentConstructionAdresseResource) -> None:
        self._rel_batiment_construction_adresse = rel_batiment_construction_adresse

        self.list = to_streamed_response_wrapper(
            rel_batiment_construction_adresse.list,
        )


class AsyncRelBatimentConstructionAdresseResourceWithStreamingResponse:
    def __init__(self, rel_batiment_construction_adresse: AsyncRelBatimentConstructionAdresseResource) -> None:
        self._rel_batiment_construction_adresse = rel_batiment_construction_adresse

        self.list = async_to_streamed_response_wrapper(
            rel_batiment_construction_adresse.list,
        )
