import streamlit as st
import requests
from bs4 import BeautifulSoup
import urllib.parse

def doct_prof(location, specialization):
    encoded_specialization = urllib.parse.quote(specialization)
    encoded_location = urllib.parse.quote(location)
    
    profiles_count = 0
    page = 1

    while True:
        url = f"https://www.practo.com/search/doctors?results_type=doctor&q=%5B%7B%22word%22%3A%22{encoded_specialization}%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22subspeciality%22%7D%2C%7B%22word%22%3A%22{encoded_location}%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22locality%22%7D%5D&city={encoded_location}&page={page}"
        res = requests.get(url)
    
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            profiles = soup.find_all('div', class_='u-border-general--bottom')
            # no_of_profiles = len(profiles)
            if not profiles:
                break

            profiles_count += len(profiles)
            page += 1
        else:
            st.error("Failed to retrieve data from the website.")
            return None
    return profiles_count
   

st.title("WEB SCRAPPING WITH STREAMLIT APPLICATION")
location = st.text_input("Enter the Location : ")
specializations = ["Dentist", "Gynecologist/obstetrician", "General Physician", "Dermatologist", "Pediatrician", "Cardiologist", 
                   "Cardiac Surgeon", "Urologist", "Ear-nose-throat (ent) Specialist"] 
specialization = st.selectbox("Select the specialization: ",specializations)

if st.button("Scrape"):
    if location and specialization:
        with st.spinner('Scraping data...'):
            profiles_count = doct_prof(location.lower(), specialization.lower())
            if profiles_count is not None:
                    st.success(f"Found {profiles_count} doctor profiles in {location} for {specialization}.")
            else:
                st.error("Failed to retrieve data. Please try again.")
    else:
        st.warning("Please enter a location and select a specialization.")