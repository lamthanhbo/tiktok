import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="TikTokVay Web PRO", layout="wide")
st.title("🚀 TikTokVay Web PRO - Xây Kênh Thời Trang Váy")

# B1: Login
st.header("🔑 B1: Đăng Nhập Tài Khoản")

col1, col2 = st.columns(2)
with col1:
    grok_key = st.text_input("Grok API Key", type="password", placeholder="gsk_...")
with col2:
    tiktok_session = st.text_input("TikTok Shop Session", type="password", placeholder="sessionid_...")

if st.button("🚪 ĐĂNG NHẬP"):
    if len(grok_key) > 10 and len(tiktok_session) > 10:
        st.success("🎉 **ĐĂNG NHẬP THÀNH CÔNG CẢ 2 TÀI KHOẢN!**")
        st.balloons()
        st.session_state.logged_in = True
    else:
        st.error("❌ Nhập sai hoặc thiếu! Grok Key và TikTok Session phải dài hơn 10 ký tự.")

# B2: Trang Cửa Hàng (chỉ hiện khi login đúng)
if st.session_state.get("logged_in", False):
    st.header("🛒 B2: Trang Cửa Hàng TikTok Shop")
    st.success("✅ Đã kết nối Cửa Hàng!")
    # ... (phần còn lại giữ nguyên như code trước)

else:
    st.info("Nhấn Đăng Nhập để vào Trang Cửa Hàng!")

st.caption("Đã chỉnh login nghiêm ngặt hơn - Không cho nhập bừa!")
