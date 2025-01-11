# Mistral Multi-Tool Calling - Getting Started

This repository demonstrates how to use Mistral AI for multi-tool calling. It includes an example application (`app.py`) and helper functions (`tools.py`) to showcase the integration of various tools for tasks like weather updates, temperature control, light control, and more.

**Futher down are suggestions for AI Agents to build yourself :)**

## Features

- **Multi-tool calling**: The example integrates multiple tools for common smart home assistant tasks.
- **Dynamic responses**: The assistant generates responses based on user input and tool output.
- **Extendable architecture**: Easily add or modify tools to enhance functionality.

## Key Points Learned
- Use ```tool_choice="auto",``` in the API call. This way Mistral AI can select whether to use a tool function. The AI can then also answer not tool related questions. 
- Return tool answer in a JSON-like structure for the AI to understand. Returning a **string sentence** will throw the AI off 

## Installation

1. Clone the repository:
   ```bash
    git clone https://github.com/srothgan/mistral-multi-tool-calling.git
    cd mistral-multi-tool-calling
   ```

2. Create a Python virtual environment (optional but recommended):
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```bash
    pip install -r requirements.txt
   ```
4. Set up enviroment
    - Create a ```.env``` file in the project directory and add your API key:
    ```bash
    MISTRAL_API_KEY=your_api_key_here
    ```

## Usage
Run the example application:

```bash
python app.py
```
The application will simulate various user inputs and showcase:
- Retrieving weather information.
- Controlling smart home devices like lights and temperature.
- Making coffee or playing music.

## Extending the Example
This is only a demonstration/getting started guide for beginners to use and learn. It can easily be extended or modified. 
1. Add a new tool in ```tools.py``` with the desired functionality.
2. Update the tools list in ```tools.py``` and names_to_functions mapping in ```app.py```.
3. Adjust the system_prompt in ```app.py``` to guide the assistant on how to use the new tool.


### 1. HR-Agent

An intelligent assistant for streamlining recruitment processes and managing candidate evaluations.

  - **LinkedIn or Similar API Calls**: Fetch and analyze job profiles, resumes, or postings from platforms like LinkedIn.
  - **Web Search Integration**: Perform targeted searches to gather information about candidates or companies.
  - **Write Job Listings**: Automatically draft compelling job postings tailored to specific roles.
  - **Rank and Evaluate Applications**: Use AI to analyze resumes and rank applicants based on relevance, skills, and experience.

### 2. Stock Agent

A financial assistant for analyzing stocks, parsing data, and generating comprehensive investment reports.

  - **Search for a Stock**: Find stock data, historical trends, and market performance for a specific ticker.
  - **Find Yearly Report and Parse PDFs**: Automatically locate and extract key insights from company annual reports and SEC filings.
  - **Find Other Metrics and Evaluations**: Gather and analyze metrics like P/E ratios, growth rates, and industry benchmarks.
  - **Generate Comprehensive Reports**: Create detailed multi-chapter investment reports and output them as a professionally formatted PDF.

### 3. Customer Support Agent

An AI assistant designed to manage and resolve customer support cases efficiently.
  - **Identify Case Type**: Classify incoming customer queries into categories like product support, billing, or complaints.
  - **Require Specialized Agents**: Route specific cases to specialized agents, such as Customer Data, Order Management, or Complaint Handling agents.
  - **Handle Cases and Respond via Email**: Process cases end-to-end and draft professional email responses to customers.

---
