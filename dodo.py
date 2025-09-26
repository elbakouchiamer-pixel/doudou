import streamlit as st
from pathlib import Path
import base64
import random

st.set_page_config(
    page_title="Douae's Day! 🎉",
    page_icon="🎉",
    layout="centered"
)
card_style = """
<style>
.card {
    max-width: 600px;
    margin: 40px auto;
    background: rgba(255, 255, 255, 0.15);
    padding: 30px;
    border-radius: 25px;
    backdrop-filter: blur(10px);
    border: 2px solid rgba(255,255,255,0.3);
    box-shadow: 0 8px 30px rgba(0,0,0,0.2);
    text-align: center;
    color: #fff;
}
.card-title {
    font-size: 2em;
    margin: 1;
}
</style>
"""
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Lateef&display=swap');

/* Gradient animation keyframes */
@keyframes gradient {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

/* Main app background styling */
.stApp {
    font-family: 'Trebuchet MS', sans-serif;
    
    background: linear-gradient(-45deg,
        #ffdde1,
        #ee9ca7,
        #fad0c4,
        #ff9a9e,
        #fecfef,
        #fcb7af
    );
    
    background-size: 400% 400%;
    animation: gradient 10s ease infinite;
}




    h1 { color: #fff; font-size: 3.2em; text-shadow: 3px 3px 6px rgba(0,0,0,0.2); margin-bottom: 15px; }
    h2 { color: #ffe6f0; font-size: 1.8em; font-style: italic; margin-bottom: 25px; text-shadow: 1px 1px 3px #ff66b2; }

    p { color: #fff; font-size: 1.2em; line-height: 1.6em; }

    .stButton>button {
        background: linear-gradient(135deg, #ff66b2, #ff3399);
        color: white; border-radius: 30px; border: none; padding: 12px 30px;
        font-size: 1.1em; font-weight: bold; box-shadow: 0 4px 15px rgba(0,0,0,0.25);
        transition: all 0.25s ease-in-out; cursor: pointer;
    }
    .stButton>button:hover { transform: scale(1.06); }

    /* Video container (square) */
    .video-container {
        width: 100%;
        max-width: 640px;
        aspect-ratio: 1 / 1; /* Square */
        margin: 22px auto;
        border-radius: 20px;
        overflow: hidden;
        border: 3px solid rgba(255,255,255,0.5);
        box-shadow: 0 6px 20px rgba(0,0,0,0.25);
        background: rgba(255,255,255,0.04);
    }
    .video-container video {
        width: 100% !important;
        height: 100% !important;
        object-fit: cover;
        display: block;
    }

    .video-placeholder {
        width: 100%;
        height: 100%;
        display:flex;
        align-items:center;
        justify-content:center;
        padding: 12px;
        box-sizing: border-box;
        color: #333;
        font-weight: 700;
        background: linear-gradient(135deg,#ffe6f0,#ffd6e8);
    }

    .divider { text-align: center; margin: 18px 0; font-size: 1.6em; color: #fff; }

    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); opacity: 1;}
        100% { transform: translateY(-800px) rotate(720deg); opacity: 0;}
    }
    .heart {
        position: fixed;
        bottom: -50px;
        font-size: 28px;
        animation: float 12s linear infinite;
        z-index: 999;
    }

    #confetti-canvas { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 1000; }
    .arabic {
        font-family: 'Lateef', serif;
        font-size: 1.8em;
        direction: rtl;
        text-align: right;
        color: #fff;
    }

    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <canvas id="confetti-canvas"></canvas>
    <script>
    function launchConfetti() {
        const duration = 3 * 1000;
        const animationEnd = Date.now() + duration;
        const defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 1000 };

        function randomInRange(min, max) {
          return Math.random() * (max - min) + min;
        }

        const interval = setInterval(function() {
          const timeLeft = animationEnd - Date.now();

          if (timeLeft <= 0) {
            return clearInterval(interval);
          }

          const particleCount = 50 * (timeLeft / duration);
          confetti(Object.assign({}, defaults, {
            particleCount,
            origin: { x: randomInRange(0.1, 0.9), y: Math.random() - 0.2 }
          }));
        }, 250);
    }
    </script>
""", unsafe_allow_html=True)

card_html = """
<div class='card'>
    <div class="card-content">
        <h2 class="card-title">Happy Anniversary, Douae! 🎉</h2>
    </div>
</div>
"""
st.markdown(card_style + card_html, unsafe_allow_html=True)

st.markdown("<h2>Celebrating Your Beautiful Journey 💫</h2>", unsafe_allow_html=True)

st.markdown("""
    <div class="arabic">
    Wishing you health, and everything you have been dreaming of this year       

    </div>
""", unsafe_allow_html=True)

st.markdown("<div class='divider'>🌟🌟🌟</div>", unsafe_allow_html=True)


def render_video_file(path: Path, missing_text: str):
    if path.exists():
        st.video(str(path))
    else:
        st.markdown(f"""
            <div class="video-container">
                <div class="video-placeholder">{missing_text}</div>
            </div>
        """, unsafe_allow_html=True)


video1 = Path("gggg.mp4")    
video2 = Path("gogo.mp4")   

render_video_file(video1, f"🔍 Vidéo non trouvée — placez '{video1.name}' dans le dossier de l'app.")
st.markdown("<div class='divider'>🌟🌟🌟</div>", unsafe_allow_html=True)

render_video_file(video2, f"🔍 Vidéo non trouvée — placez '{video2.name}' dans le dossier de l'app.")
if st.button("Send Virtual wishes! 😂"):
    st.balloons()  
    st.markdown("<p>Here's a big virtual wish for you! 🥳</p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  


for i in range(12):
    st.markdown(
        f"<div class='heart' style='left:{i*8+5}%; animation-delay:{i*1.2}s;'>❤️</div>",
        unsafe_allow_html=True
    )
heart_emojis = ["❤️", "💖", "💕", "💗", "💓", "💝", "💘", "💞"]
for i in range(15):
    heart = random.choice(heart_emojis)
    left_pos = random.randint(5, 95)
    delay = random.uniform(0, 10)
    st.markdown(
        f"<div class='heart' style='left:{left_pos}%; animation-delay:{delay}s; font-size:{random.randint(24, 40)}px;'>{heart}</div>",
        unsafe_allow_html=True
    )
pdf_path = Path("Card.pdf")  

if pdf_path.exists():
    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()

    # Encode the PDF to base64 so it can be embedded in a custom button
    b64_pdf = base64.b64encode(pdf_bytes).decode()

    custom_button_html = f"""
    <div style="text-align: center; margin-top: 30px;">
        <a href="data:application/pdf;base64,{b64_pdf}" download="{pdf_path.name}" target="_blank">
            <div style="
                display: inline-block;
                padding: 20px 30px;
                background: linear-gradient(135deg, #ff66b2, #ff99cc);
                color: white;
                font-size: 1.4em;
                font-weight: bold;
                border-radius: 15px;
                box-shadow: 0 6px 20px rgba(0,0,0,0.25);
                transition: all 0.3s ease;
                cursor: pointer;
                text-decoration: none;
            ">
                📖 Click to Read
            </div>
        </a>
    </div>
    """
    st.markdown(custom_button_html, unsafe_allow_html=True)

else:
    st.error(f"File not found: {pdf_path.name}. Please place it in the app folder.")