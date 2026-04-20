import datetime

appointments = []

def check_availability(doctor, date):
    all_slots = ["10:00", "14:00", "16:00"]
    booked = [a["time"] for a in appointments if a["doctor"] == doctor and a["date"] == date]
    return [s for s in all_slots if s not in booked]

def book_slot(doctor, date, time):
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    if date < now:
        return {"error": "Cannot book past date"}

    for a in appointments:
        if a["doctor"] == doctor and a["date"] == date and a["time"] == time:
            return {"error": "Slot already booked"}

    appointments.append({"doctor": doctor, "date": date, "time": time})
    return {"status": "confirmed", "time": time}

def cancel_slot(doctor, date, time):
    global appointments
    appointments = [a for a in appointments if not (a["doctor"] == doctor and a["date"] == date and a["time"] == time)]
    return {"status": "cancelled"}

def reschedule_slot(doctor, date, old_time, new_time):
    cancel_slot(doctor, date, old_time)
    return book_slot(doctor, date, new_time)
