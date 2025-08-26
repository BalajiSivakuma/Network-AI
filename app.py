import streamlit as st
import google.generativeai as genai

# ------------------------
# PAGE CONFIGURATION
# ------------------------
st.set_page_config(
    page_title="R J Benjamin Robert | AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------
# CUSTOM CSS (Google Theme)
# ------------------------
st.markdown(
    """
    <style>
        body {
            font-family: 'Google Sans', sans-serif;
        }
        .user-bubble {
            background-color: #4285F4;
            color: white;
            padding: 10px 15px;
            border-radius: 20px;
            margin: 5px 0;
            max-width: 70%;
            align-self: flex-end;
        }
        .bot-bubble {
            background-color: #F1F3F4;
            color: #202124;
            padding: 10px 15px;
            border-radius: 20px;
            margin: 5px 0;
            max-width: 70%;
            align-self: flex-start;
        }
        .stChatMessage {
            background: transparent !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------
# PERSONAL DATA (THE "BRAIN")
# ------------------------
my_data = """
Stall Name	Startup Domain	Founder Name	Location
FinFlow	FinTech	Alex Chen	Stall 1, Ground Floor Left Side
HealthWave	HealthTech	Olivia Brown	Stall 2, Ground Floor Left Side
CodeCraft	EdTech	Lily Harris	Stall 3, Ground Floor Left Side
EcoThread	Sustainable Fashion	Sophia Foster	Stall 4, Ground Floor Left Side
PetPals	Pet Tech	Mia Wilson	Stall 5, Ground Floor Left Side End
AgroConnect	AgriTech	Nora Ward	Stall 6, Ground Floor Right Side
MindfulMate	Mental Health	Natalie Hughes	Stall 7, Ground Floor Right Side
SupplyChainAI	Logistics	Kennedy Walker	Stall 8, Ground Floor Right Side
HomeSphere	Smart Home	Jason Long	Stall 9, Ground Floor Right Side
GreenSpark	Clean Energy	Tyler Cook	Stall 10, Ground Floor Right Side End
LegalEase	Legal Tech	Andrew Hughes	Stall 11, First Floor Left Side
Artify	Creator Economy	Chloe Davis	Stall 12, First Floor Left Side
QuantumLeap	Cybersecurity	Lucas Hall	Stall 13, First Floor Left Side
TravelTrek	Travel Tech	Wyatt Reed	Stall 14, First Floor Left Side
EduVerse	EdTech	Eleanor Gray	Stall 15, First Floor Left Side End
AdMetrics	AdTech	Nolan Bell	Stall 16, First Floor Right Side
CareerPath	EdTech	Alex Bennett	Stall 17, First Floor Right Side
FitFuel	Fitness Tech	Kai Lewis	Stall 18, First Floor Right Side
AI-Sense	SaaS	Connor Wright	Stall 19, First Floor Right Side
UrbanTransit	Mobility	Jack Baker	Stall 20, First Floor Right Side End
FemWell	FemTech	Amelia White	Stall 21, Ground Floor Left Side
HomeDecorHQ	E-commerce	Olivia Wilson	Stall 22, Ground Floor Left Side
CryptoVault	FinTech	Aaron Bennett	Stall 23, Ground Floor Left Side
MedConnect	HealthTech	Lily Evans	Stall 24, Ground Floor Left Side
RoboMeals	FoodTech	Mason Brooks	Stall 25, Ground Floor Left Side End
DataFlow	B2B SaaS	Penelope Turner	Stall 26, Ground Floor Right Side
StellarSat	SpaceTech	Violet Russell	Stall 27, Ground Floor Right Side
JobGenie	HR Tech	Evelyn Peterson	Stall 28, Ground Floor Right Side
AutoLogistics	Supply Chain	Lucas Green	Stall 29, Ground Floor Right Side
SmartShelf	Retail Tech	Caroline Hall	Stall 30, Ground Floor Right Side End
AgriFuture	AgriTech	Nora Ward	Stall 31, First Floor Left Side
MindFlow	Mental Health	Natalie Hughes	Stall 32, First Floor Left Side
Sustainabuy	E-commerce	Abigail Phillips	Stall 33, First Floor Left Side
SecureFlow	Cybersecurity	Cooper Brooks	Stall 34, First Floor Left Side
EduPath	EdTech	Liam Turner	Stall 35, First Floor Left Side End
FitWell	Fitness Tech	Kai Lewis	Stall 36, First Floor Right Side
Creatify	Creator Tools	Evan Richardson	Stall 37, First Floor Right Side
UrbanFlow	Mobility	Jack Baker	Stall 38, First Floor Right Side
LegalBot	Legal Tech	Grayson King	Stall 39, First Floor Right Side
MarketMinds	AdTech	Nolan Bell	Stall 40, First Floor Right Side End
GreenWave	Sustainable Tech	Sofia Thomas	Stall 41, Ground Floor Left Side
HR-Solve	HR Tech	Evelyn Peterson	Stall 42, Ground Floor Left Side
CodeAcademy	EdTech	Lily Harris	Stall 43, Ground Floor Left Side
FoodieBot	FoodTech	Hannah Evans	Stall 44, Ground Floor Left Side
PetCarePlus	Pet Tech	Jack Miller	Stall 45, Ground Floor Left Side End
FarmLink	AgriTech	Nora Ward	Stall 46, Ground Floor Right Side
WellnessNow	Mental Health	Natalie Hughes	Stall 47, Ground Floor Right Side
FreightFox	Logistics	Dominic Price	Stall 48, Ground Floor Right Side
AutoHome	Smart Home	Jason Long	Stall 49, Ground Floor Right Side
SunPower	Clean Energy	Tyler Cook	Stall 50, Ground Floor Right Side End
LawConnect	Legal Tech	Andrew Hughes	Stall 51, First Floor Left Side
CreativeHub	Creator Economy	Chloe Davis	Stall 52, First Floor Left Side
ShieldNet	Cybersecurity	Lucas Hall	Stall 53, First Floor Left Side
ExploreNow	Travel Tech	Wyatt Reed	Stall 54, First Floor Left Side
LearnSphere	EdTech	Eleanor Gray	Stall 55, First Floor Left Side End
AdGenius	AdTech	Nolan Bell	Stall 56, First Floor Right Side
CareerHub	EdTech	Alex Bennett	Stall 57, First Floor Right Side
FitLife	Fitness Tech	Kai Lewis	Stall 58, First Floor Right Side
DataWise	SaaS	Connor Wright	Stall 59, First Floor Right Side
CityGlide	Mobility	Jack Baker	Stall 60, First Floor Right Side End
FemmeHealth	FemTech	Amelia White	Stall 61, Ground Floor Left Side
HomeStyle	E-commerce	Olivia Wilson	Stall 62, Ground Floor Left Side
CoinFlow	FinTech	Aaron Bennett	Stall 63, Ground Floor Left Side
TeleMed	HealthTech	Lily Evans	Stall 64, Ground Floor Left Side
FoodieFuel	FoodTech	Mason Brooks	Stall 65, Ground Floor Left Side End
AnalyticsPro	B2B SaaS	Penelope Turner	Stall 66, Ground Floor Right Side
SpaceXplore	SpaceTech	Violet Russell	Stall 67, Ground Floor Right Side
WorkFlow	HR Tech	Evelyn Peterson	Stall 68, Ground Floor Right Side
GlobalFreight	Supply Chain	Lucas Green	Stall 69, Ground Floor Right Side
RetailGenius	Retail Tech	Caroline Hall	Stall 70, Ground Floor Right Side End
AgTech	AgriTech	Nora Ward	Stall 71, First Floor Left Side
CalmSpace	Mental Health	Natalie Hughes	Stall 72, First Floor Left Side
ConsciousCart	E-commerce	Abigail Phillips	Stall 73, First Floor Left Side
CyberGuard	Cybersecurity	Cooper Brooks	Stall 74, First Floor Left Side
EdVault	EdTech	Liam Turner	Stall 75, First Floor Left Side End
AdWise	AdTech	Nolan Bell	Stall 76, First Floor Right Side
LearnFlow	EdTech	Alex Bennett	Stall 77, First Floor Right Side
WellnessFit	Fitness Tech	Kai Lewis	Stall 78, First Floor Right Side
IntelliSaaS	SaaS	Connor Wright	Stall 79, First Floor Right Side
UrbanMotion	Mobility	Jack Baker	Stall 80, First Floor Right Side End
SheWell	FemTech	Amelia White	Stall 81, Ground Floor Left Side
Decorista	E-commerce	Olivia Wilson	Stall 82, Ground Floor Left Side
CoinSecure	FinTech	Aaron Bennett	Stall 83, Ground Floor Left Side
HealthNet	HealthTech	Lily Evans	Stall 84, Ground Floor Left Side
ChefBot	FoodTech	Hannah Evans	Stall 85, Ground Floor Left Side End
AnalyticsBot	B2B SaaS	Penelope Turner	Stall 86, Ground Floor Right Side
StarGazer	SpaceTech	Violet Russell	Stall 87, Ground Floor Right Side
HireRight	HR Tech	Evelyn Peterson	Stall 88, Ground Floor Right Side
LogisticsPro	Supply Chain	Lucas Green	Stall 89, Ground Floor Right Side
ShelfWise	Retail Tech	Caroline Hall	Stall 90, Ground Floor Right Side End
AgroTech	AgriTech	Nora Ward	Stall 91, First Floor Left Side
InnerPeace	Mental Health	Natalie Hughes	Stall 92, First Floor Left Side
EcoMarket	E-commerce	Abigail Phillips	Stall 93, First Floor Left Side
SafeCloud	Cybersecurity	Cooper Brooks	Stall 94, First Floor Left Side
Learnly	EdTech	Liam Turner	Stall 95, First Floor Left Side End
AdBot	AdTech	Nolan Bell	Stall 96, First Floor Right Side
SkillUp	EdTech	Alex Bennett	Stall 97, First Floor Right Side
FitBot	Fitness Tech	Kai Lewis	Stall 98, First Floor Right Side
DataDriven	SaaS	Connor Wright	Stall 99, First Floor Right Side
RideShareAI	Mobility	Jack Baker	Stall 100, First Floor Right Side End
"""

# ------------------------
# MASTER PROMPT
# ------------------------
prompt_template = f"""
1. Greeting:

Start with an enthusiastic welcome.

Clearly state the chatbot's purpose.

Example:
"Welcome to the Startup Networking Event! I'm your guide to help you navigate the venue. I can tell you where any stall is located. What stall are you looking for today?"

2. User Input & Keyword Recognition:

The chatbot should be able to recognize key phrases or stall names.

Look for keywords like "Where is...", "I'm looking for...", "Stall name...", or just the name of a stall itself.

Example:

User: "Where is GreenWave?"

Chatbot: "Searching for GreenWave..."

3. Data Retrieval & Response Generation:

This is where the chatbot accesses the data you provided. It will search for the stall name and pull the corresponding information.

The response should be clear and concise, providing the stall name, domain, and exact location.

Example:

User: "Tell me about Stall 99."

Chatbot: "Stall 99 is 'DataDriven,' a SaaS startup founded by Connor Wright. You can find it on the First Floor, Right Side."

4. Error Handling & Follow-up:

If the user's request doesn't match any data, provide a polite response.

Offer to help with another request to keep the conversation going.

Example:

User: "Where is the coffee stand?"

Chatbot: "I'm sorry, I don't have information on the coffee stand. I can only provide details on the official startup stalls. Is there a different stall I can help you find?"

5. Additional Features (Optional but Recommended):

You could add a feature where a user asks for a specific domain (e.g., "FinTech stalls"). The chatbot could then list all the stalls within that domain.

The chatbot could also be programmed to provide a fun fact or a short, engaging description of the startup when a user asks for a stall's details.
---
PROFILE INFORMATION:
{my_data}
---
"""

# ------------------------
# SIDEBAR
# ------------------------
with st.sidebar:
    #st.image("https://i.imgur.com/gL4KZc2.jpeg", width=150)
    st.title("Network Bot")
    st.markdown("*ECE Final Year | Tech Community Lead*")
    st.markdown("Sathyabama Institute of Science and Technology")
    st.divider()
    st.subheader("💡 Example Questions")
    st.info("🌟 What is Benjamin’s vision for the student community?")
    st.info("🚀 Tell me about the RideRay project.")
    st.info("🤝 What is his leadership experience?")

# ------------------------
# MAIN CONTENT
# ------------------------
st.title("🤖 AI-Powered-Me")
st.markdown("### Ask me anything about Benjamin Robert(Me)!")
st.divider()

# ------------------------
# CHATBOT LOGIC
# ------------------------
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
except KeyError:
    st.error("Deployment Error: Add your GOOGLE_API_KEY to Streamlit secrets.")
    st.stop()
except Exception as e:
    st.error(f"Error: {e}")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

chat_container = st.container()

# Display existing chat
with chat_container:
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"<div class='user-bubble'>{msg['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='bot-bubble'>{msg['content']}</div>", unsafe_allow_html=True)

# Input
if user_prompt := st.chat_input("Ask about his projects, skills, or vision..."):
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    full_prompt = prompt_template + "\nUser question: " + user_prompt
    response = model.generate_content(full_prompt)
    bot_reply = response.text

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    st.rerun()