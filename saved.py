import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from collections import Counter, defaultdict

# Load the JSON file
file_path = r'C:\Users\ufuk\Desktop\dsa210 proje\dsa210 data\saved\saved_posts.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract relevant data
saved_dates = []

for item in data.get("saved_saved_media", []):
    # Extract saved post timestamp
    timestamp = item.get("string_map_data", {}).get("Saved on", {}).get("timestamp", None)
    if timestamp:
        saved_dates.append(datetime.utcfromtimestamp(timestamp).date())

# Final exam periods
spring_finals = (datetime(2024, 5, 30).date(), datetime(2024, 6, 9).date())
fall_finals = (datetime(2025, 1, 2).date(), datetime(2025, 1, 13).date())
finals_periods = [spring_finals, fall_finals]

# Count posts per day
saved_counts = Counter(saved_dates)
dates, counts = zip(*sorted(saved_counts.items()))

# Calculate totals
total_saved_posts = sum(counts)
spring_finals_count = sum(count for date, count in saved_counts.items() if spring_finals[0] <= date <= spring_finals[1])
fall_finals_count = sum(count for date, count in saved_counts.items() if fall_finals[0] <= date <= fall_finals[1])

# Plot saved posts over time
plt.figure(figsize=(14, 6))
plt.bar(dates, counts, color='blue', alpha=0.7)
plt.axvspan(spring_finals[0], spring_finals[1], color='orange', alpha=0.3, label='Spring Finals')
plt.axvspan(fall_finals[0], fall_finals[1], color='green', alpha=0.3, label='Fall Finals')
plt.xlabel('Date')
plt.ylabel('Number of Saved Posts')
plt.title(f'Saved Posts Over Time\nTotal: {total_saved_posts}, Spring Finals: {spring_finals_count}, Fall Finals: {fall_finals_count}')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Calculate weekly averages
weekly_counts = defaultdict(int)
for date, count in saved_counts.items():
    week_start = date - timedelta(days=date.weekday())
    weekly_counts[week_start] += count

finals_weeks = []
non_finals_weeks = []

for week_start, count in weekly_counts.items():
    if any(period[0] <= week_start <= period[1] for period in finals_periods):
        finals_weeks.append(count)
    else:
        non_finals_weeks.append(count)

average_finals = sum(finals_weeks) / len(finals_weeks) if finals_weeks else 0
average_non_finals = sum(non_finals_weeks) / len(non_finals_weeks) if non_finals_weeks else 0

# Plot weekly averages
categories = ['Finals Period', 'Non-Finals Period']
averages = [average_finals, average_non_finals]

plt.figure(figsize=(8, 6))
plt.bar(categories, averages, color=['orange', 'blue'], alpha=0.7)
plt.xlabel('Period')
plt.ylabel('Average Saved Posts Per Week')
plt.title('Weekly Average Saved Posts: Finals vs Non-Finals')
plt.tight_layout()
plt.show()

# Print summary
print(f"Total saved posts: {total_saved_posts}")
print(f"Saved posts during Spring Finals: {spring_finals_count}")
print(f"Saved posts during Fall Finals: {fall_finals_count}")
print(f"Average saved posts per week during finals: {average_finals:.2f}")
print(f"Average saved posts per week during non-finals: {average_non_finals:.2f}")
