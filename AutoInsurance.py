import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

insurance = pd.read_csv('AutoInsurance.csv')
insurance.columns = insurance.columns.str.replace(' ','_')
insurance['Effective_Date'] = pd.to_datetime(insurance['Effective_To_Date'])
insurance['Response'] = insurance['Response'].map({'Yes': True, 'No': False}) 

st.header("Auto Insurance Analysis")
st.subheader('This is customer data with their vehicle insurance policies. Details about customers and the insurance taken for their vehicles are provided. ')

st.divider()

col1,col2 = st.columns(2)
customers  = insurance.groupby('State')['Customer'].count()
with col1:
    st.markdown('This graph shows that most of our customers are from California and Oregon ')
    st.write('It was also analyzed that the highest customer lifetime value came back to a client from Oregon')
    st.dataframe(insurance[insurance['Customer_Lifetime_Value']==83325.38119][['Customer','State','Customer_Lifetime_Value']])
with col2:
    st.write(px.bar(customers))
    
    
st.subheader('Our Sales Channels')
st.divider()

col1,col2 = st.columns(2)
response_rates_by_channel = insurance.groupby('Sales_Channel')['Response'].mean()
with col1:
    st.markdown('This graph shows that the most effective channel based on customers reponse is the Agent channel')
with col2:
    st.write(px.bar(response_rates_by_channel))
    

    
st.header('Response of Customers')
st.divider()
response_rate = (insurance['Response'].sum()/insurance['Response'].count()*100)
correlation = round(insurance['Response'].corr(insurance['Number_of_Policies']),2)
col1,col2 = st.columns(2)
with col1:
    st.write('We found that the response rate of customers is only ',round(response_rate,2),'%')
    st.write(f'Also, it was found that the customers who set more policies are the ones who tend not to respond, That was indicated after                calculating the correlation between the number of policies and response rate which is {correlation}.')
    st.write('The correlation is negative which means that the higher the number of policies the less responde we get.')
    
    
with col2:
    st.image('no-response-thats-fine-yep-cool-just-talking-to-myself.gif',width=400)
    
    
sales = insurance.groupby("Sales_Channel").agg(response_rate=('Response', 'mean'),
                                         customer_lifetime_value=('Customer_Lifetime_Value', 'mean')).reset_index()
st.write(px.bar(sales, x="Sales_Channel", y="response_rate"))


st.header('Reasons that why this could occured')
st.markdown(
"""
- Increased workload
                       
- Lack of automated solutions
                              
- Staff training and knowledge gaps 
"""
)

st.subheader('which means that we should find some solutions')
st.markdown(
"""
- Implement chatbots or AI-powered assistants 
                       
- Conduct customer satisfaction surveys
                              
- Streamline the communication process

- Simplify the claims process
"""
)
st.divider()



st.header('Customer Lifetime Value')
st.markdown('Which is a metric that represents the total net profit a company can expect to generate from a customer throughout their entire relationship.')


Policy_Type, Renew_Offer_Type, Sales_Channel = st.tabs(["Policy_Type", "Renew_Offer_Type", "Sales_Channel" ])

with Policy_Type:
    clv_by_policy_type = insurance.groupby('Policy_Type')['Customer_Lifetime_Value'].mean()
    col1,col2 = Policy_Type.columns(2)
    with col1:
        st.markdown("The difference between policy types it not big, but Special Auto policy type remains to be the one givind the highest customer lifetime value")
        st.subheader('What could be done?')
        st.markdown('''
        - Increase premiums for the Special Auto policy type if customers are willing to pay more for it.
        
        - Invest more in marketing efforts to target specific customer segments that are more likely to opt for this high-value policy                 type. 
        
        - Retention efforts: Identifying customers who have purchased the high-value policy type allows the company to provide special                incentives, discounts, or improved customer service to increase policy renewals and promote customer loyalty.
        
        - Review and analyze the least profitable policies to determine the reason for their lack of profitability by examining factors such           as the risk profile of the policyholders, pricing strategies, and the cost of claims.
        
        ''')
    with col2:
                st.write( px.bar(clv_by_policy_type))
        
        
