results = []
for x in data:
    if iseven(x):  # even
        y = delayed(double)(x)
    else:          # odd
        y = delayed(inc)(x)

    results.append(y)
    
total = delayed(sum)(results)
total.compute()
