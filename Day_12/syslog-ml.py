import pandas as pd
from sklearn.linear_model import LinearRegression
import datetime
import time

log_file_path = '2023-09-07-pub.log'

while True:
    try:
        df = pd.read_csv(log_file_path, parse_dates=[0], names=["Timestamp", "CPU Usage", "Logical CPUs", "Used Memory", "Used Disk Space", "Host IP"])

        df['Date'] = df['Timestamp'].dt.date

        daily_cpu_usage = df.groupby('Date')['CPU Usage'].mean().reset_index()

        prediction_date = daily_cpu_usage['Date'].max() + datetime.timedelta(days=1)

        X = daily_cpu_usage['Date'].values.reshape(-1, 1)
        y = daily_cpu_usage['CPU Usage'].values

        model = LinearRegression()
        model.fit(X, y)

        predicted_cpu_usage = model.predict([[prediction_date]])[0]

        print(f"Predicted CPU Usage for {prediction_date}: {predicted_cpu_usage}%")

        time.sleep(300)

    except KeyboardInterrupt:
        break

print("Prediction stopped.")

