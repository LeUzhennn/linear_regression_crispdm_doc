import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st

st.title("簡單線性回歸互動示範")

# 使用者輸入
st.sidebar.header("設定參數")
a_true = st.sidebar.slider("斜率 a", -10.0, 10.0, 2.0)
b_true = st.sidebar.slider("截距 b", -20.0, 20.0, 5.0)
noise_std = st.sidebar.slider("雜訊標準差", 0.0, 10.0, 2.0)
num_points = st.sidebar.slider("資料點數量", 10, 500, 50)

# 生成資料
np.random.seed(42)
X = np.random.rand(num_points, 1) * 10
y = a_true * X + b_true + np.random.randn(num_points, 1) * noise_std

st.subheader("資料預覽")
st.write(np.hstack([X[:5], y[:5]]))

# 建模
model = LinearRegression()
model.fit(X, y)
a_pred = model.coef_[0][0]
b_pred = model.intercept_[0]

# 畫圖
st.subheader("資料與回歸線")
fig, ax = plt.subplots()
ax.scatter(X, y, color='blue', label='資料點')
ax.plot(X, model.predict(X), color='red', label=f'回歸線 y={a_pred:.2f}x+{b_pred:.2f}')
ax.set_xlabel("X")
ax.set_ylabel("y")
ax.legend()
st.pyplot(fig)

# 模型評估
r2 = model.score(X, y)
st.subheader("模型評估")
st.write(f"真實線性方程式: y = {a_true}x + {b_true}")
st.write(f"預測回歸方程式: y = {a_pred:.2f}x + {b_pred:.2f}")
st.write(f"R² 分數: {r2:.4f}")
