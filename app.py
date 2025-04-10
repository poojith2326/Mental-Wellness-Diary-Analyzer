import streamlit as st
import google.generativeai as genai

# Set up Google Gemini API Key
GEMINI_API_KEY = "AIzaSyAgO5I6sN-2euuM_ZeomQG-ZVZ2EYqEOA4"
genai.configure(api_key=GEMINI_API_KEY)

# Streamlit UI Config
st.set_page_config(page_title="🧠 Mental Wellness Diary Analyzer", page_icon="🧘", layout="wide")

# Custom CSS for Styling
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 34px;
        font-weight: bold;
        color: #2196F3;
        text-shadow: 2px 2px 5px rgba(33, 150, 243, 0.4);
    }
    .sub-title {
        text-align: center;
        font-size: 18px;
        color: #bbb;
        margin-bottom: 20px;
    }
    .stButton button {
        background: linear-gradient(to right, #2196F3, #1976D2);
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 8px;
        transition: 0.3s;
    }
    .stButton button:hover {
        background: linear-gradient(to right, #1976D2, #0D47A1);
    }
    .result-card {
        background: rgba(33, 150, 243, 0.1);
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 10px;
        box-shadow: 0px 2px 8px rgba(33, 150, 243, 0.2);
    }
    .success-banner {
        background: linear-gradient(to right, #1976D2, #0D47A1);
        color: white;
        padding: 15px;
        font-size: 18px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
        margin-top: 15px;
        box-shadow: 0px 2px 8px rgba(33, 150, 243, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar instructions
st.sidebar.title("📝 How to Use")
st.sidebar.write("- Type your journal entry in the text box.")
st.sidebar.write("- The AI will analyze emotional tone, themes, and provide motivational advice.")
st.sidebar.write("- Use this tool daily for better emotional insight and encouragement.")

# Page Title
st.markdown('<h1 class="main-title">🧠 Mental Wellness Diary Analyzer</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Enter your journal entry to receive emotional insights and personalized tips</p>', unsafe_allow_html=True)

# Journal Entry Input
journal_entry = st.text_area("📔 Write your journal entry here:", height=250)

# Analysis Function
def analyze_journal_entry(entry):
    model = genai.GenerativeModel("learnlm-1.5-pro-experimental")
    prompt = f"""
    Analyze the following journal entry: {entry}

    1. Determine the emotional tone (e.g., happy, stressed, anxious, hopeful).
    2. Identify recurring themes or sentiments.
    3. Provide 2-3 personalized motivational tips or advice to improve emotional well-being.
    """
    response = model.generate_content(prompt)
    return response.text.strip() if response else "⚠ Unable to analyze entry."

# Submit Button
if st.button("🧠 Analyze Entry"):
    if not journal_entry.strip():
        st.warning("⚠ Please write something in your journal entry before submitting.")
    else:
        with st.spinner("🔍 Analyzing your entry..."):
            analysis = analyze_journal_entry(journal_entry)

        st.markdown('<div class="result-card"><b>🧾 Emotional Insight Report</b></div>', unsafe_allow_html=True)
        st.write(analysis)
        st.markdown('<div class="success-banner">💡 Reflection Complete! Keep journaling to grow. 🌱</div>', unsafe_allow_html=True)
        st.balloons()
