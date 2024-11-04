def first_missing_positive(numbers):
    numbers_max = max(numbers)

    for i in range(1, numbers_max + 1):  # assume starting from number one
        for j in numbers:
            if j == i:
                break
        else:
            missing_positive = i
            break

    return print(f"The first missing positive number is: {missing_positive}")


first_missing_positive([1, 2, 3, 4, 8, 9])
