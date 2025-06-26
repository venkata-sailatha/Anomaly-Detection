## 📊 Anomaly Detection from Excel using Isolation Forest

This project provides a **Streamlit web app** that allows users to upload an Excel file containing time-series data and detects anomalies using the **Isolation Forest** algorithm. The detected anomalies are visualized on a time series plot, and users can download the updated Excel file with anomaly labels.

---

### 🚀 Demo

![image](https://github.com/user-attachments/assets/86aaac93-d7ec-46b2-bde3-b8b41fc7251e)
---

### 📁 Features

* Upload `.xlsx` file with `Timestamp` and `Value` columns
* Automatically detects anomalies using **Isolation Forest**
* Visualize results with matplotlib
* Download the processed file with anomaly annotations

---

### 📄 Sample Excel Format

| Timestamp           | Value |
| ------------------- | ----- |
| 2025-01-01 00:00:00 | 124.5 |
| 2025-01-01 00:15:00 | 130.2 |
| ...                 | ...   |

---

### 💻 Technologies Used

* **Python**
* **Streamlit** – for web UI
* **Pandas** – for data manipulation
* **Matplotlib** – for plotting
* **scikit-learn** – for Isolation Forest
* **openpyxl** – for Excel read/write

---

### 🛠️ Installation

#### 1. Clone the repository

```bash
git clone https://github.com/your-username/anomaly-detection-streamlit.git
cd anomaly-detection-streamlit
```

#### 2. Install dependencies

```bash
pip install -r requirements.txt
```

#### 3. Run the app locally

```bash
streamlit run app.py
```

---

### 🌐 live app

```
https://anomaly-detection-nq92.onrender.com
```

#### ✅ `requirements.txt` should include:

```
streamlit
pandas
matplotlib
scikit-learn
openpyxl
```

---

### 📦 Folder Structure

```
.
├── app.py
├── requirements.txt
├── README.md
└── sample_data.xlsx (optional)
```

---

### 📥 Output

* 📈 Time-series plot with anomaly points in red
* 📥 Downloadable `.xlsx` file with:

  * `anomaly_score`
  * `Anomaly` column (True/False)

---
