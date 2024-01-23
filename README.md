# Photon Geocoder

## Overview
Photon Geocoder is a Python library designed to provide efficient and easy-to-use geocoding capabilities using OpenStreetMap data. It offers a robust solution for translating addresses into geographic coordinates and vice versa.

## Features
- Leverage OpenStreetMap data for accurate geocoding.
- Support for various geocoding queries, including address, city, and postal code lookups.
- Ability to filter results by specific OpenStreetMap tags.
- Asynchronous API for efficient network operations.

## Installation
To install Photon Geocoder, run the following command:

```
pip install photon-geocoder
```

## Usage
Here's a quick example of how to use Photon Geocoder:

```python
from photon_geocoder import PhotonGeocoder

# Create a geocoder instance
geocoder = PhotonGeocoder()

# Geocode an address
addresses = await geocoder.query("Brandenburg Gate, Berlin")
print(addresses)
```

## API Reference
The main class in Photon Geocoder is `PhotonGeocoder`. It provides the following methods:
- `query(address, layers=None, osm_tags=None, limit=10)`: Performs a geocoding query.

## Contributing
Contributions to Photon Geocoder are welcome! Please read our contribution guidelines for more information on how to contribute.

## License
Photon Geocoder is licensed under the [MIT License](LICENSE).