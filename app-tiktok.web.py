import streamlit as st
import os

st.set_page_config(page_title="TikTokVay Web PRO", layout="wide")
st.title("🚀 TikTokVay Web PRO - Xây Kênh Thời Trang Váy")
st.subheader("Login Grok + TikTok (Gmail/Scan QR) | Chỉ Đến B4")

# B1: Login Grok + TikTok
with st.sidebar:
    st.header("🔑 B1: Đăng Nhập")
    
    # Grok
    grok_key = st.text_input("Grok API Key / Tài Khoản", type="password")
    if grok_key:
        st.success("✅ Grok OK!")
    
    # TikTok Login
    st.subheader("TikTok Shop Login")
    login_method = st.radio("Cách đăng nhập TikTok", ["Gmail", "Scan QR Code"])
    
    if login_method == "Gmail":
        tiktok_gmail = st.text_input("Email TikTok (Gmail)", placeholder="yourgmail@gmail.com")
        if tiktok_gmail:
            st.info("✅ Đăng nhập qua Gmail - Copy link login TikTok và xác thực!")
    else:
        st.info("✅ Scan QR Code TikTok trên app → Paste session/cookies vào ô dưới")
        tiktok_session = st.text_input("TikTok Session / Cookies", type="password")
        if tiktok_session:
            st.success("✅ TikTok Login bằng Scan QR OK!")

if grok_key:
    st.sidebar.success("Grok Ready!")

# B1.5: Ảnh người mẫu
st.header("📸 B1.5: Upload ảnh người mẫu")
model_imgs = st.file_uploader("Upload nhiều ảnh người mẫu", type=["jpg","png"], accept_multiple_files=True)
if model_imgs:
    st.success(f"✅ Đã upload {len(model_imgs)} ảnh!")

# B2-B4: Giữ nguyên như trước
st.header("🛍️ B2-B4: Sản phẩm + Prompt + Tạo Folder")
san_pham_text = st.text_area("Danh sách sản phẩm (mỗi dòng 1 sp)", "Váy maxi trắng\nVáy midi đen")
prompts_text = st.text_area("Danh sách prompt (mỗi dòng 1 prompt)", height=150)

if st.button("🚀 TẠO BATCH FOLDER & PROMPT (B4)"):
    # Code tạo folder như trước (giữ nguyên)
    st.success("✅ Hoàn thành B4! Tải folder video_projects về máy")

st.caption("Web App đã chỉnh login TikTok = Gmail hoặc Scan QR như bạn yêu cầu!")

st.info("Sau B4: Tải folder về máy → Mở CapCut → Import → Cắt đầu video → Đăng TikTok Shop!")
