from pathlib import Path

memory = {}
def min_num_of_drops(n, h):
    if h == 0: return 0
    if h == 1: return 1
    if n == 1: return h

    if(n, h) in memory:
        return memory[(n, h)]
    
    result = h
    for i in range(1, h, + 1):
        attempts = 1 + max(min_num_of_drops(n - 1, i - 1), min_num_of_drops(n, h - i))
        if attempts < result:
            result = attempts

    memory[n, h] = result
    return result

def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    for line in data.splitlines():
        line = line.strip().split(',')
        n = int(line[0])
        h = int(line[1])
        print(f"{min_num_of_drops(n, h)}")



if __name__ == "__main__":
    main()
