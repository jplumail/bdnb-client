# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_client import Bdnb, AsyncBdnb
from tests.utils import assert_matches_type
from bdnb_client.types import AutocompletionEntitesTexte
from bdnb_client.pagination import SyncDefault, AsyncDefault

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAutocompletion:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Bdnb) -> None:
        autocompletion = client.autocompletion.list()
        assert_matches_type(SyncDefault[AutocompletionEntitesTexte], autocompletion, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Bdnb) -> None:
        autocompletion = client.autocompletion.list(
            code="code",
            geom="geom",
            limit="limit",
            nom="nom",
            nom_unaccent="nom_unaccent",
            offset="offset",
            order="order",
            origine_code="origine_code",
            origine_nom="origine_nom",
            select="select",
            type_entite="type_entite",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(SyncDefault[AutocompletionEntitesTexte], autocompletion, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Bdnb) -> None:
        response = client.autocompletion.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocompletion = response.parse()
        assert_matches_type(SyncDefault[AutocompletionEntitesTexte], autocompletion, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Bdnb) -> None:
        with client.autocompletion.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocompletion = response.parse()
            assert_matches_type(SyncDefault[AutocompletionEntitesTexte], autocompletion, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAutocompletion:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnb) -> None:
        autocompletion = await async_client.autocompletion.list()
        assert_matches_type(AsyncDefault[AutocompletionEntitesTexte], autocompletion, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnb) -> None:
        autocompletion = await async_client.autocompletion.list(
            code="code",
            geom="geom",
            limit="limit",
            nom="nom",
            nom_unaccent="nom_unaccent",
            offset="offset",
            order="order",
            origine_code="origine_code",
            origine_nom="origine_nom",
            select="select",
            type_entite="type_entite",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(AsyncDefault[AutocompletionEntitesTexte], autocompletion, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnb) -> None:
        response = await async_client.autocompletion.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autocompletion = await response.parse()
        assert_matches_type(AsyncDefault[AutocompletionEntitesTexte], autocompletion, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnb) -> None:
        async with async_client.autocompletion.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autocompletion = await response.parse()
            assert_matches_type(AsyncDefault[AutocompletionEntitesTexte], autocompletion, path=["response"])

        assert cast(Any, response.is_closed) is True
