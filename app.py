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
Event Overview
Event Name: The Catalyst Startup Summit 2025

Date: August 27, 2025

Venue: Grand Innovation Center, Chennai

Tagline: "Igniting Connections, Fueling Futures"

Physical Venue Plan
The event is hosted at the two-story Grand Innovation Center, with distinct zones on each floor designed to facilitate networking and knowledge sharing.

Ground Floor Plan:

Main Entrance (Right Side): The primary entry point.

Registration Desks (Left of Entrance): Where attendees check-in and receive their event badges.

Stall Exhibition Area (Central Hall):

Ground Floor Left Side (Stalls 1-25): Primarily features startups in FinTech, HealthTech, and EdTech.

Ground Floor Right Side (Stalls 26-50): Dedicated to SaaS & AI, and Mobility & Logistics startups.

Courtyard & Food Zone (Rear of Venue): A large, open-air area at the back of the ground floor for lunch, snacks, and casual networking.

Auditorium Alpha (Front, Left Side): The main auditorium for the opening keynote and closing ceremony.

First Floor Plan:

Stall Exhibition Area (Hallways):

First Floor Left Side (Stalls 51-75): Features FoodTech, AgriTech, and E-commerce & Retail startups.

First Floor Right Side (Stalls 76-100): Showcases Sustainable Tech, Clean Energy, Creator Economy, HR Tech, and B2B Solutions.

Hall Beta (First Floor, Left Corner): The "Tech for Good" stage for sustainability and social impact panel discussions.

Hall Gamma (First Floor, Right Corner): The "Growth & Scale" stage for business and investment-focused panel discussions.

Pitch Zone (Hallway near Hall Gamma): A designated area with private booths for 1v1 pitch sessions with investors and mentors.

Government Stalls (Stalls 96-100): Located at the far end of the First Floor, Right Side.

Incubator Zone (Stalls 101-110, Second Floor): A special, smaller zone on the floor above, dedicated to startups organized by their incubators.

List of 50 Participating Startups
Startup Name	Startup Domain	Founder Name
FinTech		
1. FinFlow	AI-Driven Personal Finance	Alex Chen
2. EthosPay	Sustainable Payments Platform	Ethan Gupta
3. CryptoVault	Secure Crypto Wallets	Aaron Bennett
4. Lendify	Peer-to-Peer Lending	Mason Davis
5. RoboWealth	Automated Financial Planning	Cole Turner
HealthTech		
6. HealthWave	Digital Health Records	Olivia Brown
7. MindfulMate	Mental Health Therapy App	Natalie Hughes
8. TeleMed	Telemedicine for Rural Areas	Lily Evans
9. SheWell	Women's Health & Wellness	Amelia White
10. BioSense	Medical Device Diagnostics	Julia Lee
EdTech		
11. CodeCraft	Gamified Coding Platform	Lily Harris
12. EduVerse	VR-based Learning Environments	Eleanor Gray
13. Learnly	AI-powered Tutoring	Liam Turner
14. SkillUp	Vocational & Skill Training	Alex Bennett
15. CareerPath	Career Guidance & Mentoring	Evan Miller
SaaS & AI		
16. DataFlow	B2B Data Analytics	Penelope Turner
17. AI-Sense	AI-Driven Business Intelligence	Connor Wright
18. WorkFlow	Remote HR Management Suite	Evelyn Peterson
19. IntelliSaaS	AI Automation for Enterprises	Michael Evans
20. AdBot	Programmatic Advertising AI	Nolan Bell
Mobility & Logistics		
21. UrbanTransit	Smart Urban Mobility	Jack Baker
22. SupplyChainAI	AI for Logistics Optimization	Kennedy Walker
23. FreightFox	B2B Freight Marketplace	Dominic Price
24. RideShareAI	Smart Carpool Matching	Ethan Smith
25. AutoLogistics	Warehouse Automation & Robotics	Lucas Green
FoodTech & AgriTech		
26. FoodieBot	Food Delivery Robots	Hannah Evans
27. AgriTech	Vertical Farming Solutions	Nora Ward
28. RoboMeals	Automated Meal Kit Delivery	Mason Brooks
29. FarmLink	AgriTech Marketplace	David Kim
30. FoodChain	Blockchain for Food Traceability	Sarah Moore
E-commerce & Retail		
31. HomeDecorHQ	E-commerce for Home Furnishings	Olivia Wilson
32. Sustainabuy	E-commerce for Eco-friendly Products	Abigail Phillips
33. SmartShelf	AI-powered Retail Shelving	Caroline Hall
34. ConsciousCart	B2B Sustainable Supply Chain	Victoria Evans
35. Glamo	Fashion E-commerce with VR	Samantha Bell
Sustainable Tech & Clean Energy		
36. GreenWave	Waste Management Solutions	Sofia Thomas
37. SunPower	Solar Energy Micro-grids	Tyler Cook
38. EcoThread	Sustainable Apparel Supply	Sophie Foster
39. CarbonTrack	Carbon Footprint Tracking App	Audrey Scott
40. GreenSpark	Clean Energy Investment Platform	Jaxon Ward
Creator Economy & Media		
41. Artify	Marketplace for Digital Artists	Chloe Davis
42. Creatify	Tools for Content Monetization	Evan Richardson
43. Streamify	Next-gen Streaming Service	Brandon Cooper
44. PodCraft	AI-powered Podcasting Tools	Ava Cooper
45. MediaWise	AI for Media Analytics	Jayden Coleman
HR Tech & B2B Solutions		
46. HireRight	AI-powered Recruitment Software	Riley Baker
47. JobGenie	Employee Benefits Platform	Evelyn Peterson
48. LegalBot	Legal Document Automation	Andrew Hughes
49. SecureFlow	B2B Cybersecurity Solutions	Cooper Brooks
50. DataDriven	Enterprise Data Management	Nathan King

