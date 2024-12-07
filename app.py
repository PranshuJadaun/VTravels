import streamlit as st
from datetime import datetime, timedelta
# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'reg_no' not in st.session_state:
    st.session_state.reg_no = None

sd = "student_data.txt"
booth = ['AB1', 'AB2', 'BLOCK_1', 'BLOCK_2', 'BLOCK_3', 'BLOCK_4', 'BLOCK_5', 'BLOCK_6', 'BLOCK_G']
AB1 = ['A', 'B', 'C', 'D']
AB2 = ['E', 'F', 'G', 'H']
BLOCK_1 = ['I', 'J', 'K', 'L']
BLOCK_2 = ['M', 'N', 'O', 'P']
booth_details = {"AB1": AB1, "AB2": AB2, "BLOCK 1": BLOCK_1, "BLOCK 2": BLOCK_2}

st.title("VTravel")
st.text("By Pranshu Jadaun")

# User validation function
def user_validate(reg_no, dob):
    with open(sd, 'r') as f:
        details = [item.strip().split(",") for item in f.readlines()]
        for student in details:
            if student[0] == reg_no and student[1] == dob:
                return True
    return False

# Function to show booth availability
def show_booth(selected, booth_details):
    file_name = f"{selected}.txt"
    with open(file_name, 'r') as f:
        file = f.read()
        my_list = file.strip().split(',')
    cycle_left = len(my_list)
    return cycle_left
def check_history(reg_no):
    with open("booked.txt", 'r') as f:
        students = [line.strip().split(",") for line in f.readlines()]
    for student in students:
        if student[0] == reg_no:
            return "Already Booked"
    return "Not Booked"

def sumit_cycle(reg_no,submit):
    submit = f"{submit}.txt"
    with open("booked.txt",'r') as t:
        lines = t.readlines()
        all_list = [line.strip().split(",") for line in lines]
        for student in all_list:
            if student[0]==reg_no:
                cycle_name = student[1]
                break
    with open(submit,'a') as f:
        f.write(f",{cycle_name}")
    with open("booked.txt", "w") as file:
        for line in lines:
            if not line.startswith(reg_no):
                file.write(line)

def rent_calc(reg_no):
    with open("booked.txt", 'r') as f:
        lines = f.readlines()
        records = [line.strip().split(',') for line in lines]
        for record in records:
            if record[0] == reg_no:
                booked_time = datetime.strptime(record[2], '%Y-%m-%d %H:%M:%S.%f')
                break
    time_diff = datetime.now() - booked_time
    minutes = time_diff.total_seconds() / 60  
    r_minutes = round(minutes * 2) / 2
    return r_minutes
# Function to book booth
def book_booth(selected, reg_no):
    file_name = f"{selected}.txt"
    with open(file_name, 'r') as f:
        new_list = f.readline().strip().split(",")
    time_reg = datetime.now()
    with open("booked.txt", "a") as file:
        file.write(f"\n{reg_no},{new_list[-1]},{time_reg}")
    new_list.pop()  
    my_string = ','.join(new_list)
    with open(file_name, 'w') as f:
        f.write(my_string)

if not st.session_state.logged_in:
    reg_noo = st.text_input("Enter Registration Number")
    dob = st.text_input("Enter your DOB in YYYY-MM-DD")
    
    if st.button("Login"):
    
        if user_validate(reg_noo, dob):
            st.session_state.logged_in = True
            st.session_state.reg_no = reg_noo
            st.success("Authentication Completed: Log in Successful")
        else:
            st.error("Invalid Registration Number or DOB")
else:
    st.success(f"Welcome, {st.session_state.reg_no}")
    check = check_history(st.session_state.reg_no)
    if check == "Already Booked":
        st.warning("You have already booked a cycle.")
        rent = rent_calc(st.session_state.reg_no)
        st.warning(f"Your Rent is {rent*2}")
    selected = st.selectbox("Select Booth: ", booth)
    left = show_booth(selected, booth_details)
    st.subheader(f"Number of Cycles Left: {left-1}")
    
    if check!="Already Booked":
        if left > 1:
            if st.button("Book Now"):
                book_booth(selected, st.session_state.reg_no)
                st.success(f"Cycle booked at booth {selected}")
        else:
            st.text(f"No Cycle is left at {selected} (Try another booth)")
    else:
        st.error("You have already booked a cycle.\n(Limit Exceeded)")
        st.subheader("RETURN THE CYCLE")
        submit = st.selectbox("Select Booth to Return",booth)
        if st.button("Submit"):
            sumit_cycle(st.session_state.reg_no,submit)
            st.success("Successfully Submited")
            
