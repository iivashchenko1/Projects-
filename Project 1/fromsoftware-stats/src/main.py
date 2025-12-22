from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

# Path to your CSV file (works no matter where you run from)
BASE_DIR = Path(__file__).resolve().parent.parent   # .../fromsoftware-stats
DATA_FILE = BASE_DIR / "data" / "games.csv"

def parse_int(value: str) -> int:
    value = value.strip()
    return int(value) if value else 0


def parse_float(value: str) -> float:
    value = value.strip()
    return float(value) if value else 0.0


def parse_bool(value: str) -> bool:
    # Handles "yes/no", "true/false", "1/0"
    value = value.strip().lower()
    return value in ("yes", "true", "1", "y")

def load_games_from_csv(path: Path) -> list[dict[str, Any]]:
    games: list[dict[str, Any]] = []

    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            game = {
                "title": row["title"].strip(),
                "series": row["series"].strip(),
                "release_year": parse_int(row["release_year"]),
                "platform_main": row["platform_main"].strip(),
                "meta_score": parse_int(row["meta_score"]),
                "user_score": parse_float(row["user_score"]),
                "hours_main_story": parse_int(row["hours_main_story"]),
                "hours_completionist": parse_int(row["hours_completionist"]),
                "difficulty": parse_int(row["difficulty"]),
                "pvp": parse_bool(row["pvp"]),
                "co_op": parse_bool(row["co_op"]),
            }
            games.append(game)

    return games

def print_all_games(games: list[dict[str, Any]]) -> None:
    if not games:
        print("No games to display.")
        return

    # Choose what to show
    headers = ["Title", "Year", "Series", "Meta", "User", "Main hrs", "Diff", "PVP", "Co-op"]
    widths = [32, 6, 12, 6, 6, 9, 5, 5, 6]

    def cut(text: str, w: int) -> str:
        return text if len(text) <= w else text[: w - 1] + "…"

    # Header row
    line = " | ".join(h.ljust(w) for h, w in zip(headers, widths))
    print(line)
    print("-" * len(line))

    # Rows
    for g in games:
        row = [
            cut(str(g["title"]), widths[0]).ljust(widths[0]),
            str(g["release_year"]).ljust(widths[1]),
            cut(str(g["series"]), widths[2]).ljust(widths[2]),
            str(g["meta_score"]).ljust(widths[3]),
            f'{g["user_score"]:.1f}'.ljust(widths[4]),
            str(g["hours_main_story"]).ljust(widths[5]),
            str(g["difficulty"]).ljust(widths[6]),
            ("yes" if g["pvp"] else "no").ljust(widths[7]),
            ("yes" if g["co_op"] else "no").ljust(widths[8]),
        ]
        print(" | ".join(row))

def filter_by_year_range(games: list[dict[str, Any]], start_year: int, end_year: int) -> list[dict[str, Any]]:
    return [g for g in games if start_year <= g["release_year"] <= end_year]


def filter_by_min_meta(games: list[dict[str, Any]], min_score: int) -> list[dict[str, Any]]:
    return [g for g in games if g["meta_score"] >= min_score]


def compute_stats(games: list[dict[str, Any]]) -> None:
    if not games:
        print("No games to analyze.")
        return

    longest = max(games, key=lambda g: g["hours_main_story"])
    shortest = min(games, key=lambda g: g["hours_main_story"])
    best_meta = max(games, key=lambda g: g["meta_score"])

    avg_meta = sum(g["meta_score"] for g in games) / len(games)
    avg_main = sum(g["hours_main_story"] for g in games) / len(games)

    print("\nStats")
    print("-----")
    print(f'Longest (main story): {longest["title"]} — {longest["hours_main_story"]} hrs')
    print(f'Shortest (main story): {shortest["title"]} — {shortest["hours_main_story"]} hrs')
    print(f'Highest meta score: {best_meta["title"]} — {best_meta["meta_score"]}')
    print(f"Average meta score: {avg_meta:.1f}")
    print(f"Average main story hours: {avg_main:.1f}\n")

def get_int(prompt: str) -> int:
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            print("Please enter a valid number.")


def main() -> None:
    if not DATA_FILE.exists():
        print(f"Could not find: {DATA_FILE}")
        print("Make sure games.csv is in the /data folder.")
        return

    games = load_games_from_csv(DATA_FILE)

    while True:
        print("\nFromSoftware / Souls-like Explorer")
        print("1) Show all games")
        print("2) Filter by year range")
        print("3) Filter by minimum meta score")
        print("4) Show stats")
        print("0) Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            print_all_games(games)

        elif choice == "2":
            start_year = get_int("Start year: ")
            end_year = get_int("End year: ")
            filtered = filter_by_year_range(games, start_year, end_year)
            print_all_games(filtered)

        elif choice == "3":
            min_score = get_int("Minimum meta score: ")
            filtered = filter_by_min_meta(games, min_score)
            print_all_games(filtered)

        elif choice == "4":
            compute_stats(games)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
