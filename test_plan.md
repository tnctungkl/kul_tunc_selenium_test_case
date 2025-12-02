# TEST PLAN – Inspector Popup Automation Suite  
Version: 1.0  
Planner: Tunç KUL  
Role: QA Tester 
Tech Stack: Python, Selenium WebDriver, Pytest, Allure 

---

## 1. Introduction
- This Test Plan defines the scope, objectives, approach, risks, and deliverables for the automation testing of the **Inspector Popup Component** used in the Onsite Experiment product.
- The purpose is to validate popup visibility logic, campaign metadata consistency, and responsive behavior on supported viewports.

---

## 2. Scope

### 2.1 In Scope
The automation covers the following flows:
- Popup visibility only on **Product Detail Pages**  
- Inspector reflecting correct campaign state  
- Campaign data validation **(Campaign ID, Name, Language, Custom Rule)**  
- Popup rendering and layout verification  
- Responsive behavior on **desktop, tablet, and mobile** 
- Negative scenario: Popup must **not** appear on home page

### 2.2 Out of Scope (for Now)
- Backend API validation  
- Database-level verification  
- Visual pixel-perfect UI comparison  
- Performance testing  
- Mobile native app validation  

---

## 3. Objectives

- Detect rendering issues and UI regressions early  
- Validate visibility rules against real campaign configurations  
- Ensure popup state matches Inspector state  
- Co
