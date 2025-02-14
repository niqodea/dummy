from __future__ import annotations

from collections.abc import Callable

import requests


class Client:
    def __init__(
        self,
        base_url: str,
        url_getter: Callable[[str], dict],
    ) -> None:
        self._base_url = base_url
        self._url_getter = url_getter

    def get_data(self, path: str) -> dict:
        url = f"{self._base_url}/{path}"
        data = self._url_getter(url)
        return data

    @staticmethod
    def create() -> Client:
        return Client(
            base_url="https://httpbin.org",
            url_getter=lambda url: requests.get(url).json(),
        )
