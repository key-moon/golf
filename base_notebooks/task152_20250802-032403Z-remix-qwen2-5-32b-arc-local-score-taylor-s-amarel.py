def p(input):
    n = len(input)
    output = [[0] * (2 * n) for _ in range(2 * n)]
    for i in range(n):
        for j in range(n):
            output[i][j] = input[i][j]
            output[i][2 * n - j - 1] = input[i][j]
            output[2 * n - i - 1][j] = input[i][j]
            output[2 * n - i - 1][2 * n - j - 1] = input[i][j]
    return output