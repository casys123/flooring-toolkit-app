# app.py - Streamlit Flooring Market Toolkit

import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import folium
from streamlit_folium import folium_static

st.set_page_config(page_title="Flooring Market Toolkit", layout="wide")
st.title("📊 Flooring Market Penetration Toolkit")

# ------------------ Module 1: Lead Generation Engine ------------------

st.header("1️⃣ Permit-Based Lead Generator")

@st.cache_data

def scrape_permit_data(county_url):
    response = requests.get(county_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    permit_data = []
    for row in soup.select("table.permit-table tr"):
        cells = row.find_all('td')
        if len(cells) >= 6:
            permit_data.append({
                "Property Address": cells[0].text.strip(),
                "Owner Contact": cells[1].text.strip(),
                "Project Type": cells[2].text.strip(),
                "Square Footage": cells[3].text.strip(),
                "Permit Issue Date": cells[4].text.strip(),
                "Contractor Name": cells[5].text.strip(),
            })
    return pd.DataFrame(permit_data)

if st.button("Scrape Permits from Miami-Dade & Broward"):
    miami_df = scrape_permit_data("https://www.miamidade.gov/permits")
    broward_df = scrape_permit_data("https://www.broward.org/Regulation/Permits")
    combined_df = pd.concat([miami_df, broward_df], ignore_index=True)
    if 'Project Type' in combined_df.columns:
        flooring_df = combined_df[combined_df['Project Type'].str.contains("floor|remodel|renovation|construction", case=False, na=False)]
        st.dataframe(flooring_df)
    else:
        st.warning("Column 'Project Type' not found in scraped data. Please verify the website structure.")

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
