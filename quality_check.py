"""Check the three quality attributes selected for the project."""

from pathlib import Path
from time import perf_counter

from app import rank_destinations


def main():
    print("DOG DAY TRIP PLANNER - QUALITY ATTRIBUTE CHECK")

    app_text = Path(__file__).with_name("app.py").read_text(encoding="utf-8")
    labels = ["Add destination", "Rate destination", "View ranked destinations"]
    usability = all(label in app_text for label in labels)
    print(f"Usability: clear menu labels - {'PASS' if usability else 'FAIL'}")

    reliability = "1 <= int(value) <= 5" in app_text
    print(f"Reliability: rating validation - {'PASS' if reliability else 'FAIL'}")

    destinations = []
    for number in range(100):
        destinations.append({
            "name": f"Destination {number}",
            "description": "Test destination",
            "ratings": [4, 4, 4, 5],
        })

    start = perf_counter()
    ranked = rank_destinations(destinations)
    elapsed = perf_counter() - start
    responsiveness = len(ranked) == 100 and elapsed < 2
    print(
        f"Responsiveness: ranked 100 destinations in {elapsed:.6f} seconds "
        f"- {'PASS' if responsiveness else 'FAIL'}"
    )

    if not (usability and reliability and responsiveness):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