with Renew_Offer_Type:
    col1,col2 = Renew_Offer_Type.columns(2)
    clv_by_offer_type = insurance.groupby('Renew_Offer_Type')['Customer_Lifetime_Value'].mean()

    with col1:
        st.markdown('It is shown that Offer1 is the most profitable offer')
        st.header('How to benefit from this?')
        st.markdown('''
        - Focus the resources and efforts on promoting and selling that particular Offer.
        - Market its unique value proposition, emphasize the advantages of the profitable offer, and position itself as a leader in that               specific product or service category.
        - Future business decisions, The company can make informed choices regarding pricing strategies, product development, resource                  allocation, and market expansion.
        - Catering to customers' preferences and needs.
        - Company that consistently offers highly profitable products or services can build a strong brand reputation. 
        
        ''')
        
    with col2:
        st.write( px.bar(clv_by_offer_type))
        
        
with Sales_Channel:
    col1,col2 = Sales_Channel.columns(2)
    clv_by_sales_channel = insurance.groupby('Sales_Channel')['Customer_Lifetime_Value'].mean()
    with col1:
        st.markdown('The most profitable sales channel goes to the Branch channel, but also other channels are doing great their is no such                      a big difference.')
        st.subheader('Ways to boost the profits more')
        st.markdown('''
        -  Provide sales training and incentives to sales staff workingto improve their skills and maximize their sales potential.
        - Invest in technology solutions that can automate processes, enhance customer experience, and provide insights into sales                     performance.
        - Implement key performance indicators (KPIs) to measure profitability, such as gross profit margin, return on investment, and                   average transaction value.
        - Ensure that pricing is competitive yet profitable.
        - Build customer loyalty
        - Understand your customers.
        ''')
        
        
    with col2:
                st.write( px.bar(clv_by_sales_channel))

            
st.divider()

st.header('Claims based on employment status and gender')
grouped_data1 = insurance.groupby(["EmploymentStatus", "Gender"])["Number_of_Open_Complaints"].mean()  
#Reshape the grouped data to make it easier to plot and analyze
grouped_data1 = grouped_data1.reset_index()
col1,col2 = st.columns(2)
with col1:
    st.markdown('Retired people recorded the highest claims where males claimed more.')
    st.header('What can we do about that?')
    st.markdown('''
               - Offer comprehensive retirement planning assistance
               - Tailor insurance products to retiree needs
               - Provide incentives for proactive risk management: Encourage retired customers to take preventive measures by offering                        discounts or incentives for implementing safety measures, maintaining a healthy lifestyle, or participating in wellness                      programs.
               - Not all males or females share the same experiences, perspectives, or interests. It is important to recognize and value the                  unique contributions that individuals from all genders can bring to any discussion or situation.
               
               
               ''')
with col2:
     st.write(px.bar(grouped_data1, x="EmploymentStatus", y="Number_of_Open_Complaints", color="Gender", barmode="group"))

        
        
st.divider()
st.header('Best offer choosed by customers')
by_offer_type = insurance.loc[insurance.Response == True].groupby("Renew_Offer_Type")["Customer"].count()/insurance.groupby("Renew_Offer_Type")["Customer"].count()

col1,col2 = st.columns(2)
with col1:
    st.write('It is shown that Offer 2 is the most responded offer to by customers')
    st.write("Since that we knew before that offer 1 was the most profitable by the customer lifetime value, We have to change things about              the offer to make it also most demanded.")
    st.header('Actions to take')
    st.markdown('''
                - Implement the most effective offer across all relevant marketing channels.
                - Allocate resources to support the most effective offer.
                - Keep a close eye on customer response and feedback. 
                - Use the data collected from customer response analysis to identify any areas of improvement.
                - Regularly evaluate and adjust the offer: Keep track of market dynamics, customer preferences, and changing trends, and                       periodically evaluate the effectiveness of the offer.
                
                
                ''')
with col2:
    st.write(px.bar(data_frame = by_offer_type))