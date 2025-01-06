import requests
import json

def test_device_api(endpoint):
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        try:
            data = response.json()
            # Check if data contains expected keys
            assert "device_id" in data, "Missing device_id"
            assert "status" in data, "Missing status"
            
            print("API Test Passed: Data integrity validated.")
        except (json.JSONDecodeError, AssertionError) as e:
            print(f"API Test Failed: {e}")
    else:
        print(f"API Test Failed: HTTP Status {response.status_code}")

# Example API endpoint of IoT device
test_device_api("http://iot-device.local/api/status")