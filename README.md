# 🤖 AI Test Case Generator Agent

Generate high-quality QA test cases automatically from User Stories and Acceptance Criteria using Large Language Models (LLMs).

---

# 📌 Overview

AI Test Case Generator is an intelligent QA assistant that helps testers, SDETs, Business Analysts, and Product Owners quickly generate structured test cases from requirements.

Instead of manually creating test cases, users simply provide:

* User Story
* Acceptance Criteria

The system generates:

* Positive Test Cases
* Negative Test Cases
* Validation Scenarios
* Boundary Cases
* Structured Test Steps
* Expected Results
* Priority

The generated test cases can be exported directly to Excel.

---

# 🚀 Features

✅ AI-Powered Test Case Generation

✅ User Story Analysis

✅ Acceptance Criteria Processing

✅ Structured JSON Output

✅ Excel Export

✅ Modern Streamlit UI

✅ OpenRouter Integration

✅ Multi-LLM Support

✅ Easy Deployment

---

# 🖥️ Application Preview

## Input

```text
As a registered user

I want to login using email and password

So that I can access my dashboard
```

## Acceptance Criteria

```text
1. User enters valid email and password

2. Dashboard should load

3. Invalid password should show error

4. Empty fields should show validation

5. Locked account should not login
```

---

## Output

| Scenario         | Steps                     | Expected Result      | Priority |
| ---------------- | ------------------------- | -------------------- | -------- |
| Valid Login      | Enter valid credentials   | Dashboard displayed  | High     |
| Invalid Password | Enter wrong password      | Error displayed      | High     |
| Blank Email      | Leave email blank         | Validation displayed | Medium   |
| Blank Password   | Leave password blank      | Validation displayed | Medium   |
| Locked Account   | Login with locked account | Access denied        | High     |

---

# 🏗 High Level Architecture

```text
User Story
      ↓

Acceptance Criteria
      ↓

Prompt Template (.md)
      ↓

OpenRouter LLM
      ↓

Structured JSON Response
      ↓

Streamlit UI
      ↓

Excel Export
```

---

# 📂 Project Structure

```text
test-case-agent/

├── app.py

├── agents/
│   └── testcase_agent.py

├── prompts/
│   └── testcase_generation.md

├── utils/
│   ├── parser.py
│   └── excel_writer.py

├── output/

├── .env

├── README.md

└── .gitignore
```

---

# ⚙️ Tech Stack

| Component       | Technology             |
| --------------- | ---------------------- |
| Language        | Python 3.12+           |
| UI              | Streamlit              |
| LLM Gateway     | OpenRouter             |
| Models          | GPT-4o, Claude, Gemini |
| Data Processing | Pandas                 |
| Excel Export    | OpenPyXL               |
| Environment     | UV                     |
| Secrets         | Dotenv                 |

---

# 📦 Installation

## Step 1 - Install UV

Mac/Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify

```bash
uv --version
```

---

## Step 2 - Clone Repository

```bash
git clone https://github.com/ANSHULAGARWAL09/test-case-agent.git

cd test-case-agent
```

---

## Step 3 - Install Dependencies

```bash
uv sync
```

or

```bash
uv add openai
uv add streamlit
uv add pandas
uv add openpyxl
uv add python-dotenv
```

---

# 🔑 OpenRouter Setup

## Create API Key

Visit:

https://openrouter.ai

### Steps

1. Sign Up
2. Login
3. Click API Keys
4. Generate New Key

Example:

```env
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxx
```

---

# 🔒 Create .env

```env
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxx
```

---

# ▶️ Run Application

```bash
uv run streamlit run app.py
```

Application URL:

```text
http://localhost:8501
```

---

# 📝 Prompt Engineering

Prompts are stored inside:

```text
prompts/testcase_generation.md
```

Benefits:

* Easy maintenance
* Version control
* Prompt experimentation
* Model switching

---

# 📤 Excel Export

Generated test cases can be downloaded as:

```text
generated_testcases.xlsx
```

Useful for:

* QA Documentation
* Test Execution
* Jira Import
* TestRail Upload
* Client Deliverables

---

# 🛣 Roadmap

## Phase 1 — Foundation ✅

* Project Setup
* OpenRouter Integration
* Prompt Templates
* Streamlit UI
* Excel Export

---

## Phase 2 — Context Awareness 🚧

* RAG Integration
* Existing Test Case Repository
* Company Standards
* Historical Test Cases

---

## Phase 3 — Integrations 🚧

* Jira Integration
* TestRail Integration
* Zephyr Scale Integration
* Azure DevOps Integration

---

## Phase 4 — Multi-Agent QA System 🚧

### Test Case Agent

Generate Test Cases

### Test Data Agent

Generate Synthetic Test Data

### Defect Triage Agent

Analyze and Prioritize Bugs

### Execution Insights Agent

Analyze Execution Trends

---

## Phase 5 — Enterprise Ready 🚧

* SSO Authentication
* Role-Based Access
* Audit Logs
* Monitoring
* CI/CD Deployment
* Docker Support

---

# 🎯 Future Enhancements

* Multi-Language Support
* AI Test Scenario Review
* Requirement Gap Detection
* Duplicate Test Case Detection
* Risk-Based Test Generation
* Requirement Coverage Matrix
* Test Automation Script Generation
* AI Agent Collaboration

---

# 👨‍💻 Author

## Anshul Agarwal

QA Engineer | AI Enthusiast | Automation Architect

Building intelligent QA tools using AI, Automation, and Modern Engineering Practices.

### GitHub

https://github.com/ANSHULAGARWAL09/

### LinkedIn

https://www.linkedin.com/in/anshulagarwal30/

### Email

[anshulagarwal711@gmail.com](mailto:anshulagarwal711@gmail.com)

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

⭐ Share it with your network

⭐ Connect on LinkedIn

⭐ Contribute new ideas and enhancements

---

# 📜 License

MIT License

Feel free to use, modify, and extend this project.




<img width="1328" height="698" alt="image" src="https://github.com/user-attachments/assets/d9dcebd3-f25b-49fb-847e-e27081904d85" />
<img width="1218" height="1288" alt="image" src="https://github.com/user-attachments/assets/e6bd1c6e-4a6b-4b22-a209-d2883a05138f" />
<img width="1326" height="388" alt="image" src="https://github.com/user-attachments/assets/a410248e-5d1e-4e97-9d00-121215ca8a72" />
