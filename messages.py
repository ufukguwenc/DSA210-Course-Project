import os
import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from collections import Counter, defaultdict

# Define the root path
root_path = r'C:\\Users\\ufuk\\Desktop\\dsa210 proje\\dsa210 data\\messages\\inbox'

# Final exam periods
spring_finals = (datetime(2024, 5, 30).date(), datetime(2024, 6, 9).date())
fall_finals = (datetime(2025, 1, 2).date(), datetime(2025, 1, 13).date())

# Initialize counters
sent_messages = []
received_messages = []

# Traverse folders and load data
for folder in os.listdir(root_path):
    message_file = os.path.join(root_path, folder, "message_1.json")
    if os.path.exists(message_file):
        with open(message_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for message in data.get("messages", []):
                timestamp = message.get("timestamp_ms", None)
                sender = message.get("sender_name", None)
                if timestamp:
                    message_date = datetime.utcfromtimestamp(timestamp / 1000).date()
                    if sender == "ufukguwenc":
                        sent_messages.append(message_date)
                    else:
                        received_messages.append(message_date)

# Count messages per day
sent_counts = Counter(sent_messages)
received_counts = Counter(received_messages)

# Aggregate data by date
all_dates = sorted(set(sent_counts.keys()).union(received_counts.keys()))
sent_by_date = [sent_counts.get(date, 0) for date in all_dates]
received_by_date = [received_counts.get(date, 0) for date in all_dates]

# Plot yearly messaging patterns
plt.figure(figsize=(14, 6))
plt.bar(all_dates, sent_by_date, color='blue', alpha=0.7, label='Messages Sent')
plt.bar(all_dates, received_by_date, color='orange', alpha=0.7, bottom=sent_by_date, label='Messages Received')
plt.axvspan(spring_finals[0], spring_finals[1], color='green', alpha=0.3, label='Spring Finals')
plt.axvspan(fall_finals[0], fall_finals[1], color='red', alpha=0.3, label='Fall Finals')
plt.xlabel('Date')
plt.ylabel('Number of Messages')
plt.title(f'Messages Sent and Received\nTotal Sent: {len(sent_messages)}, Total Received: {len(received_messages)}')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Weekly averages for finals and non-finals periods
weekly_counts = defaultdict(lambda: {'sent': 0, 'received': 0})

for date in sent_messages:
    week_start = date - timedelta(days=date.weekday())
    weekly_counts[week_start]['sent'] += 1

for date in received_messages:
    week_start = date - timedelta(days=date.weekday())
    weekly_counts[week_start]['received'] += 1

finals_weeks = [week for week in weekly_counts.keys() if spring_finals[0] <= week <= spring_finals[1] or fall_finals[0] <= week <= fall_finals[1]]
non_finals_weeks = [week for week in weekly_counts.keys() if week not in finals_weeks]

finals_sent_avg = sum(weekly_counts[week]['sent'] for week in finals_weeks) / len(finals_weeks)
finals_received_avg = sum(weekly_counts[week]['received'] for week in finals_weeks) / len(finals_weeks)

non_finals_sent_avg = sum(weekly_counts[week]['sent'] for week in non_finals_weeks) / len(non_finals_weeks)
non_finals_received_avg = sum(weekly_counts[week]['received'] for week in non_finals_weeks) / len(non_finals_weeks)

# Plot weekly averages
categories = ['Finals (Sent)', 'Finals (Received)', 'Non-Finals (Sent)', 'Non-Finals (Received)']
averages = [finals_sent_avg, finals_received_avg, non_finals_sent_avg, non_finals_received_avg]

plt.figure(figsize=(8, 6))
plt.bar(categories, averages, color=['blue', 'orange', 'blue', 'orange'], alpha=0.7)
plt.xlabel('Category')
plt.ylabel('Average Messages Per Week')
plt.title('Weekly Average Messages During Finals vs. Non-Finals')
plt.tight_layout()
plt.show()
