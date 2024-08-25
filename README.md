# Project Title : WEB SCRAPING WITH STREAMLIT APPLICATION
# Project Description : 
This project is a web-based application created using Streamlit to scrape doctor profiles from the Practo website, based on location and specialization.
The app connects with the server and gets count of all doctor profiles with those criteria, so that we can display total number of doctors found in less time.

# Installation Instructions : 
1. Installed required libraries and required dependencies.
2. Then build the application using streamlit.
3. Run the application.

# Usage : 
### Input Location : 
You will see an input field that reads "Enter the Location" on the app. Enter the city where you wish to search for doctors.
### Select Specialization : 
Select the specialization of doctor from drop down list. Available options include:
Dentist
Gynecologist/Obstetrician
General Physician
Dermatologist
Pediatrician
Cardiologist
Cardiac Surgeon
Urologist
ENT Specialist (EAR NOSE THROAT SURGEON)
### Start Scraping : 
Choose the country, choose Specialization and click on “Scrape”.
View Results:
This will show how many doctor profiles were found in total for the given location and specialization. 

# Output : 
After scraping and the process is completed, user will get success message with number of records found for doctors profiles by location selected on specialization.
For example:
"Found 25 doctor profiles in Bangalore for Cardiologist."
If the application fails to retrieve data, an error message will be displayed, prompting the user to check their inputs or try again.
