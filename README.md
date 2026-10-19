# Dog Day Trip Planner

Dog Day Trip Planner is a small local program for saving, rating, and comparing dog-friendly day trips. It uses only Python's standard library and stores destinations in `data/destinations.json`.

## Run the program

Python 3.10 or newer is recommended.

```bash
python3 app.py
```

The included data file contains Great Falls Park as demonstration data. Rock Creek Park is added during the recommended assignment video walkthrough. Information remains on the local computer. The program does not require an account, payment, internet connection, database, API key, or microservice.

To restore the starting demonstration data after practicing, run:

```bash
python3 reset_demo_data.py
```

## Run the quality attribute check

```bash
python3 quality_check.py
```

## Sprint 1 user stories

### Add Destination

As a dog owner, I want to add a day-trip destination with basic details so that I can keep possible outings in one place.

Given the user is on the main menu, when the user selects Add Destination, enters a nonempty name and description, and confirms the entry, then the application saves the destination and displays it in the destination list.

### Rate Destination

As a dog owner, I want to rate a destination using dog friendliness, travel convenience, activity suitability, and owner interest so that I can evaluate the outing consistently.

Given at least one destination has been saved, when the user selects that destination and enters integer ratings from 1 through 5 for dog friendliness, travel convenience, activity suitability, and owner interest, then the application saves all four ratings and displays a total equal to their sum.

### View Ranked Destinations

As a dog owner, I want to view destinations ordered by their total ratings so that I can focus on the most promising day trips.

Given at least two destinations have complete ratings, when the user selects View Ranked Destinations, then the application displays the destinations in descending order by total score and shows each destination's total.

## Inclusivity Heuristics

1. The Main Menu states that the program saves, scores, and compares dog-friendly day trips.
2. Help identifies the approximate time, local storage and privacy behavior, and lack of monetary or internet costs.
3. Extra instructions remain in an optional Help screen instead of interrupting every task.
4. Numbered choices and the Back, Cancel, Edit, and Save commands remain consistent.
5. Users can go back, edit draft information, or cancel before saving.
6. Add Destination and Rate Destination display visible step numbers and next actions.
7. Users can start rating from the Main Menu or the Ranked Destinations screen.
8. The rating screen explains the valid range, rejects invalid input, and shows a review screen before saving.

## Quality attributes

- Usability: Every menu option and input prompt uses a visible plain-language label, and required destination fields are identified before submission.
- Reliability: Invalid rating input does not terminate the application or overwrite previously saved valid ratings.
- Responsiveness: A locally stored list of up to 100 destinations is ranked in under two seconds.
