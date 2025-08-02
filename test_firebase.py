import firebase_admin
from firebase_admin import credentials, firestore

# Load credentials from secrets.toml via Streamlit
import streamlit as st

# Parse the Firebase credentials from Streamlit secrets
cred = credentials.Certificate(st.secrets["firebase"])
firebase_admin.initialize_app(cred)

# Connect to Firestore
db = firestore.client()

# Test write
doc_ref = db.collection("testCollection").document("testDoc")
doc_ref.set({
    "message": "Hello from SafeCity Pulse!",
    "status": "success"
})

# Test read
doc = doc_ref.get()
if doc.exists:
    st.success(f"Document data: {doc.to_dict()}")
else:
    st.error("No such document found.")
