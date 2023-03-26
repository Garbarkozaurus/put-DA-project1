import pandas as pd

def validate_input(alternatives: pd.DataFrame, criteria: pd.DataFrame):
    alternatives_criteria_names = alternatives.columns[1:].tolist()
    criteria_names = criteria.iloc[:, 0].tolist()

    assert len(alternatives) >= 12, f"Too few alternatives - have {len(alternatives)}, need at least 12"
    assert len(alternatives) <= 50, f"Too many alternatives - have {len(alternatives)}, need at most 50"

    assert len(criteria_names) >= 4, f"Too few criteria - have {len(criteria_names)}, need at least 4"
    assert len(criteria_names) <= 9, f"Too many criteria - have {len(criteria_names)}, need at most 9"

    assert len(criteria_names) == len(alternatives_criteria_names), f"Different number of criteria in sources - {len(criteria_names)} in criteria df, {len(alternatives_criteria_names)} in alternative df"

    mismatched_criteria = 0
    for criterion_name in criteria_names:
        if criterion_name not in alternatives_criteria_names:
            mismatched_criteria += 1
            print(criterion_name, "is not present in the columns of the dataframe for alternatives")
    assert mismatched_criteria == 0
    return True