from pathlib import Path


def is_palindrome(x):
    return x == x[::-1]

def add_one(x):
    return str(int(x) + 1)

def handle_odd(x):
    n = len(x)
    left = x[:n // 2]
    mid = x[n // 2]
    right = x[n // 2 + 1:]

def handle_even(x):
    pass

def solve(x):
    if is_palindrome(x): x = add_one(x)

    if len(x) % 2 != 0:
        handle_odd(x)
    else:
        handle_even(x)




def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    for line in data.splitlines():
        line = line.strip()
        if line:
            result = is_palindrome(line)
            print(f"A {line} palindrom-e {result}")


if __name__ == "__main__":
    main()
