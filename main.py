import streamlit as st
from options import options
from templates import (
    account_template,
    non_managed_hold,
    previous_template,
    previous_template_with_enddate,
    previous_template_blank_end
)

st.set_page_config(page_title="Revport XML Loader Generator")
st.title("Revport XML Loader Generator")

# Dropdown Section
selection = st.selectbox("Choose Loader Type", options)

# Logic for Put Account on Non-Managed Hold
if selection == "Put Account on Non-Managed Hold":
    account_id = st.text_input("Client Account Id")
    name = st.text_input("Account Name")
    start_date = st.date_input("Start Date")
    template = st.selectbox("Choose Template", account_template)

    if st.button("Generate XML"):
        xml = previous_template(account_id, name, start_date.strftime("%m/%d/%Y"), template)
        st.code(xml, language=None)

        st.download_button(
            label="Download XML",
            data=xml.encode("utf-8"),
            file_name=f"{account_id}_non_managed_hold.xml",
            mime="application/xml"
        )

# Logic for Account back on previous Template
elif selection == "Put the Account back on Previous Template":
    account_id = st.text_input("Client Account Id")
    name = st.text_input("Account Name") 
    start_date = st.date_input("Start Date")
    template = st.selectbox("Choose Template", account_template)

    if st.button("Generate XML"):
        xml = previous_template(account_id, name, start_date.strftime("%m/%d/%Y"), template)
        st.code(xml, language=None)

        st.download_button(
            label="Download XML",
            data=xml.encode("utf-8"),
            file_name=f"{account_id}_previous_template.xml",
            mime="application/xml"
        )

# Logic for Account back on previous template with updated EndDate
elif selection == "Put the Account Back On Previous Template w/ updated EndDate":
    account_id = st.text_input("Client Account Id")
    name = st.text_input("Account Name") 
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    template = st.selectbox("Choose Template", account_template)

    if st.button("Generate XML"):
        xml = previous_template_with_enddate(
            account_id, name,
            start_date.strftime("%m/%d/%Y"),
            end_date.strftime("%m/%d/%Y"),
            template
        )
        st.code(xml, language=None)

        st.download_button(
            label="Download XML",
            data=xml.encode("utf-8"),
            file_name=f"{account_id}_with_enddate.xml",
            mime="application/xml"
        )

# Logic for Account back on previous template with blanked out EndDate
elif selection == "Put Account Back on Previous Template w/ blanked out EndDate":
    account_id = st.text_input("Client Account Id")
    name = st.text_input("Account Name") 
    start_date = st.date_input("Start Date")
    template = st.selectbox("Choose Template", account_template)

    if st.button("Generate XML"):
        xml = previous_template_blank_end(account_id, name, start_date.strftime("%m/%d/%Y"), template)
        st.code(xml, language=None)

        st.download_button(
            label="Download XML",
            data=xml.encode("utf-8"),
            file_name=f"{account_id}_blanked_enddate.xml",
            mime="application/xml"
        )

st.markdown("Author: Kevin Vo")
