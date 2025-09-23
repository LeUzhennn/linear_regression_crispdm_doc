import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter, FFMpegWriter
from sklearn.linear_model import LinearRegression
import streamlit as st
import tempfile
import io
from PIL import Image

st.title("回歸線多次模擬動畫 (可下載)")

# 使用者設定
a_true = st.sidebar.slider("斜率 a", -10.0, 10.0, 2.0)
b_true = st.sidebar.slider("截距 b", -20.0, 20.0, 5.0)
noise_std = st.sidebar.slider("雜訊標準差", 0.0, 10.0, 2.0)
num_points = st.sidebar.slider("資料點數量", 10, 100, 30)
num_simulations = st.sidebar.slider("模擬次數", 1, 50, 10)

X = np.linspace(0, 10, num_points).reshape(-1, 1)
fig, ax = plt.subplots(figsize=(8, 5))
scatter = ax.scatter([], [], color='blue')
line, = ax.plot([], [], color='red')
ax.set_xlim(0, 10)
ax.set_ylim(b_true - 4*noise_std, a_true*10 + b_true + 4*noise_std)
ax.set_xlabel("X")
ax.set_ylabel("y")

def init():
    scatter.set_offsets(np.array([]))
    line.set_data([], [])
    return scatter, line

def update(frame):
    y = a_true * X + b_true + np.random.randn(num_points, 1) * noise_std
    model = LinearRegression()
    model.fit(X, y)
    scatter.set_offsets(np.hstack([X, y]))
    line.set_data(X, model.predict(X))
    ax.set_title(f"模擬 {frame+1}/{num_simulations} - y = {model.coef_[0][0]:.2f}x + {model.intercept_[0]:.2f}")
    return scatter, line

 

# 在 Streamlit 中顯示動畫
st.pyplot(fig)

# 下載 GIF / MP4
st.sidebar.header("下載動畫")

if st.sidebar.button("生成 GIF"):
    with st.spinner("正在生成 GIF..."):
        frames_list = []
        # Ensure the figure is clean before starting to capture frames
        fig.canvas.draw()
        for i in range(num_simulations):
            update(i) # Update the plot for the current frame
            buf = io.BytesIO()
            fig.savefig(buf, format='png') # Save current figure state to buffer
            buf.seek(0)
            frames_list.append(Image.open(buf)) # Open as PIL Image

        if frames_list:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".gif") as tmpfile:
                # Calculate duration based on fps
                duration_ms = int(1000 / 2) # 2 fps -> 500ms per frame
                frames_list[0].save(tmpfile.name, save_all=True, append_images=frames_list[1:], duration=duration_ms, loop=0)
                with open(tmpfile.name, "rb") as f:
                    st.download_button("下載 GIF", data=f.read(), file_name="linear_regression_simulation.gif", mime="image/gif")
        else:
            st.warning("沒有生成任何動畫幀。")

if st.sidebar.button("生成 MP4"):
    st.warning("生成 MP4 需要在您的系統上安裝 FFMpeg。")
    try:
        with st.spinner("正在生成 MP4..."):
            anim = FuncAnimation(fig, update, frames=num_simulations, init_func=init, blit=False, repeat=False)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmpfile:
                anim.save(tmpfile.name, writer=FFMpegWriter(fps=2))
                with open(tmpfile.name, "rb") as f:
                    st.download_button("下載 MP4", data=f.read(), file_name="linear_regression_simulation.mp4", mime="video/mp4")
    except FileNotFoundError:
        st.error("無法生成 MP4。請確認您的系統已安裝 FFMpeg。")
