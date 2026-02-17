import streamlit as st
import pickle

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="AI vs HUMAN", page_icon="👾", layout="wide")

# --- 2. CUSTOM CSS FOR RETRO STAGE VIBE ---
st.markdown("""
    <style>
    # .stApp {
    #     background: linear-gradient(135deg, #ff9a9e, #fad0c4, #a6c1ee);
    # }
    # h1, h2, h3, label {
    #     color: black;
    #     font-weight: bold;
    # }
            
    /* 2. CRT Scanline Overlay for Gaming Vibe */
    .stApp::before {
        position: absolute;
        top: 0; left: 0; bottom: 0; right: 0;
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), 
                    linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
        z-index: 2;
        background-size: 80% 3px, 3px 80%;
        pointer-events: none;
    }

    /* 3. Global Text & Font Styles */
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4 {
        font-family: 'Press+Start+2P', cursive !important;
        color: #e1a8f0 !important; /* Neon Green */
        text-shadow: 1px 1px #FF00FF; /* Pink shadow for retro contrast */
    }
    
    /* 4. Glassmorphism Boxes (Disco Floor Style) */
    .stTextArea, .stButton, div[data-testid="stVerticalBlock"] > div {
        background: rgba(20, 0, 40, 0.8) !important; /* Dark purple translucent */
        padding: 10px;
        border-radius: 10px;
        border: 2px solid #FF00FF;
        box-shadow: 0 0 1px #e1a8f0; /* Exterior Glow */
    }        

    /* 4. Semi-transparent boxes for readability */
    .stTextArea, .stButton, div[data-testid="stVerticalBlock"] > div {
        background: rgba(0, 0, 0, 0.7); /* Dark semi-transparent background */
        padding: 10px;
        border-radius: 10px;
        border: 3px solid #e1a8f0;
    }

    /* 5. Button Style */
    .stButton>button {
        width: 100%;
        border: 4px solid #e1a8f0 !important;
        background-color: #111 !important;
        color: #e1a8f0 !important;
        font-size: 20px !important;
    }
    
    .stButton>button:hover {
        background-color: #e1a8f0 !important;
        color: #000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOAD MODELS ---
@st.cache_resource
def load_models():
    # Ensure these names match your .sav files
    with open('ai_vs_human_model.sav', 'rb') as f:
        model = pickle.load(f)
    with open('tfidf_vectorizer.sav', 'rb') as f:
        tfidf = pickle.load(f)
    return model, tfidf

model, tfidf = load_models()

# --- 4. BATTLE ARENA UI ---
st.markdown("<h2 style='text-align: center;'>BATTLE OF THE TEXTS</h2>", unsafe_allow_html=True)

# Fighting Positions
col1, col2, col3 = st.columns([2, 1, 2])
with col1:
    st.markdown("<h1 style='text-align: center; font-size: 80px;'>👤</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'> PLAYER </p>", unsafe_allow_html=True)
with col2:
    st.markdown("<h1 style='text-align: center; margin-top: 40px;'>VS</h1>", unsafe_allow_html=True)
with col3:
    st.markdown("<h1 style='text-align: center; font-size: 80px;'>🤖</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'> ROBOT </p>", unsafe_allow_html=True)

# Input Section
user_input = st.text_area("ENTER DATA STRING TO ATTACK:", placeholder="Type sentence here...")

# --- 5. PREDICTION & BATTLE OUTCOME ---
if st.button("EXECUTE COMBO ATTACK"):
    if user_input.strip() != "":
        vec = tfidf.transform([user_input])
        prediction = model.predict(vec)[0]
        
        st.write("---")
        if prediction == 1:
            st.error("💥 CRITICAL HIT! ROBOT WINS!")
            st.markdown("### STATUS: AI DETECTED")
        else:
            st.success("🛡️ COUNTER ATTACK! PLAYER WINS!")
            st.markdown("### STATUS: HUMAN DETECTED")
    else:
        st.warning("NO DATA: ATTACK FAILED!")