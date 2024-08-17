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
from ...types.donnees import rel_batiment_groupe_adresse_list_params
from ...types.donnees.rel_batiment_groupe_adresse_list_response import RelBatimentGroupeAdresseListResponse

__all__ = ["RelBatimentGroupeAdresseResource", "AsyncRelBatimentGroupeAdresseResource"]


class RelBatimentGroupeAdresseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RelBatimentGroupeAdresseResourceWithRawResponse:
        return RelBatimentGroupeAdresseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RelBatimentGroupeAdresseResourceWithStreamingResponse:
        return RelBatimentGroupeAdresseResourceWithStreamingResponse(self)

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
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RelBatimentGroupeAdresseListResponse:
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
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/donnees/rel_batiment_groupe_adresse",
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
                    rel_batiment_groupe_adresse_list_params.RelBatimentGroupeAdresseListParams,
                ),
            ),
            cast_to=RelBatimentGroupeAdresseListResponse,
        )


class AsyncRelBatimentGroupeAdresseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRelBatimentGroupeAdresseResourceWithRawResponse:
        return AsyncRelBatimentGroupeAdresseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRelBatimentGroupeAdresseResourceWithStreamingResponse:
        return AsyncRelBatimentGroupeAdresseResourceWithStreamingResponse(self)

    async def list(
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
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RelBatimentGroupeAdresseListResponse:
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
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            "/donnees/rel_batiment_groupe_adresse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
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
                    rel_batiment_groupe_adresse_list_params.RelBatimentGroupeAdresseListParams,
                ),
            ),
            cast_to=RelBatimentGroupeAdresseListResponse,
        )


class RelBatimentGroupeAdresseResourceWithRawResponse:
    def __init__(self, rel_batiment_groupe_adresse: RelBatimentGroupeAdresseResource) -> None:
        self._rel_batiment_groupe_adresse = rel_batiment_groupe_adresse

        self.list = to_raw_response_wrapper(
            rel_batiment_groupe_adresse.list,
        )


class AsyncRelBatimentGroupeAdresseResourceWithRawResponse:
    def __init__(self, rel_batiment_groupe_adresse: AsyncRelBatimentGroupeAdresseResource) -> None:
        self._rel_batiment_groupe_adresse = rel_batiment_groupe_adresse

        self.list = async_to_raw_response_wrapper(
            rel_batiment_groupe_adresse.list,
        )


class RelBatimentGroupeAdresseResourceWithStreamingResponse:
    def __init__(self, rel_batiment_groupe_adresse: RelBatimentGroupeAdresseResource) -> None:
        self._rel_batiment_groupe_adresse = rel_batiment_groupe_adresse

        self.list = to_streamed_response_wrapper(
            rel_batiment_groupe_adresse.list,
        )


class AsyncRelBatimentGroupeAdresseResourceWithStreamingResponse:
    def __init__(self, rel_batiment_groupe_adresse: AsyncRelBatimentGroupeAdresseResource) -> None:
        self._rel_batiment_groupe_adresse = rel_batiment_groupe_adresse

        self.list = async_to_streamed_response_wrapper(
            rel_batiment_groupe_adresse.list,
        )
