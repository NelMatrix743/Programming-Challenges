def solution(number: int) -> int:
    multiples: set[int] = set()
    if number < 0:
        return 0
    for num in range(number):
        if (num % 3 == 0) or (num % 5 == 0):
        	multiples.add(num)
    return sum(multiples)


# eosc