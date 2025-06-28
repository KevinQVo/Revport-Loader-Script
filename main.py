import streamlit as st
from options import options
from templates import account_template

st.set_page_config(page_title="Revport XML Loader Generator")
st.title("Revport XML Loader Generator")

# Dropdown Section
selection = st.selectbox("Choose Loader Type", options)

#logic for Put Account on Non-Managed Hold
if selection == "Put Account on Non-Managed Hold":
  account_id = st.text_input("Client Account Id")
  name = st.text_input("Account Name")
  start_date = st.date_input("Start Date")
  if st.button("Generate XML button")
    xml = generate_xml.hold_tempalate(account_id, name, start_date)
    st.code(xml, language="xml")

#logic for Account back on previous Template
elif selection == "Put Account back on Previous Template":
  account_id = st.text_input("Client Account Id")
  name = st.text_input("Account Name") 
  start_date = st.date_input("Start Date")
  template = st.selectbox("Choose Template", generate_xml.template_list)

  if st.button("Generate XML button")
    xml = generate_xml.hold_tempalate(account_id, name, start_date, template)
    st.code(xml, language="xml")

#logic for Account back on previous template with blanked out end date
elif selection == "Put Account back on Previous Template w/ blanked out EndDate":
  account_id = st.text_input("Client Account Id")
  name = st.text_input("Account Name") 
  start_date = st.date_input("Start Date")
  end_date = st.date_input("End Date)
  template = st.selectbox("Choose Template", generate_xml.template_list)

  if st.button("Generate XML button")
    xml = generate_xml.hold_tempalate(account_id, name, start_date, end_date,  template)
    st.code(xml, language="xml")

