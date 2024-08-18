# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client.pagination import SyncDefault, AsyncDefault
from bdnb_client.types.donnees.referentiel_administratif import ReferentielAdministratifEpci

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEpci:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        epci = client.donnees.referentiel_administratif.epci.list()
        assert_matches_type(SyncDefault[ReferentielAdministratifEpci], epci, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        epci = client.donnees.referentiel_administratif.epci.list(
            code_epci_insee="code_epci_insee",
            geom_epci="geom_epci",
            libelle_epci="libelle_epci",
            limit="limit",
            nature_epci="nature_epci",
            offset="offset",
            order="order",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(SyncDefault[ReferentielAdministratifEpci], epci, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.donnees.referentiel_administratif.epci.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        epci = response.parse()
        assert_matches_type(SyncDefault[ReferentielAdministratifEpci], epci, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.donnees.referentiel_administratif.epci.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            epci = response.parse()
            assert_matches_type(SyncDefault[ReferentielAdministratifEpci], epci, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEpci:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        epci = await async_client.donnees.referentiel_administratif.epci.list()
        assert_matches_type(AsyncDefault[ReferentielAdministratifEpci], epci, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        epci = await async_client.donnees.referentiel_administratif.epci.list(
            code_epci_insee="code_epci_insee",
            geom_epci="geom_epci",
            libelle_epci="libelle_epci",
            limit="limit",
            nature_epci="nature_epci",
            offset="offset",
            order="order",
            select="select",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AsyncDefault[ReferentielAdministratifEpci], epci, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.donnees.referentiel_administratif.epci.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        epci = await response.parse()
        assert_matches_type(AsyncDefault[ReferentielAdministratifEpci], epci, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.donnees.referentiel_administratif.epci.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            epci = await response.parse()
            assert_matches_type(AsyncDefault[ReferentielAdministratifEpci], epci, path=["response"])

        assert cast(Any, response.is_closed) is True
