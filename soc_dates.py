import datetime
import random
import holidays

us_holidays = holidays.UnitedStates()

def gen_20_days(mycounter):
    try:
        while mycounter < 20:
            miso = random.randint(0, int(mylimit))
            test_date = (mydates[miso].strftime("%m-%d-%Y") in us_holidays)
            if test_date is True:
                print "Encountered a Holiday (%s) - Please re-run module!" % mydates[miso].strftime("%m-%d-%Y")
            else:
                print mydates[miso].strftime("%m-%d-%Y")
                mycounter += 1
    except:
        gen_20_days(0)

def gen_5_days(mycounter):
    try:
        while mycounter < 5:
            miso = random.randint(0, int(mylimit))
            test_date = (mydates[miso].strftime("%m-%d-%Y") in us_holidays)
            if test_date is True:
                print "Encountered a Holiday (%s) - Please re-run module!" % mydates[miso].strftime("%m-%d-%Y")
            else:
                print mydates[miso].strftime("%m-%d-%Y")
                mycounter += 1
    except:
        gen_5_days(0)

def gen_weeks(mycounter):
    try:
        while mycounter < 5:
            miso = random.randint(0, int(mylimit))
            date1 = mydates[miso].strftime("%m-%d-%Y")
            m = int(miso) + 7
            date2 = mydates[m].strftime("%m-%d-%Y")
            print(date1 + " - " + date2)
            mycounter += 1
    except:
        gen_weeks(0)

def gen_months():
    try:
        global month1
        miso = random.randint(0, int(mylimit))
        month1 = mydates[miso].strftime("%m")
        year1 = mydates[miso].strftime("%Y")
        if month1 == "01":
            month1 = "January "
        elif month1 == "02":
            month1 = "February "
        elif month1 == "03":
            month1 = "March "
        elif month1 == "04":
            month1 = "April "
        elif month1 == "05":
            month1 = "May "
        elif month1 == "06":
            month1 = "June "
        elif month1 == "07":
            month1 = "July "
        elif month1 == "08":
            month1 = "August "
        elif month1 == "09":
            month1 = "September "
        elif month1 == "10":
            month1 = "October "
        elif month1 == "11":
            month1 = "November "
        else:
            month1 = "December"
        return month1 + year1
    except:
        gen_months()

def gen_quarter():
    try:
        global quarter
        miso = random.randint(0, int(mylimit))
        month1 = mydates[miso].strftime("%m")
        year1 = mydates[miso].strftime("%Y")
        if month1 == "01" or month1 == "02" or month1 == "03":
            quarter = "Q1 " + year1
        elif month1 == "04" or month1 == "05" or month1 == "06":
            quarter = "Q2 " + year1
        elif month1 == "07" or month1 == "08" or month1 == "09":
            quarter = "Q3 " + year1
        else:
            quarter = "Q4 " + year1
        return quarter
    except:
        gen_quarter()

def get_vars(soc_start, soc_end):
    try:
        global mylimit
        global mydates

        start = datetime.datetime.strptime(soc_start, "%m-%d-%Y")
        end = datetime.datetime.strptime(soc_end, "%m-%d-%Y")
        date_array = (start + datetime.timedelta(days=x) for x in range(0, (end - start).days))
        mylimit = (end - start).days
        mydates = []

        for date_object in date_array:
            mydates.append(date_object)
        print "Generating 20 random days"
        gen_20_days(0)
        print ""
        print "Generating 5 additional random days"
        gen_5_days(0)
        print ""
        print "Generating 5 random weeks"
        gen_weeks(0)
        print ""
        print "Generating 2 random months"
        m = gen_months()
        mm = gen_months()
        if m == mm:
            print "Oops! We picked the same  month/year...Please re-run module"
        else:
            print m
            print mm
        print ""
        print "Generating 2 random quarters"
        q = gen_quarter()
        qq = gen_quarter()
        if q == qq:
            print "Oops! We picked the same quarter/year...Please re-run module"
        else:
            print q
            print qq
        print ""
    except:
        print("""
        
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!        
Something has gone wrong - you might have entered an improper date!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
        """)
