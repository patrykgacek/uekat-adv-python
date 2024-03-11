import requests


class Brewery:
    def __init__(self, brewery: list) -> None:
        self.id: str = brewery["id"]
        self.name: str = brewery["name"]
        self.brewery_type: str = brewery["brewery_type"]
        self.address_1: str = brewery["address_1"]
        self.address_2: str = brewery["address_2"]
        self.address_3: str = brewery["address_3"]
        self.city: str = brewery["city"]
        self.state_province: str = brewery["state_province"]
        self.postal_code: str = brewery["postal_code"]
        self.country: str = brewery["country"]
        self.longitude: str = brewery["longitude"]
        self.latitude: str = brewery["latitude"]
        self.phone: str = brewery["phone"]
        self.website_url: str = brewery["website_url"]
        self.state: str = brewery["state"]
        self.street: str = brewery["street"]

    def __str__(self) -> str:
        return f"""ID: {self.id}
Name: {self.name}
Type: {self.brewery_type}
Address 1: {self.address_1}
Address 2: {self.address_2}
Address 3: {self.address_3}
City: {self.city}
State: {self.state_province}
Postal code: {self.postal_code}
Country: {self.country}
Longitude: {self.longitude}
Latitude: {self.latitude}
Phone: {self.phone}
Website: {self.website_url}
State: {self.state}
Street: {self.street}
"""


# =============================================================================

url = "https://api.openbrewerydb.org/breweries?per_page=20"
res = requests.get(url)
data = res.json()
breweries = [Brewery(brewery) for brewery in data]
for idx, brewery in enumerate(breweries):
    print(f"--- Brewery {idx + 1}. ".ljust(40, "-"))
    print(brewery)
