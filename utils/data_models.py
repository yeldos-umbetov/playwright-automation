from dataclasses import dataclass, asdict
from faker import Faker

fake = Faker()

@dataclass
class AddressData:
    first_name: str
    last_name: str
    company: str
    address1: str
    address2: str
    country: str
    state: str
    city: str
    zipcode: str
    mobile: str

    @classmethod
    def generate(cls, **overrides) -> "AddressData":
        """generates realistic fake address data"""
        defaults = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "company": fake.company(),
            "address1": fake.street_address(),
            "address2": fake.secondary_address(),
            "country": "United States",
            "state": fake.state(),
            "city": fake.city(),
            "zipcode": fake.zipcode(),
            "mobile": fake.msisdn()[:10],
        }

        defaults.update(overrides)
        return cls(**defaults)

    def to_dict(self) -> dict:
        return asdict(self)
