# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import BdnbAPI, AsyncBdnbAPI
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGeocodage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: BdnbAPI) -> None:
        geocodage = client.geocodage.list(
            q="27 rue charles dullin",
        )
        assert_matches_type(object, geocodage, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: BdnbAPI) -> None:
        geocodage = client.geocodage.list(
            q="27 rue charles dullin",
            autocomplete=0,
            citycode="citycode",
            lat="lat",
            limit=0,
            lon="lon",
            postcode="postcode",
            type="street",
        )
        assert_matches_type(object, geocodage, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BdnbAPI) -> None:
        response = client.geocodage.with_raw_response.list(
            q="27 rue charles dullin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geocodage = response.parse()
        assert_matches_type(object, geocodage, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BdnbAPI) -> None:
        with client.geocodage.with_streaming_response.list(
            q="27 rue charles dullin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geocodage = response.parse()
            assert_matches_type(object, geocodage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGeocodage:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnbAPI) -> None:
        geocodage = await async_client.geocodage.list(
            q="27 rue charles dullin",
        )
        assert_matches_type(object, geocodage, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        geocodage = await async_client.geocodage.list(
            q="27 rue charles dullin",
            autocomplete=0,
            citycode="citycode",
            lat="lat",
            limit=0,
            lon="lon",
            postcode="postcode",
            type="street",
        )
        assert_matches_type(object, geocodage, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.geocodage.with_raw_response.list(
            q="27 rue charles dullin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        geocodage = await response.parse()
        assert_matches_type(object, geocodage, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.geocodage.with_streaming_response.list(
            q="27 rue charles dullin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            geocodage = await response.parse()
            assert_matches_type(object, geocodage, path=["response"])

        assert cast(Any, response.is_closed) is True
