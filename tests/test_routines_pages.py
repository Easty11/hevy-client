"""Hermetic smoke tests for the routines/--pages path.

No live Hevy call, no API key, no network: the network boundary (`_get`) and the
command handler (`list_routines`) are mocked, so these tests exercise only the
client's own logic.

They lock in the f6d94a8 fix (exposing --pages on the `routines` subcommand) by
asserting two behaviours:
  (1) `routines --pages N` flows through to `list_routines(pages=N)`;
  (2) pagination terminates as soon as a page comes back empty.
"""

import json
import sys

import hevy_client


def test_routines_subcommand_passes_pages_through(monkeypatch):
    """`routines --pages 3` must reach list_routines with pages=3 (the f6d94a8 fix)."""
    captured = {}

    def fake_list_routines(pages=1, page_size=10):
        captured["pages"] = pages

    monkeypatch.setattr(hevy_client, "list_routines", fake_list_routines)
    monkeypatch.setattr(sys, "argv", ["hevy_client.py", "routines", "--pages", "3"])

    hevy_client.main()

    assert captured["pages"] == 3


def test_routines_pagination_terminates_on_empty_page(monkeypatch, capsys):
    """list_routines must stop paging at the first empty page, even if more were asked for."""
    pages_requested = []

    def fake_get(path, params=None):
        assert path == "/routines"
        page = params["page"]
        pages_requested.append(page)
        # Page 1 has data; page 2 is empty -> the loop should break before page 3+.
        if page == 1:
            return {"routines": [{"id": "r1"}]}
        return {"routines": []}

    monkeypatch.setattr(hevy_client, "_get", fake_get)

    hevy_client.list_routines(pages=5)

    # pages=5 was requested but only pages 1 and 2 were fetched (2 = first empty).
    assert pages_requested == [1, 2]
    printed = json.loads(capsys.readouterr().out)
    assert printed == [{"id": "r1"}]
