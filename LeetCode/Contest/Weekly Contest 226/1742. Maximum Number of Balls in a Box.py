from collections import Counter

def countBalls(lowLimit: int, highLimit: int) -> int:
    ball_count = []
    for number in range(lowLimit, highLimit + 1):
        ball_number = 0

        while number:
            number, remainder = divmod(number, 10)
            ball_number += remainder
        
        ball_count.append(ball_number)

    return Counter(ball_count).most_common(1)[0][1]


if __name__ == "__main__":
    lowLimit = 5
    highLimit = 15
    print(countBalls(lowLimit, highLimit))
