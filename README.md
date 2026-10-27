<p align="center">
  <img src="https://raw.githubusercontent.com/visheshgupta0404/visheshgupta0404/11bc6108afb56bc74e687e3ed52e1844e10bd5d7/assets/profile-roles-v7.gif" width="1000" alt="Vishesh Gupta — static dotted name with animated AI/ML Engineer and Data Analyst roles.">
</p>

<p align="center">
  <code>AI / ML</code> &nbsp; × &nbsp; <code>DATA ANALYSIS</code> &nbsp; × &nbsp; <code>FULL-STACK SYSTEMS</code>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/visheshgupta0404"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square" alt="Connect on LinkedIn"></a>
  <a href="mailto:visheshg990@gmail.com"><img src="https://img.shields.io/badge/Email-Let's_talk-89EFAC?style=flat-square" alt="Email Vishesh"></a>
  <a href="https://leetcode.com/u/visheshgupta0404/"><img src="https://img.shields.io/badge/LeetCode-Practice-FFA116?style=flat-square&amp;logo=leetcode&amp;logoColor=FFA116" alt="LeetCode profile"></a>
</p>

<p align="center">
  <a href="#profilepy"><code>profile.py</code></a> &nbsp; / &nbsp;
  <a href="#projects"><code>projects/</code></a> &nbsp; / &nbsp;
  <a href="#stack"><code>stack/</code></a> &nbsp; / &nbsp;
  <a href="#repository-index"><code>index/</code></a>
</p>

## `profile.py`

```python
profile = {
    "name": "Vishesh Gupta",
    "education": "B.Tech · Computer Science",
    "focus": ["machine learning", "data analysis", "full-stack development"],
    "working_with": ["Python", "JavaScript", "Java", "SQL"],
    "learning": ["ML evaluation", "algorithms", "reliable system design"],
}
```

I build **data-driven applications**: NLP tools, chronological ML experiments, traceable analytics, and real-time web systems.

```text
raw data → clean features → models / analysis → APIs → usable interfaces
```

## `projects/`

Selected work across **real-time products, NLP, assessment systems, analytics, and ML research**. Private source repositories are labeled; public demos are linked where available.

### `01` [Syncora](https://github.com/visheshgupta0404/Syncora) &nbsp; `REALTIME · PWA`

Private watch-together rooms for up to six people, with shared YouTube playback, reusable playlists, invitations, and live chat.

```text
React client ↔ Supabase Realtime ↔ PostgreSQL room state
     └──────→ YouTube embedded player
```

**Engineering:** playback synchronization · room recovery · shared state · server-side search

`React` `Vite` `Supabase` `PostgreSQL` `Cloudflare Pages`

