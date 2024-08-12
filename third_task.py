from datetime import datetime


def date_dif(dat1, dat2):
    date1 = datetime.strptime(dat1, '%m/%d/%Y')
    date2 = datetime.strptime(dat2, '%m/%d/%Y')
    num_days = (date2 - date1).days
    result_days = num_days if num_days > 0 else - num_days
    return print(f"Разница введенных дат в днях составляет: {result_days} ")


date_dif('01/11/2011', '04/21/2024')
date_dif('01/11/2051', '04/21/2011')