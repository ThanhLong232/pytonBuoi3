#BT3:Viết hàm với tham số truyền vào là nhiệt độ F, trả về kết quả nhiệt độ C theo công thức.
# Sử dụng hàm vừa cài đặt, nhập vào độ F và in ra màn hình độ C.
F = int(input("Nhập Độ F: "))
C = 5*(F - 32) / 9
def func_greet(F,C):
     print(f"Độ F là {F}.Vậy Độ C Là {C}!")
func_greet(F,C)