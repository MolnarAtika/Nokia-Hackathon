from pathlib import Path
import math

def is_palindrome(x):
    return x == x[::-1]

def add_one(x):
    return str(int(x) + 1)

def compare(x, y):
    for i, j in zip(x, y):
        if int(i) > int(j): return 1
        elif int(i) < int(j): return -1
        else: continue

    return 0

def handle_odd(x):
    n = len(x)
    left = x[:n // 2]
    mid = x[n // 2]
    right = x[n // 2 + 1:]

    if compare(left[::-1], right) == 1:
        return left + mid + left[::-1]
    else:
        left = left + mid
        left = add_one(left)
        return left + left[::-1][1:]


def handle_even(x):
    n = len(x)
    left = x[:n // 2]
    mid = x[n // 2]
    right = x[n // 2 + 1:]

    if compare(left[::-1], right) == 1:
        return left + left[::-1]
    else:
        left = add_one(left)
        return left + left[::-1]

def solve(x):
    if all(char == '9' for char in x):
        return str(int(x) + 2)

    if is_palindrome(x): x = add_one(x)

    if len(x) % 2 != 0:
        return handle_odd(x)
    else:
        return handle_even(x)




def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    for line in data.splitlines():
        line = line.strip()
        if '^' in line:
            snippets = line.split('^')
            firsthalf = float(snippets[0])
            secondhalf = float(snippets[1])
            pow = str(math.pow(firsthalf, secondhalf))
            result = solve(pow)
            print(f"A {line} következő palindromja: {result}")
        
        elif line:
            result = solve(line)
            print(f"A {line} következő palindromja: {result}")


if __name__ == "__main__":
    main()
