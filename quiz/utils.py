def generate_adaptive_quiz(questions, target_difficulty):
    """
    Dynamic Programming approach to select questions
    that sum up to target difficulty level.
    Difficulty levels: easy=1, medium=2, hard=3
    """

    difficulty_map = {'easy': 1, 'medium': 2, 'hard': 3}
    q_list = [(q, difficulty_map[q.difficulty]) for q in questions]

    n = len(q_list)
    dp = [[[] for _ in range(target_difficulty + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(target_difficulty + 1):
            if i == 0 or j == 0:
                dp[i][j] = []
            else:
                q, diff = q_list[i-1]
                if diff <= j:
                    if len(dp[i-1][j - diff]) + 1 > len(dp[i-1][j]):
                        dp[i][j] = dp[i-1][j - diff] + [q]
                    else:
                        dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

    return dp[n][target_difficulty]
