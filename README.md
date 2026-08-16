# LangChain Projects

This project contains a few simple LangChain examples using different AI providers.

## Included examples

- Chat Model/groq_demo.py - Groq chat model example
- Chat Model/huggingface_demo.py - Hugging Face model example
- Chatbot/simple_chatbot_ui.py - Streamlit chatbot UI

## Setup

1. Create a virtual environment
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Add your API keys in the `.env` file

## Run the chatbot

```bash
cd Chatbot
streamlit run simple_chatbot_ui.py
```

## Notes

- Use `.env` to store API keys like `GROQ_API_KEY` and `HUGGINGFACEHUB_API_TOKEN`
- Keep the app private if you are using personal API keys
