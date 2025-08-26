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
Event Data: The 'Catalyst Startup Summit 2025'
Event Overview

Event Name: The Catalyst Startup Summit 2025

Date: August 27, 2025

Venue: Grand Innovation Center, Chennai

Tagline: "Igniting Connections, Fueling Futures"

Stall Data (Ground Floor & First Floor)
This is the main exhibition area with 100 stalls, organized by startup domain.

FinTech: Stalls 1-10

HealthTech: Stalls 11-20

EdTech: Stalls 21-30

SaaS & AI: Stalls 31-40

Mobility & Logistics: Stalls 41-50

FoodTech & AgriTech: Stalls 51-60

E-commerce & Retail: Stalls 61-70

Sustainable Tech & Clean Energy: Stalls 71-80

Creator Economy & Media: Stalls 81-90

HR Tech & B2B Solutions: Stalls 91-100

For the full list of 100 stalls with names, founders, and specific floor locations, please refer to the dummy data provided in the previous response.

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

Panel 1 (2:00 PM - 3:00 PM)

Domain: Sustainable Tech & Clean Energy

Topic: "Building a Greener Future: Startups at the Forefront of Climate Action"

Panelists: CEO of Eco-Innovate, Founder of GreenSpark (Stall 75), and a Partner from Impact Ventures.

Panel 2 (3:00 PM - 4:00 PM)

Domain: HealthTech & Wellness

Topic: "Revolutionizing Healthcare: AI and Accessibility in Digital Health"

Panelists: CEO of HealthConnect, Founder of MindfulMate (Stall 15), and a lead researcher from a local university.

Panel 3 (4:00 PM - 5:00 PM)

Domain: Social Impact

Topic: "Scaling Social Ventures: From Idea to Impactful Enterprise"

Panelists: Co-founder of a non-profit tech platform, Evelyn Martinez (Wantrepreneur), and a government representative.

Hall Gamma: The "Growth & Scale" Stage

Panel 1 (2:00 PM - 3:00 PM)

Domain: FinTech & E-commerce

Topic: "Navigating the Next Wave of Digital Payments and Retail"

Panelists: A Director from HDFC Bank, Founder of CoinFlow (Stall 83), and a partner from Sequoia Capital.

Panel 2 (3:00 PM - 4:00 PM)

Domain: SaaS & AI

Topic: "The AI Advantage: How Startups Are Leveraging Generative AI"

Panelists: A CTO from a leading software company, Founder of DataDriven (Stall 99), and a senior AI engineer.

Panel 3 (4:00 PM - 5:00 PM)

Domain: Investments & Marketplaces

Topic: "Decoding the Investor Mindset: What VCs Look for in a Pitch"

Panelists: Jordan Patel (Investor), Mason Clark (Investor), and a senior partner from a prominent VC firm.

Chief Guests
Hon'ble Minister S. Kumar

Role: Minister for IT & Startups

Address Location: Auditorium Alpha (10:00 AM)

Dr. Ananya Sharma

Role: Renowned Technologist and Philanthropist

Address Location: Hall Beta (Opening Panel)

Sponsors
Platinum Sponsor: "Innovate India" - A nationwide startup investment fund.

Gold Sponsors: "GrowthEngine Tech" (SaaS Solutions), "FutureFin Capital" (FinTech Investor), "Vertex Ventures" (VC Firm)

Silver Sponsors: "CloudSphere Solutions" (Cloud Computing), "Alpha Analytics" (Data Analytics Platform)

Catering Sponsor: "Food Fusion"

Organizers
Lead Organizer: Startup Central

Community Partners: Tech Entrepreneurs Guild, Founders Network India

Event Management: Zenith Events

Logistics & Special Zones
Shuttle Service Locations:

Location A: Central Metro Station

Location B: Major Hotels District (List of 5 major hotels provided)

Drop-off/Pickup: Main Entrance of Grand Innovation Center

Food & Beverage Locations:

Lunch: Courtyard Food Zone

Snacks: Courtyard Food Zone (after 6 PM)

Coffee & Tea Stations: Located at the center of each floor.

1v1 Pitch Panels:

Location: Pitch Zone, First Floor, Hallway near Hall Gamma

Description: A dedicated area for pre-registered founders to have 1-on-1 pitch sessions with investors and mentors.

Government Stalls:

Location: Stall numbers 96-100, First Floor, Right Side

Details: Stalls representing various government bodies and schemes for startups (e.g., Startup India, SIDBI, Make in India).

Incubator-Wise Stalls:

Location: Stalls 101-110, Second Floor (Exclusive Incubator Zone)

Details: Startups are grouped by their incubator. For example, "Incubator X" will have Stalls 101-105, and "Incubator Y" will have 106-110.
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
    st.title("R J Benjamin Robert")
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


