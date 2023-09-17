names = ["Kupenov", "Mukha", "Miko"]
bets = [100, 200, 300]
bonuses = ["10.25%", "5.50%", "8.75%"]

result = {name: bet * (float(bonus.strip('%')) / 100) for name, bet, bonus in zip(names, bets, bonuses)}

print(result)
