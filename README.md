# Simple Calculator Selenium Script

This repository contains a simple Selenium script that opens an online calculator page and performs a calculation.

## Python Script

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Optional: run Chrome headless
options = webdriver.ChromeOptions()
# options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get("https://www.online-calculator.com/full-screen-calculator/")
    time.sleep(3)

    iframe = driver.find_element(By.CSS_SELECTOR, "iframe")
    driver.switch_to.frame(iframe)

    driver.find_element(By.TAG_NAME, "body").send_keys("7+3=")
    time.sleep(1)

    print("Calculation completed: 7 + 3")
finally:
    driver.quit()
```

## Usage

1. Install dependencies:
   ```bash
   pip install selenium webdriver-manager
   ```
2. Run the script:
   ```bash
   python simple_calculator_selenium.py
   ```

## Google AI Professional Certificate

- **Certificate**: Google AI Professional Certificate
- **Completed**: May 2026
- **Credential URL**: [View Certificate](https://www.coursera.org/my-learning?myLearningTab=CERTIFICATES)
- **Skills**: AI fundamentals, machine learning, TensorFlow, and model deployment.

If you want to use this with a different calculator page, update the URL and element locators accordingly.
