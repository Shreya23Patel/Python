data = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]

result = {}

for d in data:
    item = d['item']
    amount = d['amount']

    if item in result:
        result[item] += amount
    else:
        result[item] = amount

print(result)
