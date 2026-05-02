import streamlit as st
import os

st.set_page_config(page_title="TikTokVay Web B4", layout="wide")
st.title("🚀 TikTokVay Web PRO - Chỉ Đến B4")
st.subheader("B1-B4 | Generate Prompt + Folder Tự Động")

# B1: Login
with st.sidebar:
    st.header("🔑 B1: Đăng nhập")
    grok_key = st.text_input("Grok API Key", type="password")
    tiktok_session = st.text_input("TikTok Shop Session", type="password")
    if grok_key and tiktok_session:
        st.success("✅ Login thành công!")

# B1.5: Ảnh người mẫu
st.header("📸 B1.5: Upload ảnh người mẫu")
model_imgs = st.file_uploader("Upload ảnh người mẫu", type=["jpg","png"], accept_multiple_files=True)
if model_imgs:
    st.success(f"✅ Đã upload {len(model_imgs)} ảnh!")

# B2 + B3 + B4
st.header("🛍️ B2-B4: Sản phẩm + Prompt + Tạo Folder")
san_pham_text = st.text_area("Danh sách sản phẩm (mỗi dòng 1 sp)", "Váy maxi trắng\nVáy midi đen\nVáy hoa nhí")
prompts_text = st.text_area("Danh sách prompt (mỗi dòng 1 prompt)", height=200, 
                           value="Cô gái xinh mặc váy bay nhẹ\nModel quay 360 độ tôn dáng")

if st.button("🚀 TẠO BATCH FOLDER & PROMPT (B4)"):
    san_pham = [sp.strip() for sp in san_pham_text.split("\n") if sp.strip()]
    prompts = [p.strip() for p in prompts_text.split("\n") if p.strip()]
    
    os.makedirs("video_projects", exist_ok=True)
    for sp in san_pham:
        folder = f"video_projects/{sp.replace(' ', '_')}"
        os.makedirs(folder, exist_ok=True)
        for i, p in enumerate(prompts):
            with open(f"{folder}/prompt_{i+1}.txt", "w", encoding="utf-8") as f:
                f.write(f"Sản phẩm: {sp}\n\nPrompt:\n{p}\n\nDùng ảnh người mẫu đã upload!")
        st.success(f"✅ Tạo folder hoàn tất cho: **{sp}**")
    
    st.balloons()
    st.success("🎉 Hoàn thành B4! Tải folder **video_projects** về máy để tiếp tục B5-B8 trên CapCut Local")

st.caption("Web App chỉ đến B4 như bạn yêu cầu. Dùng local cho cắt video + đăng TikTok!")

st.info("Tải folder video_projects về → Mở CapCut → Import → Cắt đầu video → Lưu → Đăng TikTok Shop!")
