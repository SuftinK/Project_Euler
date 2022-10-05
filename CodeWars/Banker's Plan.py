def fortune(f0, p, c0, n, i):
    import math
    interest_rate = p / 100
    inflation = i / 100
    withdraw = c0
    budget = f0
    for year in range(1, n+1):
        budget += budget * interest_rate
        budget -= withdraw
        #budget = math.ceil(budget)
        print(budget)
        if budget <= 0:
            print(f"False. The Year {year}, budget is {budget}")
            return False
        withdraw += withdraw * inflation
        #withdraw = math.ceil(withdraw)
    print(f"True. The Year {year}, budget is {budget}")
    return True

print(fortune(100000000, 1.5, 10000000, 50, 1))