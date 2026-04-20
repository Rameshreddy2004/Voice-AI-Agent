from scheduler.engine import check_availability, book_slot, cancel_slot, reschedule_slot

def execute_tool(name, args):
    if name == "checkAvailability":
        return check_availability(args["doctor"], args["date"])

    if name == "bookAppointment":
        return book_slot(args["doctor"], args["date"], args["time"])

    if name == "cancelAppointment":
        return cancel_slot(args["doctor"], args["date"], args["time"])

    if name == "rescheduleAppointment":
        return reschedule_slot(args["doctor"], args["date"], args["old_time"], args["new_time"])

    return {"error": "unknown tool"}
