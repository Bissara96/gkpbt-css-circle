def fifth_power(n):
    return n ** 5

max_n = 150

# Предварительно создадим словарь пятых степеней чисел от 1 до max_n
fifth_powers = {i: fifth_power(i) for i in range(1, max_n + 1)}
# И обратный словарь: значение -> число
power_to_num = {v: k for k, v in fifth_powers.items()}

found = False

for a in range(1, max_n + 1):
    a5 = fifth_powers[a]
    for b in range(a, max_n + 1):
        b5 = fifth_powers[b]
        for c in range(b, max_n + 1):
            c5 = fifth_powers[c]
            for d in range(c, max_n + 1):
                d5 = fifth_powers[d]
                s = a5 + b5 + c5 + d5
                if s in power_to_num:
                    e = power_to_num[s]
                    # Проверяем, что e >= d чтобы избежать повторов
                    if e >= d:
                        print(f"Найдено: a={a}, b={b}, c={c}, d={d}, e={e}")
                        print("Сумма a+b+c+d+e =", a + b + c + d + e)
                        found = True
                        break
            if found:
                break
        if found:
            break
    if found:
        break