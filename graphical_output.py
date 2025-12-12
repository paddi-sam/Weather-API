import weather_processor as wp
import matplotlib.pyplot as plt

summary = wp.main()
print("-----------------")
print(summary)

labels = ["Temperature (°C)", "Feels Like (°C)", "Humidity (%)", "Wind Speed (kph)", "UV", "Visibility (km)"]

values = [
    summary['current']["Temp (C)"], 
    summary['current']["Feelslike (C)"], 
    summary['current']["Humidity"],
    summary['current']['Wind (kph)'],
    summary['current']['UV'],
    summary['current']['Visibility_km']
]

plt.figure(figsize=(8, 5))
plt.bar(labels, values)
plt.title(f'{summary["location"]["name"]}, {summary["location"]["country"]}')
plt.xlabel("Variables")
plt.ylabel("Values")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()