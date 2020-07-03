import random

a = []

def FillArray1(a):   #随机生成数组的样本数据
    for i in range(20):
        a.append(random.randint(0,100))

def FillArray2(a):   #生成等差数组的样本数据
    a1 = int(input('请输入首项：'))
    d = int(input('请输入公差：'))
    for i in range(20):
        a.append(a1 + i*d)

def Insert(a):   #在数组下标处插入新元素
    an = int(input('要插入在第几项？请输入：'))
    n = int(input('要插入的元素的值是多少？请输入：'))
    if an <= len(a) + 1:
        a.insert(an-1, n)
    else:
        print('输入错误！返回至前一步。')

def DeleteID(a): #删除指定下标的元素
    an = int(input('要删除第几项？请输入：'))
    if an <= len(a):
        del a[an-1]
    else:
        print('输入错误！返回至前一步。')

def DeleteValue(a):  #删除指定值的元素（全部删除）
    n = int(input('要删除的元素的值是多少？请输入：'))
    while True:
        try:
            a.remove(n)
        except:
            break

def DeleteRange(a):  #删除指定区间的元素（双闭）
    s = int(input('输入区间下限（最前项）：'))
    t = int(input('输入区间下限（最后项）：'))
    if s >= 1 and t <= len(a):
        for i in range(t-s+1):
            del a[s-1]  #数组长度是动态变化的，删除第s-1项时，原来的第s项会变成第s-1项，此时再删除“第s项”，实际上会删除第s+1项，所以这里只需固定删除第s-1项
    else:
        print('输入错误！返回至前一步。')

def isAsc(a):    #判断数组是否升序排列，返回判断值
    for i in range(1,len(a)):
        if a[i-1] > a[i]:
            return 0
    else:
        return 1

def isDesc(a):   #判断数组是否降序排列，返回判断值
    for i in range(1,len(a)):
        if a[i-1] < a[i]:
            return 0
    else:
        return 1

def isEqual(a):  #判断数组元素是否全相等，返回判断值
    for i in range(1,len(a)):
        if a[i-1] != a[i]:
            return 0
    else:
        return 1

def Average(a):  #计算数组平均值，并返回该值
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    aver = sum/len(a)
    return aver

def BubbleSort(a):   #冒泡排序（默认按升序），数组不变
    while isAsc(a) != 1:
        for i in range(1,len(a)):
            if a[i-1] > a[i]:
                a[i-1], a[i] = a[i], a[i-1]

def SelectSort(a):   #选择排序（默认按升序），排序后返回已排序的新数组
    arr = []
    while len(a) > 0:
        arr.append(min(a))
        a.remove(min(a))
    return arr

def OrderInsert(a):  #在有序数组中插入新元素并保持有序性
    n = int(input('请输入要插入的值：'))
    if isEqual(a) == 1:
        if a[0] != n:
            print('原数组为全等数组，有序性已被破坏！已将要插入的值放在最后一位。')
            a.append(n)
    elif isAsc(a) == 1:
        a.append(n)
        BubbleSort(a)
    elif isDesc(a) == 1:
        a.append(n)
        BubbleSort(a)
        a.reverse()
    else:
        print('原数组不具有有序性，插入值后默认按升序排列。')
        a.append(n)
        BubbleSort(a)

def Search(a):   #普通查找，找到返回下标，否则返回0
    arr = []
    n = int(input('请输入需要查找的值：'))
    for i in range(len(a)):
        if a[i] == n:
            arr.append(i+1)
    if len(arr) == 0:
        return 0
    else:
        return arr

def BiSearch(a): #二分查找（要求数组有序），找到返回下标，否则返回0
    low, high = 0, len(a)
    n = int(input('请输入需要查找的值：'))
    if isAsc(a) == 1 or isDesc(a) == 1:
        if (low + high)%2 == 0:
            while low <= high:
                mid = int((low + high)/2)
                if n == a[mid]:
                    return mid+1
                elif n > a[mid]:
                    low = mid + 1
                elif n < a[mid]:
                    high = mid - 1
            else:
                return 0
        else:
            if n == a[len(a)-1]:
                return len(a)-1
            else:
                high = len(a)-1
                while low <= high:
                    mid = int((low + high)/2)
                    if n == a[mid]:
                        return mid+1
                    elif n > a[mid]:
                        low = mid + 1
                    elif n < a[mid]:
                        high = mid +1
                else:
                    return 0
    elif isEqual(a) == 1:
        if a[0] == n:
            print('数组内全是你要找的值。')
        else:
            return 0
    else:
        print('二分查找要求数组有序！请排序后再使用二分查找。')
        return 0

