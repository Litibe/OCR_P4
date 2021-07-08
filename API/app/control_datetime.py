import datetime

from API import constants


def create_datetime_now():
    date_now = datetime.datetime.now(constants.TIME_ZONE)
    # date = date_now.strftime('%d/%m/%Y %H:%M:%S')
    date = date_now.strftime('%d/%m/%Y')
    date = datetime.datetime.strptime(date, '%d/%m/%Y')
    hours = date_now.strftime("%H:%M")
    return date, hours


if __name__ == "__main__":
    print(create_datetime_now())
