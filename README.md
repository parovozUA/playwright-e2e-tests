# 🧪 Playwright UI Test Automation (Python)

Playwright-based UI automation project focused on scalable architecture, data-driven testing, and real-world QA practices.

Tested app: https://www.saucedemo.com/

---

## ⚙️ Stack

Python • Pytest • Playwright • Allure • GitHub Actions

---

## 🚀 Overview

Covers core e-commerce flows:

* Login (positive & negative scenarios)
* Inventory (data validation & sorting)
* Cart (add to cart flow)
* Checkout (form validation & full purchase flow)

Focus: **test design, maintainability, and scalability**

---

## 🧠 Architecture

```
data/  
  ├── models/   → dataclasses (User, Case, Form)  
  ├── cases/    → test scenarios (login, checkout)  
  └── test_data → predefined inputs  
tests/          → test scenarios  
pages/          → Page Objects (UI interactions)  
utils/          → helpers & assertions  
```

### Key decisions

* **POM** — isolates UI logic → maintainable tests
* **Data-driven testing** — scenarios separated from logic
* **BaseCase validation** — prevents invalid test definitions
* **Layered structure** — data / cases / pages → scalable architecture

---

## 🧪 Test Design

* Positive / negative scenarios
* Edge cases
* Form validation

Techniques:

* Equivalence Partitioning
* Boundary Value Analysis

---

## 📊 Reporting

* Allure integration
* Screenshots on failure
* Browser & environment metadata

📎 Report: [GitHub Pages](https://parovozua.github.io/playwright-ui-tests/)

---

## ▶️ Run

```bash
pip install -r requirements.txt
playwright install
pytest
```

---

## 🔍 Why this project

* not just UI checks — **data-driven architecture**
* reusable test models (no hardcoded inputs)
* negative + edge case coverage
* scalable structure
* CI + reporting ready(Allure + screenshots)

---

## 👤 Author

**Constantine P.** - [LinkedIn](https://www.linkedin.com/in/constantine-qa/)
