import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from ldip.meeting import Member, PartyMeeting, generate_prompt


def create_meeting(topic: str):
    meeting = PartyMeeting(
        topic=topic,
        members=[Member.from_prompt_file("role_instructions/head_of/foreign_affairs.md")],
        chair=Member.from_prompt_file("role_instructions/president.md"),
    )
    return meeting


def main():
    meeting = create_meeting("AI in Society")
    minutes = meeting.conduct_meeting()

    # Play around with prompts
    member = Member.from_jinja_template("head_of/foreign_affairs.md")
    prompt = generate_prompt(
        template="initial_statement.md.jinja2",
        meeting=meeting,
        member=member,
        meeting_role="member",
    )
    print(prompt)

    # completion = complete(message=prompt)


if __name__ == "__main__":
    main()
