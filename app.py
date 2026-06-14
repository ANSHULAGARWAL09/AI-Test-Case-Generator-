import streamlit as st

from agents.testcase_agent import (
    generate_test_cases
)

from utils.parser import (
    parse_response
)

from utils.excel_writer import (
    save_excel
)

st.set_page_config(
    page_title="AI Test Case Generator",
    layout="wide"
)

st.title(
    "🤖 AI Test Case Generator - By Anshul"
)

st.markdown(
    "Generate QA Test Cases using AI"
)

requirement = st.text_area(
    "User Story",
    height=200
)

acceptance = st.text_area(
    "Acceptance Criteria",
    height=200
)

if st.button("Generate Test Cases"):

    result = generate_test_cases(
        requirement,
        acceptance
    )

    st.code(result)

    data = parse_response(
        result
    )

    st.success(
        "Generated Successfully"
    )

    st.dataframe(
        data,
        use_container_width=True
    )

    file = save_excel(data)

    with open(file, "rb") as f:

        st.download_button(
            "📥 Download Excel",
            f,
            file_name="testcases.xlsx"
        )

