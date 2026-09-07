from datetime import datetime

def find_peak_usage(logs):
    hours = [0] * 24

    for log in logs:
        time = datetime.fromisoformat(log)
        hours[time.hour] += 1

    return hours.index(max(hours))


logs = [
    "2026-08-04T13:21:18",
    "2026-08-04T13:45:10",
    "2026-08-04T09:15:00",
    "2026-08-04T13:50:30",
    "2026-08-04T09:30:00"
]

print(find_peak_usage(logs))
