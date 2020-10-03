#BT2:Viết hàm với tham số truyền vào là năm sinh, sử dụng hàm vừa cài đặt, nhập vào năm sinh và in ra tuổi:
ten = str(input("Nhập tên của bạn: "))
namsinh = int(input("Nhập Năm sinh của bạn:"))
x = 2020 - namsinh
def func_greet(ten,namsinh,x):
     print(f"Hello {ten}. Năm sinh {namsinh}.Vậy bạn là: {x}!")
func_greet(ten,namsinh,x)
