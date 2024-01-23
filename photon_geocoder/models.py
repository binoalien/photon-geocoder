"""
Path: photon_geocoder/models.py
"""
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    countrycode: str
    type: str
    postcode: str | None = None
    city: str | None = None
    county: str | None = None
    district: str | None = None
    housenumber: str | None = None
    state: str | None = None

    @property
    def normalized(self) -> str:
        parts = [f"{self.postcode}" if self.postcode else "",
                 f"{self.city}" if self.city else "",
                 f"{self.street}",
                 f"{self.housenumber}" if self.housenumber else ""]
        return " ".join(part for part in parts if part)

    def __str__(self) -> str:
        parts = [f"{self.postcode}" if self.postcode else "",
                 f"{self.city}" if self.city else "",
                 f"({self.district})" if self.district else "",
                 f"| {self.street}",
                 f"{self.housenumber}" if self.housenumber else "",
                 f"| {self.state}" if self.state else "",
                 f"({self.county})" if self.county else "",
                 f"| {self.countrycode.upper()}" if self.countrycode else "",
                 f"({self.type})"]
        return " ".join(part for part in parts if part)

    def __repr__(self) -> str:
        return str(self)

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Address):
            raise TypeError(f"Cannot compare Address with {type(other)}")
        return str(self) == str(other)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Address):
            raise TypeError(f"Cannot compare Address with {type(other)}")
        return str(self) < str(other)


class Geometry(BaseModel):
    coordinates: tuple[float, float]


class Properties(BaseModel):
    osm_type: str
    osm_id: int
    country: str
    countrycode: str
    type: str
    city: str | None = None
    postcode: str | None = None
    extent: list[float] | None = None
    osm_key: str | None = None
    district: str | None = None
    osm_value: str | None = None
    housenumber: str | None = None
    street: str | None = None
    name: str | None = None
    locality: str | None = None
    county: str | None = None
    state: str | None = None

    @property
    def address(self) -> Address:
        return Address(
            type=self.type,
            street=self.street or self.name,
            countrycode=self.countrycode,
            postcode=self.postcode,
            city=self.city,
            county=self.county,
            district=self.district,
            housenumber=self.housenumber,
            state=self.state
        )


class Feature(BaseModel):
    geometry: Geometry
    properties: Properties


class FeatureCollection(BaseModel):
    features: list[Feature]
