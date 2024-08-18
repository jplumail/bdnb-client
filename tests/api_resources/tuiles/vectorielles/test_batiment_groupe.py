# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from bdnb_client import Bdnb, AsyncBdnb
from bdnb_client._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatimentGroupe:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list(self, client: Bdnb, respx_mock: MockRouter) -> None:
        respx_mock.get("/tuiles/batiment_groupe/14/8276/5702.pbf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        batiment_groupe = client.tuiles.vectorielles.batiment_groupe.list(
            y="5702",
            zoom="14",
            x="8276",
        )
        assert batiment_groupe.is_closed
        assert batiment_groupe.json() == {"foo": "bar"}
        assert cast(Any, batiment_groupe.is_closed) is True
        assert isinstance(batiment_groupe, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_list(self, client: Bdnb, respx_mock: MockRouter) -> None:
        respx_mock.get("/tuiles/batiment_groupe/14/8276/5702.pbf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        batiment_groupe = client.tuiles.vectorielles.batiment_groupe.with_raw_response.list(
            y="5702",
            zoom="14",
            x="8276",
        )

        assert batiment_groupe.is_closed is True
        assert batiment_groupe.http_request.headers.get("X-Stainless-Lang") == "python"
        assert batiment_groupe.json() == {"foo": "bar"}
        assert isinstance(batiment_groupe, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_list(self, client: Bdnb, respx_mock: MockRouter) -> None:
        respx_mock.get("/tuiles/batiment_groupe/14/8276/5702.pbf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.tuiles.vectorielles.batiment_groupe.with_streaming_response.list(
            y="5702",
            zoom="14",
            x="8276",
        ) as batiment_groupe:
            assert not batiment_groupe.is_closed
            assert batiment_groupe.http_request.headers.get("X-Stainless-Lang") == "python"

            assert batiment_groupe.json() == {"foo": "bar"}
            assert cast(Any, batiment_groupe.is_closed) is True
            assert isinstance(batiment_groupe, StreamedBinaryAPIResponse)

        assert cast(Any, batiment_groupe.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_list(self, client: Bdnb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zoom` but received ''"):
            client.tuiles.vectorielles.batiment_groupe.with_raw_response.list(
                y="5702",
                zoom="",
                x="8276",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `x` but received ''"):
            client.tuiles.vectorielles.batiment_groupe.with_raw_response.list(
                y="5702",
                zoom="14",
                x="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `y` but received ''"):
            client.tuiles.vectorielles.batiment_groupe.with_raw_response.list(
                y="",
                zoom="14",
                x="8276",
            )


class TestAsyncBatimentGroupe:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list(self, async_client: AsyncBdnb, respx_mock: MockRouter) -> None:
        respx_mock.get("/tuiles/batiment_groupe/14/8276/5702.pbf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        batiment_groupe = await async_client.tuiles.vectorielles.batiment_groupe.list(
            y="5702",
            zoom="14",
            x="8276",
        )
        assert batiment_groupe.is_closed
        assert await batiment_groupe.json() == {"foo": "bar"}
        assert cast(Any, batiment_groupe.is_closed) is True
        assert isinstance(batiment_groupe, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_list(self, async_client: AsyncBdnb, respx_mock: MockRouter) -> None:
        respx_mock.get("/tuiles/batiment_groupe/14/8276/5702.pbf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        batiment_groupe = await async_client.tuiles.vectorielles.batiment_groupe.with_raw_response.list(
            y="5702",
            zoom="14",
            x="8276",
        )

        assert batiment_groupe.is_closed is True
        assert batiment_groupe.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await batiment_groupe.json() == {"foo": "bar"}
        assert isinstance(batiment_groupe, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_list(self, async_client: AsyncBdnb, respx_mock: MockRouter) -> None:
        respx_mock.get("/tuiles/batiment_groupe/14/8276/5702.pbf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.tuiles.vectorielles.batiment_groupe.with_streaming_response.list(
            y="5702",
            zoom="14",
            x="8276",
        ) as batiment_groupe:
            assert not batiment_groupe.is_closed
            assert batiment_groupe.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await batiment_groupe.json() == {"foo": "bar"}
            assert cast(Any, batiment_groupe.is_closed) is True
            assert isinstance(batiment_groupe, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, batiment_groupe.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_list(self, async_client: AsyncBdnb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zoom` but received ''"):
            await async_client.tuiles.vectorielles.batiment_groupe.with_raw_response.list(
                y="5702",
                zoom="",
                x="8276",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `x` but received ''"):
            await async_client.tuiles.vectorielles.batiment_groupe.with_raw_response.list(
                y="5702",
                zoom="14",
                x="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `y` but received ''"):
            await async_client.tuiles.vectorielles.batiment_groupe.with_raw_response.list(
                y="",
                zoom="14",
                x="8276",
            )
