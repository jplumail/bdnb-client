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
from ....types.donnees.batiment_groupe import ffo_bat_list_params
from ....types.donnees.batiment_groupe.batiment_groupe_ffo_bat import BatimentGroupeFfoBat

__all__ = ["FfoBatResource", "AsyncFfoBatResource"]


class FfoBatResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FfoBatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return FfoBatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FfoBatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return FfoBatResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        annee_construction: str | NotGiven = NOT_GIVEN,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        mat_mur_txt: str | NotGiven = NOT_GIVEN,
        mat_toit_txt: str | NotGiven = NOT_GIVEN,
        nb_log: str | NotGiven = NOT_GIVEN,
        nb_niveau: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        usage_niveau_1_txt: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[BatimentGroupeFfoBat]:
        """
        Données issues des Fichiers Fonciers agrégées à l'échelle du bâtiment

        Args:
          annee_construction: Année de construction du bâtiment

          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          limit: Limiting and Pagination

          mat_mur_txt: (ffo) Matériaux principal des murs extérieurs

          mat_toit_txt: (ffo) Matériau principal des toitures

          nb_log: (rnc) Nombre de logements

          nb_niveau: (ffo) Nombre de niveau du bâtiment (ex: RDC = 1, R+1 = 2, etc..)

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          usage_niveau_1_txt: indicateurs d'usage simplifié du bâtiment (verbose)

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
            "/donnees/batiment_groupe_ffo_bat",
            page=SyncDefault[BatimentGroupeFfoBat],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "annee_construction": annee_construction,
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "limit": limit,
                        "mat_mur_txt": mat_mur_txt,
                        "mat_toit_txt": mat_toit_txt,
                        "nb_log": nb_log,
                        "nb_niveau": nb_niveau,
                        "offset": offset,
                        "order": order,
                        "select": select,
                        "usage_niveau_1_txt": usage_niveau_1_txt,
                    },
                    ffo_bat_list_params.FfoBatListParams,
                ),
            ),
            model=BatimentGroupeFfoBat,
        )


class AsyncFfoBatResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFfoBatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncFfoBatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFfoBatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncFfoBatResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        annee_construction: str | NotGiven = NOT_GIVEN,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        mat_mur_txt: str | NotGiven = NOT_GIVEN,
        mat_toit_txt: str | NotGiven = NOT_GIVEN,
        nb_log: str | NotGiven = NOT_GIVEN,
        nb_niveau: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        usage_niveau_1_txt: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BatimentGroupeFfoBat, AsyncDefault[BatimentGroupeFfoBat]]:
        """
        Données issues des Fichiers Fonciers agrégées à l'échelle du bâtiment

        Args:
          annee_construction: Année de construction du bâtiment

          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          limit: Limiting and Pagination

          mat_mur_txt: (ffo) Matériaux principal des murs extérieurs

          mat_toit_txt: (ffo) Matériau principal des toitures

          nb_log: (rnc) Nombre de logements

          nb_niveau: (ffo) Nombre de niveau du bâtiment (ex: RDC = 1, R+1 = 2, etc..)

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          usage_niveau_1_txt: indicateurs d'usage simplifié du bâtiment (verbose)

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
            "/donnees/batiment_groupe_ffo_bat",
            page=AsyncDefault[BatimentGroupeFfoBat],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "annee_construction": annee_construction,
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "limit": limit,
                        "mat_mur_txt": mat_mur_txt,
                        "mat_toit_txt": mat_toit_txt,
                        "nb_log": nb_log,
                        "nb_niveau": nb_niveau,
                        "offset": offset,
                        "order": order,
                        "select": select,
                        "usage_niveau_1_txt": usage_niveau_1_txt,
                    },
                    ffo_bat_list_params.FfoBatListParams,
                ),
            ),
            model=BatimentGroupeFfoBat,
        )


class FfoBatResourceWithRawResponse:
    def __init__(self, ffo_bat: FfoBatResource) -> None:
        self._ffo_bat = ffo_bat

        self.list = to_raw_response_wrapper(
            ffo_bat.list,
        )


class AsyncFfoBatResourceWithRawResponse:
    def __init__(self, ffo_bat: AsyncFfoBatResource) -> None:
        self._ffo_bat = ffo_bat

        self.list = async_to_raw_response_wrapper(
            ffo_bat.list,
        )


class FfoBatResourceWithStreamingResponse:
    def __init__(self, ffo_bat: FfoBatResource) -> None:
        self._ffo_bat = ffo_bat

        self.list = to_streamed_response_wrapper(
            ffo_bat.list,
        )


class AsyncFfoBatResourceWithStreamingResponse:
    def __init__(self, ffo_bat: AsyncFfoBatResource) -> None:
        self._ffo_bat = ffo_bat

        self.list = async_to_streamed_response_wrapper(
            ffo_bat.list,
        )
