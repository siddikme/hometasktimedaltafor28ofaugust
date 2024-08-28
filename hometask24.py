# 1.
# from datetime import datetime
# def main(date):
#     if date.month == 10 and date.day == 31:
#         return "Bonfire toffee"
#     else:
#         return "toffee"
# print(main(datetime.strptime("2013/10/31", "%Y/%m/%d")))
# print(main(datetime.strptime("2012/07/31", "%Y/%m/%d")))
# print(main(datetime.strptime("2011/10/12", "%Y/%m/%d")))
# solved:




# 2.
# def func(a):
#     return (a + 99) // 100
# print(func(2005))  # 21
# print(func(1950))  # 20
# print(func(1900))  # 19
# solved:




# 3.
# def func(a, b):
#     if a == "" :
#         return "year missing"
#     if b == "" :
#         return "month missing"
#     s = b // 12
#     return a + s
# print(func(2020, 24))
# print(func(1832, 2)) 
# print(func(1444, 60))
# print(func("", 24))  
# print(func(2020, ""))
# solved:




# 4.
# def func(a):
#     month, day, year = a.split('/')
#     s = f"{year}{day}{month}"
#     return s
# print(func("11/12/2019"))
# print(func("12/31/2019"))
# solved:



# 5.
# from datetime import date
# def func(a):
#     return a.month == 12 and a.day == 24
# print(func(date(2013, 12, 24)))
# print(func(date(2013, 12, 23)))
# print(func(date(3000, 12, 24)))
# solved:


# 6.
# from datetime import datetime
# def func(a):
#     a = datetime.strptime(a, '%m/%d/%Y')
#     b = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#     c = (a.weekday() + 1) % 7
#     return b[c]
# print(func("12/07/2016")) 
# print(func("09/04/2016")) 
# print(func("12/08/2011"))
# solved: