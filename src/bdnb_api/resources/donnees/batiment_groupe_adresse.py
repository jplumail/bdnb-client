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
from ...types.donnees import batiment_groupe_adresse_list_params
from ...types.donnees.batiment_groupe_adresse_list_response import BatimentGroupeAdresseListResponse

__all__ = ["BatimentGroupeAdresseResource", "AsyncBatimentGroupeAdresseResource"]


class BatimentGroupeAdresseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatimentGroupeAdresseResourceWithRawResponse:
        return BatimentGroupeAdresseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentGroupeAdresseResourceWithStreamingResponse:
        return BatimentGroupeAdresseResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        cle_interop_adr_principale_ban: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        fiabilite_cr_adr_niv_1: str | NotGiven = NOT_GIVEN,
        fiabilite_cr_adr_niv_2: str | NotGiven = NOT_GIVEN,
        libelle_adr_principale_ban: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_adresse_valid_ban: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
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
    ) -> BatimentGroupeAdresseListResponse:
        """
        Métriques du groupe de bâtiment par rapport à ses adresses postales

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          cle_interop_adr_principale_ban: Clé d'interopérabilité de l'adresse principale (issue de la BAN)

          code_departement_insee: Code département INSEE

          fiabilite_cr_adr_niv_1: Fiabilité des données croisées à l'adresse ('données croisées à l'adresse
              fiables', 'données croisées à l'adresse fiables à l'echelle de la parcelle
              unifiee', 'données croisées à l'adresse moyennement fiables', 'problème de
              géocodage')

          fiabilite_cr_adr_niv_2: Fiabilité détaillée des données croisées à l'adresse

          libelle_adr_principale_ban: Libellé complet de l'adresse principale (issue de la BAN)

          limit: Limiting and Pagination

          nb_adresse_valid_ban: Nombre d'adresses valides différentes provenant de la BAN qui desservent le
              groupe de bâtiment

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
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/donnees/batiment_groupe_adresse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "cle_interop_adr_principale_ban": cle_interop_adr_principale_ban,
                        "code_departement_insee": code_departement_insee,
                        "fiabilite_cr_adr_niv_1": fiabilite_cr_adr_niv_1,
                        "fiabilite_cr_adr_niv_2": fiabilite_cr_adr_niv_2,
                        "libelle_adr_principale_ban": libelle_adr_principale_ban,
                        "limit": limit,
                        "nb_adresse_valid_ban": nb_adresse_valid_ban,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    batiment_groupe_adresse_list_params.BatimentGroupeAdresseListParams,
                ),
            ),
            cast_to=BatimentGroupeAdresseListResponse,
        )


class AsyncBatimentGroupeAdresseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatimentGroupeAdresseResourceWithRawResponse:
        return AsyncBatimentGroupeAdresseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentGroupeAdresseResourceWithStreamingResponse:
        return AsyncBatimentGroupeAdresseResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        cle_interop_adr_principale_ban: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        fiabilite_cr_adr_niv_1: str | NotGiven = NOT_GIVEN,
        fiabilite_cr_adr_niv_2: str | NotGiven = NOT_GIVEN,
        libelle_adr_principale_ban: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_adresse_valid_ban: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
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
    ) -> BatimentGroupeAdresseListResponse:
        """
        Métriques du groupe de bâtiment par rapport à ses adresses postales

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          cle_interop_adr_principale_ban: Clé d'interopérabilité de l'adresse principale (issue de la BAN)

          code_departement_insee: Code département INSEE

          fiabilite_cr_adr_niv_1: Fiabilité des données croisées à l'adresse ('données croisées à l'adresse
              fiables', 'données croisées à l'adresse fiables à l'echelle de la parcelle
              unifiee', 'données croisées à l'adresse moyennement fiables', 'problème de
              géocodage')

          fiabilite_cr_adr_niv_2: Fiabilité détaillée des données croisées à l'adresse

          libelle_adr_principale_ban: Libellé complet de l'adresse principale (issue de la BAN)

          limit: Limiting and Pagination

          nb_adresse_valid_ban: Nombre d'adresses valides différentes provenant de la BAN qui desservent le
              groupe de bâtiment

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
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            "/donnees/batiment_groupe_adresse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "cle_interop_adr_principale_ban": cle_interop_adr_principale_ban,
                        "code_departement_insee": code_departement_insee,
                        "fiabilite_cr_adr_niv_1": fiabilite_cr_adr_niv_1,
                        "fiabilite_cr_adr_niv_2": fiabilite_cr_adr_niv_2,
                        "libelle_adr_principale_ban": libelle_adr_principale_ban,
                        "limit": limit,
                        "nb_adresse_valid_ban": nb_adresse_valid_ban,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    batiment_groupe_adresse_list_params.BatimentGroupeAdresseListParams,
                ),
            ),
            cast_to=BatimentGroupeAdresseListResponse,
        )


class BatimentGroupeAdresseResourceWithRawResponse:
    def __init__(self, batiment_groupe_adresse: BatimentGroupeAdresseResource) -> None:
        self._batiment_groupe_adresse = batiment_groupe_adresse

        self.list = to_raw_response_wrapper(
            batiment_groupe_adresse.list,
        )


class AsyncBatimentGroupeAdresseResourceWithRawResponse:
    def __init__(self, batiment_groupe_adresse: AsyncBatimentGroupeAdresseResource) -> None:
        self._batiment_groupe_adresse = batiment_groupe_adresse

        self.list = async_to_raw_response_wrapper(
            batiment_groupe_adresse.list,
        )


class BatimentGroupeAdresseResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_adresse: BatimentGroupeAdresseResource) -> None:
        self._batiment_groupe_adresse = batiment_groupe_adresse

        self.list = to_streamed_response_wrapper(
            batiment_groupe_adresse.list,
        )


class AsyncBatimentGroupeAdresseResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_adresse: AsyncBatimentGroupeAdresseResource) -> None:
        self._batiment_groupe_adresse = batiment_groupe_adresse

        self.list = async_to_streamed_response_wrapper(
            batiment_groupe_adresse.list,
        )