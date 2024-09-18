import itertools

def solve_crypt_arithmetic():
    letters = 'SENDMOR'
    for perm in itertools.permutations(range(10), len(letters)):
        s, e, n, d, m, o, r = perm
        if s == 0 or m == 0:
            continue
        send = 1000 * s + 100 * e + 10 * n + d
        more = 1000 * m + 100 * o + 10 * r + e
        money = 10000 * m + 1000 * o + 100 * n + 10 * e + y
        if send + more == money:
            print(f"SEND: {send}, MORE: {more}, MONEY: {money}")
            print(f"Mapping: S={s}, E={e}, N={n}, D={d}, M={m}, O={o}, R={r}")

if __name__ == "__main__":
    solve_crypt_arithmetic()