Export to Sheets
Schedule of Events (All-Day)
Time	Location	Event Description
9:00 AM - 10:00 AM	Main Entrance	Registration & Welcome
10:00 AM - 10:30 AM	Auditorium Alpha	Opening Keynote: "The Future of Innovation in India"
10:30 AM - 1:00 PM	All Stalls	Stall Exhibition & Networking
1:00 PM - 2:00 PM	Courtyard & Food Zone	Lunch Break
2:00 PM - 5:00 PM	Hall Beta, Hall Gamma	Panel Discussions
5:00 PM - 6:00 PM	Pitch Zone	1v1 Pitch Panels
6:00 PM - 7:00 PM	Courtyard	Snacks & Open Networking
7:00 PM - 7:30 PM	Auditorium Alpha	Closing Remarks & Award Ceremony
7:30 PM onwards	Venue	Event Closeout

Export to Sheets
Panel Discussions
Hall Beta: The "Tech for Good" Stage

Panel 1 (2:00 PM - 3:00 PM): Sustainable Tech & Clean Energy

Panel 2 (3:00 PM - 4:00 PM): HealthTech & Wellness

Panel 3 (4:00 PM - 5:00 PM): Social Impact

Hall Gamma: The "Growth & Scale" Stage

Panel 1 (2:00 PM - 3:00 PM): FinTech & E-commerce

Panel 2 (3:00 PM - 4:00 PM): SaaS & AI

Panel 3 (4:00 PM - 5:00 PM): Investments & Marketplaces

Key Speakers & Event Partners
Chief Guests:

Hon'ble Minister S. Kumar (Minister for IT & Startups)

Dr. Ananya Sharma (Renowned Technologist and Philanthropist)

Sponsors:

Platinum: "Innovate India"

Gold: "GrowthEngine Tech," "FutureFin Capital," "Vertex Ventures"

Silver: "CloudSphere Solutions," "Alpha Analytics"

Organizers:

Lead Organizer: Startup Central

Community Partners: Tech Entrepreneurs Guild, Founders Network India"
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
    st.title("N=Umagine AI")
    st.markdown("Umagine 2025")
    st.markdown("Your one stop AI assistant for Umagine 2025")
    st.divider()
    st.subheader(" Example Questions")
    st.info(" What is todays agenda?")
    st.info(" Tell me where the Fin-Tech startups are located")
    st.info("Who are all the chief guests?")

# ------------------------
# MAIN CONTENT
# ------------------------
st.title("🤖 Umagine AI")
st.markdown("### Ask me anything about Umagine 2025")
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




