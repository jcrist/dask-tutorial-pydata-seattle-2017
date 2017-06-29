results = []
for x in data:
    y = delayed(inc)(x)
    results.append(y)

total = delayed(sum)(results)

total.compute()
