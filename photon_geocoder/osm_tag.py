"""
Path: photon_geocoder/osm_tag.py

This module defines the OSMTag class for representing and validating OpenStreetMap (OSM) tags.

The OSMTag class allows users to create and validate OSM tags with optional keys, values, and a negation capability.
It leverages Pydantic for robust data validation and includes caching for enhanced performance in repeated validation operations.

Each instance of the OSMTag class can validate keys and values to ensure they conform to defined requirements and patterns.
Furthermore, the class allows for the validation of key-value combinations against a list of permitted OSM tags.

Main Features:
- Validate keys and values according to predefined patterns and minimum lengths.
- Check the combination of key and value against a list of allowed OSM tags.
- Represent the OSMTag instance in a string format for clear and readable output.
"""
from typing import Optional
from functools import lru_cache
from pydantic import BaseModel, Field, field_validator, model_validator
from photon_geocoder.config import OSM_TAGS

PATTERN = r"^[a-z0-9_:]+$"


class OSMTag(BaseModel):
    """
    Represents an OpenStreetMap (OSM) tag with optional key, value, and negation attributes.

    Attributes:
        key (Optional[str]): The key of the OSM tag. Must follow a defined pattern and have a minimum length.
        value (Optional[str]): The value of the OSM tag. Must follow a defined pattern and have a minimum length.
        negate (bool): Indicates whether the tag is negated.

    Raises:
        ValueError: If the key or value is not valid.
        ValueError: If the value is not valid for the given key.

    Examples:
        >>> tag = OSMTag(key="highway", value="residential", negate=True)
        >>> print(tag)
        !highway:residential

        >>> tag = OSMTag(key="building", value="yes")
        >>> print(tag)
        building:yes
    """

    key: Optional[str] = Field(
        None,
        min_length=3,
        description="The key of the OSM tag",
        title="Key",
        examples=["highway", "building"],
        pattern=PATTERN)
    value: Optional[str] = Field(
        None,
        min_length=3,
        description="The value of the OSM tag",
        title="Value",
        examples=["residential", "yes"],
        pattern=PATTERN)
    negate: bool = Field(
        False,
        title="Negate",
        description="Negation of the tag")

    @field_validator('key')
    @classmethod
    def validate_key(cls, v: Optional[str]) -> Optional[str]:
        """
        Validates that the key is in the list of allowed OSM tags.

        Args:
            v (Optional[str]): The key to validate.

        Returns:
            Optional[str]: The validated key.

        Raises:
            ValueError: If the key is not valid.
        """
        if v is not None and not cls._is_valid_key(v):
            raise ValueError(f"Key '{v}' is not valid.")
        return v

    @model_validator(mode='after')
    def validate_value_in_key(self) -> 'OSMTag':
        """
        Validates that the value is allowed for the specified key.

        Returns:
            OSMTag: The instance itself if validation is successful.

        Raises:
            ValueError: If the value is not valid for the given key.
        """
        if self.key and self.value and not self._is_valid_value_for_key(self.value, self.key):
            raise ValueError(
                f"Value '{self.value}' is not valid for the key '{self.key}'.")
        return self

    @model_validator(mode='after')
    def ensure_key_or_value(self) -> 'OSMTag':
        """
        Ensures that at least one of the key or value is provided.

        Returns:
            OSMTag: The instance itself if validation is successful.

        Raises:
            ValueError: If neither key nor value is provided.
        """
        if not self.key and not self.value:
            raise ValueError("At least one of key or value must be provided.")
        return self

    @staticmethod
    @lru_cache(maxsize=128)
    def _is_valid_key(key: str) -> bool:
        return key in OSM_TAGS

    @staticmethod
    @lru_cache(maxsize=128)
    def _is_valid_value_for_key(value: str, key: str) -> bool:
        return value in OSM_TAGS.get(key, [])

    @staticmethod
    @lru_cache(maxsize=128)
    def _to_str(osm_tag: 'OSMTag') -> str:
        prefix = '!' if osm_tag.negate else ''
        key_val_str = ":".join(filter(None, [osm_tag.key, osm_tag.value]))
        return f"{prefix}{key_val_str}"

    def __str__(self) -> str:
        return self._to_str(self)

    def __repr__(self) -> str:
        return f"OSMTag(key={self.key}, value={self.value}, negate={self.negate})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, OSMTag):
            raise NotImplementedError
        return (self.key, self.value, self.negate) == (other.key, other.value, other.negate)

    def __hash__(self) -> int:
        return hash((self.key, self.value, self.negate))
