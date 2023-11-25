import streamlit as st
import psutil

# Get RAM and disk storage information using psutil
ram_info = psutil.virtual_memory()
disk_info = psutil.disk_usage('/')

# Display RAM information
st.write(f"Total RAM: {ram_info.total / (1024 ** 3):.2f} GB")
st.write(f"Available RAM: {ram_info.available / (1024 ** 3):.2f} GB")

# Display disk storage information
st.write(f"Total Disk Space: {disk_info.total / (1024 ** 3):.2f} GB")
st.write(f"Available Disk Space: {disk_info.free / (1024 ** 3):.2f} GB")
import streamlit as st
import psutil

# Get RAM and disk storage information using psutil
ram_info = psutil.virtual_memory()
disk_info = psutil.disk_usage('/')

# Display RAM information
st.write(f"Total RAM: {ram_info.total / (1024 ** 3):.2f} GB")
st.write(f"Available RAM: {ram_info.available / (1024 ** 3):.2f} GB")

# Display disk storage information
st.write(f"Total Disk Space: {disk_info.total / (1024 ** 3):.2f} GB")
st.write(f"Available Disk Space: {disk_info.free / (1024 ** 3):.2f} GB")