[Live app ↗](https://syncoramoments.pages.dev/) · [Source](https://github.com/visheshgupta0404/Syncora)

---

### `02` [PlagLe](https://github.com/visheshgupta0404/PlagLe) &nbsp; `NLP · DOCUMENT SIMILARITY`

Compare academic submissions through text extraction, TF-IDF vectors, and cosine similarity, then generate downloadable PDF reports.

```text
Documents → extracted text → TF-IDF → similarity scores → PDF report
React UI ↔ FastAPI ↔ MySQL
```

**Engineering:** document processing · text preprocessing · similarity scoring · API/database integration

`Python` `scikit-learn` `NLTK` `FastAPI` `MySQL` `React`

[Source ↗](https://github.com/visheshgupta0404/PlagLe)

---

### `03` [ExamEngine](https://github.com/visheshgupta0404/ExamEngine) &nbsp; `FULL STACK · ASSESSMENTS`

A multi-college assessment platform with separate student, professor, and administrator flows. Includes question authoring, timed attempts, autosave/recovery, written-answer grading, and controlled result release.

```text
Student / professor / admin → Google OAuth → PostgreSQL RPCs
                                      └→ timing, grading & access checks
```

**Engineering:** server-authoritative timing/grading · role and college boundaries · idempotent submissions

`JavaScript` `Supabase` `PostgreSQL` `OAuth / PKCE` `Node.js tests`

[Live app ↗](https://visheshgupta0404.github.io/ExamEngine/) · [Source & technical handoff](https://github.com/visheshgupta0404/ExamEngine)

<sub>Deployed implementation; real-account acceptance and hosted capacity checks remain launch requirements.</sub>

### `data-lab/`

#### [DispatchLens](https://github.com/visheshgupta0404/DispatchLens) &nbsp; `ANALYTICS · SQL` · private source

Investigate historical e-commerce delivery delays through ten dashboard views, seller/destination/category comparisons, a priority queue, and individual order evidence.

```text
Official CSVs → checksum audit → order-grain SQLite facts
                              → dashboard → order timelines & CSV evidence
```

**Evidence:** reconciled **83,696 eligible orders** and **5,930 late deliveries (7.09%)** for January 2017–June 2018 cohorts. SQL/UI parity and chronology checks support the analysis; findings are descriptive, not causal.

`Python` `SQLite` `SQL` `JavaScript` `Data quality` `GitHub Pages`

[Public dashboard ↗](https://visheshgupta0404.github.io/DispatchLens/) · [Case study · access required](https://github.com/visheshgupta0404/DispatchLens/blob/main/docs/case_study.md)

---

#### [NIFTY 50 Direction Prediction](https://github.com/visheshgupta0404/nifty50-direction-prediction) &nbsp; `ML · TIME SERIES` · private source

Research pipeline for next-session UP versus DOWN/FLAT classification, with audited trading-session labels, training-only imputation, chronological validation, and TreeSHAP explanations.

```text
Daily bars → session audit → returns features → chronological model selection
                                             → frozen holdout evaluation
```

**Evidence:** selected XGBoost achieved **54.10% accuracy** versus a **52.25% dummy baseline** on 488 eligible 2024–2025 sessions. The measured advantage is statistically uncertain; this is a research prototype, with no live app or demonstrated trading profitability.

`Python` `pandas` `NumPy` `scikit-learn` `XGBoost` `Matplotlib` `pytest`

[Research results · access required ↗](https://github.com/visheshgupta0404/nifty50-direction-prediction/blob/main/reports/summary.md)

---

#### [RoleRadar](https://github.com/visheshgupta0404/RoleRadar) &nbsp; `DATA PIPELINES · TEXT EXTRACTION` · private source

An India-focused job-skill intelligence MVP covering 13 career groups. Connects job-source APIs to normalized records, skill/co-occurrence reports, source evidence, profile comparisons, and CSV exports.

```text
Job APIs → validated records → SQLite → rule-based extraction
                                    → evidence reports + DuckDB / Parquet exports
```

**Engineering:** repeat-import safety · schema migrations · source traceability · annotation workflow · data-quality checks

`Python` `SQLite` `DuckDB` `Parquet` `JavaScript` `HTTP APIs`

[Project & methodology · access required ↗](https://github.com/visheshgupta0404/RoleRadar)

<sub>Local MVP. Extraction is rule-based; no measured real-data ML accuracy or public deployment is claimed.</sub>

## `stack/`

<p>
  <img src="https://img.shields.io/badge/Python-0D1117?style=flat-square&amp;logo=python&amp;logoColor=3776AB" alt="Python" />
  <img src="https://img.shields.io/badge/scikit--learn-0D1117?style=flat-square&amp;logo=scikitlearn&amp;logoColor=F7931E" alt="scikit-learn" />
  <img src="https://img.shields.io/badge/React-0D1117?style=flat-square&amp;logo=react&amp;logoColor=61DAFB" alt="React" />
  <img src="https://img.shields.io/badge/Node.js-0D1117?style=flat-square&amp;logo=nodedotjs&amp;logoColor=5FA04E" alt="Node.js" />
  <img src="https://img.shields.io/badge/FastAPI-0D1117?style=flat-square&amp;logo=fastapi&amp;logoColor=009688" alt="FastAPI" />
  <img src="https://img.shields.io/badge/PostgreSQL-0D1117?style=flat-square&amp;logo=postgresql&amp;logoColor=4169E1" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Docker-0D1117?style=flat-square&amp;logo=docker&amp;logoColor=2496ED" alt="Docker" />
  <img src="https://img.shields.io/badge/Git-0D1117?style=flat-square&amp;logo=git&amp;logoColor=F05032" alt="Git" />
</p>

```text
stack/
├── data-ml      pandas · NumPy · scikit-learn · XGBoost · NLTK
├── analytics    Plotly · Recharts · data cleaning · dashboards
├── interfaces   React · Tailwind CSS · Vite
├── services     Node.js · Express · FastAPI · Flask
├── realtime     Socket.IO · Supabase Realtime
├── storage      PostgreSQL · MySQL · MongoDB · SQLite · Firebase
└── delivery     Git · Docker Compose · GitHub Actions
```

<details>
<summary><strong>Full toolkit — technologies used across my projects</strong></summary>

| Area | Technologies & skills |
| :--- | :--- |
| **Languages** | Python · Java · JavaScript · SQL · C · C++ |
| **Data analysis** | pandas · NumPy · Data cleaning & normalization · Exploratory analysis · CSV/Excel processing |
| **ML & NLP** | scikit-learn · XGBoost · NLTK · TF-IDF · Cosine similarity · Logistic regression · Feature engineering · Chronological validation · TreeSHAP |
| **Data visualization** | Matplotlib · Plotly · Recharts · Chart.js · Interactive dashboards · Geographic & time-series visualization |
| **Frontend** | React · HTML · CSS · Tailwind CSS · Bootstrap · Vite · Framer Motion · Responsive design · PWAs |
| **Backend & real-time** | Node.js · Express · FastAPI · Flask · REST APIs · Socket.IO · Supabase Realtime · LLM API integration |
| **Databases** | PostgreSQL · MySQL · MongoDB/Mongoose · SQLite · Supabase · Firebase/Firestore · Redis · DuckDB/Parquet |
| **Android & IoT** | Android SDK · Java/XML layouts · Firebase Authentication · Sensor & media integration · Arduino |
| **Engineering** | Data structures & algorithms · OOP · Data pipelines · Schema migrations · Authentication · API integration · PDF report generation |
| **Tools & delivery** | Git · GitHub Actions · Docker Compose · npm · Gradle · Automated testing · ESLint · Prettier · Cloudflare Pages · Vercel · Render |

</details>

## `repository-index/`

<details>
<summary><strong>Browse all 24 repositories</strong></summary>

Private repositories require access to view their code.

| Repository | Short description |
| :--- | :--- |
| [Syncora](https://github.com/visheshgupta0404/Syncora) | Private watch-together rooms with shared YouTube playback, playlists, and live chat. |
| [PlagLe](https://github.com/visheshgupta0404/PlagLe) | Academic plagiarism detection with TF-IDF similarity, document comparison, and PDF reports. |
| [ExamEngine](https://github.com/visheshgupta0404/ExamEngine) | Multi-college assessments with role-based access, timed attempts, autosave, grading, and result release. |
| [DispatchLens](https://github.com/visheshgupta0404/DispatchLens) · private source | Historical delivery-delay analytics with SQL-backed metrics, investigation queues, and a [public dashboard](https://visheshgupta0404.github.io/DispatchLens/). |
| [nifty50-direction-prediction](https://github.com/visheshgupta0404/nifty50-direction-prediction) · private | Chronological ML research with audited trading-session labels, baseline comparisons, and frozen holdout evaluation. |
| [RoleRadar](https://github.com/visheshgupta0404/RoleRadar) · private | Job-skill analysis with API collection, text extraction, evidence views, and data-quality checks. |
| [PickMe](https://github.com/visheshgupta0404/PickMe) · private | A multiplayer social deduction game with an LLM-powered suspect and an experimental ML classifier. |
| [Retraction_Portal](https://github.com/visheshgupta0404/Retraction_Portal) · private | Research retraction analytics with interactive dashboards, geographic views, and comparison filters. |
| [BorrowMe](https://github.com/visheshgupta0404/BorrowMe) | An Android app for listing items, requesting loans, and managing borrowing and lending. |
| [IronRide](https://github.com/visheshgupta0404/IronRide) | A taxi-service website with booking, inquiry, and job-application APIs backed by MongoDB. |
| [Interactive-Calculator](https://github.com/visheshgupta0404/Interactive-Calculator) | A responsive calculator with expression parsing, saved history, unit conversion, and everyday maths tools. |
| [Weather-Location-Dashboard](https://github.com/visheshgupta0404/Weather-Location-Dashboard) | City weather and location details, including local time, humidity, and feels-like temperature. |
| [Weather-By-CityName](https://github.com/visheshgupta0404/Weather-By-CityName) | A simple city search for current temperature, location, and local time. |
| [Smart_Water_Leakage_Detection_System](https://github.com/visheshgupta0404/Smart_Water_Leakage_Detection_System) | Arduino-based water-leak detection with sensor monitoring, severity LEDs, and serial controls. |
| [Mobile-Application-Development](https://github.com/visheshgupta0404/Mobile-Application-Development) | Four Android apps exploring currency conversion, media playback, photo galleries, and sensors. |
| [tic-tac-toe-js](https://github.com/visheshgupta0404/tic-tac-toe-js) | A two-player browser game with turn tracking, win/draw detection, and automatic restart. |
| [ATM---Simulator](https://github.com/visheshgupta0404/ATM---Simulator) | A JavaScript ATM demo with deposits, withdrawals, and private balance state implemented using closures. |
| [Color-Code-Challenge](https://github.com/visheshgupta0404/Color-Code-Challenge) | A colour-matching browser game with random choices, scoring, and instant feedback. |
| [JavaScript](https://github.com/visheshgupta0404/JavaScript) · private | JavaScript exercises and mini-projects covering DOM interaction, events, games, and API calls. |
| [Node-Js](https://github.com/visheshgupta0404/Node-Js) · private | Node.js learning exercises covering modules, file handling, HTTP, routing, and Express middleware. |
| [DAA-Sem-4](https://github.com/visheshgupta0404/DAA-Sem-4) · private | Java coursework and practice in algorithm design and analysis. |
| [LeetCode](https://github.com/visheshgupta0404/LeetCode) · private | Java solutions to coding problems covering arrays, strings, searching, and other algorithm patterns. |
| [Checkups](https://github.com/visheshgupta0404/Checkups) · private | A small practice repository with a demo file. |
| [visheshgupta0404](https://github.com/visheshgupta0404/visheshgupta0404) | My GitHub profile README, project overview, and animated portfolio banner. |

</details>

---

<p align="center">
  <code>ideas → code → tests → iterate</code><br><br>
  <a href="mailto:visheshg990@gmail.com">Email</a> &nbsp; · &nbsp;
  <a href="https://www.linkedin.com/in/visheshgupta0404">LinkedIn</a> &nbsp; · &nbsp;
  <a href="https://github.com/visheshgupta0404?tab=repositories">Repositories ↗</a>
</p>
