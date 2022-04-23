#!/usr/bin/env python
# coding: utf-8

# In[1]:

#B06_b2_Triangle_check
def triangle_check(xA,yA,xB,yB,xC,yC):
    '''Hàm kiểm tra 3 điểm tạo thành tam giác không? là loại tam giác nào
    Đầu vào là tọa độ x,y của 3 điểm A, B, C
    tương ứng: xA,yA,xB,yB,xC,yC'''
    import math
    
    dAB = math.sqrt((xB-xA)**2 + (yB-yA)**2)
    dBC = math.sqrt((xC-xB)**2 + (yC-yB)**2)
    dAC = math.sqrt((xC-xA)**2 + (yC-yA)**2)

    print('Is direct?')
    direct = dAC == dAB + dBC or dBC == dAC + dAB or dAB == dBC + dAC

    print(direct) 
    print() 

    print('Is a equilateral triangle?') 
    equilateral_triangle = dAB == dBC and dAB == dAC
    print(equilateral_triangle) 
    print() 

    print('Is a isosceles triangle?')
    isosceles_triangle = (dAB == dBC != dAC and not direct)  or (dAB == dAC != dBC and not direct) or (dBC == dAC != dAB and not direct) 
    print(isosceles_triangle) 
    print()

    print('Is a right triangle?')
    right_triangle = math.sqrt(dAB**2 + dAC**2) == dBC or math.sqrt(dAB**2 + dBC**2) == dAC or math.sqrt(dBC**2 + dAC**2) == dAB
    print(right_triangle)
    print()


    print('Is a normal triangle?') 
    normal_triangle = dAB != dBC and dBC != dAC and dAB != dAC
    print(normal_triangle)

# B08_Kiem_tra_nguyen_am 
def kiem_tra_nguyen_am(text):
    '''Hàm kiểm ra xem chuỗi có chứa nguyên âm không'''
    return 'a' in text or 'i' in text or 'e' in text or 'o' in text or 'u' in text

# B09_check_block_character
def check_block_char(text):
    '''Kiểm tra xem post có bị block không
    post gồm 3 câu, ngăn cách bởi dấu "."
    post bị block nếu tất cả các câu trong chuỗi chứa kí tự cấm'''
    text = text.lower().strip().split('.')
    text0 = text[0].strip()
    text1 = text[1].strip()
    text2 = text[2].strip()

    check_text0 = 'sex' in text0 or 'racist' in text0 or 'violence' in text0 or 'child abuse' in text0
    check_text1 = 'sex' in text1 or 'racist' in text1 or 'violence' in text1 or 'child abuse' in text1
    check_text2 = 'sex' in text2 or 'racist' in text2 or 'violence' in text2 or 'child abuse' in text2
    
    return check_text0 and check_text1 and check_text2

# B09_pitago
def pitago_check(a,b,c):
    '''Kiểm tra xem 3 số tự nhiên a, b, c có tạo thành 1 bộ số
    pitago hay không'''
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else:
        return False

# B09_phone_fee
def phone_fee(n):
    '''Tính cước phí điện thoại khi sử dụng n phút
    Cước thuê bao: 25000
    n<=50: 600/p
    50<n<=200: 400/p
    n>200: 200/p'''
    if n < 0:
        total = 'Số phút nhập không đúng'
    else:
        if n <= 50:
            total = 25000 + 600*n
        elif n <=200:
            total = 25000 + 600*50 + 400*(n-50) 
        else:
            total = 25000 + 600*50 + 400*150 + 200*(n-50-150)
    return total

# B09_weekday
def weekday_export(day,month,year):
    '''Xuất ra thứ của ngày nhập vào
    Thứ tự nhập: day, month, year'''
    import datetime
    mydate = datetime.date(year, month, day)
    n = mydate.weekday()

    if n==0:
        return 'Thứ Hai'
    elif n==1:
        return 'Thứ Ba'
    elif n==2:
        return 'Thứ Tư'
    elif n==3:
        return 'Thứ Năm'
    elif n==4:
        return 'Thứ Sáu'
    elif n==5:
        return 'Thứ Bảy'
    elif n==6:
        return 'Chủ Nhật'
    else:
        return 'Số nhập không hợp lệ, hãy nhập số nguyên từ 0 đến 6' 

