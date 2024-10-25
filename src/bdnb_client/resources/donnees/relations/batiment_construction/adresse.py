# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, strip_not_given
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncDefault, AsyncDefault
from ....._base_client import AsyncPaginator, make_request_options
from .....types.donnees.relations.batiment_construction import adresse_list_params
from .....types.donnees.relations.batiment_construction.rel_batiment_construction_adresse import (
    RelBatimentConstructionAdresse,
)

__all__ = ["AdresseResource", "AsyncAdresseResource"]


class AdresseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdresseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AdresseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdresseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AdresseResourceWithStreamingResponse(self)

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
    ) -> SyncDefault[RelBatimentConstructionAdresse]:
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
        return self._get_api_list(
            "/donnees/rel_batiment_construction_adresse",
            page=SyncDefault[RelBatimentConstructionAdresse],
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
                    adresse_list_params.AdresseListParams,
                ),
            ),
            model=RelBatimentConstructionAdresse,
        )


class AsyncAdresseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdresseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncAdresseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdresseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncAdresseResourceWithStreamingResponse(self)

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
    ) -> AsyncPaginator[RelBatimentConstructionAdresse, AsyncDefault[RelBatimentConstructionAdresse]]:
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
        return self._get_api_list(
            "/donnees/rel_batiment_construction_adresse",
            page=AsyncDefault[RelBatimentConstructionAdresse],
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
                    adresse_list_params.AdresseListParams,
                ),
            ),
            model=RelBatimentConstructionAdresse,
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
