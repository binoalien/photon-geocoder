"""
Path: photon_geocoder/api.py
"""
from urllib.parse import urlencode
import aiohttp
import Levenshtein

from .enums import Layer
from .models import FeatureCollection, Address
from .osm_tag import OSMTag


class PhotonGeocoder:
    base_url: str = "http://localhost:2322/api"

    def __init__(self, base_url: str = None, port: int = None) -> None:
        if base_url and port:
            self.base_url = f"{base_url}:{port}/api"
        elif base_url:
            self.base_url = f"{base_url}/api"
        elif port:
            self.base_url = f"http://localhost:{port}/api"

    async def query(self, address: str, layers: list[Layer] | None = None, osm_tags: list[OSMTag] | None = None, limit: int = 10) -> list[Address]:
        params = {'q': address, 'limit': limit}
        url = self.base_url + "?" + urlencode(params, doseq=True)

        if osm_tags:
            for osm_tag in osm_tags:
                url += f"&osm_tag={osm_tag}"
        if layers:
            for layer in layers:
                url += f"&layer={layer.value}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                data = await response.json()
                addresses: list[Address] = []
                for feature in FeatureCollection(**data).features:
                    if feature.properties.street or feature.properties.name:
                        addresses.append(feature.properties.address)

                addresses.sort(
                    key=lambda a: Levenshtein.distance(a.normalized, address))

                return addresses
