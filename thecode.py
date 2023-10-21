import subprocess
import tkinter as tk
from selenium import webdriver

# Execute the command to retrieve the Wi-Fi network name
result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True)

# Parse the output to retrieve the network name
network_name = "Not connected to any Wi-Fi network."
for line in result.stdout.split('\n'):
  if 'SSID' in line:
    network_name = line.split(': ')[1].strip()

# Create a GUI window and display the network name in a label widget
window = tk.Tk()
window.title("PASSWDEXTRACTOR")
window.geometry("400x150")

name_label = tk.Label(window, text=f"Connected to: {network_name}")
name_label.pack(pady=10)

# Use selenium to retrieve the internet speed from fast.com
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
driver.get('https://fast.com')
speed = driver.find_element_by_id('speed-value').text
driver.quit()

# Display the internet speed in a label widget
speed_label = tk.Label(window, text=f"Speed: {speed} Mbps")
speed_label.pack(pady=10)

window.mainloop()


