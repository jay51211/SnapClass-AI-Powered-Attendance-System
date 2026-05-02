<div align="center">

<br/>

<img src="https://i.ibb.co/YTYGn5qV/logo.png" alt="SnapClass Logo" width="110" />

<br/>
<br/>

# SnapClass

### AI-Powered Attendance System

**Dual biometric verification — Face Recognition + Voice Authentication — with instant QR onboarding**

<br/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Supabase](https://img.shields.io/badge/Supabase-Database-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com/)
[![dlib](https://img.shields.io/badge/dlib-Face%20AI-0078D4?style=for-the-badge)](http://dlib.net/)
[![License: MIT](https://img.shields.io/badge/License-MIT-F5A623?style=for-the-badge)](LICENSE)

<br/>

[**🚀 Getting Started**](#-getting-started) &nbsp;·&nbsp;
[**🧠 How the AI Works**](#-how-the-ai-works) &nbsp;·&nbsp;
[**🏗️ Architecture**](#%EF%B8%8F-architecture) &nbsp;·&nbsp;
[**📦 Tech Stack**](#-tech-stack) &nbsp;·&nbsp;
[**🗄️ Database**](#%EF%B8%8F-database-schema)

<br/>

</div>

---

## 📌 The Problem

Manual roll call wastes **5–10 minutes every lecture**. Students mark absent friends present. Proxy attendance goes undetected. Paper records get lost.

**SnapClass eliminates all of this.**

A teacher opens a session → displays a QR code → students scan it → the system verifies each student with their **face and voice** → attendance is marked automatically. The whole process takes **under 10 seconds per student**, with no human error and no proxy attendance possible.

```
Teacher creates session
        │
        ▼
  QR code displayed on projector
        │
        ▼
  Student scans QR with phone
        │
        ▼
  App opens · student logs in
        │
        ▼
  Auto-enrolled in session
        │
     ┌──┴──┐
     ▼     ▼
  📸 Face  🎙️ Voice
  Check    Check
     │     │
     └──┬──┘
        ▼
   Both pass? ✅
   Marked Present
```

---

## ✨ Features

<table>
<tr>
<td width="50%">

**🤖 AI Verification**
- 📸 Face recognition via 128-dim ResNet embeddings
- 🎙️ Voice verification via 256-dim speaker d-vectors
- 🔐 Dual biometric — both must pass to prevent spoofing
- 📊 Configurable confidence thresholds

</td>
<td width="50%">

**👩‍🏫 Teacher Tools**
- ➕ Create sessions with subject & duration
- 📲 Auto-generated QR code per session
- 📋 Live attendance dashboard
- 📥 Download CSV attendance report

</td>
</tr>
<tr>
<td width="50%">

**🎓 Student Experience**
- 📲 Scan QR → app opens → auto-enrolled instantly
- 🔒 Secure login with bcrypt-hashed passwords
- ⚡ Attendance marked in under 10 seconds
- 📱 Works on mobile browsers

</td>
<td width="50%">

**☁️ Backend**
- 🗄️ Supabase (PostgreSQL + Auth)
- 🔑 JWT session management built-in
- 🔗 Deep-link via `?join-code=` URL param
- 📦 No server management needed

</td>
</tr>
</table>

---

## 🧠 How the AI Works

### 📸 Face Recognition Pipeline

```
Webcam photo
     │
     ▼
dlib HOG detector ──► Finds face bounding box in image
     │
     ▼
ResNet-34 model ──────► Extracts 128-dimensional face embedding
     │                   (a unique fingerprint for each face)
     ▼
Euclidean distance ───► Compares new embedding vs stored embedding
     │
     ├── distance < 0.6  ──► ✅ VERIFIED
     └── distance ≥ 0.6  ──► ❌ REJECTED
```

The **128 numbers** represent facial geometry — distance between eyes, nose width, jawline shape, cheekbone structure. Two photos of the same person produce vectors that are very close together in this 128-dimensional space. Two different people produce vectors that are far apart.

---

### 🎙️ Voice Verification Pipeline

```
Microphone recording (3–5 sec)
     │
     ▼
librosa ──────────────► Resample to 16kHz · noise reduction · normalization
     │
     ▼
resemblyzer GE2E model ► Extracts 256-dimensional speaker d-vector
     │                   (unique voice fingerprint)
     ▼
Cosine similarity ────► Compares new d-vector vs stored d-vector
     │
     ├── similarity > 0.75  ──► ✅ VERIFIED
     └── similarity ≤ 0.75  ──► ❌ REJECTED
```

Cosine similarity measures the **angle** between two vectors, not their length — so it handles variations in speaking volume naturally. A whisper and a loud voice from the same person produce vectors pointing in the same direction.

---

### 🔐 Why Both Face AND Voice?

| Attack | Face alone | Voice alone | Face + Voice |
|---|---|---|---|
| Hold up a photo | ❌ Fooled | ✅ Caught | ✅ Caught |
| Play a voice recording | ✅ Caught | ❌ Fooled | ✅ Caught |
| Send a friend | ❌ Fooled | ❌ Fooled | ✅ Caught |
| Wear a mask | ❌ Fails | ✅ Works | ✅ Partial |

---

## 🏗️ Architecture

```
app.py                          ← Entry point: routing + QR deep-link handler
│
├── src/
│   ├── screens/
│   │   ├── home_screen.py      ← Landing page, login, role selection
│   │   ├── teacher_screen.py   ← Session creation, QR display, dashboard
│   │   └── student_screen.py   ← Join session, mark attendance
│   │
│   └── components/
│       ├── dialog_auto_enroll.py  ← Auto-enrol popup from QR deep-link
│       ├── face_capture.py        ← Webcam capture + face recognition
│       └── voice_capture.py       ← Mic recording + speaker verification
│
├── requirements.txt
├── .gitignore
└── .env                        ← Supabase credentials (not committed)
```

### Application Flow

```
Browser loads app.py
        │
        ├── login_type == 'teacher' ──► teacher_screen()
        ├── login_type == 'student' ──► student_screen()
        └── login_type == None      ──► home_screen()
                                              │
                    ┌─────────────────────────┘
                    │
              ?join-code=XYZ in URL?
                    │
             ┌──────┴──────┐
            YES             NO
             │               │
       Set role = student   Normal login page
       st.rerun()
             │
       auto_enroll_dialog(join_code)
             │
       Student confirms → enrolled in session
```

---

## 🗄️ Database Schema

```sql
-- Sessions created by teachers
CREATE TABLE sessions (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  teacher_id  UUID REFERENCES auth.users(id),
  subject     TEXT NOT NULL,
  join_code   TEXT UNIQUE NOT NULL,   -- encodes into QR code URL
  duration    INT,
  created_at  TIMESTAMPTZ DEFAULT now()
);

-- Which students are in which sessions
CREATE TABLE enrollments (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  student_id  UUID REFERENCES auth.users(id),
  session_id  UUID REFERENCES sessions(id),
  UNIQUE(student_id, session_id)
);

-- Attendance records
CREATE TABLE attendance (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  student_id  UUID REFERENCES auth.users(id),
  session_id  UUID REFERENCES sessions(id),
  status      TEXT DEFAULT 'present',
  timestamp   TIMESTAMPTZ DEFAULT now()
);

-- Face embeddings (128-float numpy array stored as JSON list)
CREATE TABLE student_face_data (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  student_id  UUID REFERENCES auth.users(id) UNIQUE,
  encoding    JSONB NOT NULL
);

-- Voice d-vectors (256-float array stored as JSON list)
CREATE TABLE student_voice_data (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  student_id  UUID REFERENCES auth.users(id) UNIQUE,
  embedding   JSONB NOT NULL
);
```

---

## 📦 Tech Stack

| Library | Role |
|---|---|
| `streamlit` | Python web UI framework — no HTML/CSS needed |
| `dlib-bin` | Face detection using HOG + SVM |
| `face_recognition_models` | Pre-trained ResNet for 128-dimensional face embeddings |
| `scikit-learn` | KNN classifier and distance metrics |
| `resemblyzer` | GE2E speaker encoder — 256-dimensional d-vectors |
| `librosa` | Audio preprocessing: resampling, noise reduction |
| `supabase` | Python client for Supabase (auth + database) |
| `bcrypt` | Salted password hashing — slow by design |
| `segno` | QR code generation |
| `pillow` | Image loading and manipulation |
| `numpy` | Fast numerical operations on embeddings |
| `pandas` | Attendance data as DataFrames + CSV export |

---

## 🚀 Getting Started

### Prerequisites

- Python **3.10 or higher** (required for `match/case` syntax in `app.py`)
- A [Supabase](https://supabase.com/) account — free tier works perfectly
- A working **webcam** and **microphone**
- **CMake** — required to build dlib

```bash
# Ubuntu / Debian
sudo apt-get install cmake build-essential libopenblas-dev liblapack-dev

# macOS
brew install cmake

# Windows — download from https://cmake.org/download/
# Also install Visual Studio Build Tools (C++ workload)
```

---

### Step 1 — Clone the repository

```bash
git clone https://github.com/jay51211/SnapClass-AI-Powered-Attendance-System.git
cd SnapClass-AI-Powered-Attendance-System
```

---

### Step 2 — Create a virtual environment

```bash
python -m venv venv

source venv/bin/activate          # Linux / macOS
venv\Scripts\activate             # Windows (CMD)
.\venv\Scripts\Activate.ps1       # Windows (PowerShell)
```

---

### Step 3 — Install dependencies

```bash
# Pin setuptools FIRST — required before dlib installs correctly
pip install "setuptools<70.0.0"

# Install all dependencies
pip install -r requirements.txt
```

> **dlib won't install?**
> - Try `pip install dlib` (compiles from source using CMake)
> - Apple Silicon Mac: `pip install dlib --no-cache-dir`
> - Ensure CMake is installed and on your PATH

---

### Step 4 — Set up Supabase

1. Go to [supabase.com](https://supabase.com/) → create a new project
2. Open the **SQL Editor** → paste and run the full schema from the [Database Schema](#%EF%B8%8F-database-schema) section
3. Go to **Project Settings → API** → copy your **Project URL** and **anon public key**

---

### Step 5 — Configure environment variables

Create a `.env` file in the project root:

```env
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=your-anon-public-key
```

> ⚠️ `.env` is already listed in `.gitignore` — it will never be committed to GitHub.

---

### Step 6 — Run the app

```bash
streamlit run app.py
```

The app opens at **http://localhost:8501** 🎉

---

## 👤 Usage Guide

### First-time Student Registration

1. Open the app → click **Register as Student**
2. Enter your email and a password
3. Allow **camera access** → take 3–5 photos from different angles
4. Allow **microphone access** → say your name clearly
5. Your biometric profile is saved — you won't need to do this again

### Teacher Workflow

| Step | Action |
|---|---|
| 1 | Log in → **Teacher Dashboard** |
| 2 | Click **Create Session** → enter subject & duration |
| 3 | Display the generated **QR code** on the projector |
| 4 | Watch the **live attendance table** update in real time |
| 5 | Click **Download CSV** to export the report |

### Student Workflow

| Step | Action |
|---|---|
| 1 | **Scan the QR code** — your phone opens the app |
| 2 | Log in with your credentials |
| 3 | Confirm joining the session in the popup |
| 4 | Click **Mark Attendance** → face the camera → say your name |
| 5 | ✅ Marked present — done! |

---

## 🔒 Security & Privacy

- **Passwords** — hashed with `bcrypt` (salted, slow by design) before storage. Raw passwords are never stored anywhere.
- **Biometrics** — only the **embedding vectors** (128 or 256 numbers) are stored, never the raw photos or audio recordings. Embeddings cannot be reversed into the original image or voice.
- **Dual factor** — requiring both face AND voice simultaneously makes proxy attendance extremely difficult.
- **Supabase RLS** — Row Level Security can be enabled so each user can only read and write their own data.
- **Environment variables** — credentials are stored in `.env` (gitignored) and never hardcoded in source.

---

## 🛣️ Roadmap

- [ ] **Liveness detection** — MediaPipe eye-blink / head-turn check to prevent photo spoofing
- [ ] **Parallel verification** — run face + voice checks simultaneously with `asyncio`
- [ ] **Offline mode** — cache embeddings in local SQLite for no-internet classrooms
- [ ] **Email notifications** — notify students when their attendance is recorded
- [ ] **Analytics dashboard** — attendance trends, per-subject heatmaps, absence alerts
- [ ] **Docker support** — multi-worker container deployment for large classes
- [ ] **Admin panel** — institution-level management with multiple teachers and courses

---

## ❓ FAQ

<details>
<summary><b>What Python version is required?</b></summary>
<br/>
Python 3.10 or higher. The <code>match/case</code> statement used in <code>app.py</code> is a Python 3.10+ feature.
</details>

<details>
<summary><b>Does it work on mobile?</b></summary>
<br/>
Yes. Streamlit is mobile-responsive. The QR scan → auto-enrol deep-link flow is designed specifically for mobile browsers.
</details>

<details>
<summary><b>What if a student wears a mask or glasses?</b></summary>
<br/>
Glasses usually work fine. Face masks will likely cause face recognition to fail. In that case, the teacher can mark attendance manually, or the student can retry later. Voice verification still works regardless of face covering.
</details>

<details>
<summary><b>Where are face and voice embeddings stored?</b></summary>
<br/>
As JSON arrays in Supabase PostgreSQL using the <code>JSONB</code> column type. No raw photos or audio recordings are ever saved anywhere in the system.
</details>

<details>
<summary><b>Can someone spoof the system with a photo or a recording?</b></summary>
<br/>
A photo will pass face recognition but fail voice verification. A voice recording will pass voice verification but fail face recognition. Both must be defeated simultaneously — which is extremely difficult in a real classroom setting.
</details>

<details>
<summary><b>dlib installation is failing. What do I do?</b></summary>
<br/>

1. Make sure CMake is installed: `cmake --version`
2. Try: `pip install dlib` (compiles from source)
3. Apple Silicon Mac: `pip install dlib --no-cache-dir`
4. Ubuntu: `sudo apt-get install cmake build-essential libopenblas-dev liblapack-dev` then retry

</details>

---

## 🤝 Contributing

Contributions are welcome!

```bash
# 1. Fork the repo and clone your fork
git clone https://github.com/YOUR_USERNAME/SnapClass-AI-Powered-Attendance-System.git

# 2. Create a feature branch
git checkout -b feature/your-feature-name

# 3. Make your changes and commit
git add .
git commit -m "feat: describe your change"

# 4. Push and open a Pull Request
git push origin feature/your-feature-name
```

Please open an **Issue** first to discuss any major changes before submitting a PR.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

<br/>

Built with ❤️ by **[Jay](https://github.com/jay51211)**

Inspired by [Shradha Khapra](https://github.com/shradha-khapra) · [Apna College](https://www.apnacollege.in/)

<br/>

**⭐ Star this repo if you found it useful — it helps others discover the project! ⭐**

<br/>

</div>
