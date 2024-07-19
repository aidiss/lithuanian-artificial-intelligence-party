import json
from collections import Counter
from datetime import datetime
import subprocess
from typing import Literal

from jinja2 import Environment, FileSystemLoader

from ldip.completion import complete
from ldip.schemas import Minutes
from ldip.vote_calculator import calculate_voting_results

jinja_prompt_env = Environment(loader=FileSystemLoader("prompt_templates"))
jinja_role_env = Environment(loader=FileSystemLoader("role_instructions"))


CLEAN_MINUTES = True

MINUTES_MD_PATH = "meeting_minutes.md"
MINUTES_JSON_PATH = "meeting_minutes.json"


class PartyMeeting:
    """A meeting of a political party to discuss a topic and formulate a position statement."""

    def __init__(self, topic, members, chair, model: str):
        self.topic = topic
        self.chair: Member = chair
        self.model: str = model
        self.commit: str = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode("ascii").strip()
        self.members: list[Member] = members
        self.minutes = Minutes(
            topic=topic,
            model=model,
            commit=self.commit,
            date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            attendees=[],
            minutes=[],
            position_statement="",
            votes=[],
            vote_count=Counter(),
        )

    def conduct_meeting(self):
        """Conduct the meeting and generate the minutes.

        Every step adds to the `self.minutes`
        """
        minutes = self.minutes
        minutes.commit = self.commit
        minutes.model = self.model
        minutes.attendees = self.introduce_attendees()  # Just names
        # TODO add initial information, research, numbers, present topic.
        minutes.minutes = self.add_initial_statements()  # LLM for each member
        minutes.position_statement = self.formulate_position()  # LLM by chair
        # TODO add discussion rounds
        minutes.votes = self.hold_vote()
        minutes.vote_count = self.count_votes()
        minutes.voting_results = self.decide_voting_result()
        minutes.actions = self.create_action_plan()  # LLM
        return self.minutes

    def introduce_attendees(self) -> list[str]:
        """Introduce all members of the meeting."""
        return [f"{member.name}" for member in self.members]

    def add_initial_statements(self) -> list[dict[str, str]]:
        """Add discussion points to the minutes."""
        return [
            {"speaker": member.name, "statement": member.make_initial_statement(meeting=self)}
            for member in self.members
        ]

    def formulate_position(self) -> str:
        """Formulate a position statement based on the minutes."""
        prompt = generate_prompt("initial_statement.md.jinja2", meeting=self, member=self, meeting_role="chair")
        position_statement = complete(message=prompt, model=self.model)
        return position_statement

    def hold_vote(self) -> list[dict[str, str]]:
        """Hold a vote on the position statement."""
        # TODO: Implement a voting mechanism
        return [{"name": member.name, "vote": "yes"} for member in self.members]

    def count_votes(self) -> Counter:
        """Count the votes and store the results."""
        return Counter([vote["vote"] for vote in self.minutes.votes])

    def decide_voting_result(self) -> Literal["approved", "rejected"]:
        """Decide the voting result based on the votes."""
        result = calculate_voting_results(self.minutes.vote_count["yes"], self.minutes.vote_count["no"], unanimous=True)
        result_text = "approved" if result else "rejected"
        return result_text

    def create_action_plan(self):
        # TODO: Create an action plan based on the position statement
        return [
            {"action": "Post on social media", "due_date": "2021-12-31"},
            {"action": "Write a blog post", "due_date": "2021-12-31"},
        ]

    def log_to_file(self, text):
        mode = "w" if CLEAN_MINUTES else "a"
        with open(MINUTES_MD_PATH, mode) as file:
            file.write(text)

    def __repr__(self) -> str:
        return f"PartyMeeting(topic='{self.topic}', members='{self.members}', chair='{self.chair})'"


class Member:
    def __init__(self, name, prompt):
        self.name = name
        self.prompt = prompt

    @classmethod
    def from_prompt_file(cls, path):
        with open(path) as f:
            prompt = f.read()

        return cls(
            name=prompt.split("\n")[0].removeprefix("# "),
            prompt=prompt,
        )

    @classmethod
    def from_jinja_template(cls, name):
        jinja_template = jinja_role_env.get_template(name)
        prompt = jinja_template.render()
        name = prompt.split("\n")[0].removeprefix("# ")
        return cls(name=name, prompt=prompt)

    def make_initial_statement(self, meeting):
        prompt = generate_prompt("initial_statement.md.jinja2", meeting=meeting, member=self, meeting_role="member")
        statement = complete(message=prompt, model=meeting.model)
        return statement

    def __repr__(self) -> str:
        return self.name


def dump_minutes_as_json(meeting, path):
    with open(path, "w") as file:
        json.dump(meeting.minutes.model_dump(), file, indent=2)


def generate_prompt(template, meeting, member, meeting_role):
    print("Generating prompt")
    template = jinja_prompt_env.get_template(template)
    prompt = template.render(member=member, meeting=meeting, meeting_role=meeting_role)
    return prompt
