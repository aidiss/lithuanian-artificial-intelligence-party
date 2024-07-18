def dump_minutes_as_markdown(minutes):
    md = f"# {minutes.topic}\n\n"
    md += f"Date: {minutes.date}\n\n"

    md += "\n## Attendees\n"
    for attendee in minutes.attendees:
        md += f"- {attendee}\n"

    md += "\n## Minutes of the Meeting\n"
    for minute in minutes.minutes:
        md += f"- {minute['speaker']}: {minute['statement']}\n"

    md += f"\n## Position Statement\n\n{minutes.position_statement}\n"

    md += "\n## Votes\n\n"
    for vote in minutes.votes:
        md += f"- {vote['name']}: {vote['vote']}\n"

    md += "\n## Voting Results\n\n"
    md += f"Approved: {minutes.vote_count['yes']}\n"
    md += f"Rejected: {minutes.vote_count['no']}\n"
    md += f"Abstained: {minutes.vote_count['abstain']}\n"

    # result
    md += f"\nVoting results: {minutes.voting_results}\n"

    md += "\n## Actions\n"
    for action in minutes.actions:
        md += f"- {action['action']} (Due date: {action['due_date']})\n"

    return md
