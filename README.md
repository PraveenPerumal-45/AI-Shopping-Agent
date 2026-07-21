![Python](https://img.shields.io/badge/Python-3.12-blue) ![LangChain](https://img.shields.io/badge/LangChain-Agent-green) ![Streamlit](https://img.shields.io/badge/Streamlit-App-red) ![Docker](https://img.shields.io/badge/Docker-Ready-blue) ![License](https://img.shields.io/badge/License-MIT-green)

# 🛒 AI Shopping Assistant

An intelligent shopping assistant built using **LangChain**, **Groq LLMs**, **Streamlit**, and **SQLite**.

The assistant helps users search products, compare ratings, shop using images, place orders, view previous purchases, and summarize shopping history using AI-powered tool calling.

---

## 🚀 Features

### 🔍 Smart Product Search

Search products using natural language.

Example:

> Find organic honey under $20 with rating above 4.5

The agent automatically:

- Searches the product database
- Retrieves customer ratings
- Filters products
- Presents the best matches

---

### ⭐ Product Ratings

Every product recommendation includes:

- Average customer rating
- Total review count

Ratings are fetched dynamically from the reviews database.

Example:

```
Organic Raw Honey
★ 4.62
128 Reviews
```

---

### 🖼️ Shop by Image

Upload a product image and the assistant will:

- Analyze the image using a Vision LLM
- Identify the product
- Search similar products
- Recommend matching products available in the store

---

### 🛍️ AI Checkout

After selecting a product, the assistant can place an order.

Example:

```
User:
Buy Organic Almonds

Assistant:
Order #15 confirmed!
```

Orders are stored in SQLite.

---

### 📦 Order History

The assistant remembers previous purchases.

Example:

```
What have I ordered before?

Show my previous orders

Have I bought honey before?
```

---

### 📊 Shopping Summary

Generate personalized shopping statistics.

Example:

```
Summarize my shopping history
```

Returns:

- Total Orders
- Total Money Spent
- Average Order Value
- Favorite Products

---

### 🛡️ Guardrails

The assistant only handles shopping-related requests.

Examples rejected:

```
Write me a poem

Tell me a joke

What's the weather?
```

This prevents prompt drift and keeps the assistant focused.

---

## 🏗️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | Web Interface |
| LangChain | AI Agent |
| Groq | LLM & Vision Models |
| SQLite | Product & Order Database |
| dotenv | Environment Variables |

---

## 📂 Project Structure

```
AI-Shopping-Assistant/
│
├── app.py
├── shopping_agent.py
├── setup_db.py
├── reviews_api.py
├── orders_api.py
├── guardrails.py
├── store.db
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/<your-username>/ai-shopping-assistant.git

cd ai-shopping-assistant
```

---

### Create Virtual Environment

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file.

```
GROQ_API_KEY=your_api_key_here
```

---

### Initialize Database

```bash
python setup_db.py
```

This creates:

- Products
- Reviews
- Orders

with sample data.

---

### Run Application

```bash
streamlit run app.py
```

---

## 💬 Example Queries

### Product Search

```
Find organic honey under $20

Show organic coffee

Recommend healthy snacks

Find olive oil with rating above 4
```

---

### Image Search

Upload an image and click

```
Find Similar Products
```

---

### Checkout

```
Buy Organic Almonds

Order number 2

Yes
```

---

### Order History

```
Show my order history

What have I bought before?

Have I ordered honey?
```

---

### Shopping Summary

```
Summarize my purchases

How much have I spent?

What do I buy the most?
```

---

## 🤖 AI Agent Workflow

```
                User
                  │
                  ▼
         Conversation Guardrail
                  │
                  ▼
           LangChain Agent
                  │
      ┌───────────┼─────────────┐
      │           │             │
      ▼           ▼             ▼
 Product Tool  Review Tool  Orders Tool
      │           │             │
      └───────────┼─────────────┘
                  │
                  ▼
              SQLite Database
```

---

## 🧠 Tools Used by the Agent

The agent uses multiple tools depending on the user's request.

### Product Search Tool

Search products using filters like:

- Product name
- Category
- Price
- Organic status

---

### Rating Tool

Retrieves:

- Average Rating
- Review Count

---

### Checkout Tool

Places an order and stores it in the database.

---

### Order History Tool

Returns previous purchases.

---

### Shopping Summary Tool

Generates shopping analytics.

---

### Vision Tool

Uses an image to identify products and recommend similar items.

---

## 🗄️ Database

The application uses SQLite.

### Products

- Product Name
- Category
- Price
- Organic Flag
- Description

---

### Reviews

- Product ID
- Rating
- Reviewer
- Review

---

### Orders

- Order ID
- Product
- Quantity
- Unit Price
- Total Price
- Status
- Order Date

---

## 📸 Screenshots

### Home

<img width="1917" height="921" alt="image" src="https://github.com/user-attachments/assets/c79ff200-8c5e-45c0-97a7-34105316f817" />


---

### Product Search

<img width="1915" height="871" alt="image" src="https://github.com/user-attachments/assets/e81087eb-435c-45d9-bb12-a64cc12f20c5" />


---

### Image Search

<img width="1917" height="890" alt="image" src="https://github.com/user-attachments/assets/e8bb8e1f-3f05-4946-ad2f-373a2334733d" />

<img width="1880" height="886" alt="image" src="https://github.com/user-attachments/assets/5619dd44-1189-422f-a474-b5ee3e69701d" />



---

### Order History

<img width="1917" height="881" alt="image" src="https://github.com/user-attachments/assets/6f976db1-d780-4257-bea5-200181558b8e" />


---

### Shopping Summary

<img width="1916" height="882" alt="image" src="https://github.com/user-attachments/assets/52b95493-1101-436f-a1c6-737935cfd4e3" />


---

### Guardrails

<img width="1917" height="866" alt="image" src="https://github.com/user-attachments/assets/e7d3352d-4ef4-40c3-af01-471a0bf811f8" />

<img width="1902" height="896" alt="image" src="https://github.com/user-attachments/assets/ea83ec55-f6b3-496d-a0b3-970746764a81" />



---

## 🎯 Future Improvements

- Personalized Recommendations
- Frequently Bought Together
- Multi-user Authentication
- Shopping Cart
- Wishlist
- Price Drop Notifications
- Product Comparison
- AI Product Summaries
- Order Tracking
- LangSmith Evaluation Dashboard

---

## Run with Docker

### Build the image

```bash
docker build -t shopping-agent .
```

### Run the container

```bash
docker run -p 8501:8501 --env-file .env shopping-agent
```

Open:

```
http://localhost:8501
```

## 📌 Learning Outcomes

This project demonstrates:

- AI Agent Development
- Tool Calling
- Retrieval-Augmented Tool Usage
- Vision Models
- Prompt Engineering
- Guardrails
- Streamlit Applications
- SQLite Integration
- Multi-tool Agent Orchestration

---

## 👨‍💻 Author

**Praveen Perumal**

- LinkedIn: [*Praveen Perumal*](https://www.linkedin.com/in/praveen-perumal/)
- GitHub: https://github.com/PraveenPerumal-45

---

## ⭐ If you found this project useful, consider giving it a star!
