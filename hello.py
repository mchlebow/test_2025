def say_hello(name):
    print("Hello, " + name)

say_hello("VS Code")

from datetime import date

def say_day_of_week(date_obj):
    day_of_week = date_obj.strftime("%A")
    print("Today is " + day_of_week)

say_day_of_week(date.today())
