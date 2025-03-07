import datetime
desks = {1: None, 2: None, 3: None}
def book_desk(desk_id, date, user):
    if desks[desk_id] is None:
        desks[desk_id] = (date, user)
        return f"Desk {desk_id} booked for {user} on {date} - Ready for Indian SMEs!"
    return "Desk booked - Try another slot!"
today = datetime.date.today()
print(book_desk(1, today, "Neha"))