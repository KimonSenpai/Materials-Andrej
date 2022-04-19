# 2343 kompege

dp = [0]*21

dp[1] = 1

for i in range(2, 21):
    dp[i] = dp[i-1]

    if 2*i % 3 == 0:
        dp[i] += dp[2*i//3]

print(dp[20])