if __name__ == "__main__":
    while True:
        key0 = int(input('0、退出\n1、生成样本数据\n2、显示数组\n3、删除\n4、插入\n5、统计\n6、查找\n7、判断\n8、排列数组元素\n9、清空数组\n请选择0～9：'))
        if 0 <= key0 <= 9:
            if key0 == 0:
                break

            elif key0 == 1:
                key1 = int(input('请选择生成样本数据的方式：\n（1）生成随机数组\n（2）生成等差数组\n或按“0”键返回\n'))
                if key1 == 0:
                    continue
                elif key1 == 1:
                    FillArray1(a)
                elif key1 == 2:
                    FillArray2(a)
                else:
                    print('输入错误！返回至主菜单......')

            elif key0 == 2:
                print('样本数据如下：', a)

            elif key0 == 3:
                key3 = int(input('请选择删除方式：\n（1）删除指定下标的元素\n（2）删除指定值的元素\n（3）删除按指定下标区间（闭区间）的一组元素\n或按“0”返回\n'))
                if key3 == 0:
                    continue
                elif key3 == 1:
                    DeleteID(a)
                elif key3 == 2:
                    DeleteValue(a)
                elif key3 == 3:
                    DeleteRange(a)
                else:
                    print('输入错误！返回至主菜单......')

            elif key0 == 4:
                key4 = int(input('请选择插入方式：\n（1）按指定下标位置插入新元素\n（2）在有序数组中插入新元素\n或按“0”返回\n'))
                if key4 == 0:
                    continue
                elif key4 == 1:
                    Insert(a)
                elif key4 == 2:
                    OrderInsert(a)
                else:
                    print('输入错误！返回至主菜单......')

            elif key0 == 5:
                key5 = int(input('请选择统计方式：\n（1）求最大值\n（2）求最小值\n（3）求平均值\n或按“0”返回\n'))
                
                if key5 == 0:
                    continue
                elif key5 == 1:
                    print('最大值为：',max(a))
                elif key5 == 2:
                    print('最小值为：',min(a))
                elif key5 == 3:
                    print('平均值为：',Average(a))
                else:
                    print('输入错误！返回至主菜单......')

            elif key0 == 6:
                key6 = int(input('请选择查找方式：\n（1）普通查找\n（2）二分查找\n或按“0”返回\n'))
                if key6 == 0:
                    continue
                elif key6 == 1:
                    val = Search(a)
                    if val == 0:
                        print('未找到！')
                    else:
                        print('所查找的值的下标为：', val)
                elif key6 == 2:
                    val = BiSearch(a)
                    if val == 0:
                        print('未找到！')
                    else:
                        print('所查找的值的下标为：', val)
                else:
                    print('输入错误！返回至主菜单......')

            elif key0 == 7:
                key7 = int(input('请选择判断方式：\n（1）是否升序排列\n（2）是否降序排列\n（3）是否全部相等\n或按“0”返回\n'))
                if key7 == 0:
                    continue
                elif key7 == 1:
                    if isAsc(a) == 1:
                        print('该数组按照升序排列。')
                    else:
                        print('该数组不按升序排列。')
                elif key7 == 2:
                    if isDesc(a) == 1:
                        print('该数组按照降序排列。')
                    else:
                        print('该数组不按降序排列。')
                elif key7 == 3:
                    if isEqual(a) == 1:
                        print('数组元素全都相等。')
                    else:
                        print('数组元素不全相等。')
                else:
                    print('输入错误！返回至主菜单......')

            elif key0 == 8:
                key8 = int(input('请选择排列方式：\n（1）冒泡法排序\n（2）选择法排序\n（3）数组逆置\n或按“0”返回\n'))
                if key8 == 0:
                    continue
                elif key8 == 1:
                    BubbleSort(a)
                elif key8 == 2:
                    a = SelectSort(a)
                elif key8 == 3:
                    a.reverse()
                else:
                    print('输入错误！返回至主菜单......')
            
            elif key0 == 9:
                a.clear()

            else:
                print('输入错误！返回至主菜单......')
        else:
            print('输入错误！请重新输入：')
    print('感谢使用，再见！')