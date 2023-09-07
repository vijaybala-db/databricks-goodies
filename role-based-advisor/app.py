import streamlit as st
st.title('Role-based Advisor')
st.markdown("""<style>#MainMenu, header, footer {visibility: hidden;}</style>""", unsafe_allow_html=True)

templates = {
    'doctor' : """You are a doctor (primary care physician) with 25 years of experience practicing in California. You emphasize the importance of a healthy lifestyle that includes nutritious food and vigorous exercise.""",
    'father' : """You are the user's father and cares deeply about their well being. You emphasize the importance of working hard and getting a good education.""",
    'business_partner' : """You are the user's business partner. You share a mutual interest in the success of your company. You emphasize actions that will maximize the long term viability and profitability of the company and achieving its mission.""",
    'career_coach' : """You are the user's manager at work. You see great potential in the user to progress in their career. You emphasize actions that maximize the user's chances for a promotion and continue their trajectory to become a senior executive.""",
    'user' : "I want to live a life that maximizes happiness and creates a positive impact on the world. What are the top 5 things I should do in the next week towards these goals?"
}

with st.form('ask_form'):
    st.text_area('Ask me anything', value=templates['user'])
    def format_role(role_value):
        formatted_role = {'doctor': 'Doctor', 'father': 'Father', 'business_partner': 'Business Partner', 'career_coach': 'Career Coach'}
        return formatted_role[role_value]
    role = st.radio('Choose a role', ['doctor', 'father', 'business_partner', 'career_coach'], 
                    format_func = format_role, horizontal=True)
    submitted = st.form_submit_button('Ask')

if submitted:
    st.markdown(f'*{format_role(role)} says:*')
    st.markdown(templates[role])
