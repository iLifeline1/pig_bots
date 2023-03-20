def choice(round_score, my_score, opponent_score):
    if my_score <= 30:
        if round_score >= 18:
            return False
        else:
            return True
    if my_score - opponent_score >= 25:
        if round_score >= 25:
            return False
        else:
            return True
    if opponent_score - my_score <= 15:
        if round_score >= 20:
            return False
        else:
            return True
    if my_score - opponent_score >= 35:
        if round_score >= 14:
            return False
        else:
            return True
    if opponent_score - my_score >= 35:
        if round_score >= 25:
            return False
        else:
            return True
    else:
        return False
