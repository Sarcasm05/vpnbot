from core.FindBranch import AdoptBranch

def add_user(user_id):
    with AdoptBranch() as cur:
        cur.execute(AdoptBranch.add_user(user_id))

def autorisation(user_id):
    with AdoptBranch() as bd:
        if not bd.execute(AdoptBranch.select_user(user_id)):
            return 0
        return 1

def change_user_state(user_id, state):
    with AdoptBranch() as bd:
        bd.execute(AdoptBranch.update_user_state(user_id, state))
