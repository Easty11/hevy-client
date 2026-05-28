#!/usr/bin/env python3
"""
Hevy API client — retrieve workout data and load new workouts/routines.

Setup:
    pip install requests
    export HEVY_API_KEY="your_key_here"   # do NOT hardcode the key

Usage examples:
    python hevy_client.py count
    python hevy_client.py workouts --pages 2
    python hevy_client.py routines
    python hevy_client.py exercises --search "bench press"

Docs: https://api.hevyapp.com/docs/
Requires a Hevy Pro subscription. Key: https://hevy.com/settings?developer
"""

import argparse
import os
import sys
import json
import datetime as dt

import requests

BASE = "https://api.hevyapp.com/v1"


def _key() -> str:
    key = os.environ.get("HEVY_API_KEY")
    if not key:
        sys.exit("Set HEVY_API_KEY in your environment first.")
    return key


def _headers() -> dict:
    return {"api-key": _key(), "Content-Type": "application/json"}


def _get(path: str, params: dict | None = None) -> dict:
    r = requests.get(f"{BASE}{path}", headers=_headers(), params=params, timeout=30)
    r.raise_for_status()
    return r.json()


def _post(path: str, body: dict) -> dict:
    r = requests.post(f"{BASE}{path}", headers=_headers(), json=body, timeout=30)
    r.raise_for_status()
    return r.json()


# ---------- Read operations ----------

def workout_count() -> None:
    print(json.dumps(_get("/workouts/count"), indent=2))


def list_workouts(pages: int = 1, page_size: int = 10) -> None:
    """Hevy caps page_size at 10 for workouts."""
    all_rows = []
    for page in range(1, pages + 1):
        data = _get("/workouts", {"page": page, "pageSize": page_size})
        rows = data.get("workouts", [])
        if not rows:
            break
        all_rows.extend(rows)
    print(json.dumps(all_rows, indent=2))


def list_routines(pages: int = 1, page_size: int = 10) -> None:
    all_rows = []
    for page in range(1, pages + 1):
        data = _get("/routines", {"page": page, "pageSize": page_size})
        rows = data.get("routines", [])
        if not rows:
            break
        all_rows.extend(rows)
    print(json.dumps(all_rows, indent=2))


def list_exercises(search: str | None = None, pages: int = 5, page_size: int = 100) -> None:
    """Browse exercise templates; needed to get the exercise_template_id for creating workouts."""
    matches = []
    for page in range(1, pages + 1):
        data = _get("/exercise_templates", {"page": page, "pageSize": page_size})
        rows = data.get("exercise_templates", [])
        if not rows:
            break
        for ex in rows:
            if search is None or search.lower() in ex.get("title", "").lower():
                matches.append({"id": ex.get("id"), "title": ex.get("title")})
    print(json.dumps(matches, indent=2))


# ---------- Write operation: load a workout ----------

def create_sample_workout() -> None:
    """
    Creates a logged workout. Replace exercise_template_id values with real
    IDs from `python hevy_client.py exercises --search "<name>"`.
    """
    now = dt.datetime.now(dt.timezone.utc)
    start = (now - dt.timedelta(hours=1)).isoformat()
    end = now.isoformat()

    body = {
        "workout": {
            "title": "Loaded via API",
            "description": "Created by hevy_client.py",
            "start_time": start,
            "end_time": end,
            "is_private": False,
            "exercises": [
                {
                    # Example template id — swap for a real one from the exercises command
                    "exercise_template_id": "REPLACE_ME",
                    "superset_id": None,
                    "notes": "",
                    "sets": [
                        {"type": "normal", "weight_kg": 60, "reps": 8},
                        {"type": "normal", "weight_kg": 60, "reps": 8},
                        {"type": "normal", "weight_kg": 60, "reps": 6},
                    ],
                }
            ],
        }
    }
    print(json.dumps(_post("/workouts", body), indent=2))


def main() -> None:
    p = argparse.ArgumentParser(description="Hevy API client")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("count")

    w = sub.add_parser("workouts")
    w.add_argument("--pages", type=int, default=1)

    sub.add_parser("routines")

    e = sub.add_parser("exercises")
    e.add_argument("--search", type=str, default=None)

    sub.add_parser("create-sample")

    args = p.parse_args()
    if args.cmd == "count":
        workout_count()
    elif args.cmd == "workouts":
        list_workouts(pages=args.pages)
    elif args.cmd == "routines":
        list_routines()
    elif args.cmd == "exercises":
        list_exercises(search=args.search)
    elif args.cmd == "create-sample":
        create_sample_workout()


if __name__ == "__main__":
    main()
