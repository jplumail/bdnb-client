# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .info import (
    InfoResource,
    AsyncInfoResource,
    InfoResourceWithRawResponse,
    AsyncInfoResourceWithRawResponse,
    InfoResourceWithStreamingResponse,
    AsyncInfoResourceWithStreamingResponse,
)
from .table import (
    TableResource,
    AsyncTableResource,
    TableResourceWithRawResponse,
    AsyncTableResourceWithRawResponse,
    TableResourceWithStreamingResponse,
    AsyncTableResourceWithStreamingResponse,
)
from .colonnes import (
    ColonnesResource,
    AsyncColonnesResource,
    ColonnesResourceWithRawResponse,
    AsyncColonnesResourceWithRawResponse,
    ColonnesResourceWithStreamingResponse,
    AsyncColonnesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .colonnes_souscription import (
    ColonnesSouscriptionResource,
    AsyncColonnesSouscriptionResource,
    ColonnesSouscriptionResourceWithRawResponse,
    AsyncColonnesSouscriptionResourceWithRawResponse,
    ColonnesSouscriptionResourceWithStreamingResponse,
    AsyncColonnesSouscriptionResourceWithStreamingResponse,
)

__all__ = ["MetadonneesResource", "AsyncMetadonneesResource"]


class MetadonneesResource(SyncAPIResource):
    @cached_property
    def colonnes_souscription(self) -> ColonnesSouscriptionResource:
        return ColonnesSouscriptionResource(self._client)

    @cached_property
    def colonnes(self) -> ColonnesResource:
        return ColonnesResource(self._client)

    @cached_property
    def info(self) -> InfoResource:
        return InfoResource(self._client)

    @cached_property
    def table(self) -> TableResource:
        return TableResource(self._client)

    @cached_property
    def with_raw_response(self) -> MetadonneesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return MetadonneesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetadonneesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return MetadonneesResourceWithStreamingResponse(self)


class AsyncMetadonneesResource(AsyncAPIResource):
    @cached_property
    def colonnes_souscription(self) -> AsyncColonnesSouscriptionResource:
        return AsyncColonnesSouscriptionResource(self._client)

    @cached_property
    def colonnes(self) -> AsyncColonnesResource:
        return AsyncColonnesResource(self._client)

    @cached_property
    def info(self) -> AsyncInfoResource:
        return AsyncInfoResource(self._client)

    @cached_property
    def table(self) -> AsyncTableResource:
        return AsyncTableResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMetadonneesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jplumail/bdnb-client#accessing-raw-response-data-eg-headers
        """
        return AsyncMetadonneesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetadonneesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jplumail/bdnb-client#with_streaming_response
        """
        return AsyncMetadonneesResourceWithStreamingResponse(self)


class MetadonneesResourceWithRawResponse:
    def __init__(self, metadonnees: MetadonneesResource) -> None:
        self._metadonnees = metadonnees

    @cached_property
    def colonnes_souscription(self) -> ColonnesSouscriptionResourceWithRawResponse:
        return ColonnesSouscriptionResourceWithRawResponse(self._metadonnees.colonnes_souscription)

    @cached_property
    def colonnes(self) -> ColonnesResourceWithRawResponse:
        return ColonnesResourceWithRawResponse(self._metadonnees.colonnes)

    @cached_property
    def info(self) -> InfoResourceWithRawResponse:
        return InfoResourceWithRawResponse(self._metadonnees.info)

    @cached_property
    def table(self) -> TableResourceWithRawResponse:
        return TableResourceWithRawResponse(self._metadonnees.table)


class AsyncMetadonneesResourceWithRawResponse:
    def __init__(self, metadonnees: AsyncMetadonneesResource) -> None:
        self._metadonnees = metadonnees

    @cached_property
    def colonnes_souscription(self) -> AsyncColonnesSouscriptionResourceWithRawResponse:
        return AsyncColonnesSouscriptionResourceWithRawResponse(self._metadonnees.colonnes_souscription)

    @cached_property
    def colonnes(self) -> AsyncColonnesResourceWithRawResponse:
        return AsyncColonnesResourceWithRawResponse(self._metadonnees.colonnes)

    @cached_property
    def info(self) -> AsyncInfoResourceWithRawResponse:
        return AsyncInfoResourceWithRawResponse(self._metadonnees.info)

    @cached_property
    def table(self) -> AsyncTableResourceWithRawResponse:
        return AsyncTableResourceWithRawResponse(self._metadonnees.table)


class MetadonneesResourceWithStreamingResponse:
    def __init__(self, metadonnees: MetadonneesResource) -> None:
        self._metadonnees = metadonnees

    @cached_property
    def colonnes_souscription(self) -> ColonnesSouscriptionResourceWithStreamingResponse:
        return ColonnesSouscriptionResourceWithStreamingResponse(self._metadonnees.colonnes_souscription)

    @cached_property
    def colonnes(self) -> ColonnesResourceWithStreamingResponse:
        return ColonnesResourceWithStreamingResponse(self._metadonnees.colonnes)

    @cached_property
    def info(self) -> InfoResourceWithStreamingResponse:
        return InfoResourceWithStreamingResponse(self._metadonnees.info)

    @cached_property
    def table(self) -> TableResourceWithStreamingResponse:
        return TableResourceWithStreamingResponse(self._metadonnees.table)


class AsyncMetadonneesResourceWithStreamingResponse:
    def __init__(self, metadonnees: AsyncMetadonneesResource) -> None:
        self._metadonnees = metadonnees

    @cached_property
    def colonnes_souscription(self) -> AsyncColonnesSouscriptionResourceWithStreamingResponse:
        return AsyncColonnesSouscriptionResourceWithStreamingResponse(self._metadonnees.colonnes_souscription)

    @cached_property
    def colonnes(self) -> AsyncColonnesResourceWithStreamingResponse:
        return AsyncColonnesResourceWithStreamingResponse(self._metadonnees.colonnes)

    @cached_property
    def info(self) -> AsyncInfoResourceWithStreamingResponse:
        return AsyncInfoResourceWithStreamingResponse(self._metadonnees.info)

    @cached_property
    def table(self) -> AsyncTableResourceWithStreamingResponse:
        return AsyncTableResourceWithStreamingResponse(self._metadonnees.table)
