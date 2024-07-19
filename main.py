import os
import sys
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from ldip.meeting import Member, PartyMeeting, dump_minutes_as_json
from ldip.minutes_to_markdown import dump_minutes_as_markdown


def main():
    topic = "Defence and safety of Lithuania"
    topic = "Choose most important metrics for the country"

    meeting = PartyMeeting(
        topic=topic,
        members=[Member.from_jinja_template(f"head_of/{name}") for name in os.listdir("role_instructions/head_of")],
        chair=Member.from_jinja_template("board_chair.md"),
        model="anthropic/claude-3-5-sonnet-20240620",
        # urls=[],  # Contains important information to ground discussion on the topic
    )
    minutes = meeting.conduct_meeting()
    # format datetime
    folder_name = f"{datetime.now():%Y%m%d-%H%M%S} {topic}"
    folder_path = f"positions/{folder_name}"
    os.mkdir(folder_path)
    minutes_path = f"{folder_path}/minutes.json"
    dump_minutes_as_json(meeting, minutes_path)
    minutes_md = dump_minutes_as_markdown(minutes)
    minutes_md_path = f"{folder_path}/minutes.md"
    with open(minutes_md_path, "w") as f:
        f.write(minutes_md)


if __name__ == "__main__":
    main()
