import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from collections import Counter, defaultdict

# Load the JSON file
file_path = r'C:\Users\ufuk\Desktop\dsa210 proje\dsa210 data\content\stories.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract relevant data
story_dates = []
music_genres = []

for story in data.get("ig_stories", []):
    # Extract story creation date
    timestamp = story.get("creation_timestamp", None)
    if timestamp:
        story_dates.append(datetime.utcfromtimestamp(timestamp).date())
    
    # Extract music genre if present
    video_metadata = story.get("media_metadata", {}).get("video_metadata", {})
    genre = video_metadata.get("music_genre", None)
    if genre:
        music_genres.extend(genre.split(", "))

# Final exam periods
spring_finals = (datetime(2024, 5, 30).date(), datetime(2024, 6, 9).date())
fall_finals = (datetime(2025, 1, 2).date(), datetime(2025, 1, 13).date())
finals_periods = [spring_finals, fall_finals]

# Count stories per day
story_counts = Counter(story_dates)
dates, counts = zip(*sorted(story_counts.items()))

# Plot story sharing over time
plt.figure(figsize=(14, 6))
plt.bar(dates, counts, color='blue', alpha=0.7)
plt.axvspan(spring_finals[0], spring_finals[1], color='orange', alpha=0.3, label='Spring Finals')
plt.axvspan(fall_finals[0], fall_finals[1], color='green', alpha=0.3, label='Fall Finals')
plt.xlabel('Date')
plt.ylabel('Number of Stories Posted')
plt.title('Stories Posted Over Time (Final Exam Periods Highlighted)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Count music genres
genre_counts = Counter(music_genres)
genres, genre_freqs = zip(*genre_counts.most_common())

# Plot music genres used in stories
plt.figure(figsize=(10, 6))
plt.bar(genres, genre_freqs, color='purple', alpha=0.7)
plt.xlabel('Music Genre')
plt.ylabel('Frequency of Use')
plt.title('Music Genres Used in Stories')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Calculate weekly averages
weekly_counts = defaultdict(int)
for date, count in story_counts.items():
    week_start = date - timedelta(days=date.weekday())
    weekly_counts[week_start] += count

# Separate weekly averages into finals and non-finals periods
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
plt.ylabel('Average Stories Per Week')
plt.title('Weekly Average Stories: Finals vs Non-Finals')
plt.tight_layout()
plt.show()
