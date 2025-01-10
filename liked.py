import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from collections import Counter, defaultdict

# Load the JSON file
file_path = r'C:\Users\ufuk\Desktop\dsa210 proje\dsa210 data\likes\liked_posts.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract relevant data
liked_dates = []

for item in data.get("likes_media_likes", []):
    for entry in item.get("string_list_data", []):
        timestamp = entry.get("timestamp", None)
        if timestamp:
            liked_dates.append(datetime.utcfromtimestamp(timestamp).date())

# Final exam periods
spring_finals = (datetime(2024, 5, 30).date(), datetime(2024, 6, 9).date())
fall_finals = (datetime(2025, 1, 2).date(), datetime(2025, 1, 13).date())

# Count posts per day
liked_counts = Counter(liked_dates)
dates, counts = zip(*sorted(liked_counts.items()))

# Calculate weekly averages
all_dates = sorted(liked_counts.keys())
start_date = all_dates[0]
end_date = all_dates[-1]

weekly_counts = defaultdict(int)
weekly_totals = defaultdict(int)

for date, count in liked_counts.items():
    week_start = date - timedelta(days=date.weekday())
    weekly_counts[week_start] += count
    weekly_totals[week_start] += 1

weekly_average = {week: count / 7 for week, count in weekly_counts.items()}
finals_weeks = [
    week for week in weekly_average.keys() if spring_finals[0] <= week <= spring_finals[1] or fall_finals[0] <= week <= fall_finals[1]
]
non_finals_weeks = [week for week in weekly_average.keys() if week not in finals_weeks]

average_finals = sum(weekly_average[week] for week in finals_weeks) / len(finals_weeks)
average_non_finals = sum(weekly_average[week] for week in non_finals_weeks) / len(non_finals_weeks)

# Plot liked posts over time
plt.figure(figsize=(14, 6))
plt.bar(dates, counts, color='blue', alpha=0.7)
plt.axvspan(spring_finals[0], spring_finals[1], color='orange', alpha=0.3, label='Spring Finals')
plt.axvspan(fall_finals[0], fall_finals[1], color='green', alpha=0.3, label='Fall Finals')
plt.xlabel('Date')
plt.ylabel('Number of Liked Posts')
plt.title('Liked Posts Over Time (Final Exam Periods Highlighted)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot weekly averages
categories = ['Finals Period', 'Non-Finals Period']
averages = [average_finals, average_non_finals]

plt.figure(figsize=(8, 6))
plt.bar(categories, averages, color=['orange', 'blue'], alpha=0.7)
plt.xlabel('Period')
plt.ylabel('Average Likes Per Week')
plt.title('Comparison of Average Likes Per Week During Finals vs. Non-Finals')
plt.tight_layout()
plt.show()

# Print results
print(f"Average likes during finals weeks: {average_finals:.2f}")
print(f"Average likes during non-finals weeks: {average_non_finals:.2f}")
