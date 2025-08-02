import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import folium
from streamlit_folium import st_folium
import pandas as pd

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate(st.secrets["firebase"])
    firebase_admin.initialize_app(cred)

db = firestore.client()

st.set_page_config(page_title="SafeCity Pulse", layout="wide")

st.title("🚨 SafeCity Pulse – Cloud-based Urban Safety Monitoring System")

# ---------------- Feature 1: Smart SOS ----------------
with st.expander("🆘 Smart SOS"):
    name = st.text_input("Enter your name")
    location = st.text_input("Your current location")
    if st.button("Send SOS"):
        db.collection("sos_reports").add({"name": name, "location": location})
        st.success("🚨 SOS sent to authorities!")

# ---------------- Feature 2: Safety Heatmap ----------------
with st.expander("🗺️ Safety Heatmap"):
    map = folium.Map(location=[13.0827, 80.2707], zoom_start=12)
    st_data = st_folium(map, width=700, height=400)

# ---------------- Feature 3: AI Incident Classifier (Mock) ----------------
with st.expander("🤖 AI-Powered Incident Classification"):
    incident = st.text_input("Describe incident")
    if st.button("Predict Category"):
        st.info("🔍 Predicted: Harassment (Mock AI)")

# ---------------- Feature 4: Multilingual Report Assistant ----------------
with st.expander("🗣️ Multilingual Assistant"):
    lang = st.radio("Choose Language", ["English", "தமிழ்"])
    report = st.text_area("Report your concern")
    if st.button("Submit Report"):
        st.success("✅ Submitted")

# ---------------- Feature 5: Route Planner ----------------
with st.expander("🧭 Safe Route Planner (Mock)"):
    from_loc = st.text_input("From")
    to_loc = st.text_input("To")
    if st.button("Plan Safe Route"):
        st.info("Route planned via safest streets (Mock)")

# ---------------- Feature 6: Emergency Contacts ----------------
with st.expander("📞 Emergency Contacts"):
    st.write("🚓 Police: 100\n🚑 Ambulance: 108\n👩‍🚒 Fire: 101")

# ---------------- Feature 7: Community Safety Alerts ----------------
with st.expander("📢 Community Safety Alerts"):
    alerts = db.collection("sos_reports").stream()
    for a in alerts:
        data = a.to_dict()
        st.warning(f"{data['name']} reported from {data['location']}")

# ---------------- Feature 8: Push Notifications (Mock) ----------------
with st.expander("🔔 Push Notification (Simulated)"):
    st.info("You’ll be alerted in real-time for nearby incidents!")

# ---------------- Feature 9: Voice Alert (Text-to-Speech) ----------------
with st.expander("🔊 Voice Alert"):
    st.audio("https://www2.cs.uic.edu/~i101/SoundFiles/BabyElephantWalk60.wav")

# ---------------- Feature 10: Live Map Updates ----------------
with st.expander("📍 Live Incident Map"):
    folium.Marker([13.08, 80.27], tooltip="Recent SOS").add_to(map)
    st_folium(map, width=700, height=400)

# ---------------- Feature 11: Safety Scoreboard (Mock) ----------------
with st.expander("🏆 Leaderboard & Safety Score"):
    st.metric("Safe Actions Taken", 5)
    st.metric("User Rank", "Top 10%")

# ---------------- Feature 12: Safety Zone Suggestion ----------------
with st.expander("🛡️ Suggested Safe Zones"):
    st.success("Egmore Railway Station – Safe\nT-Nagar – Monitored Area")

# ---------------- Feature 13: Gender-Safe Zone Filter ----------------
with st.expander("🚺 Female-Friendly Zones"):
    st.info("High safety for women in: Adyar, Velachery")

# ---------------- Feature 14: AI Threat Detector (Mock) ----------------
with st.expander("⚠️ AI Threat Detector"):
    if st.button("Run Detection"):
        st.warning("Suspicious activity detected near Marina Beach")

# ---------------- Feature 15: Weather Backup (Optional) ----------------
with st.expander("⛅ Weather Backup"):
    st.info("Cloudy - 28°C. No weather threat reported.")

