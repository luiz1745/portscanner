🔍 Simple Port Scanner in Python
A lightweight and efficient script to identify open TCP ports on a specific host, using the Python standard socket library.

⚙️ How it works
The scanner sequentially attempts to connect to all TCP ports between 1 and 6534 on the configured IP.

For each attempt, if the connection is accepted, the port is considered open and displayed in the console.

Easy to customize for any IP on your network or allowed target.

🚀 How to use
Set the desired IP address by changing the LHOST variable in the script.

Run the script with Python 3 in the terminal:

bash
Copy
Edit
python3 portscanner.py
Wait for the result; the open ports will appear listed.

⚠️ Important warnings
Use this scanner only on networks and devices that you have explicit permission to test.

Scanning networks without authorization may violate local laws and terms of use.

📋 Requirements
Python 3.x installed

Standard socket library (already included in Python)
