"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes.
"""
user_age = int(input("What is your age? "))

# To find that range, subtract your age from 220.

max_heart_beat = 220 - user_age
   
"""This difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

min_range = int(.65 * max_heart_beat)

max_range = int(.85 * max_heart_beat)

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {min_range} and {max_range} beats per minute.")