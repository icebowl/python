# lambda-sort-0.def foo():
alist = ["AZA  DDD", "ABA0 ZZZ ", "ddd 999", "RRR AAA"]
alist.sort(key=lambda first: first.split(" ")[-1].lower())
print(alist)
