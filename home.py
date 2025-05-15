import sys
import streamlit as st

# Initialize session state variables if they don't exist
if 'user_answer' not in st.session_state:
    st.session_state['user_answer'] = None

st.title("Streamlit App")
st.write("Hello, welcome to my Streamlit app!")


st.divider()
links = [
    ("Snowflake Cheat Sheet (by ungifted amature)", "https://snow-flake-cheat-sheet.streamlit.app/"),
    ("RBAC", "https://medium.com/@pooja.sahu.dwh/%EF%B8%8F-role-based-access-control-rbac-in-snowflake-how-to-secure-your-data-the-right-way-2052d482f600"),
    ("Level Up: Snowflake Key Concepts and Architecture", "https://learn.snowflake.com/en/courses/OD-LVLUP-102/"),
    ("Level Up: first Concepts", "https://learn.snowflake.com/en/courses/OD-LVLUP-101/"),
    ("Level Up: Snowflake Ecosystem", "https://learn.snowflake.com/en/courses/OD-LVLUP-103/"),
    ("Level Up: Accounts and Assurances", "https://learn.snowflake.com/en/courses/OD-LVLUP-104/"),
    ("Level Up: Container Hierarchy", "https://learn.snowflake.com/en/courses/OD-LVLUP-105/"),
    ("Level Up: Backup and Recovery", "https://learn.snowflake.com/en/courses/OD-LVLUP-108/"),
    ("Level Up: Context in Snowflake", "https://learn.snowflake.com/en/courses/OD-LVLUP-202/"),
    ("Level Up: Final Exam", "https://learn.snowflake.com/en/courses/OD-LVLUP-109/"),
]
st.markdown("#### Useful Links")
compact_links = "\n".join(
    f"- [{label}]({url})" for label, url in links
)
st.markdown(compact_links, unsafe_allow_html=True)

#st.markdown("#### Useful Links")
#for label, url in links:
#    st.markdown(f"- [{label}]({url})")

#st.page_link("https://docs.streamlit.io/", label="Streamlit Docs")

resources_links = [
("", "https://medium.com/snowflake"),
("", "https://community.snowflake.com/s/article/Snowflake-s-SnowPro-Certification-Preparation-Guide-How-to-Pass-in-3-Days"),
("", "https://medium.com/snowflake/the-ungifted-amateurs-guide-to-snowflake-449284e4bd72"),
("", "https://medium.com/@jenoyamma/seeing-snow-for-the-first-time-snowflake-adventures-part-1-731ddc983c69"),
("", "https://medium.com/@jenoyamma/snowflakes-snowpro-certification-exam-preparation-guide-how-to-pass-in-3-days-5e5baa484c68"),
("", "https://medium.com/snowflake/how-to-get-snowflake-certified-fb0054ed90ee"),
("", "https://www.whizlabs.com/blog/snowflake-snowpro-core-certification/"),
("", "https://www.reddit.com/r/snowflake/comments/12dnk3u/simplified_guide_for_snowflake_certification/"),
("", "https://articles.analytics.today/mastering-snowflake-snowpro-certification-10-proven-methods"),
("hgh level theory", "https://vutr.substack.com/p/i-spent-another-6-hours-understanding"),
("", "https://vutr.substack.com/p/i-read-another-paper-to-understand"),
("", "https://vutr.substack.com/p/i-spent-8-hours-diving-deep-into"),
]
st.markdown("#### Resources")
resources_links_compact = "\n".join(
    f"{i+1}. [{url} ({label})]({url})" for i, (label, url) in enumerate(resources_links)
)
st.markdown(resources_links_compact, unsafe_allow_html=True)

st.divider()
question = "What is the question?"
options = ["Pick selection below...",
           "A) Answer 1", 
           "B) Answer 2", 
           "C) Answer 3", 
           "D) Answer n", ]                
 
user_answer = st.radio(question, options, index=0)
st.session_state['user_answer'] = user_answer

if user_answer:
    if user_answer == "Pick selection below...":
        st.write(f"Selected answer: ")
    else:
    #        answer = 'b71018c50689d88fc0f7aac8d3cbad47'
    #        response = session.sql(f"call common_db.resources.quiz_temp('{answer}', '{user_answer}', 'False')").collect()
    #        if response:
    #            value = response[0]['QUIZ_TEMP']
    #        st.write(value)

    # Example: Replace with your actual session/connection logic
    # response = your_db_connection.sql(f"call common_db.resources.quiz_temp('{answer}', '{user_answer}', 'False')").collect()
    # if response:
    #     value = response[0]['QUIZ_TEMP']
    #     st.write(value)
        st.write(f"Selected answer: {user_answer}")
