def count_string(input_string):
    result = 0
    for char in input_string:
        result += 1
    return result
input_string = input("Nhập vào chuỗi cần đếm: ")
print("Số ký tự trong chuỗi là: ",count_string(input_string))