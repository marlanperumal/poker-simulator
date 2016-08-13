class Record(object):
    def __init__(self):
        self.games = []


class Player(object):
    def __init__(self, name, opening_balance = 0):
        self.name = name
        self.balance = opening_balance
        self.record = Record()