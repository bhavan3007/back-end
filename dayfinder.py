
def cal_year (year):
    if 1600<year<2000:
        year=year-1600
    elif 2000<=year<2400:
        year=year-2000
    year=year-1
    remyear=(year%100)
    remyear1=(((remyear//4)*2)+(remyear-(remyear//4)))%7
    hund=(year//100)*100
    value={100:5,200:3,300:1,400:0}
    maped=value.get(hund,0)
    final=maped + remyear1
    return final

def cal_month(year,month):
    month_value={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        month_value[2] = 29
    days= sum(month_value[m] for m in range(1, month))
    return days

def cal_date(year,month,date):
    days_in_month = cal_month(year, month) + date
    total_days = days_in_month % 7
    return total_days


def result(year,month,date):
    day_value={0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thrusday",5:"Friday",6:"Saturday"}
    final_year = cal_year(year)
    date_is = cal_date(year, month, date)
    output = (final_year + date_is) % 7
    final_output= day_value.get(output)
    return final_output



    



    