"""
Path: tests/test_api.py
"""
import timeit
import asyncio
import unittest
from photon_geocoder import PhotonGeocoder, Layer
from tests.config import DATAS


class TestPhotonGeocoder(unittest.TestCase):

    def setUp(self):
        self.api = PhotonGeocoder()
        self.layers = [Layer.STREET, Layer.HOUSE]

    def test_query(self):
        print(f"Testing {len(DATAS)} addresses")
        asyncio.run(self.async_test_query())

    async def async_test_query(self):
        start_time = timeit.default_timer()
        tasks = [self.api.query(
            data["input"], layers=self.layers, limit=10) for data in DATAS]
        results = await asyncio.gather(*tasks)
        end_time = timeit.default_timer()
        print(f"Time: {end_time - start_time}")

        for data, addresses in zip(DATAS, results):
            assert len(addresses) > 0
            for address in addresses[:1]:
                self.assertTrue(address.postcode == data["output"]["postcode"])
                self.assertTrue(address.street == data["output"]["street"])
                self.assertTrue(address.city == data["output"]["city"])

                if address.housenumber:
                    address.housenumber = address.housenumber.replace(
                        "a", "").replace("b", "").replace("c", "").replace("d", "")
                    self.assertTrue(int(address.housenumber) <= 50)
                    self.assertTrue(int(address.housenumber) >= 1)
