# 🛠️ Toolsmith Agent
### A Multi-Tool AI Agent Powered by LangGraph, LangChain & Groq

**Toolsmith Agent** is a tool-calling AI agent that transforms natural-language requests into actionable tasks. Built with **LangGraph, LangChain, Groq, and Streamlit**, it dynamically selects and executes tools to answer questions, perform calculations, retrieve live weather information, and handle date-and-time queries.

Unlike a conventional chatbot that only generates text, Toolsmith Agent can invoke external tools, process their results, and use those results to formulate context-aware responses. It can also combine multiple tools to handle requests involving several steps.

---

## ✨ Key Features

- 🧠 **Agentic Tool Orchestration:** Uses LangChain's `create_agent` with LangGraph to coordinate tool selection, execution, and response generation.
- 🧮 **Calculator Tool:** Evaluates mathematical expressions using a restricted evaluation approach.
- 🌦️ **Live Weather Tool:** Retrieves current weather information using the Open-Meteo API, with geocoding support for city and country names.
- 🕒 **Date & Time Tool:** Retrieves the current date and time.
- 💬 **Conversational Memory:** Maintains chat history within a Streamlit session.
- 🔗 **Multi-Step Tool Execution:** Supports requests that require multiple tool calls before producing a final response.
- 🖥️ **Interactive Chat Interface:** Provides a conversational interface built with Streamlit.
- 🐳 **Docker Support:** Includes containerization for a reproducible application environment.

---

## 🏗️ Architecture

The project follows a modular architecture that separates tool implementations, agent orchestration, and the user interface.

```text
                    ┌──────────────────────┐
                    │       User           │
                    │ Natural-Language     │
                    │ Request              │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Streamlit UI      │
                    │       app.py         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     AI Agent         │
                    │      agent.py        │
                    │                      │
                    │  Groq LLM + Agent    │
                    │  LangGraph Runtime   │
                    └──────────┬───────────┘
                               │
                     Selects appropriate
                          tool(s)
                               │
             ┌─────────────────┼─────────────────┐
             ▼                 ▼                 ▼
    ┌────────────────┐ ┌──────────────┐ ┌────────────────┐
    │   Calculator   │ │    Weather   │ │   Date & Time  │
    │                │ │              │ │                │
    │ Mathematical   │ │ Open-Meteo   │ │ Current Date   │
    │ Expressions    │ │ API          │ │ & Time         │
    └────────┬───────┘ └──────┬───────┘ └────────┬───────┘
             │                │                  │
             └────────────────┼──────────────────┘
                              │
                              ▼
                    ┌──────────────────────┐
                    │   Tool Results       │
                    │  Returned to Agent   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Final AI Response   │
                    │  Displayed to User   │
                    └──────────────────────┘
```

### How It Works

1. **User Input:** The user submits a natural-language request through the Streamlit chat interface.
2. **Agent Reasoning:** The Groq-powered LLM determines whether a tool is needed and selects an appropriate tool based on the request.
3. **Tool Execution:** The selected Python function executes the requested operation, such as calculating an expression or retrieving weather information.
4. **Result Processing:** The tool returns its result to the agent, which can invoke additional tools when necessary.
5. **Response Generation:** The agent uses the available results to formulate a natural-language response.
6. **Conversation Continuity:** Chat history is maintained within the application session to support follow-up interactions.

---

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| LangChain | Tool integration and agent creation |
| LangGraph | Agent execution and orchestration |
| Groq | LLM inference |
| Streamlit | Interactive web interface |
| Open-Meteo API | Live weather data and geocoding |
| Docker | Containerization |

---

## 📂 Project Structure

```text
toolsmith-agent/
│
├── app.py              # Streamlit chat interface
├── agent.py            # LLM initialization and agent orchestration
├── tools.py            # Calculator, weather, and datetime tools
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration
├── .env.example        # Example environment configuration
├── .gitignore          # Files excluded from version control
└── README.md           # Project documentation
```

*The structure above reflects the modules described for this project. Adjust the file list if your actual repository differs.*

---

## 🚀 Getting Started

Follow these steps to run Toolsmith Agent locally.

