from datetime import datetime

# Khrihfabu events
events = [
    {
        "name": "CC Level Retreat",
        "begin": "2025-08-01 00:00:00",
        "end": "2025-08-01 11:00:00",
        "description": "Kan dihlak kal khawh i zuam hna usih",
        "location": "A hmun cu kal lai ah thanh a si te lai"
    },
    {
        "name": "CC Level Retreat",
        "begin": "2025-08-01 00:00:00",
        "end": "2025-08-01 11:00:00",
        "description": "Kan dihlak kal khawh i zuam hna usih",
        "location": "A hmun cu kal lai ah thanh a si te lai"
    },
    {
        "name": "CC Level Retreat",
        "begin": "2025-08-01 00:00:00",
        "end": "2025-08-01 11:00:00",
        "description": "Kan dihlak kal khawh i zuam hna usih",
        "location": "A hmun cu kal lai ah thanh a si te lai"
    },
    {
        "name": "CC Level Retreat",
        "begin": "2025-08-01 00:00:00",
        "end": "2025-08-01 11:00:00",
        "description": "Kan dihlak kal khawh i zuam hna usih",
        "location": "A hmun cu kal lai ah thanh a si te lai"
    },
    {
        "name": "CC Level Retreat",
        "begin": "2025-08-01 00:00:00",
        "end": "2025-08-01 11:00:00",
        "description": "Kan dihlak kal khawh i zuam hna usih",
        "location": "A hmun cu kal lai ah thanh a si te lai"
    },
    {
        "name": "CC Level Retreat",
        "begin": "2025-08-01 00:00:00",
        "end": "2025-08-01 11:00:00",
        "description": "Kan dihlak kal khawh i zuam hna usih",
        "location": "A hmun cu kal lai ah thanh a si te lai"
    },
    {
        "name": "CC Level Retreat",
        "begin": "2025-08-01 00:00:00",
        "end": "2025-08-01 11:00:00",
        "description": "Kan dihlak kal khawh i zuam hna usih",
        "location": "A hmun cu kal lai ah thanh a si te lai"
    },
    {
        "name": "CC Level Retreat",
        "begin": "2025-08-01 00:00:00",
        "end": "2025-08-01 11:00:00",
        "description": "Kan dihlak kal khawh i zuam hna usih",
        "location": "A hmun cu kal lai ah thanh a si te lai"
    },
    {
        "name": "CC Level Retreat",
        "begin": "2025-08-01 00:00:00",
        "end": "2025-08-01 11:00:00",
        "description": "Kan dihlak kal khawh i zuam hna usih",
        "location": "A hmun cu kal lai ah thanh a si te lai"
    },
    {
        "name": "CC Level Retreat",
        "begin": "2025-08-01 00:00:00",
        "end": "2025-08-01 11:00:00",
        "description": "Kan dihlak kal khawh i zuam hna usih",
        "location": "A hmun cu kal lai ah thanh a si te lai"
    },
    {
        "name": "CC Level Retreat",
        "begin": "2025-08-01 00:00:00",
        "end": "2025-08-01 11:00:00",
        "description": "Kan dihlak kal khawh i zuam hna usih",
        "location": "A hmun cu kal lai ah thanh a si te lai"
    },
    {
        "name": "CC Level Retreat",
        "begin": "2025-08-01 00:00:00",
        "end": "2025-08-01 11:00:00",
        "description": "Kan dihlak kal khawh i zuam hna usih",
        "location": "A hmun cu kal lai ah thanh a si te lai"
    },
    {
        "name": "CC Level Retreat",
        "begin": "2025-08-01 00:00:00",
        "end": "2025-08-01 11:00:00",
        "description": "Kan dihlak kal khawh i zuam hna usih",
        "location": "A hmun cu kal lai ah thanh a si te lai"
    }
]

# Function to format datetime to ICS format
def format_datetime(dt_str):
    return datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S").strftime("%Y%m%dT%H%M%S")

# Create ICS content
ics_content = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//Sample Calendar//EN\n"
for e in events:
    ics_content += "BEGIN:VEVENT\n"
    ics_content += f"SUMMARY:{e['name']}\n"
    ics_content += f"DTSTART:{format_datetime(e['begin'])}\n"
    ics_content += f"DTEND:{format_datetime(e['end'])}\n"
    ics_content += f"DESCRIPTION:{e['description']}\n"
    ics_content += f"LOCATION:{e['location']}\n"
    ics_content += "BEGIN:VALARM\n"
    ics_content += "TRIGGER:-P1D\n"  # One day before
    ics_content += "ACTION:DISPLAY\n"
    ics_content += "DESCRIPTION:Reminder\n"
    ics_content += "END:VALARM\n"
    ics_content += "END:VEVENT\n"
ics_content += "END:VCALENDAR"

# Write to .ics file
with open("events_with_alerts.ics", "w") as f:
    f.write(ics_content)

print("ICS calendar file 'events_with_alerts.ics' with one-day alerts has been created successfully.")
