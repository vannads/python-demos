import datetime


def print_header():
    print("------------------------------------")
    print("            BIRTHDAY APP")
    print("------------------------------------")


def get_birthday_from_user():
    byear = int(input("Enter your YEAR of birth : "))
    bmonth = int(input("Enter your MONTH of birth : "))
    bdate = int(input("Enter your DAY of birth : "))
    return datetime.datetime(byear, bmonth, bdate)


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days


def print_birthday_information(days):
    if days < 0:
        print("Your birthday was {} days ago.".format(-days))
    elif days > 0:
        print("Your birthday will be in {} days.".format(days))
    else:
        print("Happy Birthday!")
    pass


def main():
    print_header()
    birthday = get_birthday_from_user()
    today = datetime.date.today()
    days = compute_days_between_dates(birthday, today)
    print_birthday_information(days)


main()
