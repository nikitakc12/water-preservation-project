Smart IoT Water Quality Monitoring System for Finnish Wetlands
## Project Overview

This project presents a smart IoT-based system designed to monitor water quality parameters in Finnish wetlands.
The goal is to analyze and predict pollutant concentrations, particularly phosphorus and nitrogen, which are key indicators of water pollution and eutrophication.

The system measures essential water parameters using sensors connected to a Raspberry Pi Pico and transmits the data via LoRa communication to a cloud dashboard for visualization and predictive analysis.
It is specifically adapted to Finnish weather conditions, including snow, ice, and low temperatures.

## Key Features

Real-time measurement of Temperature, Conductivity, pH, Dissolved Oxygen (DO), and Turbidity.

Phosphorus and Nitrogen concentrations are calculated using a regression-based model derived from sensor readings.

Raspberry Pi Pico serves as the main embedded controller.

LoRa-based communication enables long-range, low-power data transmission in remote environments.

Cloud dashboard for real-time monitoring, analytics, and visualization.

Adapted for Finnish environmental and seasonal challenges.

## Hardware Components

Raspberry Pi Pico (with LoRa transceiver module)

Sensors:

Temperature Sensor

TDS Sensor

Conductivity Sensor

pH Sensor

Dissolved Oxygen (DO) Sensor

Turbidity Sensor

LoRa Gateway (for transmitting data to the cloud)

Power source (battery or solar system for field use)

## IoT Pipeline

Data Acquisition
The Raspberry Pi Pico reads sensor data (temperature, conductivity, pH, DO, turbidity) periodically.

Data Transmission
Sensor readings are sent via LoRa to a gateway, which forwards the data to a cloud server or dashboard.

Cloud Visualization
A web-based dashboard displays:

Real-time and historical data trends

Seasonal variations

Alerts for threshold breaches

Predictive Analytics
A regression model analyzes the collected parameters to predict phosphorus and nitrogen levels, supporting early pollution detection and wetland efficiency analysis.

## Setup / Usage

Connect all sensors to the Raspberry Pi Pico according to pin mapping.

Connect the LoRa transceiver module for data transmission.

Power the device using  battery/solar setup.

Ensure LoRa gateway connectivity to the cloud.

Launch data collection — the dashboard updates automatically with readings.

