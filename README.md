# 🚀 AI Event Organizer

A full-stack event management application that uses AI to simplify planning, organizing, and managing events.
Built with FastAPI, Next.js, and OpenAI.

---

## 📌 Overview

Planning events can be repetitive and time-consuming.
This project aims to reduce that friction by integrating AI into the workflow — helping users generate ideas, manage schedules, and interact through a simple interface.

The system is designed as a clean full-stack application with a modern frontend and a lightweight backend.

---

## ✨ Features

* Create and manage events easily
* AI-assisted suggestions for event planning
* Chat-based interaction for quick inputs
* Clean and responsive UI
* Fast backend with REST APIs

---

## 🛠 Tech Stack

**Frontend**

* Next.js (React framework)
* JavaScript
* Tailwind CSS

**Backend**

* FastAPI (Python)
* SQLite database
* OpenAI API integration

---

## 📂 Project Structure

```text
ai-event-organizer/
│
├── backend/        # FastAPI server
├── frontend/       # Next.js app
├── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/JatinDhyani01/ai-event-organizer.git
cd ai-event-organizer
```

---

### 2. Backend setup

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend will run on:
http://127.0.0.1:8000

---

### 3. Frontend setup

```bash
cd frontend
npm install
npm run dev
```

Frontend will run on:
http://localhost:3000

---

## 🔑 Environment Variables

Create the following files:

### backend/.env

```
OPENAI_API_KEY=your_openai_api_key
```

### frontend/.env.local

```
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

---

## 🚧 Current Status

This project is under active development.
Core features are implemented, and improvements are ongoing.

---

## 🚀 Future Improvements

* User authentication system
* Persistent user-specific event storage
* Calendar and reminder integration
* Deployment to cloud (Vercel + Render)

---

## 👤 Author

Jatin Dhyani

---

## 📄 License

This project is open for learning and personal use.
