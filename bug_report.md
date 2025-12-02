# BUG REPORT – Inspector Popup Rendering, Visibility Logic & DOM Integrity Issues

**Reporter:** Tunç KUL  
**Role:** QA Tester
**Environment:**  
- OS: Windows 11  
- Browser: Chrome 129  
- Automation: Selenium WebDriver (Python 3.14), Pytest, Allure  
- Target Host: piratesquad.rocks/
- Component: Onsite Experiment – Inspector Popup

---

## 1. Summary
Inspector popup fails to render on the Product Detail Page even under conditions where the Inspector panel reports “Visible” state. DOM contains duplicate popup containers and inconsistent rendering behavior across viewports.

This is confirmed as a **real product defect**, not a test automation error.

---

## 2. Description
While validating the Onsite Experiment popup component, the automation suite repeatedly encountered `TimeoutException` errors when waiting for the popup container to become visible. Manual investigation through Developer Tools confirmed:

- Popup is **not displayed**, although the Inspector shows status “Visible”.
- At least **two popup container nodes** exist in DOM → indicates potential template duplication or multiple script injections.
- Component renders inconsistently across **desktop, tablet, and mobile** breakpoints.
- No **loading animation, transition, or hidden-state indicator** is present.

---

## 3. Steps to Reproduce
1. Open PDP: **BASE_URL**
2. Wait for campaign trigger initialization (3–5 seconds).
3. Scroll to bottom → observe Inspector state.
4. Check Inspector → it reports **Visible**.
5. Inspect DOM → find duplicate popup container nodes.
6. Observe UI → no popup is actually shown.

---

## 4. Expected Result
- Popup should render visually when **Inspector status = Visible**.
- Only **one popup container** must exist in DOM.
- Responsive layout must adjust for **desktop/tablet/mobile**.
- Rendering logic must rely on consistent **visibility triggers**.

---

## 5. Actual Result
- Popup never renders (automation correctly times out).
- Inspector panel still reports “Visible”.
- DOM contains duplicated popup elements:
    -> Example: `.oxe-toast-container` appears more than once.
- In mobile view, zero rendering occurs despite container presence.

---

## 6. Impact Assessment
**Severity:** Critical
**Priority:** High to Prior High

**Impact Areas:**
- Conversion funnel  
- Experiment accuracy  
- UI consistency  
- Cross-platform rendering  
- Customer experience  

---

## 7. Evidence
- Failure screenshots: `/screenshots/FAILED_*`
- Allure reports: `/allure-results/`
- Repeated Selenium `TimeoutException` from explicit waits
- Manual DOM inspection (screenshots included in results)
- Network tab shows campaign loaded successfully → UI failure

---

## 8. Root Cause Hypothesis (QA Perspective)
- DOM duplicated by multiple injected scripts  
- Race condition between popup init & observer callbacks  
- CSS `visibility:hidden` / `display:none` overrides not reset  
- Failed hydration in script-injected components  
- Responsive breakpoints overriding absolute positioning  
- Unhandled asynchronous render lifecycle  

---

## 9. Recommendation
- Review popup initialization pipeline  
- Add render lifecycle logging  
- Remove duplicate root node injections  
- Introduce defensive checks in script loader  
- Ensure Inspector → Popup visibility state sync logic aligns  

---

## 10. Status
**Confirmed product defect. Not related to test automation.**  
Reported & reproducible manually and via Selenium.
