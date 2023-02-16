import streamlit as st
from datetime import *
import calendar
incomes=['Salary','Blogs','Videos']
expences=['Rent','Phone bills','car','groceries','savings','other expences']
Currency='Rupees'
page_title='Income and Expences Tracker'
page_icon=':money_with_wings:'
layout='centered'
st.set_page_config(page_title=page_title,page_icon=page_icon,layout=layout)
st.title(page_title+" "+page_icon)
# years=[2022,2023]
# months=[jan,feb,march,apr,may,june,july,aug,sep,octu,nov ,dec]
years=[datetime.today().year,datetime.today().year+1]
months=list(calendar.month_name[1:])
st.header(f'Data Entry in {Currency}')
with st.form('entry_form',clear_on_submit=True):
    col1,col2=st.columns(2)
    col1.selectbox('select Month:',months,key='month')
    col2.selectbox('select Year',years,key='year')
    submitted = st.form_submit_button('Save Data')
    if submitted:
        period=str(st.session_state['years'])+''+str(st.session_state['month'])
        imcomes={income: st.session_state[income] for income in incomes}
        expences={expence: st.session_state[expence] for expence in expences}
        st.write(f'income:{incomes}')
        st.write(f'expences:{expences}')

'------'
with st.expander('Income'):
   for income in incomes:
        st.number_input(f'{income}',min_value=0,format='%i',step=10,key=income)
with st.expander('Expenses'):
    for expence in expences:
        st.number_input(f'{expence}',min_value=0,format='%i',step=10,key=expence)
with st.expander('Comment'):
    comment=st.text_area('',placeholder='Enter a comment here...')
    '-----'
st.header("Data Visualization")
with st.form('Saved_periods'):
    period=st.selectbox('Select Period:',['2023_March'])
    submitted=st.form_submit_button('Track')
    if submitted:
        comment='Some comment'
        incomes={'Salary':1500,'Blog':50,'Videos':10}
        expences={'Rent':600,'Phone bills':20,'car':30,'groceries':100,'savings':200,'other expences':100}

        total_income=sum(incomes.values())
        total_expences=sum(expences.values())
        remaining_budget=total_income-total_expences
        c1,c2,c3=st.columns(3)
        c1.metric('Total Income',f"{total_income}{Currency}")
        c2.metric('Total Expencs',f'{total_expences}{Currency}')
        c3.metric('Remaining Budget',f'{remaining_budget}{Currency}')
