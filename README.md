# 互動式線性回歸分析平台

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-red.svg)](https://streamlit.io)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3%2B-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一個基於 Streamlit 的互動式 Web 應用，旨在透過視覺化的方式探索線性回歸模型。使用者可以動態調整參數、比較不同模型，並觀察隨機雜訊對回歸結果的影響。

<!-- 建議您錄製一個 GIF 動畫放在這裡，展示應用程式的操作畫面 -->
<!-- ![應用程式操作展示](demo.gif) -->

---

## 功能亮點

- **動態資料生成**：自由設定斜率、截距、雜訊和資料點數量。
- **多模型比較**：支援普通線性回歸、Ridge、Lasso 及 Huber 等多種模型。
- **即時視覺化**：資料散佈點與擬合的回歸線即時更新。
- **量化評估**：自動計算 R² 分數，衡量模型擬合優度。
- **蒙地卡羅模擬**：透過動畫展示模型在不同隨機抽樣下的穩定性。
- **資料與動畫下載**：可將生成的資料下載為 CSV，或將模擬過程下載為 GIF。

## 技術棧

- **核心演算法**：`scikit-learn`
- **互動介面**：`Streamlit`
- **資料處理**：`Numpy`, `Pandas`
- **視覺化**：`Matplotlib`

---

## 安裝與執行

請依照以下步驟在您的本地端環境中執行此專案。

**1. 複製專案**
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
```

**2. (建議) 建立並啟用虛擬環境**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

**3. 安裝依賴套件**
```bash
pip install -r requirements.txt
```

**4. 執行應用程式**

本專案包含三個不同版本的應用程式，您可以選擇執行其中一個：

```bash
# 執行基本版
streamlit run basic_app.py

# 執行進階版 (多模型選擇)
streamlit run advanced_app.py

# 執行動畫模擬版
streamlit run animation_app.py
```
---

## 檔案結構

```
.
├── basic_app.py         # 版本1：基本線性回歸功能
├── advanced_app.py      # 版本2：增加多模型選擇與下載功能
├── animation_app.py     # 版本3：增加蒙地卡羅模擬動畫
├── requirements.txt     # 專案依賴套件列表
└── README.md            # 專案說明文件
```

---

## CRISP-DM 流程

本專案遵循 CRISP-DM (跨產業資料探勘標準流程) 的六個階段來進行。

1.  **商業理解 (Business Understanding)**：建立一個教育工具，讓使用者能直觀地探索線性關係。
2.  **資料理解 (Data Understanding)**：動態生成 `y = ax + b + noise` 形式的合成資料。
3.  **資料準備 (Data Preparation)**：將生成的資料轉換為 `NumPy` 陣列以供模型使用。
4.  **建模 (Modeling)**：使用 `scikit-learn` 提供的多種線性回歸模型進行訓練。
5.  **評估 (Evaluation)**：透過 R² 分數和視覺化圖表來評估模型效果。
6.  **部署 (Deployment)**：使用 `Streamlit` 將整個流程封裝成一個互動式的 Web 應用。

---

## 授權條款

本專案採用 [MIT License](https://opensource.org/licenses/MIT) 授權。
