from random import choice

s_n = 0
f_n = 0
t_n = range(0, 1000)

for n in t_n:
    side = choice(range(0, 6))
    if side == 5:
        s_n = s_n + 1
    else:
        f_n = f_n + 1

ratio = int(s_n) / int(f_n)
print(ratio)

