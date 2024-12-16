**VTravel - Cycle Booking System**

VTravel is a cycle rental and return system designed for a university campus. The application allows students to book cycles from various booths, track their rental time, and return cycles when done. It uses Streamlit for the front end and simple file handling to maintain data related to students and booth availability.

**Features**

User Authentication: Students can log in by providing their Registration Number and Date of Birth (DOB).
Booth Availability: Users can view the availability of cycles at various booths (e.g., AB1, AB2, BLOCK 1).
Cycle Booking: Students can book cycles if not already booked.
Cycle Return: Students can return their cycles to any booth and update the availability.
Rental Time Calculation: The application tracks the rental time and calculates the rent in minutes.
Requirements

To run this project, make sure you have the following installed:

Python 3.7+
Streamlit (pip install streamlit)
Files

student_data.txt: Contains the details (registration number, DOB) of the students.
booked.txt: Keeps a record of all booked cycles, including the registration number and the time of booking.
{booth}.txt: Contains the available cycles at each booth (e.g., AB1.txt, BLOCK_1.txt).
Code Overview

**Key Functions**
user_validate(reg_no, dob): Checks if the student with the given registration number and DOB exists in student_data.txt.
show_booth(selected, booth_details): Displays the number of cycles left at the selected booth.
check_history(reg_no): Checks if the student has already booked a cycle.
sumit_cycle(reg_no, submit): Updates the booking records when a student returns a cycle.
rent_calc(reg_no): Calculates the rent for the student by determining the time difference from the booking time.
book_booth(selected, reg_no): Allows a student to book a cycle at the selected booth and updates the booth’s cycle list.
Flow of the Application
Login Page: Students enter their registration number and DOB to log in.
Main Page: Once logged in, students can:
Check if they have already booked a cycle.
View available booths and cycles.
Book a cycle or return a cycle if already booked.
Booking: If a student has not booked a cycle, they can select a booth and book a cycle.
Cycle Return: If the student has already booked a cycle, they can return it by selecting a booth.
Rental Time Calculation: The rental time and rent are calculated based on the time difference from the booking.

**Installation & Setup**

Clone this repository to your local machine.
git clone https://github.com/PranshuJadaun/VTravels
cd vtravel
Install required libraries:
pip install -r requirements.txt
Make sure the necessary data files (student_data.txt, booked.txt, and booth cycle files) are in place.
Run the Streamlit app:
streamlit run app.py

**How to Use**

Login: Enter your registration number and date of birth (DOB) to log in.
Booking a Cycle:
After logging in, select a booth.
If cycles are available, click Book Now to reserve a cycle.
Returning a Cycle: If you have already booked a cycle, you can return it by selecting a booth and clicking Submit.
Check Rental Time: If you’ve rented a cycle, the app will show the rent based on the time you've kept the cycle.

**File Structure**

.
├── app.py                   # Main Streamlit application
├── student_data.txt         # File containing student data (Reg No, DOB)
├── booked.txt               # File tracking booked cycles
├── AB1.txt                  # File containing cycles in booth AB1
├── AB2.txt                  # File containing cycles in booth AB2
├── BLOCK_1.txt              # File containing cycles in booth BLOCK_1
├── BLOCK_2.txt              # File containing cycles in booth BLOCK_2
└── README.md                # This readme file

**Contributing**

Feel free to fork the repository, make changes, and submit a pull request. If you encounter any bugs or have suggestions for improvements, please open an issue.

**License**

This project is licensed under the MIT License - see the LICENSE file for details.
