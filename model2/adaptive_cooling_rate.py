# adaptive_cooling_rate.py

def adaptive_cooling_rate(alpha, r_min, r_max, current_acceptance_rate, t, N, d, D_max):
    if current_acceptance_rate < r_min:
        alpha *= 0.9999  # 增大 r_min 会减少冷却速率，温度下降更慢，迭代次数增加
    elif current_acceptance_rate > r_max:
        alpha *= 1.0001  # 减小 r_max 会增加冷却速率，温度下降更快，迭代次数减少

    # 动态调整冷却速率
    # t 与冷却速率成反比，t 增大冷却速率减少，温度下降更慢，迭代次数增加
    # N 与冷却速率成正比，N 增大冷却速率增加，温度下降更快，迭代次数减少
    # d 与冷却速率成正比，d 增大冷却速率增加，温度下降更快，迭代次数减少
    # D_max 与冷却速率成反比，D_max 增大冷却速率减少，温度下降更慢，迭代次数增加
    alpha = alpha * (1 - t/N) * (1 + d/D_max)
    return alpha

if __name__ == "__main__":
    alpha_0 = 0.9  # 初始冷却速率
    r_min = 0.1  # 增大 r_min 会减少冷却速率，温度下降更慢，迭代次数增加
    r_max = 0.9  # 减小 r_max 会增加冷却速率，温度下降更快，迭代次数减少
    current_acceptance_rate = 0.5
    t = 10  # 增大 t 会减少冷却速率，温度下降更慢，迭代次数增加
    N = 100  # 增大 N 会增加冷却速率，温度下降更快，迭代次数减少
    d = 500  # 增大 d 会增加冷却速率，温度下降更快，迭代次数减少
    D_max = 1000  # 增大 D_max 会减少冷却速率，温度下降更慢，迭代次数增加

    alpha = adaptive_cooling_rate(alpha_0, r_min, r_max, current_acceptance_rate, t, N, d, D_max)
    print(f"Adjusted Cooling Rate: {alpha}")
