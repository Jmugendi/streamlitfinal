import pickle
import streamlit as st


model = pickle.load(open('C:/Users/Jaymoh/Desktop/projects/venv/lpgsafety/rf_model.pkl',"rb"))

def main():
    st.title('LPG GAS SAFETY APP')

    st.subheader("Why use the app?")
    ("Data from the Energy and Petroleum Regulatory Authority(EPRA) indicates that atleast")
    ("22 accidents involving gas cylinder explosions have been recorded in the last 12 months") 
    ("translating on average to 2 cases every month.These accidents have claimed 13 lives")

    ("It is for this reason that we request all LPG Gas consumers to input the details provided on the cylinder.")
    ("The details will give the safety assuarance while purchasing cylinder once you submit")
    
    st.subheader("Fill in and click button below")

    # INPUT VARIABLES
    Serial_Numbers =st.sidebar.text_input('Serial Number')
    Inspection_Year =st.sidebar.text_input('Inspection_Year')
    Verification_Code =st.sidebar.text_input('Verification_Code')

    # prediction
    if st.button('SUBMIT DETAILS'):
        make_prediction = model.predict([[Serial_Numbers,Inspection_Year,Verification_Code]])
        output = (make_prediction)
        st.success('The cylinder is safe until{}'.format(output))


if __name__ == '__main__': 
    main()