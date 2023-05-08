# 建一个streamlit都模板，标题是“上海房产分析”


import streamlit as st
import pandas as pd

st.title("上海房产分析")

# 在侧边栏生成两个滑块，一个控制最小面积（最小50，最大150，默认50），第二个控制最大面积（最小50，最大150，默认150）

min_area = st.sidebar.slider("最小面积", 50, 150, 50)
max_area = st.sidebar.slider("最大面积", 50, 150, 150)

# 建一个上传文件的控件


uploaded_file = st.file_uploader("选择文件", type=["csv"])

# 把上传的csv文件用表格输出，根据最大最小面积，调整输出的内容

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.loc[(df["area"] >= min_area) & (df["area"] <= max_area)])

# 表头是“id,district,area,year_built,follower_number,unit_price,bed_room,living_room,other,maopei,jianzhuang,jingzhuang,t_floors”，输出面积在90以下，建造年份在2000年以后的房子


if uploaded_file is not None:
    st.dataframe(df.loc[(df["area"] <= 90) & (df["year_built"] >= 2000)])