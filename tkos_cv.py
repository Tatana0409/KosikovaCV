import streamlit as st
from streamlit_timeline import timeline
from pathlib import Path
# Set up the page configuration
st.set_page_config(page_title='CV Tatiana Kosikova' ,layout="wide",page_icon='👩🏻‍💼')
st.markdown("""
    <style>
        .big-font {
            font-family: "Lucida Handwriting", cursive;
            font-size: 70px !important;
            font-weight: bold;
            line-height: 0.5;
            color: DarkBlue
        }
        .tight-font {
            font-family: "Arial", Sans-serif;
            font-weight: bold;
            padding: 0px;
            font-size: 25px !important;
            margin: 0px;
            line-height: 0.5;
            color: Black
        }
        body {
            font-family: "Roboto";
            color: #333;
        }
        hd1 {
            font-family: "Roboto";
            color: #2E8B57;
        }
        hd2 {
            font-family: "Roboto";
        }
        hd3 {
            font-family: "Source Sans Pro";
        }
        .custom-title {
            font-family:"Lucida Handwriting", cursive;
            font-size: 35px !important;
            color: DarkBlue;
            font-weight: bold;
        }
        html, body, [class*="css"]  {
             line-height: 1;
        }
    </style>
""", unsafe_allow_html=True)


CURRENT_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
RESUME_FILE = CURRENT_DIR / "resume.pdf"


#Header
st.markdown("""<style>.stApp { background-color: #FAEBD7; }.css-1d391kg { color: blue; }</style>""",
            unsafe_allow_html=True
            )


with st.container():
    col3,col4 = st.columns(2)
with col4:
    st.markdown("<p class='custom-title'>Ing.Tatiana Košíková </p>",unsafe_allow_html=True)
    st.markdown("\n\n")
    st.markdown("<p class='tight-font'>PROCES AUTOMATION DEVELOPER</p>",unsafe_allow_html=True)
    # Contact Information
    st.markdown("<p></p>",unsafe_allow_html=True)
    st.write("📍🗺️ Martin, Slovakia | 📧 tanicka.kosikova@gmail.com | 🔗 [LinkedIn](https://linkedin.com/in/tatiana-kosikova-b81aa7165)")
    st.markdown("\n\n")

with col3:
    st.markdown("<p class='big-font'> Curriculum </p>",unsafe_allow_html=True)
    st.markdown("\n\n")
    st.markdown ("<p class='big-font'>Vitae 📜 </p>",unsafe_allow_html=True)
st.divider()
st.markdown("\n\n")
st.write(""" 
● Results-driven RPA (Robotic Process Automation) Developer with 4 years of hands-on experience 
in developing, testing, and maintaining automation solutions across various business processes.\n\n
● Proven ability to deliver reliable and scalable robots using leading RPA tools.\n\n 
● Known for a proactive mindset, attention to detail, and commitment to quality. \n\n
● Passionate about continuous learning and professional development—currently expanding skills in Python programming, 
building simple applications, and exploring AI technologies to enhance automation capabilities and deliver smarter solutions.
""")
# with open(RESUME_FILE, "rb") as pdf_file:
#     PDFbyte = pdf_file.read()
# st.download_button(label="📥 Download Resume", data=PDFbyte, file_name="Boris_Labuda_Resume.pdf", mime="application/pdf")

#timeline
with st.container():
    st.markdown("""""")
    st.subheader('⏳ Career Snapshot ⏳')

    # load data
    with open('tk_career.json', "r") as f:
        data = f.read()

    # render timeline
    timeline(data, height=500,)

st.divider()
with st.container():
    col1,col2 = st.columns(2)
    with col1:
        # ----- EXPERIENCE -----
        st.markdown("<h2 class='hd1'> 💼 Work Experience</h2>",unsafe_allow_html=True)
        
        st.markdown("<h3>Process automation developer | Ecco SKO A/S",unsafe_allow_html=True)
        st.caption("apr 2024 – Present")
        st.write("""
            - analyzing business processes and identifying automation opportunities
            - developing and deploying RPA solutions using Blue Prism
            - collaborating with business stakeholders to gather requirements
            - providing support and maintenance for existing RPA solutions.
            - creating a well-structured and maintainable automation
            - training younger colleagues
        
        """)        
        st.markdown("<h3>Junior Process automation developer | Ecco SKO A/S</h3>",unsafe_allow_html=True)
        st.caption("sep 2021 – mar 2024")
        st.write("""
            - analyzing business processes and identifying automation opportunities
            - developing and deploying RPA solutions using Blue Prism
            - collaborating with business stakeholders to gather requirements
            - providing support and maintenance for existing RPA solutions.
        """)

        st.markdown("<h3> Senior Analyst | Prima Banka Slovensko </h3>",unsafe_allow_html=True)
        st.caption("<p style='line-height: 0.2;'>dec 2014 – aug 2021</p>",unsafe_allow_html=True)
        st.write("""
        - preparation of regular and ad hoc reports for the Board of Directors, ensuring informed decision
        - conducting client data analysis to support strategic business insights and loan approval processes
        - drafting and implementing internal regulations to enhance company operations
        - designing automation solutions to improve process efficiency and workflow optimization
        - collaborating closely with the IT department to define software requirements and oversee testing phases
        """)

        st.markdown("<h3>Credit risk Analyst  | Prima Banka Slovensko </h3>",unsafe_allow_html=True)
        st.caption("<p style='line-height: 0.2;'>jan 2013 – dec 2014</p>",unsafe_allow_html=True)
        st.write("""
        - analysing credit risk
        - analysing financial statements, credit reports, and other data 
        - determine the risk associated with lending
        - evaluating creditworthiness
        """)

        st.markdown("<h3> Fraud Analyst | Prima Banka Slovensko </h3>",unsafe_allow_html=True)
        st.caption("<p style='line-height: 0.2;'>july 2012 – dec 2012</p>",unsafe_allow_html=True)
        st.write("""
        - investigating potential instances of fraud  
        - analyzed data
        - monitoring transactions
        """)


    with col2:
        st.markdown("<h2 class='hd1'> 📚 Education</h2>",unsafe_allow_html=True)
        # Education

        st.subheader("Matej Bel University in Banská Bystrica ")
        st.subheader("The Faculty of Economics")
        st.write("**Master Study Program: Finance, Banking and Investment**")
        st.write("**Main specialization: Audit/Accounting and IT technologies**")
        st.caption("09/2007 – 06/2012")

        st.subheader("Business Academy")
        st.caption("09/2003 – 06/2007")
        st.divider()
        
        #certification
        st.subheader("Additional education and achievements")
        st.write("""
        - **Blue Prism Developer Certification** (2022)
        - **Python Developer Certification** (2025)
        """)
        st.divider()
        
        # Skills
        st.subheader("Skills")
        st.write("""
        - Programming:  Python - beginner level 🔗 [GitHub](https://github.com/Tatana0409)
        - Database: MSSQL, MySQL
        - Automation tools: Blue Prism
        - Microsoft Power Platform: Power Automate, Power BI
        - Git Hub
        - MS Copilot
        - Jira Software
        """)
        st.divider()

        # Language
        st.subheader("Language")
        st.write("""
                - English: intermediate (B2)
                """)

