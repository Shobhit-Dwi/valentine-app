import base64
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="💖 Valentine 💖", layout="wide")

if "accepted" not in st.session_state:
    st.session_state.accepted = False

# Background + cleanup
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ffafbd, #ffc3a0);
}
header, footer {visibility: hidden;}
.block-container {padding-top: 0rem;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* Hide the hidden Streamlit button completely */
button[kind="secondary"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)



def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


img1 = img_to_base64("couple.jpeg")
img2 = img_to_base64("couple1.jpeg")


# =========================================================
# 💌 SCREEN 1
# =========================================================
if not st.session_state.accepted:

    # hidden real button (logic only)
    if st.button("hidden_accept", key="accept_btn"):
        st.session_state.accepted = True
        st.rerun()

    components.html(
        """
        <style>
        .card {
            background: white;
            width: 460px;
            padding: 50px 45px 60px;
            border-radius: 40px;
            text-align: center;
            box-shadow: 0px 18px 40px rgba(0,0,0,0.25);
            margin: 120px auto 0 auto;
            font-family: 'Comic Sans MS', cursive;
        }

        h1 { color: #ff3366; }
        .emoji { font-size: 34px; margin: 25px 0; }

        .btn-row {
            display: flex;
            justify-content: center;
            gap: 26px;
            margin-top: 35px;
        }

        /* COMMON BUTTON STYLE */
        .btn {
            min-width: 140px;
            padding: 14px 0;
            border-radius: 18px;
            border: none;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            transition: 0.2s ease;
        }

        .yes-btn {
            background-color: #ff3366;
            color: white;
            box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
        }

        .yes-btn:hover {
            transform: scale(1.08);
            background-color: #ff1f5a;
        }

        .no-btn {
            background: #b5b5b5;
            color: white;
        }
        </style>

        <div class="card">
            <h1>Will you be my Valentine ? Miss Ishita Tandon !</h1>
            <div class="emoji">💘</div>

            <div class="btn-row">
                <button class="btn yes-btn"
                    onclick="window.parent.document
                    .querySelector('button[kind=secondary]')
                    .click()">
                    YES 💖
                </button>

                <button class="btn no-btn"
                  onmouseover="this.style.transform=
                  'translate('+Math.random()*120+'px,'+Math.random()*30+'px)'">
                  NO 😜
                </button>
            </div>
        </div>
        """,
        height=520
    )

# =========================================================
# 💖 SCREEN 2
# =========================================================
else:
    st.markdown(f"""
    <style>
    @keyframes fadeIn {{
        0% {{ opacity: 0; transform: translateY(20px); }}
        100% {{ opacity: 1; transform: translateY(0); }}
    }}

    .slideshow {{
        position: relative;
        width: 420px;
        height: 420px;
        margin: 40px auto;
    }}

    .slide {{
        position: absolute;
        width: 100%;
        height: 100%;
        object-fit: cover;
        opacity: 0;
        animation: slideShow 8s infinite;
        border-radius: 18px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.25);
    }}

    .slide:nth-child(1) {{ animation-delay: 0s; }}
    .slide:nth-child(2) {{ animation-delay: 4s; }}

    @keyframes slideShow {{
        0% {{ opacity: 0; }}
        10% {{ opacity: 1; }}
        40% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
        100% {{ opacity: 0; }}
    }}
    </style>

    <div style="
        text-align:center;
        margin-top:60px;
        color:white;
        font-family:'Comic Sans MS', cursive;
        animation: fadeIn 1s ease;
    ">
        <h1>She said YES 💖🥹</h1>
        <p style="font-size:22px; max-width:900px; margin:auto;">
            So now that you have finally said yes, I just want you to know what my heart has been holding for so long. I know we fight a lot, we argue, and sometimes we don’t understand each other, but despite everything, my love for you has never reduced—not even a little. In fact, it only grows stronger with time. Being in a long-distance relationship for the past 1.5 years hasn’t been easy, especially with someone who is not very communicative, but you have always been my biggest support, especially during my lowest phases when I felt lost, confused, and broken. You stood by me when things weren’t going my way, believed in me when I doubted myself, and became my lucky charm without even realizing it. Yes, this is what you mean to me—not just in words, but in reality. I miss you more than I can explain, and every day without you feels incomplete. Knowing that I’m finally traveling from Noida to Bangalore and meeting you on 13th February makes my heart feel calm and excited at the same time. I’m afraid to travel and worried about how everything will go and how I’ll manage things, but I’m also excited to see you—excited to hug you, excited to smell you, excited to finally touch you. You are not just my girlfriend; you are my comfort, my strength, my safe place where I never worry about being judged, and the person I want to share all my smiles and struggles with. So today, from the depth of my heart, I want to ask you—will you be my Valentine, not just because you clicked on yes and feel bound to say yes, but because you love me, not just for a day, but always? ❤️❤️
        </p>
    </div>

    <div class="slideshow">
        <img src="data:image/jpeg;base64,{img1}" class="slide">
        <img src="data:image/jpeg;base64,{img2}" class="slide">
    </div>
    """, unsafe_allow_html=True)
