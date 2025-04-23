from pytrends.request import TrendReq

# Get Google Trends data for a keyword
pytrends = TrendReq()
pytrends.build_payload(['AI'], timeframe='now 7-d')
data = pytrends.interest_over_time()

# Make HTML from the data
cards = ""
for date, row in data.iterrows():
    value = row['AI']
    cards += f"<div style='padding:10px;background:#A9B5DF;margin:10px;border-radius:8px;'><h3>{date.date()}</h3><p>Interest: {value}</p></div>"

# Full HTML
html = f"""
<html>
<head><title>Google Trends: AI</title></head>
<body style='font-family:sans-serif;background:#FFF2F2;padding:20px;'>
  <h1 style='text-align:center;'>Google Trends: AI</h1>
  {cards}
</body>
</html>
"""

# Save the HTML page
with open("index.html", "w") as f:
    f.write(html)

print("✅ Your website file is ready: index.html")
