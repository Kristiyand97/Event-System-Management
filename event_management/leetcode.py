def uniqueOccurrences(arr):

    unique_numbers = {}

    for number in arr:
        if number not in unique_numbers:
            unique_numbers[number] = 1
        else:
            unique_numbers[number] += 1