# B10_Checkscore
def check_score(a,b,c):
    '''Hàm đánh giá xếp loại học lực của học viên
    dựa trên 3 điểm đầu vào a, b, c tương ứng
    điểm 15p, điểm giữa kì và điểm cuối kì
    đầu vào: 0<=a,b,c<=10'''
    if a < 0 or a>10 or b<0 or b>10 or c<0 or c>10:
        return "Lỗi nhập dữ liệu"
    else:
        dtb = (a + b*1.5 + c*2)/4.5
        if dtb>=8:
            return "Loại Giỏi"
        elif dtb>=6.5:
            return "Loại Khá"
        elif dtb>=5:
            return "Loại Trung Bình"
        else:
            return "Loại Yếu"

# B10_ptb2
def ptb2_format(a,b,c):
    '''Xuất ra dạng chuẩn của phương trình bậc 2
    dựa vào tham số a, b, c'''
    if a ==0:
        if b==0:
            print(c) 
        else:
            if b==1:
                b=''
            elif b==-1:
                b = '-'
            if c ==0:
                print('{0}x'.format(b) ) 
            elif c>0:
                print('{0}x + {1}'.format(b, c)) 
            else:
                print('{0}x - {1}'.format(b, -c)) 
    else:
        if a==1:
            a=''
        elif a==-1:
            a='-'
        if b == 0:
            if c == 0:
                print('{0}x^2'.format(a)) 
            elif c>0:
                print('{0}x^2 + {1}'.format(a,c))
            else:
                print('{0}x^2 - {1}'.format(a,-c))
        else:
            if b== 1:
                if c ==0:
                    print('{0}x^2 + x'. format(a))
                elif c>0:
                    print('{0}x^2 + x + {1}'.format(a,c))
                else:
                    print('{0}x^2 + x - {1}'.format(a,-c))
            elif b== -1:
                if c ==0:
                    print('{0}x^2 - x'. format(a))
                elif c>0:
                    print('{0}x^2 - x + {1}'.format(a,c))
                else:
                    print('{0}x^2 - x - {1}'.format(a,-c))
            elif b < -1:
                if c ==0:
                    print('{0}x^2 - {1}x'. format(a,-b))
                elif c>0:
                    print('{0}x^2 - {1}x + {2}'.format(a,-b,c))
                else:
                    print('{0}x^2 - {1}x - {2}'.format(a,-b,-c))
            else:
                if c ==0:
                    print('{0}x^2 + {1}x'. format(a,b))
                elif c>0:
                    print('{0}x^2 + {1}x + {2}'.format(a,b,c))
                else:
                    print('{0}x^2 + {1}x - {2}'.format(a,b,-c))

# B11_fullname
def full_name(hoten):
    '''Xuất ra định dạng tiêu chuẩn của họ tên 1 người
    Ví dụ:  In: '     NguYễn   ThỊ phƯơnG    tHảO         '
            Out: 'Nguyễn Thị Phương Thảo' '''
    hoten = hoten.strip().lower().split()
    fullname = ''

    for i in hoten:
        i = i[0].upper() + i[1:]
        fullname += i + ' '

    return fullname.strip()       

# B11_checkcode
def check_code(code):
    '''Kiểm tra 1 mã vạch có đúng hay không
    Điều kiện: ....'''
    C = int(code[12])
    i = 0
    A, B = 0, 0
    while i<12:
        if i%2 == 0:
            A += int(code[i])
        else:
            B += int(code[i])
        i += 1
    D = A + 3*B
    if D%10 != 0:
        F = 10 - (D%10)
    else:
        F = 0
    if F == C:
        return 'Mã vạch ĐÚNG'
    else:
        return 'Mã vạch SAI'
    
# B11_chuoigiamdan
def max_range_decre(text):
    '''In ra chuỗi số giảm dần dài nhất
    Đầu vào là 1 chuỗi các số liền nhau
    '''
    i = 0
    chuoi = ''
    while i < len(text)-1:
        if int(text[i]) < int(text[i+1]):
            chuoi += text[i] +'-'
        else:
            chuoi += text[i]
        i += 1
    if chuoi[-1] == '-':
        chuoi = chuoi
    else:
        if int(chuoi[-1]) > int(text[-1]):
            chuoi += text[-1]
    chuoi = chuoi.split('-')
    max = 0
    for i in chuoi:
        if len(i) >=max:
            max = len(i)        
    for i in chuoi:
        if len(i) == max:
            print(i)

