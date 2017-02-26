import calendar

DAY_NAMES = ["Po", "Ut", "St", "Št", "Pi", "So", "Ne"]
MONTH_NAMES = ["Január", "Február", "Marec", "Apríl", "Máj", "Jún", "Júl", "August", "September", "Október", "November", "December"]
FREE_DAYS = [(1,1), (1,6), (4, 14), (4, 17), (5, 1), (5, 8), (6, 5), (8, 29), (9, 1), (9, 15), (11, 1), (11, 17), (12, 24), (12, 25), (12, 26)]

def write_year(year,f):
    f.write("<h1>" + str(year) + "</h1>\n")
    f.write('<div class="all-months">\n')
    for month in range(1,13):
        f.write('<div class="month">\n')
        f.write("<h2>" + (MONTH_NAMES[month-1]) + "</h2>\n")
        write_month(year, month, f)
        f.write('</div>\n')
    f.write('</div>\n')
        
def write_month(year, month, f):
    cal = calendar.monthcalendar(year, month)
    
    f.write("<table>\n")
    
    for weekday in range(7):
        if weekday == 6:
            f.write('    <tr class="sundays">')
        else: 
            f.write("    <tr>")
           
        f.write("<th>")
        f.write(DAY_NAMES[weekday])
        f.write("</th>")
       
        for week in cal:
            day = week[weekday]
            if day == 0:               
                f.write('<td> </td>')
#            else:
#                is_free_day = False
#                for e in FREE_DAYS:
#                    if e == (month, day):
#                        f.write('<td class="free-day">' + str(day) + "</td>")
#                        is_free_day = True
#                if not is_free_day:
#                    f.write("<td>" + str(day) + "</td>")    
            else:
                if (month, day) in FREE_DAYS:
                    f.write('<td class="free-day">' + str(day) + "</td>")
                else:
                    f.write('<td>' + str(day) + '</td>')
            
        f.write("</tr>\n")
    f.write("</table>\n")
        
f = open("kalendar.html", "w")
f.write('<meta charset="utf-8">\n')
f.write('<link rel="stylesheet" href="kalendar.css">\n')
f.write('<meta name="viewport" content="width=device-width, initial-scale=1">')
f.write('<link href="https://fonts.googleapis.com/css?family=Raleway:300,700,900" rel="stylesheet">\n')


write_year(2017,f)
f.close()

