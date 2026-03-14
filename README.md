# EHM-CFM56-7B-by-PYTHON
# Aircraft Engine Health Monitoring Dashboard

## Overview
Dashboard ini dibuat untuk memonitor kondisi engine pesawat, khususnya **CFM56-7B** yang dipakai pada **Boeing 737NG**.  
Tujuan utama: menampilkan **status parameter engine** dan memberikan **peringatan dini** jika parameter mendekati limit atau over limit.  

Dashboard dibuat **dalam bentuk HTML sederhana**, dengan fitur:

- Monitoring **EGT, N1, N2, Oil Pressure, Oil Temperature, Vibration, Fuel Flow**  
- Status parameter:  
  - **Normal 🟢**  
  - **Approaching Limit 🟡**  
  - **Warning 🔴**  
- Tampilan profesional dengan **box putih + shadow + font modern**  
- Mudah dijalankan di browser lokal  

---

## Engine Parameters & Limits (CFM56-7B Typical)

| Parameter         | Limit / Notes         | Status Logic |
|------------------|--------------------|--------------|
| EGT (°C)          | 920                | >90% Limit → Approaching Limit, > Limit → Warning |
| N1 (%)            | 102                | >90% Limit → Approaching Limit, > Limit → Warning |
| N2 (%)            | 101                | >90% Limit → Approaching Limit, > Limit → Warning |
| Oil Pressure (psi)| 30 – 60            | <30 or >60 → Warning, mendekati limit → Approaching Limit |
| Oil Temperature (°C)| 165              | >90% Limit → Approaching Limit, > Limit → Warning |
| Vibration         | 3.5                | >90% Limit → Approaching Limit, > Limit → Warning |
| Fuel Flow (kg/h)  | 6000               | >90% Limit → Approaching Limit, > Limit → Warning |

---

## How to Run

1. Pastikan Python 3.x sudah terinstall  
2. Simpan file `dashboard.html` di folder yang diinginkan  
3. Jalankan script Python untuk generate HTML:

```bash
python generate_dashboard.py
