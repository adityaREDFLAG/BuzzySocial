from pytrends.request import TrendReq
import pandas as pd
import json

# Connect to Google Trends
pytrends = TrendReq()
pytrends.build_payload(['AI'], timeframe='now 7-d')  # Change 'AI' to any keyword

# Get interest over time
data = pytrends.interest_over_time().reset_index()

# Convert to simple JSON format
output = [
    {"date": row["date"].strftime("%Y-%m-%d %H:%M"), "interest": int(row["AI"])}
    for _, row in data.iterrows()
]

# Save to JSON file
with open("trend_data.json", "w") as f:
    json.dump(output, f, indent=2)

print("✅ Saved trend_data.json")
