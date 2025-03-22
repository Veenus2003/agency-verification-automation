import os
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("Error: GROQ_API_KEY is not set in environment variables!")

# Initialize Groq LLM with the selected model
chat_model = ChatGroq(model_name="llama3-8b-8192", groq_api_key=api_key)

def analyze_with_ai(text):
    prompt = f"""
    You are an AI that determines whether a website belongs to a digital agency.
    A digital agency provides services such as web design, web development, branding, digital marketing, or advertising.

    Analyze the following website content and classify it as either:
    - "Approved" (if it is an agency)
    - "Rejected" (if it is not an agency)

    Respond with ONLY "Approved" or "Rejected". Do NOT include explanations.

    Website Content:
    {text[:4000]}  # Limit to 4000 characters
    """

    try:
        response = chat_model.invoke([HumanMessage(content=prompt)])
        decision = response.content.strip()  # Clean response

        # ✅ Debugging: Show AI output
        print(f"Raw AI Response: {decision}")

        # ✅ Directly return the response if it's correct
        if decision in ["Approved", "Rejected"]:
            return decision
        else:
            print("Unexpected AI response, forcing rejection.")
            return "Rejected"

    except Exception as e:
        print(f"AI Response Error: {e}")
        return "Rejected"  # Default to rejected if AI fails


# ✅ Test case
if __name__ == "__main__":
    sample_text = "We are a digital agency specializing in web development and branding."
    print(analyze_with_ai(sample_text))  # Expected Output: "Approved" or "Rejected"
