def min_number(numbers):
    result = numbers[0]
    for num in numbers:
        if result > num:
            result = num
    return result

numbers = [2,9,5,8,5,6,3,21,55,2,21,5,68,2,15,6,3,1,5,66]
print("Số nhỏ nhất trong mảng là: ",min_number(numbers))