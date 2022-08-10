import datetime

def get_next_monday(d):
    import datetime
    days_ahead = 0 - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


def get_dates(d):
    import datetime
    dates = []
    dates.append(d.strftime('%Y-%m-%d'))
    for _ in range(9):
        new_d = d + datetime.timedelta(weeks=1)
        dates.append(new_d)
        d = new_d
    return dates

d = datetime.date.today()
next_monday = get_next_monday(d) 
print(next_monday)
dates = get_dates(next_monday)
print(dates)