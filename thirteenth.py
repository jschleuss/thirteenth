import datetime

# finds current year and starts the ticker there
today = datetime.datetime.today()
current_year = today.year
year = current_year

# for next 100 years
for year in range(current_year, current_year+101):
	for day in range(1,13):
		if datetime.datetime(year,day,13).weekday() == 4:
			# prints dates with Friday the 13th
			print datetime.datetime(year,day,13).strftime("%m/%d/%y")