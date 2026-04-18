# Playwright E2E Tests (Python)

Automation testing framework built with **Playwright + Pytest** using Page Object Model.

## 🚀 Overview

This project demonstrates automated end-to-end testing of a web application using modern best practices.

Tested application: https://www.saucedemo.com/

Covered scenarios:

* ✅ Successful login
* ❌ Invalid login (multiple cases)
* 📦 Inventory page validation

---

## 🧱 Tech Stack

* Python
* Playwright
* Pytest
* Page Object Model (POM)

---

## ⚙️ Features

* 🔹 Clean Page Object architecture
* 🔹 Pytest fixtures (browser / context / page)
* 🔹 Data-driven tests using `@pytest.mark.parametrize`
* 🔹 Built-in Playwright auto-waits (no `sleep`)
* 🔹 Scalable structure for future tests

---

## 📁 Project Structure

```
playwright-e2e-tests/
│
├── pages/             # Page Objects
│   ├── BasePage.py
│   ├── LoginPage.py
│   └── InventoryPage.py
│
├── tests/             # Test cases
│   ├── conftest.py
│   └── test_login.py
│
├── utils/             # Helpers (optional)
├── data/              # Test data (optional)
└── README.md
```

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 2. Run tests

```bash
pytest
```

---

## 🧠 Key Design Decisions

* **Page Object Model**
  Separates UI logic from tests → improves maintainability

* **Fixtures (Pytest)**
  Handles browser lifecycle → reduces duplication

* **Locator API (Playwright)**
  Provides auto-wait → reduces flaky tests

* **Parametrize**
  Enables multiple test scenarios without duplication

---

## 🔧 Future Improvements

* Add Allure reporting
* Integrate with CI/CD (GitHub Actions)
* Add more test scenarios (cart, checkout)
* Introduce test data layer

---

## 📌 Notes

This project was built as part of my transition into QA Automation.

## Assumptions

- The inventory page always contains 6 items (as per current application behavior)