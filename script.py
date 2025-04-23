import streamlit as st
import pandas as pd
import plotly.express as px

# Настройка страницы (заголовок, favicon, цветовая схема)
st.set_page_config(
    page_title="Анализ данных Iris",  # Заголовок страницы
    page_icon="images/favicon.ico",  # Путь к favicon
    layout="wide",  # Опционально, если хочешь, чтобы интерфейс был вширину
    initial_sidebar_state="expanded"  # Открытый sidebar по умолчанию
)

# Логотип в sidebar
st.sidebar.image("images/logo.png", width=150)

# Заголовок
st.title("Анализ данных Iris")

# Загрузка данных
df = pd.read_csv("data/Iris.csv")

# Проверка загрузки
if df.empty:
    st.warning("Не удалось загрузить данные.")
    st.stop()

# Показываем таблицу
st.subheader("Первые строки таблицы")
st.dataframe(df.head())

# Слайдер для фильтра
threshold = st.slider("Минимальная длина чашелистика (SepalLengthCm)", 4.0, 8.0, 5.0)

# Фильтрация
filtered_df = df[df["SepalLengthCm"] >= threshold]

# График
st.subheader("Фильтрованные данные")
fig = px.scatter(
    filtered_df,
    x="SepalLengthCm",
    y="SepalWidthCm",
    color="Species",
    title="Sepal Length vs Width",
    labels={"SepalLengthCm": "Sepal Length", "SepalWidthCm": "Sepal Width"},
)
st.plotly_chart(fig)