# app.py - Streamlit Flooring Market Toolkit (Mocked for Cloud)

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

st.set_page_config(page_title="Flooring Market Toolkit", layout="wide")
st.title("📊 Flooring Market Penetration Toolkit")

# ------------------ Module 1: Lead Generation Engine ------------------

st.header("1️⃣ Permit-Based Lead Generator (Mocked)")

@st.cache_data
def load_mock_permit_data():
    return pd.DataFrame({
        "Property Address": ["123 Main St", "456 Ocean Dr"],
        "Owner Contact": ["John Doe", "Jane Smith"],
        "Project Type": ["Remodel", "New Construction"],
        "Square Footage": [1500, 2400],
        "Permit Issue Date": ["2024-01-15", "2024-02-20"],
        "Contractor Name": ["ABC Floors", "XYZ Contractors"]
    })

if st.button("Load Permit Leads (Sample)"):
    mock_df = load_mock_permit_data()
    flooring_df = mock_df[mock_df['Project Type'].str.contains("floor|remodel|renovation|construction", case=False, na=False)]
    st.dataframe(flooring_df)

# ------------------ Module 2: Competitive Intelligence Dashboard ------------------

st.header("2️⃣ Competitive Intelligence (Static Example)")
st.markdown("⚠️ Google Maps API integration is currently placeholder. Replace with real data.")

competitors_sample = pd.DataFrame({
    "Name": ["ABC Floors", "Miami Tile Co", "Luxury Plank Pro"],
    "Rating": [4.5, 3.8, 4.9],
    "Years in Business": [8, 5, 12],
    "Address": ["Miami, FL", "Fort Lauderdale, FL", "Weston, FL"]
})
st.dataframe(competitors_sample)

# ------------------ Module 3: Hyperlocal Targeting System ------------------

st.header("3️⃣ Hyperlocal Targeting Heatmap")

def get_census_data():
    return pd.DataFrame({
        "Neighborhood": ["Coral Gables", "Pinecrest", "Weston", "Plantation"],
        "Pre-1980 Homes": [1200, 950, 300, 700],
        "High Income": [True, True, True, False],
        "Recent Sales": [25, 18, 20, 15]
    })

census_df = get_census_data()
m = folium.Map(location=[25.7617, -80.1918], zoom_start=10)

for i, row in census_df.iterrows():
    folium.Circle(
        location=[25.76 + 0.01 * i, -80.19 + 0.01 * i],
        radius=row['Pre-1980 Homes'] * 2,
        popup=row['Neighborhood'],
        color='green' if row['High Income'] else 'orange',
        fill=True
    ).add_to(m)

folium_static(m)

# ------------------ Module 4: Automated Outreach Module ------------------

st.header("4️⃣ Automated Outreach Emails")

templates = {
    "pre-1980": "Subject: Restore the Charm of Your Classic Home\n\nOur Historical Home Preservation Flooring Package is designed for timeless beauty and durability...",
    "luxury": "Subject: Premium Designer Flooring for Elegant Homes\n\nDiscover our high-end flooring options crafted for luxury living...",
    "flood_zone": "Subject: Protect Your Home with Water-Resistant Flooring\n\nIdeal for flood-prone areas, our water-resistant systems offer peace of mind and style..."
}

def generate_email(template_key, recipient_name):
    return templates[template_key].replace("[NAME]", recipient_name)

template_key = st.selectbox("Choose Customer Type", list(templates.keys()))
recipient = st.text_input("Recipient Name", "Luis")
if st.button("Generate Email"):
    st.text_area("Email Content", generate_email(template_key, recipient), height=200)
