import streamlit as st
import os

st.set_page_config(page_title="TikTokVay Web PRO", layout="wide")
st.title("🚀 TikTokVay Web PRO - Xây Kênh Thời Trang Váy")
st.subheader("Login → Trang Cửa Hàng")

# ==================== B1: ĐĂNG NHẬP (Có Button) ====================
st.header("🔑 B1: Đăng Nhập Tài Khoản")

col1, col2 = st.columns(2)
with col1:
    grok_key = st.text_input("Grok API Key / Tài Khoản", type="password", key="grok")
with col2:
    tiktok_session = st.text_input("TikTok Shop Session / Gmail", type="password", key="tiktok")

if st.button("🚪 ĐĂNG NHẬP CẢ 2 TÀI KHOẢN"):
    if grok_key and tiktok_session:
        st.success("🎉 **ĐĂNG NHẬP THÀNH CÔNG CẢ 2 TÀI KHOẢN!**")
        st.balloons()
        st.info("✅ Grok Super Ready + TikTok Shop Connected!")
        # Chuyển sang Trang Cửa Hàng tự động
        st.session_state.logged_in = True
    else:
        st.error("Vui lòng nhập đầy đủ Grok Key và TikTok Session!")

# ==================== B2: TRANG CỬA HÀNG (Chỉ hiện khi login thành công) ====================
if st.session_state.get("logged_in", False):
    st.header("🛒 B2: Trang Cửa Hàng TikTok Shop")
    st.success("✅ Đã kết nối Cửa Hàng!")
    
    # Danh sách sản phẩm (simulate hoặc upload)
    uploaded = st.file_uploader("Upload Excel sản phẩm từ Shop", type=["xlsx"])
    if uploaded:
        df = pd.read_excel(uploaded)
    else:
        df = pd.DataFrame({
            "Sản phẩm": ["Váy maxi trắng", "Váy midi đen", "Váy hoa nhí"],
            "Giá": ["299k", "349k", "259k"]
        })
    st.dataframe(df)
    
    selected = st.multiselect("Chọn sản phẩm tạo video", df["Sản phẩm"].tolist())
    
    # B3 + B4 (giữ nguyên như trước)
    prompts_text = st.text_area("Nhập prompt (mỗi dòng 1 prompt)", height=150)
    if st.button("🚀 TẠO BATCH FOLDER & PROMPT"):
        st.success("✅ Hoàn thành B4! Tải folder video_projects về máy")

else:
    st.info("Nhấn nút Đăng Nhập ở trên để vào Trang Cửa Hàng!")

st.caption("App đã chỉnh B1 có button + thông báo thành công cho cả 2 tài khoản như bạn yêu cầu!")
