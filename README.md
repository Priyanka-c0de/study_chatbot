**Study Bot: AI-Powered Academic Assistant**
    Study Bot is a stateful API designed to provide structured academic support to students. The system integrates Large Language Models (LLMs) with a NoSQL database to maintain conversation context and deliver   personalized tutoring.

**Project Deliverables**
     Hosted API Link: [https://study-chatbot-8pvi.onrender.com]
     Interactive Documentation: [https://study-chatbot-8pvi.onrender.com/docs]

**Technical Stack**
      Framework: FastAPI (Python)
      AI Orchestration: LangChain
      LLM Engine: Groq (openai/gpt-oss-20b)
      Database: MongoDB Atlas
      Cloud Infrastructure: Render

**System Architecture**
      The application is built on a modular, three-tier architecture:

Request Processing: The API receives a JSON payload containing a user_id and a question.
Context Retrieval: The system queries MongoDB Atlas for the last 10 messages associated with the user_id to provide contextual continuity.
Inference Logic: LangChain bundles the system-level academic instructions, the retrieved history, and the new query into a prompt for the Llama-3 model.
Data Persistence: The generated response and the original query are saved back to MongoDB with UTC timestamps for future recall.

**Key Features**
   Academic Scoping: The assistant is governed by system-level guardrails to ensure responses remain educational and professional.
   Persistent Memory: Unlike stateless bots, Study Bot retains context across multiple sessions using a dedicated database layer.
   CORS Support: Configured for cross-origin resource sharing, enabling seamless integration with web and mobile frontends.

**Installation and Setup**
Prerequisites
VS Code
Python 3.10 or higher
MongoDB Atlas Cluster
Groq API Key


Local Installation
Clone the repository:

Install the required dependencies:

Create a .env file in the root directory and configure the following:

Launch the application:

**API Documentation**
The API is fully documented via Swagger UI. To test the chat functionality, use the following endpoint:

POST /chat
Payload Structure:

Report: [https://drive.google.com/file/d/1_0v0UyiqAihypNjLsSfn-9gbeoCQr8xT/view?usp=sharing]
