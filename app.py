
import streamlit as st
import pandas as pd
import plotly.express as px
import random
import datetime

st.set_page_config(page_title="Self-Healing Cyber Immune System", page_icon="🛡️", layout="wide")
st.title("🛡️ Self-Healing Cyber Immune System")
st.divider()

col1, col2, col3, col4 = st.columns(4)
col1.metric("🔴 Threats Detected", "1,029")
col2.metric("🟢 Normal Traffic", "8,971")
col3.metric("⚡ Detection Speed", "<200ms")
col4.metric("🎯 F1 Score", "98%")
st.divider()

attacks = ["DoS Attack","Probe Attack","R2L Attack","U2R Attack","Normal Traffic"]
severity = {"DoS Attack":"🔴 HIGH","Probe Attack":"🟠 MEDIUM",
            "R2L Attack":"🟡 MEDIUM","U2R Attack":"🔴 CRITICAL",
            "Normal Traffic":"✅ NONE"}
responses = {
    "DoS Attack":    ["✅ IP Blocked","✅ Rate Limited","✅ Admin Alerted"],
    "Probe Attack":  ["✅ IP Flagged","✅ Port Scan Blocked","✅ Team Notified"],
    "R2L Attack":    ["✅ Access Blocked","✅ Session Terminated","✅ Admin Alerted"],
    "U2R Attack":    ["✅ System Isolated","✅ Privilege Blocked","✅ Emergency Alert"],
    "Normal Traffic":["✅ Traffic Allowed","✅ No Action Needed","✅ Logged Normal"]
}

if st.button("🚨 Simulate Network Traffic"):
    attack = random.choice(attacks)
    ip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"
    time_now = datetime.datetime.now().strftime("%H:%M:%S")

    if attack == "Normal Traffic":
        st.success("✅ NORMAL TRAFFIC — No threat detected!")
    else:
        st.error(f"🚨 {attack} DETECTED!")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 🔍 Analysis")
        st.write(f"**Type:** {attack}")
        st.write(f"**Severity:** {severity[attack]}")
        st.write(f"**IP:** {ip}")
        st.write(f"**Time:** {time_now}")
    with c2:
        st.markdown("### 🛡️ Response")
        for r in responses[attack]:
            st.success(r)

st.divider()
data = pd.DataFrame({
    "Attack Type":["Normal","DoS","Probe","R2L","U2R"],
    "Count":[7431,1890,421,187,71]
})
fig = px.bar(data, x="Attack Type", y="Count", color="Attack Type",
             color_discrete_sequence=["green","red","orange","yellow","blue"])
st.plotly_chart(fig, use_container_width=True)
