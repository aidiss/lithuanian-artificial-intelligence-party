import json
from collections import Counter
from datetime import datetime
from typing import Literal

from jinja2 import Environment, FileSystemLoader

from ldip.minutes_to_markdown import dump_minutes_as_markdown
from ldip.schemas import Minutes
from ldip.vote_calculator import calculate_voting_results

jinja_prompt_env = Environment(loader=FileSystemLoader("prompt_templates"))
jinja_role_env = Environment(loader=FileSystemLoader("role_instructions"))


CLEAN_MINUTES = True

MINUTES_MD_PATH = "meeting_minutes.md"
MINUTES_JSON_PATH = "meeting_minutes.json"


class PartyMeeting:
    """A meeting of a political party to discuss a topic and formulate a position statement."""

    def __init__(self, topic, members, chair):
        self.topic = topic
        self.chair: Chair = chair
        self.members: list[Member] = members
        self.position_statement = ""
        self.minutes = Minutes(
            topic=topic,
            date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            attendees=[],
            minutes=[],
            position_statement="",
            votes=[],
            vote_count=Counter(),
        )
        self.votes = {}

    def conduct_meeting(self):
        """Conduct the meeting and generate the minutes.

        Every step adds to the `self.minutes`
        """

        # Steps that add to the minutes
        # self.introduce_attendees()
        minutes = self.minutes
        minutes.attendees = self.introduce_attendees()  # Just names

        minutes.minutes = self.add_initial_statements()  # LLM for each member
        minutes.position_statement = self.formulate_position()  # LLM by chair
        # Todo, add discussion rounds.
        minutes.votes = self.hold_vote()  # LLM by each
        minutes.vote_count = self.count_votes()
        minutes.voting_results = self.decide_voting_result()

        minutes.actions = self.create_action_plan()  # LLM

        dump_minutes_as_json(self)
        minutes_md = dump_minutes_as_markdown(self.minutes)
        self.log_to_file(minutes_md)
        return self.minutes

    def introduce_attendees(self) -> list[str]:
        """Introduce all members of the meeting."""
        return [member.name for member in self.members]

    def add_initial_statements(self) -> list[dict[str, str]]:
        """Add discussion points to the minutes."""
        return [{"speaker": member.name, "statement": member.make_initial_statement()} for member in self.members]

    def formulate_position(self) -> str:
        """Formulate a position statement based on the minutes."""
        position_statement = self.chair.draft_position_statement(self.minutes)
        position_statement = "FOOBAR FAKE STATEMENT The party supports the use of AI in society."
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

    def make_initial_statement(self):
        # TODO Create initial statement based based on meeting topic and role
        # statement = self.call_model()
        statement = "FOOBARFAKE I support the use of AI in society."
        return statement

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

    def draft_position_statement(self, minutes):
        # TODO: Chair drafts position statement based on minutes
        # position_statement = self.call_model()
        position_statement = "FOOBARFAKE The party supports the use of AI in society."
        return position_statement

    def __repr__(self) -> str:
        return self.name


class Chair(Member):
    def draft_position_statement(self, minutes):
        # Chair drafts position statement based on minutes
        return f"{self.name} : I propose that we support the use of AI in society."


def dump_minutes_as_json(meeting):
    with open(MINUTES_JSON_PATH, "w") as file:
        json.dump(meeting.minutes.model_dump(), file, indent=2)


def generate_prompt(template, meeting, member, meeting_role):
    template = jinja_prompt_env.get_template(template)
    prompt = template.render(member=member, meeting=meeting, meeting_role=meeting_role)
    return prompt
