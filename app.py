import streamlit as st
import os
import psutil

# Use `os.system` to execute a command that retrieves the machine specs
machine_specs_command = "cat /proc/cpuinfo"  # Example command for Linux-based systems
machine_specs_output = os.popen(machine_specs_command).read()

# Display the machine specs in Streamlit
st.code(machine_specs_output, language='text')


# Get RAM and disk storage information using psutil
ram_info = psutil.virtual_memory()
disk_info = psutil.disk_usage('/')

# Display RAM information
st.write(f"Total RAM: {ram_info.total / (1024 ** 3):.2f} GB")
st.write(f"Available RAM: {ram_info.available / (1024 ** 3):.2f} GB")

# Display disk storage information
st.write(f"Total Disk Space: {disk_info.total / (1024 ** 3):.2f} GB")
st.write(f"Available Disk Space: {disk_info.free / (1024 ** 3):.2f} GB")
