import streamlit as st
import pickle

pickle_in = open("model.pkl","rb")
model = pickle.load(pickle_in)


def pred(preg, plas, pres, skin, insu, mass, pedi, age):
    pred = model.predict([[preg, plas, pres, skin, insu, mass, pedi, age]])
    print(pred)
    return pred

def main():
    st.title("Diabetes in Pima Indians")
    preg = st.text_input("Number of times Pregnant")
    plas = st.text_input("Plasma glucose concentration")
    pres = st.text_input("Diastolic blood pressure")
    skin = st.text_input("Triceps skin fold thickness")
    insu = st.text_input("2-Hour serum insulin")
    mass = st.text_input("Body mass index")
    pedi = st.text_input("Diabetes pedigree function")
    age = st.text_input("Age")

    result=""
    if st.button("Predict"):
        result=pred(preg, plas, pres, skin, insu, mass, pedi, age)
    st.success('The person will be {}'.format(result))

if __name__=='__main__':
    main()