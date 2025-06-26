import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from io import BytesIO

st.title("📊 Anomaly Detection from Excel using Isolation Forest")

uploaded_file = st.file_uploader("Upload Excel File (.xlsx)", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)

        if 'Timestamp' not in df.columns or 'Value' not in df.columns:
            st.error("Excel file must contain 'Timestamp' and 'Value' columns.")
        else:
            df['Timestamp'] = pd.to_datetime(df['Timestamp'])
            df.sort_values(by='Timestamp', inplace=True)

            model = IsolationForest(contamination=0.05, random_state=42)
            df['anomaly_score'] = model.fit_predict(df[['Value']])
            df['Anomaly'] = df['anomaly_score'] == -1

            # Plotting
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(df['Timestamp'], df['Value'], label='Value')
            ax.scatter(df[df['Anomaly']]['Timestamp'], df[df['Anomaly']]['Value'],
                       color='red', label='Anomaly')
            ax.set_title("Anomaly Detection")
            ax.set_xlabel("Timestamp")
            ax.set_ylabel("Value")
            ax.legend()
            plt.xticks(rotation=45)
            st.pyplot(fig)

            # Download updated Excel
            output = BytesIO()
            df.to_excel(output, index=False)
            output.seek(0)

            st.download_button("📥 Download Result Excel", data=output,
                               file_name="data_with_anomalies.xlsx", mime="application/vnd.ms-excel")

    except Exception as e:
        st.error(f"❌ Error reading file: {e}")

if __name__ == "__main__":
    main()  # or whatever function you're calling

