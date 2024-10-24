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
from .....types.donnees.relations.batiment_groupe import adresse_list_params
from .....types.donnees.relations.batiment_groupe.rel_batiment_groupe_adresse import RelBatimentGroupeAdresse

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
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        classe: str | NotGiven = NOT_GIVEN,
        cle_interop_adr: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        geom_bat_adresse: str | NotGiven = NOT_GIVEN,
        lien_valide: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        origine: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[RelBatimentGroupeAdresse]:
        """
        Table de relation entre les adresses et les groupes de bâtiment

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          classe: Classe de méthodologie de croisement à l'adresse (Fichiers_fonciers, Cadastre)

          cle_interop_adr: Clé d'interopérabilité de l'adresse postale

          code_departement_insee: Code département INSEE

          geom_bat_adresse: Géolocalisant du trait reliant le point adresse à la géométrie du bâtiment
              groupe (Lambert-93, SRID=2154)

          lien_valide: [DEPRECIEE] (bdnb) un couple (batiment_groupe ; adresse) est considéré comme
              valide si l'adresse est une adresse ban et que le batiment_groupe est associé à
              des fichiers fonciers

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          origine: Origine de l'entrée bâtiment. Elle provient soit des données foncières (Fichiers
              Fonciers), soit d'un croisement géospatial entre le Cadastre, la BDTopo et des
              bases de données métiers (ex: BPE ou Mérimée)

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
            "/donnees/rel_batiment_groupe_adresse",
            page=SyncDefault[RelBatimentGroupeAdresse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "classe": classe,
                        "cle_interop_adr": cle_interop_adr,
                        "code_departement_insee": code_departement_insee,
                        "geom_bat_adresse": geom_bat_adresse,
                        "lien_valide": lien_valide,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "origine": origine,
                        "select": select,
                    },
                    adresse_list_params.AdresseListParams,
                ),
            ),
            model=RelBatimentGroupeAdresse,
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
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        classe: str | NotGiven = NOT_GIVEN,
        cle_interop_adr: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        geom_bat_adresse: str | NotGiven = NOT_GIVEN,
        lien_valide: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        origine: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[RelBatimentGroupeAdresse, AsyncDefault[RelBatimentGroupeAdresse]]:
        """
        Table de relation entre les adresses et les groupes de bâtiment

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          classe: Classe de méthodologie de croisement à l'adresse (Fichiers_fonciers, Cadastre)

          cle_interop_adr: Clé d'interopérabilité de l'adresse postale

          code_departement_insee: Code département INSEE

          geom_bat_adresse: Géolocalisant du trait reliant le point adresse à la géométrie du bâtiment
              groupe (Lambert-93, SRID=2154)

          lien_valide: [DEPRECIEE] (bdnb) un couple (batiment_groupe ; adresse) est considéré comme
              valide si l'adresse est une adresse ban et que le batiment_groupe est associé à
              des fichiers fonciers

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          origine: Origine de l'entrée bâtiment. Elle provient soit des données foncières (Fichiers
              Fonciers), soit d'un croisement géospatial entre le Cadastre, la BDTopo et des
              bases de données métiers (ex: BPE ou Mérimée)

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
            "/donnees/rel_batiment_groupe_adresse",
            page=AsyncDefault[RelBatimentGroupeAdresse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "classe": classe,
                        "cle_interop_adr": cle_interop_adr,
                        "code_departement_insee": code_departement_insee,
                        "geom_bat_adresse": geom_bat_adresse,
                        "lien_valide": lien_valide,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "origine": origine,
                        "select": select,
                    },
                    adresse_list_params.AdresseListParams,
                ),
            ),
            model=RelBatimentGroupeAdresse,
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
