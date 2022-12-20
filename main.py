import streamlit as st

def main():
    st.title("Fake news detection")

    options = st.selectbox(
         'Choose model:',
         ['None', 'Logistic Regression', 'MLP Classifier', 'SVM with kernel RBF'])

    st.write('Options: ', options)

    with st.form(key="text"):
        raw_domain = st.text_area("Domain")
        raw_text = st.text_area("News")
        submit = st.form_submit_button(label='Submit')

if __name__ == '__main__':
    main()