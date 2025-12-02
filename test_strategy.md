# TEST STRATEGY – Inspector Popup Component Automation

## 1. Overview
This strategy outlines the automation approach for validating the Inspector Popup component within the Onsite Experiment system. The component dynamically displays campaign-related visuals and metadata on specific product pages. Testing ensures consistent rendering, correct visibility logic, and alignment with campaign configuration.

---

## 2. Testing Pillars

### ✓ 2.1 Functional Accuracy
- Popup visibility must match rule-based triggers.  
- Inspector panel must reflect true campaign state.  
- DOM structure and rendering pipeline must behave deterministically.

### ✓ 2.2 User Interface Integrity
- Popup must display properly on all supported viewports.
- No DOM duplication or invalid HTML structures.
- Visual layout must not overflow or collapse.

### ✓ 2.3 Cross-Page Behavior
- Popup must appear **only** on PDP.  
- Home page and non-campaign pages must remain unaffected.

### ✓ 2.4 Automation Reliability
- Explicit waits, not fixed sleeps.  
- Fail-fast methodology (errors surfaced immediately).  
- Screenshots on all critical failures.  
- Allure step-level logging for traceability.

---

## 3. Test Architecture

### 3.1 POM (Page Object Model)
Structure:
- `ProductPage` (popup logic, PDP interactions)
- `InspectorPanel` (state validation, campaign metadata)
- `BasePage` (common actions)
- `Utilities` (waiter, driver factory, logging)
- `Config Layer` (settings, test data, environments)

Rationale:  
Modular, scalable, easy to maintain, onboarding-friendly.

---

## 4. Test Coverage

### 4.1 Visibility Logic
- Popup visible when rules satisfied  
- Popup hidden on home page  
- Inspector status transitions: Hidden → Visible  

### 4.2 Rendering Pipeline
- Element injection  
- DOM presence  
- Transition to visible state  
- Failure fallback behavior  

### 4.3 Campaign Metadata Validation
- Campaign ID  
- Rule ID  
- Language  
- Campaign Name  
- Matching inspector output  

### 4.4 Responsive Design
- Desktop (1920x1080)  
- Tablet (768x1024)  
- Mobile (375x812)  

---

## 5. Pass/Fail Criteria

### PASS:
- Popup renders correctly  
- Inspector & popup states match  
- No duplicated DOM nodes  
- All metadata fields match JSON test data  

### FAIL:
- Popup invisible despite valid rule  
- Inspector states inconsistent  
- DOM injection duplicated  
- Rendering broken in any viewport  
- Explicit wait timeout  

---

## 6. Risk Analysis

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Asynchronous render delays | Medium | High | Explicit waits |
| DOM duplication | High | Medium | DOM integrity checks |
| Responsive CSS overrides | High | Medium | Multi-viewport testing |
| Third-party script delays | Medium | High | Timeout handling |
| Network spikes | Low | Medium | Test retry mechanism (optional) |

---

## 7. Reporting Strategy

### ✓ Allure Reporting
- Step-level logs  
- Failure screenshots  
- Stacktrace + metadata  
- Viewport separation in reports  

### ✓ Bug Reports
Each unique failure → separate BUG_REPORT.md  
Includes evidence, screenshots, logs.

### ✓ Executive Summary
High-level explanation for PM, Engineering Manager, or Recruiter.

---

## 8. Final Assessment

Automation design aligns with:
- ISTQB test principles  
- Modern CI/CD expectations  
- Enterprise-grade POM standards  
- Scalable data-driven test methodology  

# REMINDER: 
- The strategy ensures high confidence in popup functionality and exposes real defects rapidly and reliably.