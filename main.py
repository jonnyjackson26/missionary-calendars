from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import calendar
from datetime import datetime, timedelta
import os

class ImportantDate:
    def __init__(self, month, day, text):
        self.month = month
        self.day = day
        self.text = text


importantDates = [
    ImportantDate(9, 26, "Jonny's birthday"),
    ImportantDate(1, 13, "Jessy's birthday"),
    ImportantDate(1, 16, "Dad's birthday"),
    ImportantDate(8, 27, "Jacobs's birthday"),
    ImportantDate(8, 15, "Gloria's birthday"),
    ImportantDate(12, 26, "Christmas"),
    ImportantDate(10, 27, "Thanksgiving"),
    ImportantDate(2, 13, "Valentines Day"),
    ImportantDate(7, 4, "Fouth of July"),
    ImportantDate(7, 3, "Mom's birthday"),
]

# Missionary details
missionaryName = "Jonathan Jackson"
missionName = "Dominican Republic, Santo Domingo West Mission"
isElder = False
startDate = datetime(2024, 10, 1)  # October 2024 (year, month, day)


# Directory containing images
pics_folder = 'pics'

def draw_month(c, year, month):
    # Calculate margins and grid dimensions
    page_width, page_height = landscape(letter)
    left_margin = 0.5 * inch
    right_margin = 0.5 * inch
    top_margin = 1.5 * inch  # Top margin for month title
    days_of_week_margin = 0.5 * inch  # Margin between days of the week and the grid
    bottom_margin = 1 * inch
    
    # Dimensions for the grid
    grid_width = page_width - left_margin - right_margin
    grid_height = page_height - top_margin - bottom_margin - days_of_week_margin
    
    cell_width = grid_width / 7
    cell_height = grid_height / 6
    
    # Set font and draw the month title
    c.setFont("Helvetica-Bold", 24)
    title = f"{calendar.month_name[month]} {year}"
    title_width = c.stringWidth(title, "Helvetica-Bold", 24)
    c.drawString((page_width - title_width) / 2, page_height - top_margin + 0.5 * inch, title)

    # Get the month's calendar as a matrix
    month_cal = calendar.monthcalendar(year, month)
    num_weeks = len(month_cal)  # Get the number of weeks in the month

    # Set font for the days of the week
    c.setFont("Helvetica", 12)

    # Draw the days of the week
    days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
    days_of_week_y = page_height - top_margin - 0.1 * inch  # Position below the month title

    for i, day in enumerate(days):
        c.drawString(left_margin + i * cell_width + (cell_width - c.stringWidth(day, "Helvetica", 12)) / 2, 
                     days_of_week_y, day)

    # Draw the grid and numbers for the days of the month
    for week in range(num_weeks):  # Use the actual number of weeks
        for day in range(7):
            x = left_margin + day * cell_width
            y = page_height - top_margin - (week + 1) * cell_height - days_of_week_margin
            
            # Draw the border for each day
            c.rect(x, y, cell_width, cell_height)
            
            # Add the day number in the top left of each box
            if month_cal[week][day] != 0:
                day_number = str(month_cal[week][day])
                c.drawString(x + 0.1 * inch, y + cell_height - 0.2 * inch, day_number)
                
                # Draw important dates text if it matches
                for important_date in importantDates:
                    if important_date.month == month and important_date.day == month_cal[week][day]:
                        c.setFont("Helvetica-Oblique", 8)
                        c.drawString(x + 0.1 * inch, y + cell_height / 2, important_date.text)
                        c.setFont("Helvetica", 12)  # Reset font after drawing important dates



def add_image_page(c, image_path):
    c.drawImage(image_path, 0, 0, width=letter[1], height=letter[0])  # Draw the image full-page in landscape
    c.showPage()  # End the image page

def create_mission_calendar():
    # Determine calendar duration
    endDate = startDate + timedelta(days=2 * 365) if isElder else startDate + timedelta(days=18 * 30)

    # Determine the title based on Elder/Sister
    title_prefix = "Elder" if isElder else "Sister"
    cal_name = f"{title_prefix} {missionaryName}'s Mission Calendar"
    c = canvas.Canvas(f"{cal_name}.pdf", pagesize=landscape(letter))

    current_date = startDate
    image_files = sorted([f for f in os.listdir(pics_folder) if os.path.isfile(os.path.join(pics_folder, f))])
    image_index = 0

    add_image = True  # Start with an image page

    while current_date <= endDate:
        if add_image:
            # Add a full-page image
            if image_index < len(image_files):
                image_path = os.path.join(pics_folder, image_files[image_index])
                add_image_page(c, image_path)
                image_index += 1
        else:
            # Draw the month calendar
            draw_month(c, current_date.year, current_date.month)
            # Ensure to show page after adding a month
            c.showPage()
            # Move to the next month
            if current_date.month == 12:
                current_date = datetime(current_date.year + 1, 1, 1)
            else:
                current_date = datetime(current_date.year, current_date.month + 1, 1)

        # Toggle between image and month
        add_image = not add_image

    c.save()

# Generate the calendar with images
create_mission_calendar()
