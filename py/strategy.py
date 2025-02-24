def get_score_volume(volume):
    if volume >= 20000:
        return 0.9
    elif 18000 <= volume < 20000:
        return 0.85
    elif 17000 <= volume < 18000:
        return 0.8
    elif 16000 <= volume < 17000:
        return 0.7
    elif 15000 <= volume < 16000:
        return 0.65
    elif 10000 <= volume < 15000:
        return 0.5
    else:
        return -1

def get_score_limitup(limitup_count):
    if limitup_count >= 100:
        return 0.9
    elif 50 <= limitup_count < 100:
        return 0.7
    elif 20 <= limitup_count < 50:
        return 0.5
    elif 10 <= limitup_count < 20:
        return 0.3
    else:
        return 0

def get_score_limitdown(limitdown_count):
    if limitdown_count >= 100:
        return 0.9
    elif 50 <= limitdown_count < 100:
        return 0.7
    elif 10 <= limitdown_count < 50:
        return 0.5
    else:
        return 0

def get_score_updays(updays_count):
    if updays_count >= 3:
        return -0.9
    elif 2 <= updays_count < 3:
        return -0.7
    elif 1 <= updays_count < 2:
        return 0.5
    else:
        return 0.1

def get_score_index(index_change):
    if index_change >= 2:
        return 0.9
    elif 1 <= index_change < 2:
        return 0.7
    elif 0 <= index_change < 1:
        return 0.5
    elif -1 <= index_change < 0:
        return -0.5
    elif -2 <= index_change < -1:
        return -0.7
    else:
        return -0.9
