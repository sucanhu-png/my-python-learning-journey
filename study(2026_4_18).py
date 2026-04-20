# # #print(type(2))
# # string_type = type("黑马程序员")
# # print(string_type)
# # int_type = type(123)
# # print(int_type)
# # float_type = type(3.14)
# # print(float_type)
# # name = "黑马程序员"
# # print(type(name)
# # name = str(123)
# # print(type(name),name)
# # num3 = int("黑马程序员")
# # print(type(num3),num3)
# # int_num = int(11.634)
# # print(type(int_num), int_num)
# #变量的名字，方法的名字，类的名字，统一称为标识符
# #内容限定：英文，中文，数字，下划线（不推荐使用 中文，数字不可以开头，区分大小写，不可使用关键字）
# #first_number = 1
# # print("1 + 1 = ", 1 + 1)
# # print(10//4)
# # print(10 % 4)
# # """我是黑马程序员  """
# # print("\"黑马程序员\"")
# #可以通过占位的方式完成数字和字符串的拼接
# # name = 3
# # message = "学IT就来%s" %name
# # print(message)
# # class_num = 57
# # avg_salary = 10000.23
# # message = "Python大数据学科： 北京%d期，毕业生平均工资：%f"%(class_num,avg_salary)
# # print(message)
# # insert = 23.55555
# # print("the number is:%7.2f"%insert)
# # print(" ")
# name = "船只博客"
# set_up_year = 2006
# stock_price = 19.99
# print(f"我是{name},我成立于：{set_up_year},我今天的股票价格是{stock_price}")
# print(f"1*1的结果是：{1 * 2}")
# print("字符串在python中的类型名是：%s"%type("字符串"))
# name = "传智博客"
# stock_price = 19.99
# stock_code = "003032"
# daily_growth = 1.2
# growth_days = 7
# sum = stock_price*daily_growth**growth_days
# print(f"公司：{name},股票代码：{stock_code},当前股价：{stock_price}"+"每日增长系数%3.1f,经过%s天的增长后，股价达到了：%5.2f"%(daily_growth,growth_days,sum))
# name = input("请输入你是谁")
# print("我知道了，你是：%s"%name)
# num = input("请告诉我你的银行卡密码")
#
# print("你的银行卡密码类型是： %s" % type(num))
# change = int(num)
# bool_1 = True
# bool_2 = False
# print(f"bool_1: {bool_1}，类型是{type(bool_1)}")
# print(f"bool_2: {bool_2}，类型是{type(bool_2)}")
# num1 = 10
# num2 = 20
# print(f"num1与num2的比较结果是：{num1 == num2} ")
# age = 30
# if age >= 18:
#     print("mature")
# else:
#     print("not mature")
# print("Are you a kid?")
# print("欢迎来到黑马儿童乐园，儿童免费，成人收费")
# age = input("请输入年龄： ")
# age = int(age)
# if 100 >= age >= 18:
#     print("你已成年，游玩需要补票10元")
# elif 0 < age < 18:
#     print("请进吧小朋友")
# else:
#     print("输入的年龄非法")
# height = int(input("请输入你的身高（cm）： "))
# if height >= 120:
#     print("您的身高超出120cm，需要购票十元。\n祝您游玩愉快！")
# else:
#     print("您的身高超出120cm，可以免费游玩。\n 祝您游玩愉快！")
# if int(input("请输入你的身高（cm）")) <120:
#     print("可以免费")
# elif int(input("vip级别大于三")) >3:
#     print("1")
import random
num = random.randint(1,10)
guess_num = int(input("请输入你要猜的数字： "))

if guess_num == num:
    print("猜对")
else:
    if num > guess_num:
        print("往大了猜")
    else :
        print("往小了猜")


