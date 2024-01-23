"""
Path: tests/config.py
"""


def convert_address_format(addresses):
    converted_addresses = []

    for address in addresses:

        # normalizing street names
        street = address['street'].replace("strasse", "straße").replace(
            "Strasse", "Straße").replace("Str.", "Straße").replace("str.", "straße")

        # Creating the output dictionary
        for i in range(1, 10):
            address['house_number'] = str(i)
            # Constructing the input string
            input_str = f"{address['postal_code']} {address['city']} {
                address['street']} {address['house_number']}"
            output_dict = {
                "postcode": address['postal_code'],
                "city": address['city'],
                "street": street,
                "housenumber": str(i)
            }

            # Appending the converted address to the list
            converted_addresses.append(
                {"input": input_str, "output": output_dict})

    return converted_addresses


UNCLEANED_DATAS = [
    {"postal_code": "66663", "city": "Merzig", "country": "Germany",
        "street": "Am Stadtwald"},
    {"postal_code": "56203", "city": "Höhr-Grenzhausen", "country": "Germany",
        "street": "Bergstraße"},
    {"postal_code": "35037", "city": "Marburg", "country": "Germany",
        "street": "Sfaxer Strasse"},
    {"postal_code": "21509", "city": "Glinde", "country": "Germany",
        "street": "Eichloh"},
    {"postal_code": "39365", "city": "Eilsleben", "country": "Germany",
        "street": "Bergstrasse"},
    {"postal_code": "94424", "city": "Arnstorf", "country": "Germany",
        "street": "Steingasse"},
    {"postal_code": "66763", "city": "Dillingen/Saar", "country": "Germany",
        "street": "Rosenstraße"},
    {"postal_code": "54636", "city": "Altscheid", "country": "Germany",
        "street": "Weidinger Str."},
    {"postal_code": "46145", "city": "Oberhausen", "country": "Germany",
        "street": "Friedrichstrasse"},
    {"postal_code": "63849", "city": "Leidersbach", "country": "Germany",
        "street": "Kolpingstrasse"},
    {"postal_code": "51789", "city": "Lindlar", "country": "Germany",
        "street": "Breslauer Strasse"},
    {"postal_code": "84307", "city": "Eggenfelden", "country": "Germany",
        "street": "Am alten Bad"},
    {"postal_code": "25836", "city": "Garding", "country": "Germany",
        "street": "Gartenstraße"},
    {"postal_code": "84106", "city": "Volkenschwand", "country": "Germany",
        "street": "Mainburger Straße"},
    {"postal_code": "12167", "city": "Berlin", "country": "Germany",
        "street": "Brandenburgische Straße"},
    {"postal_code": "26489", "city": "Ochtersum", "country": "Germany",
        "street": "Esenser Strasse"},
    {"postal_code": "86159", "city": "Augsburg", "country": "Germany",
        "street": "Finnenbahn"},
    {"postal_code": "89250", "city": "Senden", "country": "Germany",
        "street": "Lessingstraße"},
    {"postal_code": "76831", "city": "Billigheim-Ingenheim", "country": "Germany",
        "street": "Poststraße"},
    {"postal_code": "92367", "city": "Pilsach", "country": "Germany",
        "street": "Lindenstraße"},
    {"postal_code": "96138", "city": "Burgebrach", "country": "Germany",
        "street": "Burgebracher Straße"},
    {"postal_code": "88456", "city": "Ingoldingen", "country": "Germany",
        "street": "Grodter Weg"},
    {"postal_code": "41748", "city": "Viersen", "country": "Germany",
        "street": "Maasweg"},
    {"postal_code": "08606", "city": "Oelsnitz/Vogtland", "country": "Germany",
        "street": "Mühlstraße"},
    {"postal_code": "84186", "city": "Vilsheim", "country": "Germany",
        "street": "St.-Leonhard-Straße"},
    {"postal_code": "33104", "city": "Paderborn", "country": "Germany",
        "street": "Sommerbrede"},
    {"postal_code": "67065", "city": "Ludwigshafen am Rhein", "country": "Germany",
        "street": "Rheingönheimer Strasse"},
    {"postal_code": "17438", "city": "Wolgast", "country": "Germany",
        "street": "Lange Straße"},
    {"postal_code": "20099", "city": "Hamburg", "country": "Germany",
        "street": "An der Alster"},
    {"postal_code": "49124", "city": "Georgsmarienhütte", "country": "Germany",
        "street": "Ulmenstraße"},
    {"postal_code": "89231", "city": "Neu-Ulm", "country": "Germany",
        "street": "Meininger Allee", },
    {"postal_code": "37269", "city": "Eschenweg", "country": "Germany",
        "street": "Südring"},
    {"postal_code": "88524", "city": "Uttenweiler", "country": "Germany",
        "street": "In den Thaläckern"}
]

DATAS = convert_address_format(UNCLEANED_DATAS)
