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


class TestIris:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list(self, client: Bdnb, respx_mock: MockRouter) -> None:
        respx_mock.get("/tuiles/iris/14/8276/5702.pbf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        iris = client.tuiles.vectorielles.iris.list(
            y="5702",
            zoom="14",
            x="8276",
        )
        assert iris.is_closed
        assert iris.json() == {"foo": "bar"}
        assert cast(Any, iris.is_closed) is True
        assert isinstance(iris, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_list(self, client: Bdnb, respx_mock: MockRouter) -> None:
        respx_mock.get("/tuiles/iris/14/8276/5702.pbf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        iris = client.tuiles.vectorielles.iris.with_raw_response.list(
            y="5702",
            zoom="14",
            x="8276",
        )

        assert iris.is_closed is True
        assert iris.http_request.headers.get("X-Stainless-Lang") == "python"
        assert iris.json() == {"foo": "bar"}
        assert isinstance(iris, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_list(self, client: Bdnb, respx_mock: MockRouter) -> None:
        respx_mock.get("/tuiles/iris/14/8276/5702.pbf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.tuiles.vectorielles.iris.with_streaming_response.list(
            y="5702",
            zoom="14",
            x="8276",
        ) as iris:
            assert not iris.is_closed
            assert iris.http_request.headers.get("X-Stainless-Lang") == "python"

            assert iris.json() == {"foo": "bar"}
            assert cast(Any, iris.is_closed) is True
            assert isinstance(iris, StreamedBinaryAPIResponse)

        assert cast(Any, iris.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_list(self, client: Bdnb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zoom` but received ''"):
            client.tuiles.vectorielles.iris.with_raw_response.list(
                y="5702",
                zoom="",
                x="8276",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `x` but received ''"):
            client.tuiles.vectorielles.iris.with_raw_response.list(
                y="5702",
                zoom="14",
                x="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `y` but received ''"):
            client.tuiles.vectorielles.iris.with_raw_response.list(
                y="",
                zoom="14",
                x="8276",
            )


class TestAsyncIris:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list(self, async_client: AsyncBdnb, respx_mock: MockRouter) -> None:
        respx_mock.get("/tuiles/iris/14/8276/5702.pbf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        iris = await async_client.tuiles.vectorielles.iris.list(
            y="5702",
            zoom="14",
            x="8276",
        )
        assert iris.is_closed
        assert await iris.json() == {"foo": "bar"}
        assert cast(Any, iris.is_closed) is True
        assert isinstance(iris, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_list(self, async_client: AsyncBdnb, respx_mock: MockRouter) -> None:
        respx_mock.get("/tuiles/iris/14/8276/5702.pbf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        iris = await async_client.tuiles.vectorielles.iris.with_raw_response.list(
            y="5702",
            zoom="14",
            x="8276",
        )

        assert iris.is_closed is True
        assert iris.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await iris.json() == {"foo": "bar"}
        assert isinstance(iris, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_list(self, async_client: AsyncBdnb, respx_mock: MockRouter) -> None:
        respx_mock.get("/tuiles/iris/14/8276/5702.pbf").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.tuiles.vectorielles.iris.with_streaming_response.list(
            y="5702",
            zoom="14",
            x="8276",
        ) as iris:
            assert not iris.is_closed
            assert iris.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await iris.json() == {"foo": "bar"}
            assert cast(Any, iris.is_closed) is True
            assert isinstance(iris, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, iris.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_list(self, async_client: AsyncBdnb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zoom` but received ''"):
            await async_client.tuiles.vectorielles.iris.with_raw_response.list(
                y="5702",
                zoom="",
                x="8276",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `x` but received ''"):
            await async_client.tuiles.vectorielles.iris.with_raw_response.list(
                y="5702",
                zoom="14",
                x="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `y` but received ''"):
            await async_client.tuiles.vectorielles.iris.with_raw_response.list(
                y="",
                zoom="14",
                x="8276",
            )
