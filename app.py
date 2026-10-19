"""Dog Day Trip Planner - CS361 Milestone 1."""

import json
from pathlib import Path


DATA_FILE = Path(__file__).parent / "data" / "destinations.json"
RATING_LABELS = [
    "Dog friendliness",
    "Travel convenience",
    "Activity suitability",
    "Owner interest",
]


def title(text):
    print("\n" + "=" * 56)
    print(text)
    print("=" * 56)


def load_destinations():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return []


def save_destinations(destinations):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(destinations, file, indent=2)
        return True
    except OSError:
        print("The destinations could not be saved.")
        return False


def total_score(destination):
    ratings = destination.get("ratings", [])
    if len(ratings) != 4:
        return None
    return sum(ratings)


def rank_destinations(destinations):
    rated = []
    for destination in destinations:
        if total_score(destination) is not None:
            rated.append(destination)

    def sort_value(destination):
        return (-total_score(destination), destination["name"].lower())

    return sorted(rated, key=sort_value)


def show_help():
    title("HELP / HOW IT WORKS")
    print("Use the planner to compare outings before you leave.")
    print("\n1  Add a destination name and description.")
    print("2  Rate four criteria from 1 to 5.")
    print("3  Compare trips by total score.")
    print("\nTime: about 1 minute per trip.")
    print("Privacy: information stays on this computer.")
    print("Cost: no account, payment, or internet connection.")
    print("\nYou can rate from the Main Menu or the Rankings screen.")
    input("Press Enter for the Main Menu: ")


def add_destination(destinations):
    while True:
        title("ADD DESTINATION - STEP 1 OF 2")
        print("Enter a name and a short description.")
        print("Type B to go back or C to cancel.")

        name = input("Name (required): ").strip()
        if name.lower() in ["b", "c"]:
            return
        if not name:
            print("A name is required.")
            continue

        description = input("Description (required): ").strip()
        if description.lower() == "c":
            return
        if description.lower() == "b":
            continue
        if not description:
            print("A description is required.")
            continue

        title("REVIEW DESTINATION - STEP 2 OF 2")
        print(f"Name: {name}")
        print(f"Description: {description}")
        print("\nSaving adds this destination to your trip list.")
        choice = input("[E] Edit  [S] Save  [C] Cancel: ").strip().lower()

        if choice == "e":
            continue
        if choice == "c":
            return
        if choice != "s":
            print("Choose E, S, or C.")
            continue

        destinations.append({
            "name": name,
            "description": description,
            "ratings": [],
        })
        if save_destinations(destinations):
            print(f'\nSaved "{name}."')
            print("\nSaved destinations:")
            for number, destination in enumerate(destinations, start=1):
                print(f"{number}  {destination['name']}")
        else:
            destinations.pop()
        input("Press Enter for the Main Menu: ")
        return


def choose_destination(destinations):
    while True:
        title("RATE DESTINATION - STEP 1 OF 3")
        for number, destination in enumerate(destinations, start=1):
            score = total_score(destination)
            status = f"{score}/20" if score is not None else "Not rated"
            print(f"{number}  {destination['name']} - {status}")

        choice = input("Choose a number or [B] Back: ").strip()
        if choice.lower() == "b":
            return None
        if choice.isdigit():
            number = int(choice)
            if 1 <= number <= len(destinations):
                return destinations[number - 1]
        print("Choose a listed number or B.")


def read_ratings():
    ratings = []
    for label in RATING_LABELS:
        while True:
            value = input(f"{label}: ").strip()
            if value.lower() in ["b", "c"]:
                return value.lower()
            if value.isdigit() and 1 <= int(value) <= 5:
                ratings.append(int(value))
                break
            print("Enter a whole number from 1 to 5.")
    return ratings


def rate_destination(destinations):
    if not destinations:
        print("\nNo destinations have been saved yet.")
        input("Press Enter for the Main Menu: ")
        return

    while True:
        destination = choose_destination(destinations)
        if destination is None:
            return

        while True:
            title(f"RATE {destination['name'].upper()} - STEP 2 OF 3")
            print("Score each item from 1 (low) to 5 (high).")
            print("Type B to go back or C to cancel.")
            ratings = read_ratings()

            if ratings == "c":
                return
            if ratings == "b":
                break

            title("REVIEW RATINGS - STEP 3 OF 3")
            print(destination["name"])
            for label, rating in zip(RATING_LABELS, ratings):
                print(f"{label}: {rating}")
            print(f"Total: {sum(ratings)}/20")
            print("\nNothing is saved until you choose Save.")
            choice = input("[E] Edit  [S] Save  [C] Cancel: ").strip().lower()

            if choice == "e":
                continue
            if choice == "c":
                return
            if choice != "s":
                print("Choose E, S, or C.")
                continue

            old_ratings = destination.get("ratings", [])
            destination["ratings"] = ratings
            if save_destinations(destinations):
                print(f'\nSaved ratings for "{destination["name"]}."')
            else:
                destination["ratings"] = old_ratings
            input("Press Enter for the Main Menu: ")
            return


def show_rankings(destinations):
    title("RANKED DESTINATIONS")
    print("Highest total score appears first.\n")
    ranked = rank_destinations(destinations)

    if not ranked:
        print("No destinations have complete ratings yet.")
    else:
        for number, destination in enumerate(ranked, start=1):
            print(f"{number}  {destination['name']} - {total_score(destination)}/20")

    print("\nTied totals are ordered alphabetically.")
    choice = input("[R] Rate a destination  [M] Main Menu  [H] Help: ").strip().lower()
    if choice == "r":
        rate_destination(destinations)
    elif choice == "h":
        show_help()


def main():
    destinations = load_destinations()

    while True:
        title("DOG DAY TRIP PLANNER")
        print("Save, score, and compare dog-friendly day trips.")
        print("\n1  Add destination")
        print("2  Rate destination")
        print("3  View ranked destinations")
        print("4  Help / how it works")
        print("5  Exit")
        print("\nSaved locally. No account, payment, or internet required.")
        choice = input("Choose an option [1-5]: ").strip()

        if choice == "1":
            add_destination(destinations)
        elif choice == "2":
            rate_destination(destinations)
        elif choice == "3":
            show_rankings(destinations)
        elif choice == "4":
            show_help()
        elif choice == "5":
            print("\nYour destinations are saved. Goodbye!")
            break
        else:
            print("Choose a whole number from 1 to 5.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nYour saved destinations were not changed. Goodbye!")
