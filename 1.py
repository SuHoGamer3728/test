a = input('nhập: ')
# đếm số kí tự trong sâu
print(len(a))
# đảo xâu
print(a[::-1])
# kiểm tra xâu đảo
b = a[::-1]
if a == b :
    print('xâu chx đảo ngược')
else :
    print('xâu đã đảo ngược')
# thay thế kí tự 
c = a.replace(input('kí tự cần thay thế:'),input('nhập kí tự mới:'))
print(c)
# tách xâu dựa vào khoảng trắng
print(a.split())
# xâu thường thành viết hoa và ngược lại
print(a.upper()) # đổi thành hoa
print(a.lower()) # đổi thành thường
print(a.capitalize()) # viết hoa chữ đầu

