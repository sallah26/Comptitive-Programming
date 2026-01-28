n = int(input())
if n == 0:
    print("++")
    print("++")
else:
    print(f"+{n * '-'}+")
    for i in range(n):
        print(f"|{n * ' '}|")
    print(f"+{n * '-'}+")