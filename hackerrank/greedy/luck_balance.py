class Contest:
    def __init__(self, luck_balance, is_important):
        self.is_important = is_important
        self.luck_balance = luck_balance

    def win(self):
        return -self.luck_balance

    def lose(self):
        return self.luck_balance

    def __lt__(self, other):
        # we want the important contests with the most luck balance to be first
        if self.is_important and other.is_important:
            return self.luck_balance >= other.luck_balance
        elif self.is_important:
            return True
        else:
            return False

contest_count, lost_imp_contest_count = [int(p) for p in input().split()]
contests = []

for _ in range(contest_count):
    luck_balance, is_important = [int(p) for p in input().split()]
    contests.append(Contest(luck_balance, is_important))

contests_to_lose = 0
contests = sorted(contests)
curr_luck_balance = 0
for cont in contests:
    if cont.is_important:
        # important contest, see if we can lose it
        if contests_to_lose != lost_imp_contest_count:
            curr_luck_balance += cont.lose()
            contests_to_lose += 1
        else:
            curr_luck_balance += cont.win()
    else:
        # non-important contest, just lose anyway
        curr_luck_balance += cont.lose()
print(curr_luck_balance)