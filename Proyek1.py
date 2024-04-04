import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

day_df = pd.read_csv("day.csv")
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

season_mapping = {
    1: "Springer",
    2: "Summer",
    3: "Fall",
    4: "Winter"
}
day_df['season_str'] = day_df['season'].map(season_mapping)

weather_mapping = {
    1: "Sunny",
    2: "Cloudy",
    3: "Rainy",
    4: "Snowy"
}

day_df['weathersit'] = day_df['weathersit'].map(weather_mapping)

hour_df = pd.read_csv("hour.csv")
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
hour_df['season_str'] = hour_df['season'].map(season_mapping)
hour_df['weathersit'] = hour_df['weathersit'].map(weather_mapping)

total_weekday_cnt = day_df.loc[day_df['workingday'] == 1, 'cnt'].sum()
total_holiday_cnt = day_df.loc[day_df['holiday'] == 1, 'cnt'].sum()

df_vis = pd.DataFrame({
    'weekday': ['Weekday', 'Holiday'],
    'cnt': [total_weekday_cnt, total_holiday_cnt]
})

fig1, ax1 = plt.subplots(figsize=(8, 6))
sns.barplot(x='weekday', y='cnt', data=df_vis, palette=['skyblue', 'lightgreen'], ax=ax1)
ax1.set_xlabel('Kategori Hari')
ax1.set_ylabel('Jumlah Penyewaan')
ax1.set_title('Distribusi Total Penyewaan Sepeda: Hari Kerja vs Akhir Pekan')
st.pyplot(fig1)

fig2, ax2 = plt.subplots(figsize=(12, 8))
for season in hour_df['season_str'].unique():
    df_season_hour = hour_df[hour_df['season_str'] == season].groupby('hr')['cnt'].sum()
    ax2.plot(df_season_hour.index, df_season_hour.values, label=season)
ax2.set_xlabel('Jam/Hari')
ax2.set_ylabel('Jumlah Penyewaan')
ax2.set_title('Total Penyewaan Sepeda per Jam/Hari per Musim')
ax2.legend()
st.pyplot(fig2)

