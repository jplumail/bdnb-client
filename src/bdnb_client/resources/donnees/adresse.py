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
from ...types.donnees import adresse_list_params
from ...types.donnees.adresse import Adresse

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
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[Adresse]:
        """Table de description des adresses.

        Les adresses dans la BDNB sont un
        sous-ensemble des adresses BAN de type `housenumber` (adressage au numéro) et
        uniquement localisé en France hexagonale et Corse. Des adresses ARCEP viennent
        compléter les adresses BAN quand ces adresses n'existent pas dans la BAN. Les
        géolocalisants ponctuels sont au format Lambert-93 (ESPG:2154).

        Args:
          cle_interop_adr: Clé d'interopérabilité de l'adresse postale

          code_commune_insee: Code INSEE de la commune

          code_departement_insee: Code département INSEE

          code_postal: Code postal

          geom_adresse: Géométrie de l'adresse (Lambert-93)

          libelle_adresse: Libellé complet de l'adresse

          libelle_commune: Libellé de la commune

          limit: Limiting and Pagination

          nom_voie: Nom de la voie

          numero: Numéro de l'adresse

          offset: Limiting and Pagination

          order: Ordering

          rep: Indice de répétition du numéro de l'adresse

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
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get_api_list(
            "/donnees/adresse",
            page=SyncDefault[Adresse],
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
            model=Adresse,
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
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Adresse, AsyncDefault[Adresse]]:
        """Table de description des adresses.

        Les adresses dans la BDNB sont un
        sous-ensemble des adresses BAN de type `housenumber` (adressage au numéro) et
        uniquement localisé en France hexagonale et Corse. Des adresses ARCEP viennent
        compléter les adresses BAN quand ces adresses n'existent pas dans la BAN. Les
        géolocalisants ponctuels sont au format Lambert-93 (ESPG:2154).

        Args:
          cle_interop_adr: Clé d'interopérabilité de l'adresse postale

          code_commune_insee: Code INSEE de la commune

          code_departement_insee: Code département INSEE

          code_postal: Code postal

          geom_adresse: Géométrie de l'adresse (Lambert-93)

          libelle_adresse: Libellé complet de l'adresse

          libelle_commune: Libellé de la commune

          limit: Limiting and Pagination

          nom_voie: Nom de la voie

          numero: Numéro de l'adresse

          offset: Limiting and Pagination

          order: Ordering

          rep: Indice de répétition du numéro de l'adresse

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
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get_api_list(
            "/donnees/adresse",
            page=AsyncDefault[Adresse],
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
            model=Adresse,
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
