"""Restore the starting demonstration destination."""

import json
from pathlib import Path


def main():
    destinations = [
        {
            "name": "Great Falls Park",
            "description": "Potomac River overlooks and hiking trails.",
            "ratings": [4, 4, 4, 5],
        }
    ]

    data_path = Path(__file__).parent / "data" / "destinations.json"
    with open(data_path, "w", encoding="utf-8") as file:
        json.dump(destinations, file, indent=2)
        file.write("\n")

    print("Demo data restored: Great Falls Park.")


if __name__ == "__main__":
    main()
