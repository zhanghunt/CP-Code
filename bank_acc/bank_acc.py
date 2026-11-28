from collections import deque

class Account:
    def __init__ (self, balance):
        self.balance = balance
        self.pending = deque()

    def fund(self, day, method, amount):
        if method == "WIRE":
            self.balance += amount
        else:
            self.pending.append((day + 1, amount))

    def balance_on(self, day):
        while self.pending and self.pending[0][0] <= day:
            self.balance += self.pending.popleft()[1]
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def process(self, line):
        parts = line.split()
        cmd = parts[0]
        if cmd == "INIT":
            self.accounts[parts[1]] = Account(int(parts[2]))
        elif cmd == "FUND":
            day, acc, method, amt = int(parts[1], parts[2], parts[3], int(parts[4]))
            if acc in self.accounts:
                self.accounts[acc].fund(day, method, amt)
        elif cmd == "BALANCE":
            day, acc = int (parts[1]), parts[2]
            if acc not in self.accounts:
                return "FAILURE"
            return str(self.accounts[acc].balance_on(day))
        return None