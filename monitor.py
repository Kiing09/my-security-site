import requests
import time

# MISSION CONFIGURATION
TARGET_URL = "https://your-site-name.netlify.app" # Replace with your real link
CHECK_INTERVAL = 60 # Check every 60 seconds

def run_security_check():
    print(f"--- INITIATING SECURITY SCAN ON {TARGET_URL} ---")
    
    try:
        # The script "pings" your site
        response = requests.get(TARGET_URL)
        
        if response.status_code == 200:
            print("[STATUS: ONLINE] - Connection secure.")
            print(f"[LATENCY: {response.elapsed.total_seconds()}s]")
        else:
            print(f"[ALERT] - Status Code: {response.status_code}. Possible breach or downtime.")

    except Exception as e:
        print("[CRITICAL ERROR] - Could not reach server. Check uplink.")

# Run the loop
while True:
    run_security_check()
    print(f"Waiting {CHECK_INTERVAL} seconds for next scan...\n")
    time.sleep(CHECK_INTERVAL)