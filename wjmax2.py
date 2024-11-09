import streamlit as st
from datetime import datetime, timedelta
from PIL import Image
import time
import pytz

st.set_page_config(
    page_title="WJMAX 2th countdown",
    page_icon="wjmax.webp"
)

hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

st.logo(
    "wjmax.webp",
    link="https://wjmax.kr/",
    icon_image="wjmax.webp",
)

clear = 0
end = 0

title,imgs = st.columns([2,1])
with title:
    st.title("WJMAX 2th countdown")
with imgs:
    wjmax_img = Image.open('wjmax.webp')
    st.image(wjmax_img)
    st.markdown("""
<style>
img {
	max-height: 94px;
}
</style>
""", unsafe_allow_html=True)
st.title(" ")




title_placeholder = st.empty()
title_placeholder2 = st.empty()


while end == 0:

    now = datetime.now(tz)
    remaining_time = target_date - now


    if remaining_time <= timedelta(0):
        title_placeholder2.text("Happy WJMAX 2nd anniversary!")
        end = 1
    else:
        days = remaining_time.days
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        title_placeholder.text(f"현재 시간: {now.strftime('%H:%M:%S')}")
        title_placeholder2.text(f"남은 시간: {days}일 {hours}시간 {minutes}분 {seconds}초")

    time.sleep(1) 
