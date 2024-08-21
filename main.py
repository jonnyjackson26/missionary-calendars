
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

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import calendar

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

def create_two_year_calendar(start_year):
    # Create a canvas for a letter-sized PDF
    c = canvas.Canvas("two_year_calendar.pdf", pagesize=letter)

    # Loop through the two years
    for year in range(start_year, start_year + 2):
        for month in range(1, 13):
            draw_month(c, year, month)
            c.showPage()  # Create a new page after each month

    # Save the PDF
    c.save()

# Generate the calendar for the years 2024 and 2025
create_two_year_calendar(2024)