### Prerequisites

- Python 3.10 or a compatible version supported by your dependencies
- A Groq API key
- Git
- Docker (optional)

### 1. Clone the Repository

```bash
git clone https://github.com/Aagashaaa/toolsmith-agent.git
cd toolsmith-agent
```

### 2. Create a Virtual Environment

**Windows (PowerShell)**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root and configure your Groq API key and the model name expected by your implementation.

For example:

```env
GROQ_API_KEY=your_groq_api_key
```

If your implementation reads a model name from an environment variable, add that variable as well.

**Security:** Never commit your `.env` file or expose your API key in source code.

### 5. Launch the Application

```bash
streamlit run app.py
```

Open the local URL printed in the terminal to access the application.

---

## 🐳 Running with Docker

If your repository includes a working `Dockerfile`, you can build and run the container.

### Build the Image

```bash
docker build -t toolsmith-agent .
```

### Run the Container

```bash
docker run --rm -p 8501:8501 --env-file .env toolsmith-agent
```

Open the local Streamlit URL shown for the application.

Ensure that your Docker configuration exposes port `8501` and starts Streamlit on `0.0.0.0` so the application is accessible outside the container.

---

## 💡 Example Use Cases

The following examples illustrate the kinds of requests the agent is designed to handle.

### 🧮 Mathematical Calculations

**User:**
> Calculate the compound interest on ₹10,000 at 8% annually for 3 years.

**Agent workflow:**
1. Identifies the mathematical calculation.
2. Invokes the calculator if the required expression is supported.
3. Returns the calculated result.

### 🌦️ Weather Information

**User:**
> What is the current weather in Coimbatore?

**Agent workflow:**
1. Identifies the location.
2. Uses geocoding to resolve the location.
3. Calls the Open-Meteo weather endpoint.
4. Presents the returned weather information.

### 🕒 Date and Time

**User:**
> What is today's date?

**Agent workflow:**
1. Recognizes that the request requires date-and-time information.
2. Calls the datetime tool.
3. Returns the result.

### 🔗 Multi-Tool Requests

**User:**
> Check the current weather in Chennai and tell me the date and time.

**Agent workflow:**
1. Identifies that the request requires weather and date-and-time information.
2. Invokes the appropriate tools.
3. Combines the results into a single response.

The exact sequence and number of tool calls depend on the agent's implementation and the LLM's tool-selection decisions.

---

## 🧠 Key Concepts Demonstrated

This project explores several important concepts in modern AI engineering.

**1. Tool Calling**

The LLM selects a tool and generates the structured arguments needed to invoke it. The actual computation or API request is performed by the corresponding Python function.

**2. Agent Orchestration**

LangGraph provides the execution framework for coordinating model calls, tool execution, and subsequent responses.

**3. Separation of Concerns**

Tool implementations, agent orchestration, and the user interface are kept in separate modules, making the code easier to maintain and extend.

**4. Stateful Conversations**

Conversation history allows the application to maintain context across interactions within a session. This is different from persistent memory across application restarts.

**5. External API Integration**

The weather tool demonstrates how an AI application can interact with an external service to retrieve information that may change over time.

---

## 🔮 Future Improvements

Potential enhancements include:

- 📈 **Observability:** Add tracing, structured logging, and component-level latency measurements.
- 🛡️ **Tool Safety:** Add strict input validation, execution limits, and robust error handling.
- 🧠 **Expanded Toolset:** Add tools for document search, web search, and other useful operations.
- 💾 **Persistent Memory:** Support conversation history across sessions using an appropriate storage mechanism.
- 🚀 **Deployment:** Host the application so it can be accessed through a public URL.
- ⚡ **Performance Optimization:** Measure model latency, token consumption, and the cost of individual requests.

These are potential improvements, not claims that the features are already implemented.

---

## 🎯 Project Objective

The goal of Toolsmith Agent is to explore how LLMs can move beyond text generation by selecting and executing tools to solve practical tasks.

By combining tool calling, agent orchestration, external API integration, and a conversational interface, the project provides a foundation for experimenting with more capable AI agents.

---

