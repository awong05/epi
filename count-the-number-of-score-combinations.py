"""
In an American football game, a play can lead to 2 points (safety), 3 points
(field goal), or 7 points (touchdown, assuming the extra point). Many different
combinations of 2, 3, and 7 point plays can make up a final score. For example,
four combinations of plays yield a score of 12.

- 6 safeties (2 * 6 = 12),
- 3 safeties and 2 field goals (2 * 3 + 3 * 2 = 12),
- 1 safety, 1 field goal and 1 touchdown (2 * 1 + 3 * 1 + 7 * 1 = 12), and
- 4 field goals (3 * 4 = 12).

Write a program that takes a final score and scores for individual plays, and
returns the number of combinations that result in a final score.

Hint: Count the number of combinations in which there are 0 w0 plays, then 1 w0
plays, etc.

"""

def num_combinations_for_final_score(final_score, individual_play_scores):
    """
    Space complexity: O(sn)
    Time complexity: O(sn)

    """

    num_combinations_for_score = [
        [1] + [0] * final_score for _ in individual_play_scores
    ]

    for i in range(len(individual_play_scores)):
        for j in range(1, final_score + 1):
            without_this_play = (
                num_combinations_for_score[i - 1][j] if i >= 1 else 0
            )
            with_this_play = (
                num_combinations_for_score[i][j - individual_play_scores[i]] \
                if j >= individual_play_scores[i] else 0
            )
            num_combinations_for_score[i][j] = (
                without_this_play + with_this_play
            )
    return num_combinations_for_score[-1][-1]
