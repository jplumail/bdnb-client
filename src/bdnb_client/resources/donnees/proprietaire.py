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
from ...types.donnees import proprietaire_list_params
from ...types.donnees.proprietaire import Proprietaire

__all__ = ["ProprietaireResource", "AsyncProprietaireResource"]


class ProprietaireResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProprietaireResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return ProprietaireResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProprietaireResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return ProprietaireResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        code_postal: str | NotGiven = NOT_GIVEN,
        dans_majic_pm: str | NotGiven = NOT_GIVEN,
        denomination: str | NotGiven = NOT_GIVEN,
        forme_juridique: str | NotGiven = NOT_GIVEN,
        libelle_commune: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_locaux_open: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        personne_id: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        siren: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDefault[Proprietaire]:
        """
        Données des propriétaires de bâtiment (principalement issues des Fichiers
        Fonciers) (la version open filtre sur la colonne `dans_majic_pm`)

        Args:
          code_departement_insee: Code département INSEE

          code_postal: Code postal

          dans_majic_pm: (majic_pm) Ce propriétaire possède des bâtiments déclarés dans majic_pm

          denomination: Dénomination du propriétaire (FF)

          forme_juridique: Forme juridique du propriétaire (FF)

          libelle_commune: Libellé de la commune

          limit: Limiting and Pagination

          nb_locaux_open: (majic_pm) nombre de locaux déclarés dans majic_pm

          offset: Limiting and Pagination

          order: Ordering

          personne_id: Concaténation de code département et du numéro de personne Majic3 (FF) (appelé
              aussi NUMà‰RO PERSONNE PRESENT DANS Lâ€™APPLICATION MAJIC dans les fichiers des
              locaux des personnes morales)

          select: Filtering Columns

          siren: Numéro de SIREN de la personne morale (FF)

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
            "/donnees/proprietaire",
            page=SyncDefault[Proprietaire],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "code_departement_insee": code_departement_insee,
                        "code_postal": code_postal,
                        "dans_majic_pm": dans_majic_pm,
                        "denomination": denomination,
                        "forme_juridique": forme_juridique,
                        "libelle_commune": libelle_commune,
                        "limit": limit,
                        "nb_locaux_open": nb_locaux_open,
                        "offset": offset,
                        "order": order,
                        "personne_id": personne_id,
                        "select": select,
                        "siren": siren,
                    },
                    proprietaire_list_params.ProprietaireListParams,
                ),
            ),
            model=Proprietaire,
        )


class AsyncProprietaireResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProprietaireResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncProprietaireResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProprietaireResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncProprietaireResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        code_postal: str | NotGiven = NOT_GIVEN,
        dans_majic_pm: str | NotGiven = NOT_GIVEN,
        denomination: str | NotGiven = NOT_GIVEN,
        forme_juridique: str | NotGiven = NOT_GIVEN,
        libelle_commune: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_locaux_open: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        personne_id: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        siren: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Proprietaire, AsyncDefault[Proprietaire]]:
        """
        Données des propriétaires de bâtiment (principalement issues des Fichiers
        Fonciers) (la version open filtre sur la colonne `dans_majic_pm`)

        Args:
          code_departement_insee: Code département INSEE

          code_postal: Code postal

          dans_majic_pm: (majic_pm) Ce propriétaire possède des bâtiments déclarés dans majic_pm

          denomination: Dénomination du propriétaire (FF)

          forme_juridique: Forme juridique du propriétaire (FF)

          libelle_commune: Libellé de la commune

          limit: Limiting and Pagination

          nb_locaux_open: (majic_pm) nombre de locaux déclarés dans majic_pm

          offset: Limiting and Pagination

          order: Ordering

          personne_id: Concaténation de code département et du numéro de personne Majic3 (FF) (appelé
              aussi NUMà‰RO PERSONNE PRESENT DANS Lâ€™APPLICATION MAJIC dans les fichiers des
              locaux des personnes morales)

          select: Filtering Columns

          siren: Numéro de SIREN de la personne morale (FF)

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
            "/donnees/proprietaire",
            page=AsyncDefault[Proprietaire],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "code_departement_insee": code_departement_insee,
                        "code_postal": code_postal,
                        "dans_majic_pm": dans_majic_pm,
                        "denomination": denomination,
                        "forme_juridique": forme_juridique,
                        "libelle_commune": libelle_commune,
                        "limit": limit,
                        "nb_locaux_open": nb_locaux_open,
                        "offset": offset,
                        "order": order,
                        "personne_id": personne_id,
                        "select": select,
                        "siren": siren,
                    },
                    proprietaire_list_params.ProprietaireListParams,
                ),
            ),
            model=Proprietaire,
        )


class ProprietaireResourceWithRawResponse:
    def __init__(self, proprietaire: ProprietaireResource) -> None:
        self._proprietaire = proprietaire

        self.list = to_raw_response_wrapper(
            proprietaire.list,
        )


class AsyncProprietaireResourceWithRawResponse:
    def __init__(self, proprietaire: AsyncProprietaireResource) -> None:
        self._proprietaire = proprietaire

        self.list = async_to_raw_response_wrapper(
            proprietaire.list,
        )


class ProprietaireResourceWithStreamingResponse:
    def __init__(self, proprietaire: ProprietaireResource) -> None:
        self._proprietaire = proprietaire

        self.list = to_streamed_response_wrapper(
            proprietaire.list,
        )


class AsyncProprietaireResourceWithStreamingResponse:
    def __init__(self, proprietaire: AsyncProprietaireResource) -> None:
        self._proprietaire = proprietaire

        self.list = async_to_streamed_response_wrapper(
            proprietaire.list,
        )
