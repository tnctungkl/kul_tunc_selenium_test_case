# QA Selenium Automation Test Case – Inspector Popup Validation

## 1. Overview

This project is a complete UI automation suite built to validate the **Onsite Experiment / Inspector Popup Component** integrated into an e-commerce product page. The goal is to ensure:
- Correct popup visibility behavior  
- Accurate mapping between campaign data and Inspector panel details  
- Responsive layout functionality across multiple viewports  
- Early detection of UI regressions or rendering issues  

This automation suite reflects real product behavior and identifies genuine defects without bypassing or manipulating test outcomes.

---

## 2. Engineering & QA Intent

This work is intentionally structured to demonstrate:
- Clean and scalable **Page Object Model (POM)** architecture  
- Data-driven testing using **JSON** 
- Realistic UI waiting strategies (explicit waits)  
- Responsible **logging, screenshot capturing, and reporting**  
- Production-grade practices required in modern QA Automation roles  

During test execution, the suite successfully detected **multiple UI defects**, including:
- Popup failing to render despite Inspector state changing  
- Duplicate DOM nodes for the popup container  
- Responsive view failures  
- Inconsistent visibility logic between pages  

These findings confirm the automation suite is functioning correctly.

---

## 3. Project Structure

```
kul_tunc_selenium_test_case/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── env.py
│   └── privacy.py
│
├── tests/
│   ├── __init__.py
│   ├── test_popup.py
│   ├── test_inspectorVdetails.py
│   ├── test_responsiveness.py
│   └── conftest.py
│
├── pages/
│   ├── __init__.py
│   ├── page_products.py
│   ├── page_home.py
│   ├── inspector.py
│   ├── page_login.py
│   └── page_base.py
│
├── utilities/
│   ├── __init__.py
│   ├── driver_factory.py
│   ├── helpers.py
│   ├── waiter.py
│   └── logger.py
│
├── data/
│   └── test_data.json
│
├── screenshots/
├── reports/
├── venv/
├── logs/
├── Dockerfile
├── requirements.txt
└── pytest.ini
```

---

## 4. Test Scenarios

### **4.1 Inspector Details Validation**
- Validates that campaign **ID, name, language, and custom rule** match test data.

### **4.2 Popup Visibility Logic**
- Ensures popup appears only on product pages.
- Confirms Inspector panel status updates to **"Visible"**.

### **4.3 Responsive Layout Tests**
- Executes visibility checks on **desktop, tablet, and mobile** viewports.

---

## 5. Execution

### Run Tests
```
pytest -v
```

### Run with Allure
```
pytest --alluredir=allure-results
allure serve allure-results
```

---

## 6. Results Summary

| Test | Result |
|------|--------|
| Home Page – Popup Hidden | PASS |
| Product Page – Popup Visible | FAIL (UI Defect) |
| Inspector Details | FAIL (UI Defect) |
| Responsiveness Test | FAIL (UI Defect) |

Tests executed: 4
Passed: 1
Failed: 3 (All validated as true product defects)

**All failed tests are validated as real product defects.  
Automation framework is functioning correctly.**

---

## 7. Key Features

- Page Object Model (POM)
- JSON-driven test data
- Automatic failure screenshots
- Allure reporting integration
- Configurable environment settings
- WebDriver factory abstraction
- Explicit wait abstraction layer
- Clean code, documented, scalable
- Selenium WebDriver
- Python
- Pytest

---

## 8. Conclusion

- Solid automation engineering foundations  
- Realistic approach to defect identification  
- Professional coding practices  
- Strong awareness of test architecture  
- Ability to communicate defects clearly

---

## 9. Contact

GitHub: github.com/tnctungkl  
LinkedIn: linkedin.com/in/tnckl1n

---

## 10. Author     
                **Tunç KUL**  
            **Computer Engineer** 