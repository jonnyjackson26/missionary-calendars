from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import calendar
from datetime import datetime, timedelta

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
isElder=False
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

    # Grid layout variables
    top_margin = 8.5 * inch
    left_margin = 0.75 * inch
    cell_width = inch
    cell_height = inch
    num_weeks = len(month_cal)

    # Draw the grid and numbers for the days of the month
    for week in range(num_weeks):
        for day in range(7):
            x = left_margin + day * cell_width
            y = top_margin - week * cell_height

            # Draw the border for each day
            c.rect(x, y - cell_height, cell_width, cell_height)

            # Add the day number in the top left of each box
            if month_cal[week][day] != 0:
                c.drawString(x + 0.1 * inch, y - 0.2 * inch, str(month_cal[week][day]))



def create_mission_calendar():
    # Determine calendar duration
    endDate = startDate + timedelta(days=2 * 365) if isElder else startDate + timedelta(days=18 * 30)

    # Determine the title based on Elder/Sister
    title_prefix = "Elder" if isElder else "Sister"
    cal_name = f"{title_prefix} {missionaryName}'s Mission Calendar"
    c = canvas.Canvas(f"{cal_name}.pdf", pagesize=letter)

    current_date = startDate
    while current_date <= endDate:
        draw_month(c, current_date.year, current_date.month)
        c.showPage()  # Create a new page after each month
        # Move to the next month
        if current_date.month == 12:
            current_date = datetime(current_date.year + 1, 1, 1)
        else:
            current_date = datetime(current_date.year, current_date.month + 1, 1)

    c.save()


# Generate the calendar for the years 2024 and 2025
create_mission_calendar()
