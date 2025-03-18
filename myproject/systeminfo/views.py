from django.http import HttpResponse
import os
import subprocess
import getpass
from datetime import datetime
import pytz

def htop(request):
    # Get system details
    full_name = "Shonit Yadav"  # Replace with your actual name
    username = getpass.getuser()  # FIXED: Use getpass.getuser() instead of os.getlogin()
    
    # Get current time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z%z')
    
    # Get top command output
    try:
        top_output = subprocess.check_output("top -b -n 1", shell=True, text=True)
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"

    # HTML Output
    response = f"""
    <h2>Name: {full_name}</h2>
    <h3>Username: {username}</h3>
    <h3>Server Time (IST): {server_time}</h3>
    <h4>TOP Output:</h4>
    <pre>{top_output}</pre>
    """
    
    return HttpResponse(response)
