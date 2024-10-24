# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, strip_not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncDefault, AsyncDefault
from ...._base_client import AsyncPaginator, make_request_options
from ....types.donnees.batiment_groupe import adresse_list_params
from ....types.donnees.batiment_groupe.batiment_groupe_adresse import BatimentGroupeAdresse

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
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[BatimentGroupeAdresse]:
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
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get_api_list(
            "/donnees/batiment_groupe_adresse",
            page=SyncDefault[BatimentGroupeAdresse],
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
                    adresse_list_params.AdresseListParams,
                ),
            ),
            model=BatimentGroupeAdresse,
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
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BatimentGroupeAdresse, AsyncDefault[BatimentGroupeAdresse]]:
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
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get_api_list(
            "/donnees/batiment_groupe_adresse",
            page=AsyncDefault[BatimentGroupeAdresse],
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
                    adresse_list_params.AdresseListParams,
                ),
            ),
            model=BatimentGroupeAdresse,
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
