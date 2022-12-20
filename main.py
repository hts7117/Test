import streamlit as st
import pickle

navieBayes = pickle.load(open("NavieBayes.pkl", "rb"))

def predict_from_raw(model, text):
    return "Đây là tin thật" if model.predict([text]) == 0.0 else "Đây là tin giả"

def main():
    st.title("Fake news detection")

    options = st.selectbox(
         'Choose model:',
         ['None', 'Navie Bayes', 'SVM Gausssian', 'SVM Liner', 'SVM Poly', 'SVM Sigmoid'])

    st.write('Options: ', options)

    with st.form(key="text"):
        raw_text = st.text_area("News")
        submit = st.form_submit_button(label='Submit')

    if submit:
        if options == 'Navie Bayes':
            model = navieBayes
            st.write(predict_from_raw(model, raw_text))

if __name__ == '__main__':
    main()