# 🗃️ Chat with SQL & SQLite3 DB using Langchain
A powerful AI-enabled interface that allows users to interact with SQL databases (both SQLite3 and MySQL) using natural language. This project integrates Langchain, Groq’s LLaMA3-8B, and Streamlit to build a seamless, conversational SQL query assistant.

## 📌 Features
* 🧠 Ask questions in plain English — get SQL-generated answers from the database
* ⚙️ Supports both SQLite3 (local) and MySQL (remote) databases
* 🔐 Input secure connection details (host, user, password) directly from UI for MySQL
* 🧩 Powered by Langchain SQL Agent & Groq LLM for real-time query generation
* 🧾 Built-in student database with preloaded academic records for demo

## 🧠 Technologies Used
* Streamlit – Interactive frontend
* Langchain – SQL agent and toolkit orchestration
* Groq API – LLaMA3-8B for ultra-fast LLM responses
* SQLite3 – Lightweight embedded demo DB
* MySQL – External DB support via SQLAlchemy
* SQLAlchemy – Database abstraction and connectivity
* dotenv – Environment-based API key handling

## 🗂 Project Structure
```
├── app.py              # Main application logic
├── sqlite.py           # Script to create and seed SQLite3 DB (student.db)
├── student.db          # Local database with sample data
├── requirements.txt    # Dependencies
└── .env                # API keys (excluded from repo)
```

## ⚙️ Setup Instructions
1. Clone the Repository
```
git clone https://github.com/bhaskar2311/Chat-with-SQL-and-Sqlite3-DB-with-Langchain
cd Chat-with-SQL-and-Sqlite3-DB-with-Langchain
```
2. Create a Virtual Environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Setup Environment Variables
  * Create a .env file in the root directory and add your API keys like this:
```
# .env
GROQ_API_KEY=your_groq_key_here
```
🚨 Warning: Never commit .env files to public repositories.

## 🚀 How to Run
```
streamlit run app.py
```
#### 🧪 Options in the UI:
###### ✅ Use SQLite3:
* No DB credentials required
* Just enter your Groq API Key and start chatting with the local student.db file

###### ✅ Connect to MySQL:
* Enter your host, user, password, and database name along with your Groq API Key
* App will securely connect and interact with your remote DB

## 💬 Sample Queries
* "Show me all the students in the Optimization class"
* "What are the marks for section B?"
* "List names of students who scored above 80"

## 📸 Screenshots
✅ SQLite3 Mode
![Output 1 - SQLite3](https://github.com/user-attachments/assets/4e54d90a-2c11-4c48-8d84-3174d7520fca)
![Output 2 - SQLite3](https://github.com/user-attachments/assets/87a493ed-a1c8-4945-b506-925a9a9076c2)

✅ MySQL Mode
![Output 3 - MySQL](https://github.com/user-attachments/assets/1ad14213-bd80-4751-a50a-312116af75d3)

## 📝 Notes
This project was fully developed by me. The README was written based on my knowledge and experience, with support from generative AI tools to refine its structure and presentation.

## 📄 License
This project is open source and available under the MIT License.

## 🙋‍♂️ Author
Made with ❤️ by Bhaskar Shivaji Kumbhar
