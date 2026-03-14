import streamlit as st

st.set_page_config(page_title="Engine Health Monitoring", layout="wide")

st.title("Aircraft Engine Health Monitoring System")
st.subheader("CFM56-7B – Boeing 737NG")

st.markdown("---")

# ==============================
# INPUT AIRCRAFT
# ==============================

aircraft = st.text_input("Aircraft Registration","PK-LAB")
engine = st.selectbox("Engine Position",["Engine 1","Engine 2"])

st.markdown("### Engine Parameters Input")

col1,col2,col3 = st.columns(3)

with col1:
    egt = st.number_input("EGT (°C)",0.0,1200.0,850.0)

with col2:
    n1 = st.number_input("N1 (%)",0.0,110.0,97.0)

with col3:
    n2 = st.number_input("N2 (%)",0.0,110.0,98.0)

col4,col5,col6 = st.columns(3)

with col4:
    oil_pressure = st.number_input("Oil Pressure (psi)",0.0,100.0,45.0)

with col5:
    oil_temp = st.number_input("Oil Temperature (°C)",0.0,200.0,140.0)

with col6:
    vibration = st.number_input("Vibration",0.0,10.0,2.0)

st.markdown("---")

# ==============================
# ENGINE LIMITS
# ==============================

EGT_LIMIT = 920
N1_LIMIT = 102
N2_LIMIT = 101
OIL_PRESS_LOW = 30
OIL_TEMP_LIMIT = 165
VIB_LIMIT = 3.5

# ==============================
# STATUS FUNCTION
# ==============================

def status(value,limit):

    if value > limit:
        return "WARNING 🔴"
    
    elif value > limit*0.9:
        return "ABNORMAL 🟡"
    
    else:
        return "NORMAL 🟢"


# ==============================
# ANALYSIS BUTTON
# ==============================

if st.button("Analyze Engine Condition"):

    st.markdown("## Engine Health Status")

    col1,col2,col3 = st.columns(3)

    with col1:
        st.metric("EGT",f"{egt} °C",status(egt,EGT_LIMIT))

    with col2:
        st.metric("N1",f"{n1} %",status(n1,N1_LIMIT))

    with col3:
        st.metric("N2",f"{n2} %",status(n2,N2_LIMIT))

    col4,col5,col6 = st.columns(3)

    with col4:
        st.metric("Oil Pressure",f"{oil_pressure} psi")

    with col5:
        st.metric("Oil Temperature",f"{oil_temp} °C")

    with col6:
        st.metric("Vibration",vibration,status(vibration,VIB_LIMIT))

    st.markdown("---")

# ==============================
# MAINTENANCE RECOMMENDATION
# ==============================

    recommendation=[]

    if egt>EGT_LIMIT*0.9:
        recommendation.append("Monitor EGT trend – possible compressor fouling")

    if vibration>2.5:
        recommendation.append("Check fan rotor balance")

    if oil_pressure<OIL_PRESS_LOW:
        recommendation.append("Inspect lubrication system")

    if oil_temp>OIL_TEMP_LIMIT:
        recommendation.append("Check bearing condition")

    if recommendation:
        st.warning("Maintenance Recommendation")
        for r in recommendation:
            st.write("-",r)

    else:
        st.success("Engine operating within normal parameters")