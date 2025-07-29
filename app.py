# app.py - Miami Master Flooring Market Toolkit

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

st.set_page_config(
    page_title="Miami Master Flooring | Market Toolkit",
    layout="wide",
    page_icon="📐"
)

st.title("🏢 Miami Master Flooring Sales Accelerator")
st.markdown("""
Welcome to the Miami Master Flooring Market Toolkit. 
We specialize in premium **vinyl**, **LVT**, and **carpet tile** solutions for commercial and residential properties in South Florida.
Explore local permit leads, competitor insights, heatmaps, and email outreach tools to grow your business.
""")

# ------------------ Module 1: Lead Generation Engine ------------------

st.header("1️⃣ Permit-Based Lead Generator (Mocked Data)")

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
st.markdown("Compare your business with other **vinyl, LVT, and carpet tile** contractors nearby.")

competitors_sample = pd.DataFrame({
    "Name": ["ABC Floors", "Miami Tile Co", "Luxury Plank Pro"],
    "Rating": [4.5, 3.8, 4.9],
    "Years in Business": [8, 5, 12],
    "Address": ["Miami, FL", "Fort Lauderdale, FL", "Weston, FL"]
})
st.dataframe(competitors_sample)

# ------------------ Module 3: Hyperlocal Targeting System ------------------

st.header("3️⃣ High-Potential Neighborhoods Heatmap")
st.markdown("Target homes built before 1980 and areas with recent property sales and high income.")

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

st.header("4️⃣ Automated Email Templates")

st.markdown("Use these emails to target property owners and managers looking for durable, modern flooring.")

templates = {
    "pre-1980": "Subject: Restore the Charm of Your Classic Property\n\nMiami Master Flooring offers stylish vinyl and carpet tile flooring ideal for updating historic homes with modern, durable materials.",
    "luxury": "Subject: Premium Designer Flooring for Elegant Spaces\n\nElevate your property with high-end luxury vinyl tile and carpet tile flooring from Miami Master Flooring — trusted by developers across South Florida.",
    "flood_zone": "Subject: Flooring That Withstands Water & Time\n\nOur water-resistant vinyl and carpet tile solutions are perfect for flood-prone areas in Miami-Dade and Broward counties."
}

def generate_email(template_key, recipient_name):
    return templates[template_key].replace("[NAME]", recipient_name)

template_key = st.selectbox("Choose Customer Type", list(templates.keys()))
recipient = st.text_input("Recipient Name", "Luis")
if st.button("Generate Email"):
    st.text_area("Email Content", generate_email(template_key, recipient), height=200)
