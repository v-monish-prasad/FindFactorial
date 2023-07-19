def findFactorial(num):
    if num == 0:
        return 1

    return findFactorial(num - 1) * num


if __name__ == "__main__":
    number = int(input())

    print(findFactorial(number))
