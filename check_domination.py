import pandas as pd

def check_domination(target: pd.Series, potential_dominator: pd.Series, criteria: pd.DataFrame) -> bool:
    """
    Returns True if the alternative passed first argument is dominated by the second under the provided criteria. Otherwise - returns False
    """
    for row in criteria.iterrows():
        criterion =  row[1]
        criterion_name = criterion["criterion_name"]
        criterion_type = criterion["criterion_type"]
        if criterion_type == "gain":
            if target[criterion_name] > potential_dominator[criterion_name]:
                return False

        if criterion_type == "cost":
            if target[criterion_name] < potential_dominator[criterion_name]:
                return False

    print(target.iloc[0], "dominated by", potential_dominator.iloc[0])
    return True

def find_domminated_alternatives(alternatives: pd.DataFrame, criteria: pd.DataFrame) -> pd.DataFrame:
    number_of_alternatives = len(alternatives.index)
    dominated_alternatives = pd.DataFrame(columns=alternatives.columns)
    for i in range(number_of_alternatives-1):
        alternative = alternatives.iloc[i]
        for j in range(i+1, number_of_alternatives):
            dominator = alternatives.iloc[j]
            domination = check_domination(alternative, dominator, criteria)
            if domination:
                dominated_alternatives.loc[len(dominated_alternatives)] =  alternative
    return dominated_alternatives

if __name__ == "__main__":
    a = pd.read_csv("./data/games.csv")
    c = pd.read_csv("./data/games_criteria.csv")
    df = find_domminated_alternatives(a, c)
    print(df)