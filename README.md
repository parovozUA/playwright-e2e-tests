# Playwright Automation Tests (Python)

This project was built to demonstrate real-world QA Automation skills, including handling edge cases, negative scenarios, and scalable test design.

Tested application: https://www.saucedemo.com/

---

## 🚀 Overview

The project covers core user flows of an e-commerce application:

- 🔐 Login (positive & negative scenarios)
- 📦 Inventory (data validation & sorting)
- 🛒 Cart (adding items)
- 💳 Checkout (form validation & full purchase flow)

The goal is not just to test UI, but to demonstrate **scalable test design**.

---

## ⚙️ Key Features

- **Page Object Model**
  Clear separation of UI logic and test logic

- **Data-driven testing**
  Test cases are modeled using `dataclasses` and executed via `pytest.mark.parametrize`

- **Reusable test models**
  Base case abstraction with built-in validation (e.g. required error messages)

- **Custom test data layer**
  Structured test data (users, forms, cases)

- **Automatic waits (Playwright)**
  No `sleep`, stable and reliable tests

- **Pytest fixtures**
  Reusable setup

- **Automatic screenshots on failure**
  Debug-friendly test runs via pytest hooks

---

## 🧠 Architecture

### Project Structure
```
data/  
  ├── models/   → dataclasses (User, Case, Form)  
  ├── cases/    → test scenarios (login, checkout)  
  └── test_data → predefined inputs  
tests/          → test scenarios  
pages/          → Page Objects (UI interactions)  
utils/          → helpers & assertions  
```
---

### Example: Data-driven test

```python
@pytest.mark.parametrize("case", LOGIN_CASES)
def test_login_form_validation(page, case):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(case.user)

    if case.should_pass:
        expect(page).to_have_url(...)
    else:
        assert_error_message(...)
```

---

### Example: Case model

```python
@dataclass(kw_only=True)
class BaseCase:
    name: str
    should_pass: bool
    error_message: str | None = None

    def __post_init__(self):
        if not self.should_pass and self.error_message is None:
            raise ValueError("error_message is required")
```

---

## 📊 Test Coverage

### Login
- valid user
- wrong username / password
- empty fields
- locked user
- error message validation
- error message close

### Inventory
- page load
- items count
- item names & prices validation
- sorting:
  - name (asc / desc)
  - price (asc / desc)

### Cart
- add item to cart
- cart badge update
- item presence in cart

### Checkout
- form validation (multiple cases)
- successful checkout flow
- error message handling
- edge cases (xfail for known issues)

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

## 🧪 Notes

- Inventory item count is assumed to be constant (6 items)
- Some negative checkout cases are marked as `xfail` due to known application limitations

---

## 🔮 Future Improvements

- CI integration (GitHub Actions)
- Allure reporting
- API layer testing (if backend available)
- Test data generation (faker)
- Parallel execution optimization
