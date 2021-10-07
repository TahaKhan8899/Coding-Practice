# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):

    output = []
    for i in range(1, N//2 + 1):
        output.append(i)
        output.append(-i)
    if N % 2 > 0:
        output.append(0)
    return output


ans = solution(5)
print(ans)