# B11_checkdiemtrongvung
def check_point_in_area(x,y):
    '''Hàm kiểm tra xem điểm P(x,y) có nằm trong vùng D không
    vùng D giới hạn bởi nửa đường tròng tâm 0,0 bán kính 2 về phí trục x âm
    và 2 đoạn thẳng đi qua các điểm:
    đoạn thẳng 1 đi qua: 0,2 & 6,0
    đoạn thẳng 2 đi qua: 0,-2 & 6,0 '''
    if x < -2 or x > 6 or y < -2 or y > 2:
        print('P không thuộc vùng D')
    elif x >= -2 and x <=0:
        d = (x**2 + y**2)**0.5
        if d <=2:
            print('P thuộc vùng D')
        else:
            print('P không thuộc vùng D')
    else:
        ptd1 = x/3 + y - 2
        ptd2 = -x/3 + y + 2
        if ptd1<=0 and ptd2 >=0:
            print('P thuộc vùng D')
        else:
            print('P không thuộc vùng D') 
# B12_nghiem_gan_dung
def nghiem_gan_dung(a,b,alpha):
    '''Tìm nghiệm gần đúng của phương trình f(x)=e^x + sin(x)
    trong đoạn [a,b] với sai số alpha'''
    import math
    delta = math.fabs(b-a)
    fa = math.exp(a) + math.sin(a)
    fb = math.exp(b) + math.sin(b)
    if fa*fb>0:
        return 'Phương trình không có nghiệm trong đoạn này'
    else:
        while delta > alpha:
            c = (a+b)/2
            fc = math.exp(c) + math.sin(c)
            fa = math.exp(a) + math.sin(a)
            fb = math.exp(b) + math.sin(b)
            if fa*fc < 0:
                b = c
            if fc*fb < 0:
                a = c
            delta = math.fabs(b-a)
        return c            

# B12_bang_cuu_chuong   
def bang_cuu_chuong_nam_ngang(m,n):
    '''Hàm in ra bảng cửu chương nằm ngang của các số từ m đến n'''
    for j in range(1,10):
        for i in range(m,n+1):
            print('{0}*{1}={2}'.format(i,j,i*j),end='\t')
        print()
    
# B13_ve_hinh_sao
def draw_star(n,m):
    '''Hàm vẽ m hình thoi gồm các kí tự *
    n: số kí tự * ở dòng trung tâm hình thoi'''
    if n%2==0:
        n-=1
    for i in range(2*n):
        if i <= n:
            if i%2!=0:
                print((' '*int((n-i)/2) + '*'*i+ ' '*int((n-i+4)/2))*m)
            else:
                print()
        else:
            if i%2!=0:
                print((' '*int((i-n)/2)+'*'*(2*n-i)+' '*int((i-n+4)/2))*m)
            else:
                print()   

# B13_cach_cong_tien              
def money(a,b,c,total):
    '''Hàm đếm số cách cộng tiền các mệnh giá a, b, c
    sao cho tổng bằng total'''
    step = 0
    for i in range(total//a + 1):
        for j in range(total//b + 1):
            for k in range(total//c + 1):
                if i*a + j*b + k*c==total:
                    step+=1
    return step  

# B14_ve_n_ngoi_sao
def draw_n_star(n):
    '''Hàm vẽ ra n ngôi sao và tô màu cho chúng trong turtle'''
    import turtle
    tl = turtle.Turtle()
    tl.shape('turtle')
    tl.speed(20)
    tl.penup()
    tl.backward(30*n)
    tl.pendown()

    for i in range(n):
        tl.fillcolor('yellow')
        tl.begin_fill()
        for j in range(5):
            tl.forward(50)
            tl.right(144)
        tl.end_fill()
        tl.penup()
        tl.forward(60)
        tl.pendown()

    turtle.done()

# B14_fullname_en  
def fullname_en(text):
    '''Hàm chuyển đổi tiếng việt thành tiếng việt không dấu'''
    text = text.lower().strip()
    text2 =''
    for i in text:
        if i in 'áàảãạâấầẩẫậăắằẳẵạ':
            i = 'a'
        elif i in 'íìỉĩị':
            i = 'i'
        elif i in 'éèẻẽẹêếềểễệ':
            i = 'e'
        elif i in 'úùủũụưứừửữự':
            i = 'u'
        elif i in 'óòỏõọơớờởỡợôốồổỗộ':
            i = 'o'
        elif i in 'đ':
            i = 'd'
        text2 += i
    text2 = text2.split()
    fullname = ''
    for i in text2:
        i = i[0].upper() + i[1:]
        fullname += i + ' '
    return fullname.strip()      