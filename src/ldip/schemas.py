from typing import Literal
from pydantic import BaseModel
from collections import Counter


class Vote(BaseModel):
    name: str
    vote: Literal["yes", "no", "abstain"]


class Minutes(BaseModel):
    topic: str  # topic of the meeting
    date: str  # date and time of the meeting
    attendees: list[str]  # list of attendee names
    minutes: list[dict[str, str]]  # list of dictionaries with keys: speaker, statement
    position_statement: str  # position statement - the final statement of the meeting
    votes: list[dict[str, str]]  # results of the voting, list of dictionaries with keys: name, vote
    vote_count: Counter = Counter()
    voting_results: Literal["approved", "rejected", "in_progress"] = "in_progress"
    actions: list[dict[str, str]] = []
