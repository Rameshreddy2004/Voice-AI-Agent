# SIMPLE MEMORY (NO REDIS NEEDED)

store = {}

def get_session(user_id):
    return store.get(user_id, {})

def set_session(user_id, data):
    store[user_id] = data