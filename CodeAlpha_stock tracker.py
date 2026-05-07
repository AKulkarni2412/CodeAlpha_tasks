stocks = {"AAPL": 180, "TSLA": 250, "GOOG": 2800}

total = 0

while True:
    name = input("Enter stock name (or 'done'): ").upper()
    if name == "DONE":
        break
    if name in stocks:
        qty = int(input("Enter quantity: "))
        total += stocks[name] * qty
    else:
        print("Stock not found")

print("Total Investment Value:", total)

with open("portfolio.txt", "w") as f:
    f.write("Total Investment: " + str(total))
