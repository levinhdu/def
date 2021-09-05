def remove_langest_number(numbers):
    langest = 0
    for number in numbers:
        if number > langest:
            langest = number
    numbers.remove(langest)
numbers = [1,9,2,3,5,4,6,8,11,20,21,20,25,1,2,3,5,66,95,14,23]
remove_langest_number(numbers)
print(numbers)