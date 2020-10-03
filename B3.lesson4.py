#BT4:Viết hàm với tham số truyền vào là một tháng và trả về mùa tương ứng trong năm. 
# Sử dụng hàm vừa cài đặt, nhập vào một tháng và in ra màn hình mùa trong năm.
n = int(input("Nhập N: "))
def func_greet(n):
    if(1<= 4 and n < 4):
        print("Mùa Xuân")
    elif(4 <= 6 and n <= 6 and n >= 4):
        print("Mùa Hạ")
    elif(7 <= 9 and n <= 9 and n >= 7):
        print("Mùa Thu") 
    elif(10 <= 12 and n <= 12 ):
        print("Mùa Đông")
func_greet(n)