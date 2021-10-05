my_list = [
    ["001","Bút bi", 2000,"30/08/2021"]
]
def add_item(my_list,item):
    my_list.append(item)
    return my_list
def input_items():
    number = input("Nhập mã số: ")
    items = input("Nhập lần lượt tên: ")
    cost = int(input("Nhập giá thành: "))
    days = input("Nhập ngày chi: ")
    new_list = []
    new_list.append(number)
    new_list.append(items)
    new_list.append(cost)
    new_list.append(days)
    return new_list

def show_header():
    print(f"{'Mã chi tiêu:':<10}{'Tên mặt hàng':^20}{'Giá thành(vnd)':^40}{'Ngày chi':<20}")

def show_items(my_list):
    show_header()
    for i in my_list:
            number = i[0]
            name = i[1]
            cost = i[2]
            day = i[3]
            print(f"{number:<10}{name:^20}{cost:^40}{day:<20}")

def remove_item(my_list):
    number = input("Nhập mã chi tiêu muốn xóa:")
    for i in my_list:
        if number == i[0]:
            my_list.remove(i)
    return my_list

def show_menu():
    print("""
            Hãy chọn tính năng muốn thực hiện.
            1. Thêm mục chi tiêu
            2. Xóa mục chi tiêu
            3.Hiển thị các mục chi tiêu
            4.Kết thúc
        """)


def get_choice():
    return input("Lựa chọn của bạn: ")


while True:
    show_menu()
    choice = get_choice()
    if choice == "1":
        my_list = add_item(my_list,input_items())
    if choice == "2":
        my_list == remove_item(my_list)
    if choice == "3":
        show_items(my_list)
    if choice == "4":
        break

