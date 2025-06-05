# 🚀 Flask + MongoDB Atlas DevOps App

This is a simple web application built using Flask that connects to a MongoDB Atlas database and supports:

- ✅ Submitting form data and storing it in MongoDB Atlas
- ✅ Viewing a static JSON file through a `/api` route
- ✅ Handling success and error messages using Flask flash system

---

## 📦 Technologies Used

- **Flask** – Lightweight Python web framework
- **MongoDB Atlas** – Cloud-hosted NoSQL database
- **pymongo** – Python MongoDB driver
- **python-dotenv** – To manage secrets securely
- **HTML/CSS** – For the frontend form interface

---

## 🔧 How It Works

### `/`  
Displays a form where users enter their name and email. Upon successful submission, data is inserted into MongoDB Atlas.

### `/api`  
Reads a static `data.json` file and returns it as a JSON API response.

---

## 📁 Project Structure

flask-mongodb-devops-app/
│
├── app.py
├── .env
├── requirements.txt
├── data.json
└── templates/
└── form.html

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/flask-mongodb-devops-app.git
   cd flask-mongodb-devops-app
Create a .env file and add your MongoDB URI:

env
Copy
Edit
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
python app.py
📸 Screenshots
Add images of your form UI, JSON API, MongoDB Atlas collection, and CLI here.

🙌 Contributing
Feel free to fork this repo, use it for your own projects, or open a pull request for improvements!

📬 Contact
Sahil Verma
📧 sahilkumarverma301103@gmail.com
