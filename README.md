# 🚀 TestPilotAI

**TestPilotAI** is an autonomous AI-powered tool that interacts with websites like a real user — navigating, clicking, adding items to carts, and reporting back results.  
It’s powered by OpenAI's GPT-4o and a browser automation agent, making it ideal for simulating real-user workflows, QA testing, or intelligent scraping tasks.

---

## ✨ Features

- 🧠 **LLM Agent**: Uses GPT-4o to reason and interact intelligently.
- 🌐 **Browser Automation**: Navigate websites, click elements, and extract text.
- 📊 **Logs Results**: Get product names, prices, or page responses.
- 🔐 **.env Support**: Keep your API keys secure and flexible.

---

## 🧩 Tech Stack

- [`LangChain`](https://www.langchain.com/) + [`OpenAI`](https://platform.openai.com/) GPT-4o
- Custom `browser_use.Agent` module (or replaceable with Playwright/Selenium)
- Python `asyncio`
- `dotenv` for environment management

---

## 🚀 Getting Started

### 🔧 Prerequisites
- An OpenAI API key

---



### 1. Clone the Repository

```bash
git clone https://github.com/GiroeStefanBogdan/testpilotai.git
cd testpilotai
```

### 2. Create a .env File

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Create a virtual enviroment

```bash
python3 -m venv venv
```

### 4. Activate virtual enviroment

```bash
source venv/bin/activate
```

### 5. Install everything is in requirements.txt

```bash
pip install -r requirements.txt
```

### 6. Project Structure

```bash
testpilotai/
├── app.py               # Main app logic and agent runner
├── .env                 # Your secret keys 
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

### 7. How It Works

The app uses GPT-4o to interpret and execute a browser task like this: 

```bash
agent = Agent(
    task="""
    Go to https://automationteststore.com.
    Navigate to 'Fragrance', click on the first product.
    Add it to the cart.
    Tell me the name and price of the product.
    """,
    llm=ChatOpenAI(model="gpt-4o"),
)
result = await agent.run()
```

### 8. Example Use Cases

```bash
🧪 Example Use Cases
    ✅ Simulate E2E checkout flows
    🧪 Perform QA smoke tests before releases
    📦 Test product pages or add-to-cart logic
    🔍 Extract price and availability info
```

### 9. 📜 License

```bash
MIT License. Fork it, test it, improve it — open source all the way.
```

### 10. 🤝 Contributing

```bash
Pull requests and ideas welcome!
If you make it smarter, faster, or prettier — open a PR.
```

### 11. 📮 Contact

# Made with ❤️ by @GiroeStefanBogdan
