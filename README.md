# Smart IoT Load Monitoring Station for Finnish Wetlands

## Project Overview
This project demonstrates a prototype IoT measurement station for monitoring water quality before and after wetlands. It focuses on pollutant load reduction, especially phosphorus, and includes Finnish seasonal effects like snow and cold temperatures.

### Key Features
* Two tanks simulate inflow (polluted) and outflow (treated) water.
* Sensors measure pH, turbidity, temperature; optional conductivity/DO.
* ESP32 embedded system reads sensor data and transmits it to the cloud.
* Dashboard shows real-time inflow/outflow comparison, predicted phosphorus load, and seasonal variation.
* Predictive analytics estimate phosphorus (and optionally nitrogen) using regression based on sensor data.

## Hardware
* ESP32 microcontroller
* pH Sensor
* Turbidity Sensor
* Temperature Sensor
* Optional: Conductivity Sensor, Dissolved Oxygen Sensor
* Two water tanks (inflow/outflow)
* Power source + Wi-Fi connectivity

## Software / IoT Pipeline
1. ESP32 reads sensor data continuously.
2. Data sent via MQTT/Wi-Fi to cloud dashboard.
3. Dashboard visualizes:
   * Inflow vs outflow water quality
   * Predicted phosphorus (and optional nitrogen)
   * Seasonal effects and alerts

## Setup / Usage
* Connect sensors to ESP32 and place them in inflow/outflow tanks.
* Power ESP32 and ensure Wi-Fi connection.
* Start data transmission via MQTT to the cloud dashboard.
* Monitor real-time measurements, predictions, and alerts on the dashboard.

## Unique Contributions
* Finnish climate simulation (snow, ice, cold temperatures)
* Predictive phosphorus estimation based on turbidity & temperature
* Interactive dashboard with inflow/outflow comparison and alerts
