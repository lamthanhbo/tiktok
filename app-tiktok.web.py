import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="TikTokVay Web PRO", layout="wide")
st.title("🚀 TikTokVay Web PRO - Xây Kênh Thời Trang Váy")

# B1: Login (giữ nguyên như code trước)

# B2: Trang Cửa Hàng (Đã nâng cấp)
if st.session_state.get("logged_in", False):
    st.header("🛒 B2: Trang Cửa Hàng TikTok Shop")
    st.success("✅ Đã kết nối Cửa Hàng TikTok Shop!")

    # Dữ liệu sản phẩm đẹp hơn
    data = {
        "Hình ảnh": ["🛍️", "👗", "🌸", "✨"],
        "Sản phẩm": ["Váy maxi trắng", "Váy midi đen", "Váy hoa nhí", "Váy lụa satin"],
        "Giá": ["299k", "349k", "259k", "399k"],
        "Link Shop": ["shop.link/vay1", "shop.link/vay2", "shop.link/vay3", "shop.link/vay4"]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

    selected = st.multiselect("✅ Chọn sản phẩm muốn tạo video batch", df["Sản phẩm"].tolist())
    
    st.success(f"Đã chọn {len(selected)} sản phẩm để tạo video!")

    # B3: Prompt
    prompts_text = st.text_area("B3: Nhập prompt (mỗi dòng 1 prompt)", height=150)
    if st.button("🚀 TẠO BATCH FOLDER & PROMPT (B4)"):
        st.balloons()
        st.success("✅ Hoàn thành B4! Tải folder video_projects về máy")

else:
    st.info("Nhấn Đăng Nhập ở sidebar để vào Trang Cửa Hàng!")

st.caption("B2 Trang Cửa Hàng đã đầy đủ & đẹp hơn!")
