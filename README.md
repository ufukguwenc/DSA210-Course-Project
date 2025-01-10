# DSA210 Course Project 

# Examining Instagram Usage Patterns: A Comparative Analysis of Finals vs. Non-Finals Weeks


# Motivation
Social media usage has become a ubiquitous part of my daily life, often impacting my productivity, time management, and overall mental well-being. By analyzing my Instagram data, I aim to gain valuable insights into how my social media activity correlates with significant academic periods, particularly final exam weeks. Understanding these patterns can help identify trends and suggest strategies for balancing social media engagement with academic responsibilities.

# Project Idea
The goal of this project is to explore the relationship between my Instagram activity and specific academic milestones, such as final exam periods. The analysis will cover:

Messages: Analyzing the number of messages sent and received on a daily basis to observe communication trends, particularly during finals.

Stories: Evaluating the frequency of stories shared.

Saved Posts: Investigating saved posts to identify trends in content consumption, with a focus on academic versus non-academic periods.

Likes: Analyzing liked posts to assess engagement levels and their fluctuation during critical academic periods.

By combining these datasets, I will test a null hypothesis about how Instagram activity changes during high-stress academic periods and regular weeks. 

Null Hypothesis: There is no significant difference in Instagram activity (messages, stories, saved posts, or likes) during final exam weeks compared to non-final weeks.


# Data Source & Scope
I requested and exported my personal Instagram data. I collected my yearly Instagram activity data that spans from 09-01-2024 to 09-01-2025. Although Instagram provides it's user with a variaty of his/her data, in this project I will only use datas from "content" (stories and posts i shared), "messages", "likes" and "saved" folders which are inside the folder of "your_instagram_activity".

![image](https://github.com/user-attachments/assets/4a08f135-faa6-43c7-9a3e-600ab6c48c33)

Image 1: Main Folder 


![image](https://github.com/user-attachments/assets/b3a5602a-bb5f-4f74-85a3-41c69fdf31b1)

Image 2: Folders inside "your_instagram_activity"

Since the data I obtained directly from Instagram was well structured (hierarchically alligned JSON formay), already clean and consistent, I didn't perform any extra operation, such as cleaning or restructuring, on the data I received. Below, an example image can be found.

![image](https://github.com/user-attachments/assets/2a368b66-a461-4dff-a3be-f0092783f8ee)

Image 3: Example of my data, obtained from "saved_posts".

# Tools 

Programming Languages: Python with libraries: os, json, datetime, collections, matplotlib, pandas, numpy.

Environment: VisualStudio Code for coding and visualizations.

Data Management: JSON parsing for Instagram exports.

# Project Plan
## 1. Data Collection
Data was collected from Instagram to ensure a comprehensive analysis of Instagram activity. The datasets include:

-Messages: Exported from Instagram’s message history for all contacts, containing timestamps and sender information.

-Stories: Retrieved timestamps.

-Saved Posts: Timestamps of posts saved, providing insights into content consumption trends.

-Liked Posts: Timestamps of liked posts, reflecting engagement levels and preferences.

Academic periods, including Spring and Fall final exam weeks, were defined to compare Instagram activity during high-stress and regular periods.

## 2. Data Preprocessing

-Parsed and cleaned all datasets to ensure uniformity and accuracy.

-Standardized timestamps to ensure all activities were aligned to the same time zone.

-Filtered out irrelevant or incomplete data entries to maintain data integrity.

-Categorized activities based on whether they occurred during finals or non-finals periods.


## 3. Exploratory Data Analysis & Data Visualization

Performed an in-depth analysis to uncover patterns and trends:

### Yearly Activity:

-Created plots showing daily activity for messages, stories, saved posts, and likes.

-Highlighted final exam periods to observe behavioral changes.

### Weekly Averages:

-Compared weekly averages of Instagram activity during finals and non-finals periods for all datasets.

-Segmented data by sent and received messages, stories shared, and types of saved or liked content.

### Correlation Analysis:

-Calculated correlations between activity levels and academic milestones.

## 4. Report

The findings are presented in a detailed project report, which includes:

-Comprehensive visualizations and interpretations of data trends.

-Statistical analyses, including hypothesis testing results.

-Recommendations for managing social media usage during high-stress periods like final exams.

The report serves as a resource for understanding how social media activity correlates with academic performance and can guide strategies for improved time management.


