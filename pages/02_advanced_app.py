import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso, HuberRegressor
import streamlit as st

st.title("升級版簡單線性回歸互動示範 (含資料下載)")

# 使用者輸入
a_true = st.sidebar.slider("斜率 a", -10.0, 10.0, 2.0)
b_true = st.sidebar.slider("截距 b", -20.0, 20.0, 5.0)
noise_std = st.sidebar.slider("雜訊標準差", 0.0, 10.0, 2.0)
num_points = st.sidebar.slider("資料點數量", 10, 500, 50)
reg_method = st.sidebar.selectbox("回歸方法", ["Linear", "Ridge", "Lasso", "Huber"])
alpha = st.sidebar.slider("Ridge / Lasso alpha", 0.0, 10.0, 1.0)

# 生成資料
np.random.seed()
X = np.random.rand(num_points, 1) * 10
y = a_true * X + b_true + np.random.randn(num_points, 1) * noise_std

st.subheader("資料預覽")
st.write(np.hstack([X[:5], y[:5]]))

# 選擇模型
if reg_method == "Linear":
    model = LinearRegression()
elif reg_method == "Ridge":
    model = Ridge(alpha=alpha)
elif reg_method == "Lasso":
    model = Lasso(alpha=alpha)
elif reg_method == "Huber":
    model = HuberRegressor()
else:
    model = LinearRegression()

# 訓練模型
model.fit(X, y.ravel())
a_pred = model.coef_[0]
b_pred = model.intercept_

# 畫圖
fig, ax = plt.subplots(figsize=(8, 5))
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
st.write(f"選擇回歸方法: {reg_method}")
st.write(f"預測回歸方程式: y = {a_pred:.2f}x + {b_pred:.2f}")
st.write(f"R² 分數: {r2:.4f}")

# 下載 CSV
df = pd.DataFrame(np.hstack([X, y]), columns=["X", "y"])
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("下載 CSV 資料", data=csv, file_name='linear_regression_data.csv', mime='text/csv')
