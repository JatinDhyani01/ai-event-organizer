# 🚀 AI Event Organizer

An AI-powered full-stack event management system built using FastAPI, Next.js, and OpenAI.

---

## 🧠 Features

* 📅 Create & manage events
* 🤖 AI chatbot for event interaction
* ⚡ Fast backend with FastAPI
* 🎨 Modern UI with Next.js
* 💾 SQLite database

---

## 🛠 Tech Stack

* **Frontend:** Next.js, React
* **Backend:** FastAPI, Python
* **Database:** SQLite
* **AI:** OpenAI API

---

## 📂 Project Structure

```
ai-event-organizer/
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── .env
├── ai-event-frontend/
│   ├── app/
│   ├── components/
│   ├── .env.local
```

---

## ⚙️ Setup

### 1. Clone

```
git clone https://github.com/JatinDhyani01/ai-event-organizer.git
cd ai-event-organizer
```

---

### 2. Backend

```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

---

### 3. Frontend

```
cd ai-event-frontend
npm install
npm run dev
```

---

## 🔐 Environment Variables

### Backend `.env`

```
OPENAI_API_KEY=your_api_key
```

### Frontend `.env.local`

```
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

---

## 🚀 Future Improvements

* Authentication (JWT)
* Deployment (Vercel + Render)
* AI recommendations
* Notifications

---

## 👨‍💻 Author

Jatin Dhyani
