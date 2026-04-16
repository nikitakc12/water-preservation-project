### Smart IoT Water Quality Monitoring System

## Overview
This project presents a cloud-connected IoT system designed to monitor, analyse, and predict water quality in real outdoor environments, specifically tailored for Finnish wetlands and river ecosystems. The system bridges the gap between field-level hardware collection and predictive analytics, providing a robust solution for remote environmental surveillance.
The system is designed for high reliability in the field, featuring dual-path connectivity and local data redundancy to ensure continuous monitoring regardless of network stability.

## Features
•	Live Environmental Monitoring: Real-time collection of pH and Total Dissolved Solids (TDS) data.
•	Connectivity: Supports SIM-based mobile internet for deployment in remote areas.
•	Local Redundancy: Integrated SD card module for local data backup, preventing data loss during network outages.
•	Predictive Analytics: Implements Linear Regression to analyse water quality trends based on live sensor inputs.
•	Cloud Visualization: Real-time time-series graphing and dashboard access via ThingSpeak.

## Mechanical Design & Prototyping
The physical housing and structural model of the system were developed in collaboration with Mechanical Engineering students.
•	Custom Enclosure: Designed to protect sensitive electronics from harsh outdoor weather and water ingress.
•	Structural Integrity: Focused on secure sensor mounting and buoyancy/stability for river and wetland deployment.
•	Material Selection: Optimized for long-term environmental exposure and durability.

## Getting Started
## Prerequisites
•	Hardware:
o	Raspberry Pi Pico
o	pH and TDS Sensors
o	SIM Module (Cellular)
o	SD Card and Module
o	Waterproof enclosure and battery system
•	Software:
o	MicroPython for Raspberry Pi Pico
o	Python 3.x (Scikit-learn, Pandas)
o	ThingSpeak account

## Installation
1.	Hardware Assembly: Connect sensors and the SIM/SD modules to the Raspberry Pi Pico. Ensure the unit is housed in a waterproof enclosure for outdoor deployment.
2.	Environment Setup: Install the necessary analysis libraries:
3.	pip install scikit-learn pandas matplotlib requests
4.	Configuration: Update your source code with ThingSpeak API keys (Field 1 for pH, Field 2 for TDS) and network credentials .

## Usage
•	Field Deployment: Once powered, the system samples data every 30 minutes, saving a copy to the SD card and transmitting the results to the cloud.
•	Cloud Monitoring: Use the ThingSpeak dashboard for live trend visualization and shared company access.
•	Machine Learning Analysis:
1.	Retrieve live data from ThingSpeak via the Python API.
2.	Feed data into the Linear Regression model to generate quality predictions.
3.	Analyse results via scatter plots and regression trend graphs.

## Project Structure and Tech Stack
•	Microcontroller: Raspberry Pi Pico (MicroPython)
•	Connectivity: WiFi / SIM Module (Cellular Internet)
•	Storage: ThingSpeak Cloud + Local SD Card Backup
•	Analytics: Python (Linear Regression, CSV Export)

## Architecture Overview
Water Sensors (pH, TDS)
        ↓
Raspberry Pi Pico (MicroPython)
        ↓
SIM Module (Cellular Internet)
        ↓
ThingSpeak Cloud (Storage + Visualization)
        ↓
Python ML Model (Prediction)
        ↓
Dashboard + CSV Export

## Data Transmission Strategy
•	Frequency: Data is transmitted every 30 minutes (~48 points per day).
•	Efficiency: This schedule ensures a robust dataset for machine learning while remaining within the free-tier cloud limits.
•	Reliability: If internet connectivity fails, the SD card maintains a local record of all readings.

## Deployment Considerations
•	Harsh Conditions: The system requires a waterproof casing to survive Finnish outdoor weather.
•	Power Management: Battery systems are essential for river and wetland locations where mains power is unavailable.
•	Network Availability: The SIM-based module is the preferred primary connection for remote field use.

## Roadmap
•	Sensor Integration: Add Temperature, Turbidity, Dissolved Oxygen, and Conductivity.
•	Advanced Modelling: Transition to multi-variable prediction models for higher accuracy.
•	Dashboard Evolution: ThingSpeak dashboard.
•	Automation: Implement cloud-automated ML pipelines and anomaly/pollution alerts.

## License
This project is licensed under the MIT License.

## Acknowledgments
•	Mechanical Design: Developed in collaboration with the Mechanical Engineering department for the physical structural model.

## Contact
Nikita.K.C@student.lab.fi
Uzmatul.Bushra@student.lab.fi
Numaer.Abdus.Salique@student.lab.fi
Project Link: https://github.com/nikitakc12/water-preservation-project 
