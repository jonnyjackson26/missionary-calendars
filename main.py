from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import calendar
from datetime import datetime

def notes():
    pass
    #is your missionary an elder or a sister?
        #2 year or 18 month calendar

    #what is the name of the mission? 
        #can know country specific holidays
        #to put on the front of the calendar

    #when is your missionaires mtc start date?
    #when is your missionaires arrive in field date?
    #when is your missionaires schedueled relase date?

    #input important events you'd like on the calendar: (birthdays)

    #checkboxes for holidays (christmas, halloween, etc)

    #input 50 pictures 
        #can have ai choose where to put them so they look good

    #choose first day of week
    #choose language
missionaryName="Jonathan Jackson"
missionName="Dominican Republic, Santo Domingo West Mission"
isElder=True
startDate = datetime(2024, 10, 1) #October 2024 (year, month, day)



def draw_month(c, year, month):
    # Set font and draw the month title
    c.setFont("Helvetica-Bold", 24)
    c.drawString(3 * inch, 10 * inch, f"{calendar.month_name[month]} {year}")

    # Get the month's calendar as a matrix
    month_cal = calendar.monthcalendar(year, month)

    # Set font for the days
    c.setFont("Helvetica", 12)

    # Draw the days of the week
    days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
    for i, day in enumerate(days):
        c.drawString(0.75 * inch + i * inch, 9 * inch, day)

    # Draw the days of the month
    for week in range(len(month_cal)):
        for day in range(len(month_cal[week])):
            if month_cal[week][day] != 0:
                c.drawString(0.75 * inch + day * inch, 8.5 * inch - week * inch, str(month_cal[week][day]))


def create_two_year_calendar(startDate):
    title_prefix = "Elder" if isElder else "Sister"
    cal_name = f"{title_prefix} {missionaryName}'s Mission Calendar"
    c = canvas.Canvas(f"{cal_name}.pdf", pagesize=letter)     # Create a canvas for a letter-sized PDF

    start_year = startDate.year
    start_month = startDate.month

    # Loop through two years starting from the given start date
    for year in range(start_year, start_year + 2):
        for month in range(start_month, 13):
            draw_month(c, year, month)
            c.showPage()  # Create a new page after each month

        start_month = 1  # Reset to January after the first year
    c.save()


# Generate the calendar for the years 2024 and 2025
create_two_year_calendar(startDate)
