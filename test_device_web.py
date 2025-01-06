from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()

def test_device_web_interface(url):
    try:
        driver.get(url)  # Open IoT device's web dashboard
        time.sleep(2)
        
        # Check if page title is correct (can be adjusted based on actual page)
        assert "Device Dashboard" in driver.title
        
        # Validate if specific elements are visible (e.g., device status)
        status_element = driver.find_element(By.ID, "device-status")
        assert status_element.is_displayed(), "Device status not visible"
        
        print("Test passed: Device web interface is functioning correctly.")
        
    except AssertionError as e:
        print(f"Test failed: {e}")
        
    finally:
        driver.quit()

# Example URL of IoT device web interface
test_device_web_interface("http://iot-device.local")