#  Water Quality Prediction: Kuonanjoki Catchment (Finland)
> **Machine Learning Integration for Real-Time Environmental Monitoring**

##  Project Overview
This project leverages Machine Learning to enhance water quality monitoring in Finnish catchments. By utilizing the **Kuonanjoki Water Quality Dataset**, we have developed two distinct regression models to bridge the gap between expensive laboratory measurements and real-time sensor data.

###  The Two-Fold ML Objective
1.  **Nutrient Prediction :** Predicting **Total Phosphorus (Ptot)** using historical data.
2.  **State Prediction:** Predicting **Turbidity** and **Conductivity** using historical data.

---

## Dataset
The study uses high-frequency monitoring data from **Etsin (Fairdata.fi)** , focusing on the Kuonanjoki catchment.
- **Source:** [Dataset - Data - Etsin](https://etsin.fairdata.fi/dataset/7f2f6cf0-a250-4ba2-be06-73510368dcb2)
- **Parameters:** Water Temperature, Conductivity, Dissolved Oxygen, Turbidity, Suspended Solids and Ptot (Phosphorus).
- **Interval:** 30-minute sensor readings.

---


##  Machine Learning Architecture
We utilized the **Random Forest Regressor** for both tasks. This ensemble method was chosen because hydrochemical relationships are non-linear—nutrient spikes often occur only after specific "turning points" in flow velocity or rainfall.



### Model 1: The Virtual Nutrient Sensor
- **Target:** `Ptot [µg/l]` (Phosphorus)
- **Inputs:** Turbidity, Temperature, Conductivity.
- **Use Case:** Provides real-time phosphorus data every 30 minutes, replacing the 2-week delay of traditional lab tests.

### Model 2: Environmental State Forecaster
- **Targets:** `Turbidity [FNU]` and `Conductivitiy [µS/cm]`
- **Inputs:** Phosphorus, Oxygen, and Time Features (Month/Hour).
- **Use Case:** Identifies unusual water states and helps detect anomalies by comparing predicted physical states against measured values.

---

## Performance & Evaluation
Models are evaluated using the following metrics:
- **R² Score (Coefficient of Determination):** Measuring how closely the predictions follow the actual sensor "peaks."
- **RMSE (Root Mean Square Error):** Quantifying the precise deviation in units (µg/l or FNU).

### Visualizing Results
The project generates time-series plots that overlay **Actual Measured Data** with **Model Predictions**, demonstrating the model's ability to track runoff events during heavy rain or seasonal shifts.



---

##  Conclusion & Practical Impact
The integration of Machine Learning transforms raw sensor data into actionable environmental intelligence:
- **Infrastructure Planning:** Finnish municipalities can predict phosphorus spikes to optimize water treatment plant capacity.
- **Anomaly Detection:** If measured turbidity deviates significantly from the ML-predicted turbidity, it flags potential localized pollution or sensor malfunction.
- **Cost Efficiency:** Reduces the reliance on manual chemical sampling, providing 24/7 monitoring at a fraction of the operational cost.

---
