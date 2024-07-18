def calculate_voting_results(
    yes,
    no,
    threshold: float | None = None,
    unanimous: bool = False,
    absolute_majority: bool = False,
) -> bool:
    """
    Calculate the voting result based on the votes.

    Examples:
    >>> create_voting_function(3, 0, unanimous=True)
    True
    >>> create_voting_function(3, 2, unanimous=True)
    False
    >>> create_voting_function(3, 2, absolute_majority=True)
    True
    >>> create_voting_function(2, 2, absolute_majority=True)
    False
    >>> create_voting_function(3, 2, threshold=0.6)
    True
    >>> create_voting_function(3, 3, threshold=0.6)
    False
    """
    assert sum([unanimous, absolute_majority, bool(threshold)]) == 1, "Only one voting method can be selected."

    if unanimous:
        return yes > 0 and no == 0
    elif absolute_majority:
        return yes > no
    elif threshold:
        return yes / (yes + no) > threshold
    else:
        raise ValueError("One of the voting methods must be selected.")
