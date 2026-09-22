# 🧪 TrendPilot: Multi-Level Test Cases

This document outlines the systematic test cases used to evaluate the dynamic behavior, prompt adaptability, state routing, and memory persistence of the TrendPilot Agentic AI system across varying complexity levels.

---

## 📋 Test Matrix Overview

| Test ID | Complexity Level | Topic | Target Tone | Expected Outcome | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Easy | Python Syntax (Missing brackets) | Humorous & Casual | Relatable, fast-paced script focusing on debugging frustrations. | ✅ Passed |
| **TC-02** | Medium | FastAPI & Pydantic Validation | Professional & Educational | Clear technical breakdown highlighting speed and type safety. | ✅ Passed |
| **TC-03** | Medium | YOLOv8 Real-Time Object Detection | High-Energy & Hyped | Dynamic visual cues and energetic hooks for computer vision. | ✅ Passed |
| **TC-04** | Hard | SQL to SQLAlchemy ORM Migration | Professional & Educational | Abstract database mapping translated into structured visual steps. | ✅ Passed |
| **TC-05** | Hard | Asynchronous Queues (Celery & Redis) | Professional & Educational | Advanced distributed system architecture structured for Reels. | ✅ Passed (Handled Timeout) |

---

## 📝 Detailed Test Specifications

### **Test Case 01: Easy & Casual**
* **Input Topic:** Forgetting to close a bracket or parenthesis in Python code
* **Selected Tone:** Humorous & Casual
* **Execution Flow:** 
  1. *Trend Generator* builds funny concepts around late-night syntax errors.
  2. *Script Writer* crafts a 45-second script focusing on the panic of a red terminal error log.
  3. *Hashtag Generator* produces a mix of Python and developer humor tags.
  4. *File Saver & Memory* logs the markdown to `outputs/generated_scripts/` and commits the full content to SQLite.

### **Test Case 02: Standard Technical Showcase (Medium)**
* **Input Topic:** Building a REST API using FastAPI and Pydantic validation
* **Selected Tone:** Professional & Educational
* **Execution Flow:** Focuses on code cleanliness, automatic Swagger documentation, and robust payload validation.

### **Test Case 03: High-Energy Tech (Medium)**
* **Input Topic:** YOLOv8 real-time object detection
* **Selected Tone:** High-Energy & Hyped
* **Execution Flow:** Emphasizes rapid-fire visual frames, bounding boxes, and instant inference speeds on live camera streams.

### **Test Case 04: Architectural Migration (Hard)**
* **Input Topic:** Migrating a Learning Management System database from raw SQL cursors to SQLAlchemy ORM
* **Selected Tone:** Professional & Educational
* **Execution Flow:** Balances database abstraction, session management, and maintainability benefits.

### **Test Case 05: Distributed Systems (Hard)**
* **Input Topic:** Implementing asynchronous background task queues with Celery and Redis for heavy machine learning pipelines
* **Selected Tone:** Professional & Educational
* **Execution Flow:** Translates heavy background architecture into sequential visual cues while documenting hardware timeout thresholds under local execution constraints.

* **TC-06 (Pandas Optimization):** Focuses on converting object types to category/int downcasting to save RAM.
* **TC-07 (Dockerization):** Translates `Dockerfile` layers and multi-stage builds into visual step-by-step actions.
* **TC-08 (JWT Auth):** Breaks down stateless token verification and secure password hashing with bcrypt.
* **TC-09 (WebSockets):** Highlights live chat event loops and instant client-server packet transmission.
* **TC-10 (Streamlit State):** Explains session dictionaries and `st.cache_data` decorators for high-performance apps.