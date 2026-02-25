 ### Smart IoT Water Quality Monitoring System

### For Finnish Wetlands

##  Project Overview

This project presents a cloud-connected IoT system designed to monitor and predict water quality conditions in Finnish wetlands and river environments.

The system collects environmental sensor data in the field, securely transmits it via 4G cellular internet, stores it in AWS cloud infrastructure, and applies machine learning to predict key pollution indicators such as **Nitrogen** and **Phosphorus**.

The solution is engineered for:

* Remote deployment 
* Low operational cost
* Long-term environmental monitoring
* Academic and industry demonstration

---

##  System Architecture

```
Water Sensors
      ↓
Raspberry Pi Pico 
      ↓
4G SIM Router / LTE Module
      ↓
AWS IoT Core (MQTT)
      ↓
IoT Rule Engine
      ↓
Amazon Timestream
      ↓
AWS Lambda (ML Prediction)
      ↓
Dashboard + CSV Export
```

---

##  Hardware Components

* Raspberry Pi Pico 
* 4G SIM Router / LTE Cellular Module
* Waterproof outdoor enclosure
* Battery backup system (field deployment)

### Sensors Used

* Temperature
* pH
* Turbidity
* Dissolved Oxygen (DO)
* Conductivity

Designed to operate in Finnish environmental conditions, including cold weather and outdoor exposure.

---

##  Data Transmission Strategy

* **Sampling interval:** Every 6 hours
* 4 transmissions per day
* ~120 transmissions per month

This approach ensures:

* Very low cloud cost
* Efficient data storage
* Long-term sustainability

---

##  Cloud Infrastructure (AWS)

The system uses the following AWS services:

* **AWS IoT Core** – Secure MQTT communication
* **Amazon Timestream** – Time-series data storage
* **AWS Lambda** – Machine learning prediction service
* **Amazon S3** – CSV data export storage
* **EventBridge Scheduler** – Daily automated export
* **Amazon Cognito** – Secure dashboard authentication

---

##  Machine Learning Prediction

A **Multiple Linear Regression** model runs inside AWS Lambda to predict:

* Nitrogen concentration
* Phosphorus concentration

### Input Parameters:

* Temperature
* pH
* Turbidity
* Dissolved Oxygen
* Conductivity

This enables early pollution detection and wetland performance analysis.

---

##  Dashboard Features

* Real-time sensor values
* Historical data visualization
* Pollution prediction results
* Secure company login
* Automated daily CSV export

---

##  Cost Efficiency

The system is designed to be highly cost-effective.

Estimated operational cost after free tier:

~ **$10–20 per month per monitoring station**

---

##  Deployment Considerations

Field risks include:

* Moisture exposure
* Power instability
* Cellular signal loss

Mitigation:

* Waterproof enclosure
* Backup battery
* Signal strength monitoring

---

##  Project Purpose

This project demonstrates:

* End-to-end IoT system design
* Secure cloud integration
* Time-series data engineering
* Serverless machine learning
* Cost-aware environmental monitoring

---

##  Use Cases

* Wetland monitoring
* River pollution analysis
* Environmental research
* Smart city water management
* Academic IoT & cloud projects

---

#  Summary

A field-deployable, AWS-powered IoT monitoring system designed for reliable, scalable, and cost-efficient water quality monitoring in remote Finnish environments.

