import streamlit as st
import pickle

def process_text(s):

    # Check string to see if they are a punctuation
    nopunc = [char for char in s if char not in string.punctuation]

    # Join the characters again to form the string.
    nopunc = ''.join(nopunc)
    
    # Convert string to lowercase and remove stopwords
    clean_string = [word for word in nopunc.split()]
    return clean_string

test = pickle.load(open('Model/NaiveBayes.pkl', 'rb'))

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
            model = test
            st.write(predict_from_raw(model, raw_text))

if __name__ == '__main__':
    main()