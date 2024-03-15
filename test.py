def delete_nth(order, max_e):
    d = {}
    res = []
    for item in order:
      n = d.get(item, 0)
      if n < max_e:
        res.append(item)
        print(d)
        d[item] = n+1
        print(d)
    return res

print(delete_nth([4, 1, 1, 3, 1, 2, 1, 2, 3, 4, 3, 4], 2))