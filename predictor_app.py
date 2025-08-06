
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load CSVs (assumed to be in the same directory)
df_UTS = pd.read_csv("E:\My Research_Main\IIT Indore Conference\ML Code\Dataframe_UTS.csv")
df_FS = pd.read_csv("E:\My Research_Main\IIT Indore Conference\ML Code\Dataframe_FS.csv")
df_IS_Charpy = pd.read_csv("E:\My Research_Main\IIT Indore Conference\ML Code\Dataframe_IS_Charpy.csv")
df_IS_Izod = pd.read_csv("E:\My Research_Main\IIT Indore Conference\ML Code\Dataframe_IS_Izod.csv")

# Prediction function
def predict_all_models(layer_thickness, curing_temp, curing_time, weight_gain,
                       uts_before, fs_before, charpy_before, izod_before):
    targets = {
        "UTS After 72h (MPa)": ("UTS Before (MPa)", df_UTS, uts_before),
        "Flexural Strength After 72h (MPa)": ("Flexural Strength Before (MPa)", df_FS, fs_before),
        "Impact Strength (Charpy) After 72h (kJ/m2)": ("Impact Strength (Charpy) Before (kJ/m2)", df_IS_Charpy, charpy_before),
        "Impact Strength (Izod) After 72h (kJ/m2)": ("Impact Strength (Izod) Before (kJ/m2)", df_IS_Izod, izod_before)
    }

    results = {}
    for target_name, (before_col, df, before_value) in targets.items():
        features = ['Layer Thickness (µm)', 'Curing Temperature (in deg. Celcius)',
                    'Curing Time (in Minutes)', 'Weight Gain (24h, %)', before_col]
        X = df[features]
        y = df[target_name]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        sample = pd.DataFrame([[layer_thickness, curing_temp, curing_time, weight_gain, before_value]], columns=X.columns)
        pred = model.predict(sample)[0]
        results[target_name] = round(pred, 2)
    return results

# Streamlit UI
st.title("SLA 3D Printed Material Property Predictor for Grey Resin V5 Prepared by Sandeep Kumar, IIT Ropar, PhD (Click on '>' symbol on top left corner for entering your input values)")

st.sidebar.header("Enter Sample Input Values")
layer_thickness = st.sidebar.slider("Layer Thickness (µm)", 25, 100, 50, step=25)
curing_temp = st.sidebar.slider("Curing Temperature (°C)", 30, 80, 60)
curing_time = st.sidebar.slider("Curing Time (minutes)", 5, 30, 15)
weight_gain = st.sidebar.number_input("Weight Gain (%)", min_value=0.0, max_value=5.0, value=1.5, step=0.1)

st.sidebar.markdown("### Mechanical Properties (Before)")
uts_before = st.sidebar.number_input("UTS Before (MPa)", value=55)
fs_before = st.sidebar.number_input("Flexural Strength Before (MPa)", value=89)
charpy_before = st.sidebar.number_input("Impact Strength (Charpy) Before (kJ/m²)", value=35)
izod_before = st.sidebar.number_input("Impact Strength (Izod) Before (kJ/m²)", value=35)

if st.sidebar.button("Predict Properties After 72h"):
    with st.spinner("Predicting..."):
        results = predict_all_models(layer_thickness, curing_temp, curing_time, weight_gain,
                                     uts_before, fs_before, charpy_before, izod_before)

    st.success("Prediction complete!")
    st.subheader("🔎 Predicted Values After 72h:")
    for prop, val in results.items():
        st.write(f"**{prop}**: {val}")

    # ✅ ✅ Chart code INSIDE the button block
    st.subheader("📊 Visual Summary")
    chart_data = pd.DataFrame(results.values(), index=results.keys(), columns=["Predicted Value"])
    st.bar_chart(chart_data)
