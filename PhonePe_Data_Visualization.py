#Neccessary Libraries
import os
import git
import sys
import json
import requests
import numpy as np
import pandas as pd
import mysql.connector
from PIL import Image
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

#Page Icon Setup
image_path = "C:/Users/91733/OneDrive/Desktop/PhonePe/download.png"
st.set_page_config(page_title="PhonePe Pulse Data", page_icon=Image.open(image_path), layout="wide",)

#Home Page Setup
title_html = """<h1 style="text-align: center;"><span style="color: #800080;">Exploring Payment Trends in India with </span>
        <span style="color: #800080; text-decoration: underline;">PhonePe</span></h1>"""
st.markdown(title_html, unsafe_allow_html=True)
Home, About, Data_overview, Data_Insights, Exit=st.tabs(["HOME", "ABOUT", "DATA OVERVIEW", "DATA INSIGHTS",  "EXIT"])

#Home TAB
with Home:
    col1,col2=st.columns([2.5,3])
    with col1:
        image_path="C:/Users/91733/OneDrive/Desktop/PhonePe/fast-secure-video-poster-v3-6f33427d52f42e474727f7442b029c59.png"
        st.image(Image.open(image_path), width=450)    
              
        st.write("---")
        st.markdown("## :violet[Done by] : Selvi K")
        st.markdown("[Inspired from](https://www.phonepe.com/pulse/about-us/)")
        st.markdown("[Githublink](https://github.com/Selvi-Kimchi)")
        st.markdown("[LinkedIn](https://www.linkedin.com/in/selvi-k/)")
        
    with col2:
        st.title("Welcome to PhonePe Pulse Data Insights!")
        st.markdown("Explore the heartbeat of digital transactions with our interactive visualizations.")
        st.markdown("Discover trends, spending patterns, and more.")

        # Overview Section
        st.header("Overview")
        overview_points = [
            "PhonePe Pulse provides personalized analytics based on your transaction history.",
            "Understand your financial behavior and make informed decisions.",
            "From transactions to trends, we’ve got you covered."
        ]
        for point in overview_points:
            st.markdown(f"- {point}")

        # Key Features Section
        st.header("Key Features")
        features_points = [
            "📊 All India Insights: Explore nationwide trends.",
            "🗺️ State-wise Analysis: Dive into regional data.",
            "🔍 Top Categories: Discover popular spending areas."
        ]
        for point in features_points:
            st.markdown(f"- {point}")

#ABOUT TAB
with About:
        

    
    # Founders Section
    founders_data = [
    {
        "name": "Sameer Nigam",
        "role": "Founder and CEO",
        "description": "Sameer Nigam, the Founder and CEO of PhonePe, brings extensive expertise in engineering, marketing, and product management, honed through key roles at Flipkart and Shopzilla Inc. He holds an MBA from Wharton Business School and a Master’s in Computer Science from the University of Arizona.",
        "image_path": "C:/Users/91733/OneDrive/Desktop/PhonePe/sameer-nigam-793cafbd4e3997f4383551fd9778b717.png"
    },
    {
        "name": "Rahul Chari",
        "role": "Co-Founder and CTO",
        "description": "Rahul Chari, the Chief Technology Officer at PhonePe, brings over two decades of diverse experience in embedded systems, enterprise software development, and e-commerce platforms. He played a pivotal role in building supply chain systems at Flipkart and holds a Master's degree in Computer Science from Purdue University, USA.",
        "image_path": "C:/Users/91733/OneDrive/Desktop/PhonePe/rahul-chari-f32d8c77ff33502f4aaaa50b3e61c96e.png"
    },
    {
        "name": "Burzin Engineer",
        "role": "Co-Founder and CRO",
        "description": "Burzin Engineer, Chief Reliability Officer at PhonePe, brings over 25 year of IT industry experience, specializing in web-scale infrastructure and engineering projects. He holds a Master of Science in Computer Science from the University of Southern California.",
        "image_path": "C:/Users/91733/OneDrive/Desktop/PhonePe/burzin-engineer-0eedaf98eb5b4077d6a1859a07618e6d.png"
    }
]

    # Display founders information
    st.header(":blue[Founders]")
    
    col1, col2 = st.columns([1, 3])

    for founder in founders_data:
        with col1:
            st.image(Image.open(founder["image_path"]), width=145)
        with col2:
            st.subheader(f"{founder['name']} - {founder['role']}")
            st.markdown(founder["description"])
            

    # Company Overview Section
    st.header("Company Overview")
    overview_points = [
        "PhonePe provides a Unified Payments Interface (UPI)-based payment platform.",
        "It facilitates various financial transactions, including money transfers, mobile and DTH recharges, utility payments, and in-store payments.",
        "The app is accessible in 11 Indian languages."
    ]
    for point in overview_points:
        st.markdown(f"- {point}")

    # History Section
    st.header("History")
    history_points = [
        "PhonePe was incorporated in December 2015.",
        "In April 2016, it was acquired by Flipkart, and the FxMart license was transferred to PhonePe, rebranded as the PhonePe wallet.",
        "The PhonePe app, based on the government-backed UPI platform, went live in August 2016.",
        "Over the year, PhonePe surpassed BHIM in UPI transactions and expanded its services internationally."
    ]
    for point in history_points:
        st.markdown(f"- {point}")

    # Achievements Section
    st.header("Achievements")
    achievements_points = [
        "PhonePe currently holds a 50% market share by value of transactions in the UPI market.",
        "It obtained licensing from the Reserve Bank of India for operating a Semi-Closed Prepaid Payment system."
    ]
    for point in achievements_points:
        st.markdown(f"- {point}")

    # Vision Section
    st.header("Vision")
    st.markdown("PhonePe aims to empower users by providing seamless digital payment experiences and insights into their financial behavior.")
    
    #PhonePe App features
    st.header("PhonePe App Features and Facilities")
    col1,col2=st.columns(2)
    with col1:
        app_features=["UPI Payments: 📲💸",
                        "Multiple Payment Options: 💳💰",
                        "Mobile Recharge & Bill Payments: 📱🔋💡",
                        "Online Shopping & Merchant Payments: 🛒💳",
                        "Insurance Premium Payments: 🛡️💵",
                        "Investment Options (Mutual Funds, Gold, ELSS): 📈💰",
                        "Money Transfers (Bank Account & IFSC): 💸🔄",
                        "QR Code Payments: 📷💳",
                        "Transaction History & Statements: 📊📜",
                        "Rewards & Cashback: 🎁💰",
                        "Customer Support: 🤝📞",
                        "Security Features (Encryption, 2FA): 🔒🛡️"]
        for point in app_features:
                st.markdown(f"- {point}")
    with col2:
        text = "--> Click Here to Download the PhonePe app"
        url = "https://play.google.com/store/apps/details?id=com.phonepe.app&hl=en_IN&shortlink=2kk1w03o&c=consumer_app_icon&pid=PPWeb_app_download_page&af_xp=custom&source_caller=ui&pli=1"
        
        
        markdown_text = f"""
        <div style='text-align: center;'>
            <a href='{url}' target='_blank'>
                <i class='fas fa-download' style='font-size: 24px;'></i> {text}
            </a>
        </div>
        """
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.write("")
        st.video("https://youtu.be/Yy03rjSUIB8")
        st.markdown("[Watch all videos](https://www.youtube.com/watch?v=aI2aqXtfXr8&list=PL4dV2TSluEZyeLy1MovjRnyECn1o25FFQ)")
        

    st.markdown("[PhonePe official YouTube Link](https://www.youtube.com/@PhonePe_#)")

#Data overview TAB
with Data_overview:
    st.title(":violet[Data Overview]")
    st.markdown("[GitHub Link for PhonePe Pulse Dateset](https://github.com/PhonePe/pulse.git)")
    st.write("PhonePe Pulse is a comprehensive dataset that contains transaction data from the PhonePe digital payment platform. This dataset provides valuable insights into customer behavior, transaction patterns, and trends related to digital payments in India.")
    st.subheader("1. Aggregated Data")
    aggregated_data_points = [
        "PhonePe Pulse offers aggregated values across various payment categories.",
        "These categories include transactions related to bill payments, recharges, online shopping, and more.",
        "By analyzing aggregated data, users can understand overall trends and preferences in digital payments."
    ]

    # Geospatial Insights Section
    st.subheader("2. Geospatial Insights")
    geospatial_insights_points = [
        "The dataset includes data at both the state and district levels.",
        "Users can explore total transaction values for different regions, helping them identify geographic patterns."
    ]

    # Top Metrics Section
    st.subheader("3. Top Metrics")
    top_metrics_points = [
        "PhonePe Pulse provides totals for the top state, district, and postal codes.",
        "These metrics highlight areas with the highest transaction volumes and offer insights into local payment behavior."
    ]

    # Display insights with bullet points
    st.markdown("### Aggregated Data")
    for point in aggregated_data_points:
        st.markdown(f"- {point}")

    st.markdown("### Geospatial Insights")
    for point in geospatial_insights_points:
        st.markdown(f"- {point}")

    st.markdown("### Top Metrics")
    for point in top_metrics_points:
        st.markdown(f"- {point}")

    st.header("Folder Structure of PhonePe Pulse Data")
    st.image(Image.open("C:/Users/91733/OneDrive/Desktop/PhonePe/DataFormat.jpg"))
    
    metrics_definitions = {
        "App installs": "The total number of times the PhonePe app was installed on mobile devices.",
        "App opens": "Includes in-app opens and out-of-app opens. In-app opens are the number of times the PhonePe app was opened by users and the app's home page loaded successfully. Out-of-app opens are counted when a user initiates a payment on a merchant's website/app.",
        "Billpay": "An action of paying a bill online, through the PhonePe app. This includes successful utility bill payments (e.g., Electricity, internet, telephone bill payments, etc.), net of reversals.",
        "CAGR": "Compounded Annual Growth Rate, representing the total growth % over a period, annualized to a year.",
        "Category": "The broad need under which a transaction occurs (e.g., utility bill payments, mobile recharges, etc.).",
        "Customers": "Users that performed at least one transaction on the PhonePe app within a specific period.",
        "Digital payments": "Monetary exchange executed via digital instructions, where the money leaves the sender's bank and arrives directly in the receiver's bank account.",
        "Financial services transactions": "Total number of successful payments made to buy financial services or gold on the PhonePe app.",
        "Gold customers": "Total number of registered users who made a successful payment to buy gold on PhonePe.",
        "Merchant transactions": "Total number of successful payments made to merchants on the PhonePe app.",
        "Monthly active users": "Count of unique users who opened the PhonePe app or initiated a PhonePe payment outside of the app at least once in a month.",
        "Offline merchants": "Brick-and-mortar outlets that PhonePe has onboarded as merchants.",
        "Offline transactions": "Digital transactions occurring face-to-face, such as payments made at physical stores using a digital app like PhonePe.",
        "Online merchants": "Merchants integrated with PhonePe as a payment method on their app/website.",
        "Online transactions": "Digital transactions occurring over the internet, such as payments on apps or websites.",
        "P2P transactions": "Total number of successful money transfer transactions on the UPI framework.",
        "Recharges": "Top-up of talk time or data packs by prepaid mobile users.",
        "Registered Users": "Number of unique users who downloaded the PhonePe app and accepted the Terms and Conditions within a specific period.",
        "TPAPs": "Third Party Application Providers participating in the UPI via banks.",
        "TPV": "Total Payment Value, representing the total amount/value (in rupees) of transactions processed in a given time period.",
        "Value of gold purchased": "Total value of successful payments made to purchase gold on the PhonePe app."
    }

    st.title("Metric Definitions")

    # Display metric definitions
    for metric_name, metric_definition in metrics_definitions.items():
        st.subheader(metric_name)
        st.write(metric_definition)
 
#GEO DETAILS
class state:
    def ins_state_list():
        connection =  mysql.connector.connect(
                                            host='localhost',
                                            user='root',
                                            password='Kimch!811',
                                            database='PhonePe_Data'
                                        )
        cursor = connection.cursor()
        cursor.execute(f"""select distinct state from aggregated_insurance
                            order by state asc;""")
        s = cursor.fetchall()
        state = [i[0].title() for i in s]
        return state


    def ins_year_list():
        connection =  mysql.connector.connect(
                                            host='localhost',
                                            user='root',
                                            password='Kimch!811',
                                            database='PhonePe_Data'
                                        )
        cursor = connection.cursor()
        cursor.execute(f"""select distinct year from aggregated_insurance
                            order by year asc;""")
        s = cursor.fetchall()
        year = [i[0] for i in s]
        return year
    
    def type_list():
        connection =  mysql.connector.connect(
                                            host='localhost',
                                            user='root',
                                            password='Kimch!811',
                                            database='PhonePe_Data'
                                        )
        cursor = connection.cursor()
        cursor.execute(f"""select distinct transaction_type from aggregated_transaction;""")
        s = cursor.fetchall()
        type_list = [i[0] for i in s]
        return type_list
    
    def geo_state_list():
        url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response = requests.get(url)
        data = json.loads(response.content)
        geo_state = [i['properties']['ST_NM'] for i in data['features']]
        geo_state.sort(reverse=False)
        return geo_state

    def original_state_list():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select distinct State
                            from aggregated_transaction
                            order by State asc;""")
        s = cursor.fetchall()
        original_state = [i[0] for i in s]
        return original_state

    def state_dict():
        original = state.original_state_list()
        geo = state.geo_state_list()
        data = {}
        for i in range(0, len(original)):
            data[original[i]] = geo[i]
        return data

    def state_list(data):
        missed = set(state.original_state_list()
                     ).symmetric_difference(set(data))
        missed = list(missed)
        all_state = state.state_dict()
        if len(missed) > 0:
            for i in missed:
                del all_state[i]
        return list(all_state.values())
        
    def find_district(pincode):
        url = "https://api.postalpincode.in/pincode/" + str(pincode)
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if data and isinstance(data, list) and len(data) > 0:
                    post_offices = data[0].get('PostOffice', [])
                    if post_offices and isinstance(post_offices, list) and len(post_offices) > 0:
                        district = post_offices[0].get('District', 'Unknown')
                        return district
            return 'Unknown'
        except Exception as e:
            print(f"Error occurred while retrieving district for pincode {pincode}: {e}")
            return 'Unknown'

    def convert(transaction):
        amount = int(transaction.replace(',', ''))
        SUFFIXES = {
            3: 'K',   # Thousand
            6: 'M',   # Million
            9: 'B',   # Billion
            12: 'T',  # Trillion
            13: 'T'   
        }
        
        for magnitude in sorted(SUFFIXES.keys(), reverse=True):
            if len(str(amount)) >= magnitude:
                scaled_amount = amount / (10 ** magnitude)
                formatted_amount = f'{scaled_amount:.2f}{SUFFIXES[magnitude]}'
                return formatted_amount
        return str(amount)

#MAIN MENU
#1. INSURANCE 
class aggregated_insurance:

    def state_wise_premium_count():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, sum(transaction_count) as transaction_count 
                            from aggregated_insurance
                            group by state
                            order by state asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Premium Count'], index=i)
               
        data = data.sort_values(by='Premium Count', ascending=False)
        data = data.rename_axis('S.No')
        return data

    def state_wise_premium_amount():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, sum(transaction_amount) as transaction_amount 
                            from aggregated_insurance
                            group by state
                            order by state asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Premium Amount'], index=i)
               
        data = data.sort_values(by='Premium Amount', ascending=True)
        data['Premium Amount'] = data['Premium Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Premium'] = data['Premium Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data
    
    def year_wise_premium_count():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, sum(transaction_count) as transaction_count 
                            from aggregated_insurance
                            group by year
                            order by year asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['Year', 'Premium Count'], index=i)
        data = data.rename_axis('S.No')
        return data

    def year_wise_premium_amount():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, sum(transaction_amount) as transaction_amount 
                            from aggregated_Insurance
                            group by year
                            order by year asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'Premium Amount'], index=i)
        data['Premium Amount'] = data['Premium Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Premium'] = data['Premium Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def year_quarter_wise_premium_count():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(transaction_count) as transaction_count 
                            from aggregated_Insurance
                            group by quarter, year
                            order by year, quarter asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'Quarter', 'Premium Count'], index=i)
        data = data.rename_axis('S.No')
        data['Premium'] = data['Premium Count'].apply(lambda x: state.convert(str(x)))
        return data

    def year_quarter_wise_premium_amount():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(transaction_amount) as transaction_amount 
                            from aggregated_Insurance
                            group by quarter, year
                            order by year, quarter asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'Quarter', 'Premium Amount'], index=i)
        data['Premium Amount'] = data['Premium Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Premium'] = data['Premium Amount']
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_year_wise_premium_count(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, sum(transaction_count) as transaction_count 
                            from aggregated_insurance
                            where state=%s
                            group by year, state
                            order by year asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Premium Count'], index=i)
        data = data.rename_axis('S.No')
        return data

    def selectstate_year_wise_premium_amount(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, sum(transaction_amount) as transaction_amount 
                            from aggregated_insurance
                            where state=%s
                            group by year, state
                            order by year asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Premium Amount'], index=i)
        data['Premium Amount'] = data['Premium Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Premium'] = data['Premium Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_quarter_wise_premium_count(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, sum(transaction_count) as transaction_count 
                        from aggregated_insurance
                        where state=%s
                        group by quarter, state
                        order by quarter asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Quarter', 'Premium Count'], index=i)
        data = data.rename_axis('S.No')
        return data

    def selectstate_quarter_wise_premium_amount(select_state):
        connection = mysql.connector.connect(
                                            host='localhost',
                                            user='root',
                                            password='Kimch!811',
                                            database='PhonePe_Data'
                                           )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, sum(transaction_amount) as transaction_amount 
                            from aggregated_insurance
                            where state=%s
                            group by quarter, state
                            order by quarter asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Quarter', 'Premium Amount'], index=i)
        data['Premium Amount'] = data['Premium Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Premium'] = data['Premium Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_year_quarter_wise_premium_count(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(transaction_count) as transaction_count 
                        from aggregated_insurance
                        where state=%s
                        group by quarter, year, state
                        order by year, quarter asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Premium Count'], index=i)
        data = data.rename_axis('S.No')
        return data

    def selectstate_year_quarter_wise_premium_amount(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(transaction_amount) as transaction_amount 
                            from aggregated_insurance
                            where state=%s
                            group by quarter, year, state
                            order by year, quarter asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Premium Amount'], index=i)
        data['Premium Amount'] = data['Premium Amount'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Premium'] = data['Premium Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data
      
    def selectstate_selectyear_quarter_wise_premium_count(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(transaction_count) as transaction_count 
                        from aggregated_insurance
                        where state=%s and year=%s
                        group by quarter, year, state
                        order by quarter asc, transaction_count desc;""", (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Premium Count'], index=i)
        data = data.rename_axis('S.No')
        return data

    def selectstate_selectyear_quarter_wise_premium_amount(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(transaction_amount) as transaction_amount 
                            from aggregated_insurance
                            where state=%s and year=%s
                            group by quarter, year, state
                            order by quarter asc, transaction_amount desc;""", (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'Premium Amount'], index=i)
        data['Premium Amount'] = data['Premium Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        return data

    def selectstate_selectquarter_year_wise_premium_count(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(transaction_count) as transaction_count 
                        from aggregated_insurance
                        where state=%s and quarter=%s
                        group by quarter, year, state
                        order by year asc;""", (select_state, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'Premium Count'], index=i)
        data = data.rename_axis('S.No')
        return data

    def selectstate_selectquarter_year_wise_premium_amount(select_state, select_quarter):
        connection =mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(transaction_amount) as transaction_amount
                        from aggregated_insurance
                        where state=%s and quarter=%s
                        group by quarter, year, state
                        order by year asc;""", (select_state, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'Premium Amount'], index=i)
        data['Premium Amount'] = data['Premium Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Premium'] = data['Premium Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data
 
    def selectyear_state_wise_premium_count(select_year):
        connection =mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, sum(transaction_count) as transaction_count 
                            from aggregated_insurance
                            where year=%s
                            group by state, year;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Premium Count'], index=i)
        data['State']=data['State'].str.title()
        data = data.sort_values(by='Premium Count', ascending=False)
        data = data.rename_axis('S.No')
        return data

    def selectyear_state_wise_premium_amount(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, sum(transaction_amount) as transaction_amount 
                            from aggregated_insurance
                            where year=%s
                            group by year, state
                            order by state asc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Premium Amount'], index=i)
               
        data = data.sort_values(by='Premium Amount', ascending=False)
        data['Premium Amount'] = data['Premium Amount'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Premium'] = data['Premium Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_quarter_wise_premium_count(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(transaction_count) as transaction_count 
                            from aggregated_insurance
                            where year=%s
                            group by quarter, year
                            order by quarter asc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['Year', 'Quarter', 'Premium Count'], index=i)
        data = data.rename_axis('S.No')
        return data

    def selectyear_quarter_wise_premium_amount(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(transaction_amount) as transaction_amount 
                            from aggregated_insurance
                            where year=%s
                            group by quarter, year
                            order by year, quarter asc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'Quarter', 'Premium Amount'], index=i)
        data['Premium Amount'] = data['Premium Amount'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Premium'] = data['Premium Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selectquarter_state_wise_premium_count(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(transaction_count) as transaction_count 
                            from aggregated_insurance
                            where year=%s and quarter=%s
                            group by quarter, year, state
                            order by state asc;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'Premium Count'], index=i)
               
        data = data.sort_values(by='Premium Count', ascending=False)
        data = data.rename_axis('S.No')
        return data

    def selectyear_selectquarter_state_wise_premium_amount(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(transaction_amount) as transaction_amount 
                            from aggregated_insurance
                            where year=%s and quarter=%s
                            group by quarter, year, state
                            order by state asc;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Premium Amount'], index=i)
               
        data = data.sort_values(by='Premium Amount', ascending=False)
        data['Premium Amount'] = data['Premium Amount'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Premium'] = data['Premium Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data
   
    def selectquarter_state_wise_premium_count(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, sum(transaction_count) as transaction_count 
                            from aggregated_insurance
                            where quarter=%s
                            group by quarter, state
                            order by state asc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Quarter', 'Premium Count'], index=i)
               
        data = data.sort_values(by='Premium Count', ascending=False)
        data = data.rename_axis('S.No')
        return data

    def selectquarter_state_wise_premium_amount(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, sum(transaction_amount) as transaction_amount 
                            from aggregated_insurance
                            where quarter=%s
                            group by quarter, state
                            order by state asc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Quarter', 'Premium Amount'], index=i)
               
        data = data.sort_values(by='Premium Amount', ascending=False)
        data['Premium Amount'] = data['Premium Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Premium'] = data['Premium Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_year_wise_premium_count(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(transaction_count) as transaction_count 
                            from aggregated_insurance
                            where quarter=%s
                            group by quarter, year
                            order by year asc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'Quarter', 'Premium Count'], index=i)
        data = data.rename_axis('S.No')
        return data

    def selectquarter_year_wise_premium_amount(select_quarter):
        connection =mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(transaction_amount) as transaction_amount 
                            from aggregated_insurance
                            where quarter=%s
                            group by quarter, year
                            order by year asc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['Year', 'Quarter', 'Premium Amount'], index=i)
        data['Premium Amount'] = data['Premium Amount'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Premium'] = data['Premium Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data
 
class map_insurance:
    def state_wise_premium_count():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, sum(transaction_count) as transaction_count 
                            from map_transaction
                            group by state
                            order by transaction_count desc;""")
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State',  'Premium Count'])
               
        data = data.sort_values(by='Premium Count', ascending=False)
        data.reset_index(drop=True, inplace=True)
        data.index+=1
        data = data.rename_axis('S.No')
        return data
    
    def state_wise_premium_amount():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, sum(transaction_amount) as transaction_amount,  sum(transaction_amount)/sum(transaction_count) as avg_transaction
                            from map_transaction
                            group by state
                            order by transaction_amount desc, avg_transaction desc;""")
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State',  'Premium Amount', 'Average Premium'])
               
        data['Average Premium Amount'] = data['Average Premium'].apply(lambda x: float(round(x, 2)))
        data.reset_index(drop=True, inplace=True)
        data.index+=1
        data = data.rename_axis('S.No')
        return data

    def selectstate_district_wise_premium_count(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, district, sum(transaction_count) as transaction_count 
                            from map_transaction
                            where state=%s
                            group by district, state
                            order by transaction_count desc;""", (select_state,))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'District', 'Premium Count']) 
        data.reset_index(drop=True, inplace=True)
        data.index+=1
        data = data.rename_axis('S.No')
        return data
    
    def selectyear_state_wise_premium_count(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, state, sum(transaction_count) as transaction_count 
                            from map_transaction
                            where year=%s
                            group by state, year;
                            
                            """, (select_year,))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Premium Count'])
        data.reset_index(drop=True, inplace=True)
        data.index+=1
        data = data.rename_axis('S.No')
        return data
    
    def selectquarter_district_wise_premium_amount(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select quarter, district, sum(transaction_amount) as transaction_amount 
                            from map_insurance
                            where quarter=%s
                            group by district, quarter
                            order by transaction_amount desc limit 10;                            
                            """, (select_quarter,))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=[ 'Quarter', 'District', 'Premium Amount'])
        data.reset_index(drop=True, inplace=True)
        data.index+=1
        data = data.rename_axis('S.No')
        return data
    
    def selectquarter_district_wise_premium_count(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select quarter, district, sum(transaction_count) as transaction_count 
                            from map_insurance
                            where quarter=%s
                            group by district, quarter
                            order by transaction_count desc;
                            
                            """, (select_quarter,))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['Quarter','District',  'Premium Count'])
        data.reset_index(drop=True, inplace=True)
        data.index+=1
        data = data.rename_axis('S.No')
        return data
    
    def selectyear_district_wise_premium_count(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, district, sum(transaction_count) as transaction_count 
                            from map_transaction
                            where year=%s
                            group by district, year
                            order by transaction_count desc
                            limit 10;""", (select_year,))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['Year', 'District', 'Premium Count'])
        data.reset_index(drop=True, inplace=True)
        data.index+=1
        data = data.rename_axis('S.No')
        return data
    
    def selectyear_district_wise_premium_amount(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, district, sum(transaction_amount) as transaction_amount
                            from map_transaction
                            where year=%s
                            group by district, year
                            order by transaction_amount desc
                            limit 10;""", (select_year,))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['Year', 'District', 'Premium Amount'])
        data.reset_index(drop=True, inplace=True)
        data.index+=1
        data = data.rename_axis('S.No')
        return data

    def selectstate_district_wise_premium_amount(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, district, sum(transaction_amount) as transaction_amount, sum(transaction_amount)/sum(transaction_count) as avg_transaction
                            from map_transaction
                            where state=%s
                            group by district, state
                            order by transaction_amount desc, avg_transaction desc; """, (select_state))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'District', 'Premium Amount', 'Average Premium'], index=i)
               
        data['Premium Amount'] = data['Premium Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Premium'] = data['Average Premium'].apply(lambda x: float(round(x, 2)))
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['Premium Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_district_wise_premium_count(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, district, sum(transaction_count) as transaction_count 
                            from map_transaction
                            where state=%s and year=%s
                            group by district, year, state
                            order by year asc, transaction_count desc;""", (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'District', 'Premium Count'], index=i)
        data = data.rename_axis('S.No')
        return data

    def selectstate_selectyear_district_wise_premium_amount(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, district, sum(transaction_amount) as transaction_amount, sum(transaction_amount)/sum(transaction_count) as avg_transaction
                            from map_transaction
                            where state=%s and year=%s
                            group by district, year, state
                            order by year asc, transaction_amount desc, avg_transaction desc;""", (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'District', 'Premium Amount', 'Average Premium'], index=i)
               
        data['Premium Amount'] = data['Premium Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Premium'] = data['Average Premium'].apply(lambda x: float(round(x, 2)))
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['Premium Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectquarter_district_wise_premium_count(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, district, sum(transaction_count) as transaction_count 
                            from map_transaction
                            where state=%s and quarter=%s
                            group by district, quarter, state
                            order by quarter asc, transaction_count desc;""", (select_state, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Quarter', 'District', 'Premium Count'], index=i)
               
        data = data.rename_axis('S.No')
        return data

    def selectyear_selectquarter_district_wise_premium_count(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, district, sum(transaction_count) as transaction_count, sum(transaction_amount)/sum(transaction_count) as avg_transaction
                            from map_transaction
                            where year=%s and quarter=%s
                            group by district, quarter, state
                            order by quarter asc, transaction_count desc, avg_transaction desc;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'Quarter', 'District', 'Premium Count', 'Average Premium'], index=i)
        data['Average Premium'] = data['Average Premium'].apply(lambda x: float(round(x, 2)))
        data = data.rename_axis('S.No')
        return data

    def selectyear_selectquarter_district_wise_premium_amount(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, district, sum(transaction_amount) as transaction_amount, sum(transaction_amount)/sum(transaction_count) as avg_transaction
                            from map_transaction
                            where year=%s and quarter=%s
                            group by district, quarter, state
                            order by quarter asc, transaction_amount desc, avg_transaction desc;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'Quarter', 'District', 'Premium Amount', 'Average Premium'], index=i)
        data['Average Premium'] = data['Average Premium'].apply(lambda x: float(round(x, 2)))
        data = data.rename_axis('S.No')
        return data
    
    def selectstate_selectquarter_district_wise_premium_amount(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, district, sum(transaction_amount) as transaction_amount, sum(transaction_amount)/sum(transaction_count) as avg_transaction
                            from map_transaction
                            where state=%s and quarter=%s
                            group by district, quarter, state
                            order by quarter asc, transaction_amount desc, avg_transaction desc;""", (select_state, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Quarter', 'District', 'Premium Amount', 'Average Premium'], index=i)
        data['Premium Amount'] = data['Premium Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Premium'] = data['Average Premium'].apply(lambda x: float(round(x, 2)))
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['Premium Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_selectquarter_district_wise_premium_count(select_state, select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, district, sum(transaction_count) as transaction_count 
                            from map_transaction
                            where state=%s and year=%s and quarter=%s
                            group by district, quarter, year, state
                            order by year, quarter asc, transaction_count desc;""", (select_state, select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'District', 'Premium Count'], index=i)
        data = data.rename_axis('S.No')
        return data

    def selectstate_selectyear_selectquarter_district_wise_premium_amount(select_state, select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, district, sum(transaction_amount) as transaction_amount, sum(transaction_amount)/sum(transaction_count) as avg_transaction
                            from map_transaction
                            where state=%s and year=%s and quarter=%s
                            group by district, quarter, year, state
                            order by year, quarter asc, transaction_amount desc, avg_transaction desc;""", (select_state, select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'District', 'Premium Amount', 'Average Premium'], index=i)
               
        data['Premium Amount'] = data['Premium Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Premium'] = data['Average Premium'].apply(lambda x: float(round(x, 2)))
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['Premium Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

class top_insurance:
    #Premium Count
       
    def selectstate_pincodewise_top10_insurance(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, pincode, sum(transaction_count) as transaction_count
                            from top_insurance
                            where state=%s
                            group by state, pincode
                            order by transaction_count desc
                            limit 10;""",(select_state,))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Pincode', 'Premium Count'])
        data.reset_index(drop=True, inplace=True)
        data.index += 1
        data = data.rename_axis('S.No')
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['District_State'] = data['District'] + '@(' + data['State'] + ')'
        return data
    
    def selectstate_selectyear_pincodewise_top10_insurance(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, pincode, sum(transaction_count) as transaction_count
                            from top_insurance
                            where state=%s and year=%s
                            group by state, year, pincode
                            order by transaction_count desc
                            limit 10;""",(select_state,select_year))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Pincode', 'Premium Count'])
        data.reset_index(drop=True, inplace=True)
        data.index += 1
        data = data.rename_axis('S.No')
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['District_State'] = data['District'] + '@(' + data['State'] + ')'
        return data
    
    def selectstate_selectquarter_pincodewise_top10_insurance(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, pincode, sum(transaction_count) as transaction_count
                            from top_insurance
                            where state=%s and quarter=%s
                            group by state, year, pincode
                            order by transaction_count desc
                            limit 10;""",(select_state,select_quarter))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Quarter', 'Pincode', 'Premium Count'])
        data.reset_index(drop=True, inplace=True)
        data.index += 1
        data = data.rename_axis('S.No')
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['District_State'] = data['District'] + '@(' + data['State'] + ')'
        return data
    
    def selectyear_statewise_top10_insurance(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, sum(transaction_count) as transaction_count 
                            from top_insurance
                            where year=%s
                            group by state, year
                            order by transaction_count desc
                            limit 10;""", (select_year,))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Premium Count'])
        data.reset_index(drop=True, inplace=True)
        data.index += 1
        data = data.rename_axis('S.No')
        return data
    
    def selectyear_pincodewise_top10_insurance(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, pincode, sum(transaction_count) as transaction_count
                            from top_insurance
                            where year=%s
                            group by pincode,year, state
                            order by transaction_count desc
                            limit 10;""", (select_year,))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Pincode', 'Premium Count'])
        data['State']=data['State'].str.title()
        data.reset_index(drop=True, inplace=True)
        data.index+=1
        data = data.rename_axis('S.No')
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['District and State'] = data['District'] + ' district @ ' + data['State'] 
        return data

    def selectquarter_pincodewise_top10_insurance(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, pincode, sum(transaction_count) as transaction_count
                            from top_insurance
                            where quarter=%s
                            group by pincode,quarter, state
                            order by transaction_count desc
                            limit 10;""", (select_quarter,))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Quarter', 'Pincode', 'Premium Count'])
        data['State']=data['State'].str.title()
        data.reset_index(drop=True, inplace=True)
        data.index+=1
        data = data.rename_axis('S.No')
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['District and State'] = data['District'] + ' district @ ' + data['State'] 
        return data
    
    def selectquarter_pincodewise_top10_premium_amount(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, pincode, sum(transaction_amount) as transaction_amount
                            from top_insurance
                            where quarter=%s
                            group by pincode,quarter, state
                            order by transaction_amount desc
                            limit 10;""", (select_quarter,))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Quarter', 'Pincode', 'Premium Amount'])
        data['State']=data['State'].str.title()
        data.reset_index(drop=True, inplace=True)
        data.index+=1
        data = data.rename_axis('S.No')
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['District and State'] = data['District'] + ' district @ ' + data['State'] 
        return data
   
    def selectyear_districtwise_top10_insurance(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, pincode, sum(transaction_count) as transaction_count
                            from top_insurance
                            where year=%s
                            group by pincode,year
                            order by transaction_count desc;
                            """, (select_year,))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data1 = pd.DataFrame(s, columns=['Year', 'Pincode', 'Premium Count'])
        data1['District'] = data1['Pincode'].apply(lambda x: state.find_district(x))
        data2=data1.groupby('District')['Premium Count'].sum()
        data = data2.sort_values(ascending=False).head(10)            
        return data
     
    def selectyear_selectquarter_statewise_top10_insurance(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(transaction_count) as transaction_count, sum(transaction_amount) as transaction_amount 
                            from top_insurance
                            where year=%s and quarter=%s
                            group by quarter, year, state
                            order by transaction_amount desc
                            limit 10;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Transaction Count', 'Transaction Amount'], index=i)
               
        data['Transaction Amount'] = data['Transaction Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Count'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data['Amount'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data['Avg. Transaction Value'] = data['Transaction Amount'] // data['Transaction Count']
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selectquarter_pincodewise_top10_insurance(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, pincode, sum(transaction_count) as transaction_count, sum(transaction_amount) as transaction_amount
                            from top_insurance
                            where year=%s and quarter=%s
                            group by pincode, quarter, year, state
                            order by transaction_count desc
                            limit 10;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Pincode', 'Premium Count', 'Premium Amount'], index=i)
        
        data['Premium Amount'] = data['Premium Amount'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
  
        data['Avg. Premium Value'] = data['Premium Amount'] // data['Premium Count']
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['Pincode_District_State'] = data['Pincode'] + '@(' + data['District'] + ' -@' + data['State'] + ')'
        return data

    def selectstate_selectyear_selectquarter_pincodewise_top10_insurance(select_state, select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, pincode, sum(transaction_count) as transaction_count
                            from top_insurance
                            where state=%s and year=%s and quarter=%s
                            group by pincode, quarter, year, state
                            order by transaction_count desc
                            limit 10;""", (select_state, select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Pincode', 'Premium Count'], index=i)
        data = data.rename_axis('S.No')      
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['Pincode_District'] = data['Pincode'] + '@(' + data['District'] + ')'
        return data
    
    #Premium Amount
    def selectstate_pincodewise_top10_premium_amount(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, pincode, sum(transaction_amount) as transaction_amount
                            from top_insurance
                            where state=%s
                            group by state, pincode
                            order by transaction_amount desc
                            limit 10;""",(select_state,))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Pincode', 'Premium Amount'])
        data.reset_index(drop=True, inplace=True)
        data.index += 1
        data = data.rename_axis('S.No')
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['District_State'] = data['District'] + '@(' + data['State'] + ')'
        return data
    
    def selectstate_selectyear_pincodewise_top10_premium_amount(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, pincode, sum(transaction_amount) as transaction_amount
                            from top_insurance
                            where state=%s and year=%s
                            group by state, year, pincode
                            order by transaction_amount desc
                            limit 10;""",(select_state,select_year))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Pincode', 'Premium Amount'])
        data.reset_index(drop=True, inplace=True)
        data.index += 1
        data = data.rename_axis('S.No')
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['District_State'] = data['District'] + '@(' + data['State'] + ')'
        return data

    def selectyear_statewise_top10_insurance(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, sum(transaction_count) as transaction_count, sum(transaction_amount) as transaction_amount 
                            from top_insurance
                            where year=%s
                            group by state, year
                            order by transaction_amount desc
                            limit 10;""", (select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Premium Count', 'Premium Amount'], index=i)
        data['Premium Amount'] = data['Premium Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Count'] = data['Premium Count'].apply(lambda x: state.convert(str(x)))
        data['Amount'] = data['Premium Amount'].apply(lambda x: state.convert(str(x)))
        data['Avg. Premium Value'] = data['Premium Amount'] // data['Premium Count']
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data
    
    def selectyear_pincodewise_top10_premium_amount(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select  year, pincode, sum(transaction_count) as transaction_count, sum(transaction_amount) as transaction_amount
                            from top_insurance
                            where year=%s
                            group by pincode
                            order by transaction_amount desc
                            limit 10;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['Year', 'Pincode', 'Premium Count', 'Premium Amount'], index=i)
        data['Premium Amount'] = data['Premium Amount'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Count'] = data['Premium Count'].apply(lambda x: state.convert(str(x)))
        data['Amount'] = data['Premium Amount'].apply(lambda x: state.convert(str(x)))
        data['Avg. Premium Value'] = data['Premium Amount'] // data['Premium Count']
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        return data

    def selectstate_selectquarter_pincodewise_top10_premium_amount(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, pincode, sum(transaction_amount) as transaction_amount
                            from top_insurance
                            where state=%s and quarter=%s
                            group by state, year, pincode
                            order by transaction_amount desc
                            limit 10;""",(select_state,select_quarter))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Quarter', 'Pincode', 'Premium Amount'])
        data.reset_index(drop=True, inplace=True)
        data.index += 1
        data = data.rename_axis('S.No')
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['District_State'] = data['District'] + '@(' + data['State'] + ')'
        return data

    def selectyear_selectquarter_statewise_top10_premium_amount(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(transaction_count) as transaction_count, sum(transaction_amount) as transaction_amount 
                            from top_insurance
                            where year=%s and quarter=%s
                            group by quarter, year, state
                            order by transaction_amount desc
                            limit 10;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Premium Count', 'Premium Amount'], index=i)
               
        data['Premium Amount'] = data['Premium Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Count'] = data['Premium Count'].apply(lambda x: state.convert(str(x)))
        data['Amount'] = data['Premium Amount'].apply(lambda x: state.convert(str(x)))
        data['Avg. Premium Value'] = data['Premium Amount'] // data['Premium Count']
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selectquarter_pincodewise_top10_premium_amount(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, pincode, sum(transaction_count) as transaction_count, sum(transaction_amount) as transaction_amount
                            from top_insurance
                            where year=%s and quarter=%s
                            group by pincode, quarter, year, state
                            order by transaction_amount desc
                            limit 10;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Pincode', 'Premium Count', 'Premium Amount'], index=i)
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['Pincode_District_State'] = data['Pincode'] + '@(' + data['District'] + ' -@' + data['State'] + ')'
        return data

    def selectstate_selectyear_selectquarter_pincodewise_top10_premium_amount(select_state, select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, pincode, sum(transaction_count) as transaction_count, sum(transaction_amount) as transaction_amount
                            from top_transaction
                            where state=%s and year=%s and quarter=%s
                            group by pincode, quarter, year, state
                            order by transaction_amount desc
                            limit 10;""", (select_state, select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Pincode', 'Premium Count', 'Premium Amount'], index=i)
        data['Premium Amount'] = data['Premium Amount'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Avg. Premium Value'] = data['Premium Amount'] // data['Premium Count']
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['Pincode_District'] = data['Pincode'] + '@(' + data['District'] + ')'
        return data

#2. TRANSACTION
class aggregated_transaction:

#COMMON
    def state_wise_transaction_count():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            group by state
                            order by state asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Transaction Count'], index=i)
               
        data = data.sort_values(by='Transaction Count', ascending=True)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def state_wise_transaction_amount():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, sum(transaction_amount) as transaction_amount, 
                            sum(transaction_amount)/sum(transaction_count) as avg_transaction  
                            from aggregated_transaction
                            group by state
                            order by transaction_amount desc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Transaction Amount', 'Average Transaction'], index=i)
               
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Transaction'] = data['Average Transaction'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data
    
    def year_wise_transaction_count():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            group by year
                            order by year asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['Year', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def year_wise_transaction_amount():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, sum(transaction_amount) as transaction_amount 
                            from aggregated_transaction
                            group by year
                            order by year asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'Transaction Amount'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def year_quarter_wise_transaction_count():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            group by quarter, year
                            order by year, quarter asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'Quarter', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def year_quarter_wise_transaction_amount():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(transaction_amount) as transaction_amount 
                            from aggregated_transaction
                            group by quarter, year
                            order by year, quarter asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'Quarter', 'Transaction Amount'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def year_type_wise_transaction_count():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, transaction_type, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            group by transaction_type, year
                            order by year asc, case when transaction_type = 'Others' then 1 else 0 end, transaction_type asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def year_type_wise_transaction_amount():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, transaction_type, sum(transaction_amount) as transaction_amount 
                            from aggregated_transaction
                            group by transaction_type, year
                            order by year asc, case when transaction_type = 'Others' then 1 else 0 end, transaction_type asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'Transaction Type', 'Transaction Amount'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data
 
    def quarter_wise_transaction_count():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select quarter, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            group by quarter
                            order by quarter asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Quarter', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def quarter_wise_transaction_amount():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select quarter, sum(transaction_amount) as transaction_amount 
                            from aggregated_transaction
                            group by quarter
                            order by quarter asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Quarter', 'Transaction Amount'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data
   
    def quarter_type_wise_transaction_count():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select quarter, transaction_type, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            group by transaction_type, quarter
                            order by quarter asc, case when transaction_type = 'Others' then 1 else 0 end, transaction_type asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Quarter', 'Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def quarter_type_wise_transaction_amount():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select quarter, transaction_type, sum(transaction_amount) as transaction_amount 
                            from aggregated_transaction
                            group by transaction_type, quarter
                            order by quarter asc, case when transaction_type = 'Others' then 1 else 0 end, transaction_type asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Quarter', 'Transaction Type', 'Transaction Amount'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data
    
    def type_wise_transaction_count():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select transaction_type, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            group by transaction_type
                            order by case when transaction_type = 'Others' then 1 else 0 end, transaction_count desc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def type_wise_transaction_amount():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select transaction_type, sum(transaction_amount) as transaction_amount 
                            from aggregated_transaction
                            group by transaction_type
                            order by case when transaction_type = 'Others' then 1 else 0 end, transaction_amount desc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Transaction Type', 'Transaction Amount'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

#STATEWISE
    def selectstate_year_wise_transaction_count(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            where state=%s
                            group by year, state
                            order by year asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_year_wise_transaction_amount(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, sum(transaction_amount) as transaction_amount,  
                                   sum(transaction_amount)/sum(transaction_count) as average_transaction
                            from aggregated_transaction
                            where state=%s
                            group by year, state
                            order by year asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Transaction Amount', 'Average Transaction'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Transaction'] = data['Average Transaction'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_quarter_wise_transaction_count(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, sum(transaction_count) as transaction_count 
                        from aggregated_transaction
                        where state=%s
                        group by quarter, state
                        order by quarter asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Quarter', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_quarter_wise_transaction_amount(select_state):
        connection = mysql.connector.connect(
                                            host='localhost',
                                            user='root',
                                            password='Kimch!811',
                                            database='PhonePe_Data'
                                           )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, sum(transaction_amount) as transaction_amount, 
                                sum(transaction_amount)/sum(transaction_count) as avg_transaction
                            from aggregated_transaction
                            where state=%s
                            group by quarter, state
                            order by quarter asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Quarter', 'Transaction Amount', 'Average Transaction'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Transaction'] = data['Average Transaction'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_type_wise_transaction_count(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, transaction_type, sum(transaction_count) as transaction_count 
                        from aggregated_transaction
                        where state=%s
                        group by transaction_type, state
                        order by case when transaction_type = 'Others' then 1 else 0 end, transaction_count desc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_type_wise_transaction_amount(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, transaction_type, sum(transaction_amount) as transaction_amount,
                            sum(transaction_amount)/sum(transaction_count) as avg_transaction
                        from aggregated_transaction
                        where state=%s
                        group by transaction_type, state
                        order by case when transaction_type = 'Others' then 1 else 0 end, transaction_amount desc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Transaction Type', 'Transaction Amount', 'Average Transaction'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Transaction'] = data['Average Transaction'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_year_quarter_wise_transaction_count(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(transaction_count) as transaction_count 
                        from aggregated_transaction
                        where state=%s
                        group by quarter, year, state
                        order by year, quarter asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_year_quarter_wise_transaction_amount(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(transaction_amount) as transaction_amount,
                            sum(transaction_amount)/sum(transaction_count) as avg_transaction
                            from aggregated_transaction
                            where state=%s
                            group by quarter, year, state
                            order by year, quarter asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'Transaction Amount', 'Average Transaction'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Transaction'] = data['Average Transaction'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_year_type_wise_transaction_count(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, transaction_type, sum(transaction_count) as transaction_count 
                        from aggregated_transaction
                        where state=%s
                        group by transaction_type, year, state
                        order by year asc, case when transaction_type = 'Others' then 1 else 0 end, transaction_type asc;""", 
                        (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_year_type_wise_transaction_amount(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, transaction_type, sum(transaction_amount) as transaction_amount, 
                                    sum(transaction_amount)/sum(transaction_count) as avg_transaction
                            from aggregated_transaction
                            where state=%s
                            group by transaction_type, year, state
                            order by year asc, case when transaction_type = 'Others' then 1 else 0 end, transaction_type asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Transaction Type', 'Transaction Amount', 'Average Transaction'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Transaction'] = data['Average Transaction'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_quarter_type_wise_transaction_count(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, transaction_type, sum(transaction_count) as transaction_count 
                        from aggregated_transaction
                        where state=%s
                        group by transaction_type, quarter, state
                        order by quarter asc, case when transaction_type = 'Others' then 1 else 0 end, transaction_type asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Quarter', 'Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_quarter_type_wise_transaction_amount(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, transaction_type, sum(transaction_amount) as transaction_amount,
                                sum(transaction_amount)/sum(transaction_count) as avg_transaction
                            from aggregated_transaction
                            where state=%s
                            group by transaction_type, quarter, state
                            order by quarter asc, case when transaction_type = 'Others' then 1 else 0 end, transaction_type asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Quarter', 'Transaction Type', 'Transaction Amount', 'Average Transaction'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Transaction'] = data['Average Transaction'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

        def selectstate_selectyear_quarter_wise_transaction_count(select_state, select_year):
            connection = mysql.connector.connect(
                                            host='localhost',
                                            user='root',
                                            password='Kimch!811',
                                            database='PhonePe_Data'
                                        )
            cursor = connection.cursor()
            cursor.execute(f"""select state, year, quarter, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            where state=%s and year=%s
                            group by quarter, year, state
                            order by quarter asc, transaction_count desc;""", (select_state, select_year))
            s = cursor.fetchall()
            i = [i for i in range(1, len(s)+1)]
            pd.set_option('display.max_columns', None)
            data = pd.DataFrame(
                s, columns=['State', 'Year', 'Quarter', 'Transaction Count'], index=i)
            data = data.rename_axis('S.No')
            data['Transaction'] = data['Transaction Count'].apply(
                lambda x: state.convert(str(x)))
            data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
            return data

    def selectstate_selectyear_quarter_wise_transaction_count(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            where state=%s and year=%s
                            group by quarter, year, state
                            order by quarter asc, transaction_count desc;""", (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data
  
    def selectstate_selectyear_quarter_wise_transaction_amount(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(transaction_amount) as transaction_amount,
                            sum(transaction_amount)/sum(transaction_count) as avg_transaction
                            from aggregated_transaction
                            where state=%s and year=%s
                            group by quarter, year, state
                            order by quarter asc, transaction_amount desc;""", (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'Transaction Amount', 'Average Transaction'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Transaction'] = data['Average Transaction'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_type_wise_transaction_count(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, transaction_type, sum(transaction_count) as transaction_count 
                        from aggregated_transaction
                        where state=%s and year=%s
                        group by transaction_type, year, state
                        order by case when transaction_type = 'Others' then 1 else 0 end, transaction_count desc;""",
                          (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Transaction Type', 'Transaction Count'], index=i)
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_type_wise_transaction_amount(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, transaction_type, sum(transaction_amount) as transaction_amount,
                          sum(transaction_amount)/sum(transaction_count) as avg_transaction
                        from aggregated_transaction
                        where state=%s and year=%s
                        group by transaction_type, year, state
                        order by case when transaction_type = 'Others' then 1 else 0 end, transaction_amount desc;""", (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Transaction Type', 'Transaction Amount','Average Transaction'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Transaction'] = data['Average Transaction'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_quarter_type_wise_transaction_count(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, transaction_type, sum(transaction_count) as transaction_count 
                        from aggregated_transaction
                        where state=%s and year=%s
                        group by transaction_type, quarter, year, state
                        order by quarter asc, case when transaction_type = 'Others' then 1 else 0 end, transaction_count desc;""", (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_quarter_type_wise_transaction_amount(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, transaction_type, sum(transaction_amount) as transaction_amount,
                                sum(transaction_amount)/sum(transaction_count) as avg_transaction
                            from aggregated_transaction
                            where state=%s and year=%s
                            group by transaction_type, quarter, year, state
                            order by quarter asc, case when transaction_type = 'Others' then 1 else 0 end, transaction_amount desc;""",
                              (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'Transaction Type', 'Transaction Amount','Average Transaction'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Transaction'] = data['Average Transaction'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectquarter_year_wise_transaction_count(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(transaction_count) as transaction_count 
                        from aggregated_transaction
                        where state=%s and quarter=%s
                        group by quarter, year, state
                        order by year asc;""", (select_state, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectquarter_year_wise_transaction_amount(select_state, select_quarter):
        connection =mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(transaction_amount) as transaction_amount,
                           sum(transaction_amount)/sum(transaction_count) as avg_transaciton
                        from aggregated_transaction
                        where state=%s and quarter=%s
                        group by quarter, year, state
                        order by year asc;""", (select_state, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Transaction Amount', 'Average Transaction'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Transaction'] = data['Average Transaction'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectquarter_type_wise_transaction_count(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, transaction_type, sum(transaction_count) as transaction_count 
                        from aggregated_transaction
                        where state=%s and quarter=%s
                        group by transaction_type, quarter, state
                        order by case when transaction_type = 'Others' then 1 else 0 end, transaction_count desc;""", 
                        (select_state, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Quarter', 'Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectquarter_type_wise_transaction_amount(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, transaction_type, sum(transaction_amount) as transaction_amount,
                                sum(transaction_amount)/sum(transaction_count) as avg_transaction
                        from aggregated_transaction
                        where state=%s and quarter=%s
                        group by transaction_type, quarter, state
                        order by case when transaction_type = 'Others' then 1 else 0 end, transaction_amount desc;""", 
                        (select_state, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Quarter', 'Transaction Type', 'Transaction Amount', 'Average Transaction'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Transaction'] = data['Average Transaction'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectquarter_year_type_wise_transaction_count(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, transaction_type, sum(transaction_count) as transaction_count 
                        from aggregated_transaction
                        where state=%s and quarter=%s
                        group by transaction_type, quarter, year, state
                        order by year asc, case when transaction_type = 'Others' then 1 else 0 end, transaction_count desc;""", (select_state, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectquarter_year_type_wise_transaction_amount(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, transaction_type, sum(transaction_amount) as transaction_amount,
                        sum(transaction_amount)/sum(transaction_count) as avg_transaction
                        from aggregated_transaction
                        where state=%s and quarter=%s
                        group by transaction_type, quarter, year, state
                        order by year asc, case when transaction_type = 'Others' then 1 else 0 end, transaction_amount desc;""", 
                        (select_state, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'Transaction Type', 'Transaction Amount', 'Average Transaction'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Transaction'] = data['Average Transaction'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selecttype_year_wise_transaction_count(select_state, select_type):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, transaction_type, sum(transaction_count) as transaction_count
                            from aggregated_transaction
                            where state=%s and transaction_type=%s
                            group by transaction_type, year, state
                            order by year asc;""", (select_state, select_type))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data
    
    def selectstate_selecttype_year_wise_transaction_amount(select_state, select_type):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, transaction_type, sum(transaction_amount) as transaction_amount,
                            sum(transaction_amount)/sum(transaction_count) as avg_transaction
                            from aggregated_transaction
                            where state=%s and transaction_type=%s
                            group by transaction_type, year, state
                            order by year asc;""", (select_state, select_type))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Transaction Type', 'Transaction Amount', 'Average Transaction'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Transaction'] = data['Average Transaction'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selecttype_quarter_wise_transaction_count(select_state, select_type):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, transaction_type, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            where state=%s and transaction_type=%s
                            group by transaction_type, quarter, state
                            order by quarter asc;""", (select_state, select_type))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Quarter', 'Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selecttype_quarter_wise_transaction_amount(select_state, select_type):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, transaction_type, sum(transaction_amount) as transaction_amount,
                        sum(transaction_amount)/sum(transaction_count) as avg_transaction
                            from aggregated_transaction
                            where state=%s and transaction_type=%s
                            group by transaction_type, quarter, state
                            order by quarter asc;""", (select_state, select_type))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Quarter', 'Transaction Type', 'Transaction Amount', 'Average Transaction'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Transaction']=data['Average Transaction'].apply(lambda x: int(round(x,0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selecttype_year_quarter_wise_transaction_count(select_state, select_type):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, transaction_type, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            where state=%s and transaction_type=%s
                            group by transaction_type, quarter, year, state
                            order by year, quarter asc;""", (select_state, select_type))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selecttype_year_quarter_wise_transaction_amount(select_state, select_type):
        connection =mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, transaction_type, sum(transaction_amount) as transaction_amount,
                            sum(transaction_amount)/sum(transaction_count) as avg_transaction
                            from aggregated_transaction
                            where state=%s and transaction_type=%s
                            group by transaction_type, quarter, year, state
                            order by year, quarter asc;""", (select_state, select_type))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'Transaction Type', 'Transaction Amount', 'Average Transaction'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Transaction'] = data['Average Transaction'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_selecttype_quarter_wise_transaction_count(select_state, select_year, select_type):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, transaction_type, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            where state=%s and year=%s and transaction_type=%s
                            group by transaction_type, quarter, year, state
                            order by quarter asc;""", (select_state, select_year, select_type))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_selecttype_quarter_wise_transaction_amount(select_state, select_year, select_type):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, transaction_type, sum(transaction_amount) as transaction_amount,
                            sum(transaction_amount)/sum(transaction_count) as avg_transaction
                            from aggregated_transaction
                            where state=%s and year=%s and transaction_type=%s
                            group by transaction_type, quarter, year, state
                            order by quarter asc;""", (select_state, select_year, select_type))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'Transaction Type', 'Transaction Amount', 'Average Transaction'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Transaction'] = data['Average Transaction'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectquarter_selecttype_year_wise_transaction_count(select_state, select_quarter, select_type):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, transaction_type, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            where state=%s and quarter=%s and transaction_type=%s
                            group by transaction_type, quarter, year, state
                            order by year asc;""", (select_state, select_quarter, select_type))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectquarter_selecttype_year_wise_transaction_amount(select_state, select_quarter, select_type):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, transaction_type, sum(transaction_amount) as transaction_amount,
                            sum(transaction_amount)/sum(transaction_count) as avg_transaction
                            from aggregated_transaction
                            where state=%s and quarter=%s and transaction_type=%s
                            group by transaction_type, quarter, year, state
                            order by year asc;""", (select_state, select_quarter, select_type))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'Transaction Type', 'Transaction Amount', 'Average Transaction'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Transaction'] = data['Average Transaction'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_selectquarter_type_wise_transaction_count(select_state, select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, transaction_type, sum(transaction_count) as transaction_count 
                        from aggregated_transaction
                        where state=%s and year=%s and quarter=%s
                        group by transaction_type, quarter, year, state
                        order by case when transaction_type = 'Others' then 1 else 0 end, transaction_count desc;""", (select_state, select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_selectquarter_type_wise_transaction_amount(select_state, select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
            
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, transaction_type, sum(transaction_amount) as transaction_amount,
                       sum(transaction_amount)/sum(transaction_count) as avg_transaction
                        from aggregated_transaction
                        where state=%s and year=%s and quarter=%s
                        group by transaction_type, quarter, year, state
                        order by case when transaction_type = 'Others' then 1 else 0 end, transaction_amount desc;""", (select_state, select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'Transaction Type', 'Transaction Amount', 'Average Transaction'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Transaction'] = data['Average Transaction'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_selectquarter_selecttype_wise_transaction_count(select_state, select_year, select_quarter, select_type):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, transaction_type, sum(transaction_count) as transaction_count 
                        from aggregated_transaction
                        where state=%s and year=%s and quarter=%s and transaction_type=%s
                        group by transaction_type, quarter, year, state;""", (select_state, select_year, select_quarter, select_type))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_selectquarter_selecttype_wise_transaction_amount(select_state, select_year, select_quarter, select_type):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, transaction_type, sum(transaction_amount) as transaction_amount,
                            sum(transaction_amount)/sum(transaction_count) as avg_transaction
                        from aggregated_transaction
                        where state=%s and year=%s and quarter=%s and transaction_type=%s
                        group by transaction_type, quarter, year, state;""", 
                        (select_state, select_year, select_quarter, select_type))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Transaction Type', 'Transaction Amount', 'Average Transaction'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data['Average Transaction'] = data['Average Transaction'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

#YEARWISE
    def selectyear_state_wise_transaction_count(select_year):
            connection =mysql.connector.connect(
                                            host='localhost',
                                            user='root',
                                            password='Kimch!811',
                                            database='PhonePe_Data'
                                        )
            cursor = connection.cursor()
            cursor.execute(f"""select state, year, sum(transaction_count) as transaction_count 
                                from aggregated_transaction
                                where year=%s
                                group by year, state
                                order by transaction_count desc;""", (select_year,))
            s = cursor.fetchall()
            i = [i for i in range(1, len(s)+1)]
            pd.set_option('display.max_columns', None)
            data = pd.DataFrame(
                s, columns=['State', 'Year', 'Transaction Count'], index=i)
                       
            data = data.sort_values(by='Transaction Count', ascending=False)
            data = data.rename_axis('S.No')
            data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
            data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
            return data

    def selectyear_state_wise_transaction_amount(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, sum(transaction_amount) as transaction_amount 
                            from aggregated_transaction
                            where year=%s
                            group by state
                            order by transaction_amount desc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Transaction Amount'], index=i)
        data['State'] = data['State'].str.title()
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_quarter_wise_transaction_count(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            where year=%s
                            group by quarter, year
                            order by quarter asc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'Quarter', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_quarter_wise_transaction_amount(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(transaction_amount) as transaction_amount 
                            from aggregated_transaction
                            where year=%s
                            group by quarter, state
                            order by transaction_amount desc, quarter asc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Transaction Amount'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_type_wise_transaction_count(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, transaction_type, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            where year=%s
                            group by transaction_type, year
                            order by case when transaction_type = 'Others' then 1 else 0 end, transaction_count desc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_type_wise_transaction_amount(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, transaction_type, sum(transaction_amount) as transaction_amount 
                            from aggregated_transaction
                            where year=%s
                            group by transaction_type, year
                            order by case when transaction_type = 'Others' then 1 else 0 end, transaction_amount desc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame( s, columns=['Year', 'Transaction Type', 'Transaction Amount'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_quarter_type_wise_transaction_count(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, transaction_type, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            where year=%s
                            group by transaction_type, quarter
                            order by quarter asc, case when transaction_type = 'Others' then 1 else 0 end, transaction_type asc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['Year', 'Quarter', 'Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_quarter_type_wise_transaction_amount(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, transaction_type, sum(transaction_amount) as transaction_amount 
                            from aggregated_transaction
                            where year=%s
                            group by transaction_type, quarter
                            order by quarter asc, case when transaction_type = 'Others' then 1 else 0 end, transaction_type asc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['Year', 'Quarter', 'Transaction Type', 'Transaction Amount'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data
    
    def selectyear_state_type_wise_transaction_count(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, state, transaction_type, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            where year=%s
                            group by transaction_type, state
                            order by state asc, case when transaction_type = 'Others' then 1 else 0 end, transaction_type asc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data
    
    def selectyear_state_type_wise_transaction_amount(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, state, transaction_type, sum(transaction_amount) as transaction_amount 
                            from aggregated_transaction
                            where year=%s
                            group by transaction_type,state
                            order by state asc, case when transaction_type = 'Others' then 1 else 0 end, transaction_type asc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Transaction Type', 'Transaction Amount'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data
    
    def selectyear_selectquarter_state_wise_transaction_count(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            where year=%s and quarter=%s
                            group by state
                            order by transaction_count desc;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Transaction Count'], index=i)
               
        data = data.sort_values(by='Transaction Count', ascending=False)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selectquarter_state_wise_transaction_amount(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(transaction_amount) as transaction_amount 
                            from aggregated_transaction
                            where year=%s and quarter=%s
                            group by state
                            order by transaction_amount desc;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Transaction Amount'], index=i)
        data['State'] = data['State'].str.title()
        data = data.sort_values(by='Transaction Amount', ascending=False)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selectquarter_type_wise_transaction_count(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, transaction_type, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            where year=%s and quarter=%s
                            group by transaction_type
                            order by case when transaction_type = 'Others' then 1 else 0 end, transaction_count desc;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'Quarter', 'Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selectquarter_type_wise_transaction_amount(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, transaction_type, sum(transaction_amount) as transaction_amount 
                            from aggregated_transaction
                            where year=%s and quarter=%s
                            group by transaction_type
                            order by case when transaction_type = 'Others' then 1 else 0 end, transaction_amount desc;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['Year', 'Quarter', 'Transaction Type', 'Transaction Amount'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selecttype_state_wise_transaction_count(select_year, select_type):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, transaction_type, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            where year=%s and transaction_type=%s
                            group by state
                            order by transaction_count desc;""", (select_year, select_type))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Transaction Type', 'Transaction Count'], index=i)
               
        data = data.sort_values(by='Transaction Count', ascending=False)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selecttype_state_wise_transaction_amount(select_year, select_type):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, transaction_type, sum(transaction_amount) as transaction_amount 
                            from aggregated_transaction
                            where year=%s and transaction_type=%s
                            group by state
                            order by transaction_amount desc;""", (select_year, select_type))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=[
                            'State', 'Year', 'Transaction Type', 'Transaction Amount'], index=i)
               
        data = data.sort_values(by='Transaction Amount', ascending=False)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selecttype_quarter_wise_transaction_count(select_year, select_type):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, transaction_type, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            where year=%s and transaction_type=%s
                            group by quarter
                            order by quarter asc;""", (select_year, select_type))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['Year', 'Quarter', 'Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selecttype_quarter_wise_transaction_amount(select_year, select_type):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, transaction_type, sum(transaction_amount) as transaction_amount 
                            from aggregated_transaction
                            where year=%s and transaction_type=%s
                            group by quarter
                            order by quarter asc;""", (select_year, select_type))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['Year', 'Quarter', 'Transaction Type', 'Transaction Amount'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selectquarter_selecttype_state_wise_transaction_count(select_year, select_quarter, select_type):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, transaction_type, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            where year=%s and quarter=%s and transaction_type=%s
                            group by transaction_type, quarter, year, state
                            order by state asc;""", (select_year, select_quarter, select_type))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Transaction Type', 'Transaction Count'], index=i)
               
        data = data.sort_values(by='Transaction Count', ascending=False)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selectquarter_selecttype_state_wise_transaction_amount(select_year, select_quarter, select_type):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, transaction_type, sum(transaction_amount) as transaction_amount 
                            from aggregated_transaction
                            where year=%s and quarter=%s and transaction_type=%s
                            group by state
                            order by transaction_amount desc;""", (select_year, select_quarter, select_type))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Transaction Type', 'Transaction Amount'], index=i)
               
        data = data.sort_values(by='Transaction Amount', ascending=False)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

#QUARTERWISE
    def selectquarter_state_wise_transaction_count(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                    )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            where quarter=%s
                            group by state
                            order by transaction_count desc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Quarter', 'Transaction Count'], index=i)
        data['State']=data['State'].str.title()    
        data = data.sort_values(by='Transaction Count', ascending=False)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data
    
    def selectquarter_state_wise_transaction_amount(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, sum(transaction_amount) as transaction_amount 
                            from aggregated_transaction
                            where quarter=%s
                            group by quarter, state
                            order by transaction_amount desc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Quarter', 'Transaction Amount'], index=i)
               
        data = data.sort_values(by='Transaction Amount', ascending=False)
        data['Transaction Amount'] = data['Transaction Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_year_wise_transaction_count(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            where quarter=%s
                            group by quarter, year
                            order by year asc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'Quarter', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_year_wise_transaction_amount(select_quarter):
        connection =mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(transaction_amount) as transaction_amount 
                            from aggregated_transaction
                            where quarter=%s
                            group by quarter, year
                            order by year asc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'quarter', 'Transaction Amount'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_type_wise_transaction_count(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select quarter, transaction_type, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            where quarter=%s
                            group by transaction_type, quarter
                            order by case when transaction_type = 'Others' then 1 else 0 end, transaction_count desc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['quarter', 'Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_type_wise_transaction_amount(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select quarter, transaction_type, sum(transaction_amount) as transaction_amount 
                            from aggregated_transaction
                            where quarter=%s
                            group by transaction_type, quarter
                            order by case when transaction_type = 'Others' then 1 else 0 end, transaction_amount desc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['quarter', 'Transaction Type', 'Transaction Amount'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_year_type_wise_transaction_count(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, transaction_type, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            where quarter=%s
                            group by transaction_type, quarter, year
                            order by year asc, case when transaction_type = 'Others' then 1 else 0 end, transaction_type asc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'quarter', 'Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_year_type_wise_transaction_amount(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, transaction_type, sum(transaction_amount) as transaction_amount 
                            from aggregated_transaction
                            where quarter=%s
                            group by transaction_type, quarter, year
                            order by year asc, case when transaction_type = 'Others' then 1 else 0 end, transaction_type asc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'quarter', 'Transaction Type', 'Transaction Amount'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

        def selectstate_selecttype_year_wise_transaction_count(select_state, select_type):
            connection = mysql.connector.connect(
                                            host='localhost',
                                            user='root',
                                            password='Kimch!811',
                                            database='PhonePe_Data'
                                        )
            cursor = connection.cursor()
            cursor.execute(f"""select state, year, transaction_type, sum(transaction_count) as transaction_count 
                                from aggregated_transaction
                                where state=%s and transaction_type=%s
                                group by transaction_type, year, state
                                order by year asc;""", (select_state, select_type))
            s = cursor.fetchall()
            i = [i for i in range(1, len(s)+1)]
            pd.set_option('display.max_columns', None)
            data = pd.DataFrame(
                s, columns=['State', 'Year', 'Transaction Type', 'Transaction Count'], index=i)
            data = data.rename_axis('S.No')
            data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
            data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
            return data

   
#    def selectquarter_selecttype_state_wise_transaction_count(select_quarter, select_type):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, transaction_type, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            where quarter=%s and transaction_type=%s
                            group by transaction_type, quarter, state
                            order by state asc;""", (select_quarter, select_type))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=[
                            'State', 'quarter', 'Transaction Type', 'Transaction Count'], index=i)
               
        data = data.sort_values(by='Transaction Count', ascending=False)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_selecttype_state_wise_transaction_amount(select_quarter, select_type):
        connection =mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, transaction_type, sum(transaction_amount) as transaction_amount 
                            from aggregated_transaction
                            where quarter=%s and transaction_type=%s
                            group by transaction_type, quarter, state
                            order by state asc;""", (select_quarter, select_type))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=[
                            'State', 'quarter', 'Transaction Type', 'Transaction Amount'], index=i)
               
        data = data.sort_values(by='Transaction Amount', ascending=False)
        data['Transaction Amount'] = data['Transaction Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_selecttype_year_wise_transaction_count(select_quarter, select_type):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, transaction_type, sum(transaction_count) as transaction_count 
                            from aggregated_transaction
                            where quarter=%s and transaction_type=%s
                            group by transaction_type, quarter, year
                            order by year asc;""", (select_quarter, select_type))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'quarter', 'Transaction Type', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_selecttype_year_wise_transaction_amount(select_quarter, select_type):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, transaction_type, sum(transaction_amount) as transaction_amount 
                            from aggregated_transaction
                            where quarter=%s and transaction_type=%s
                            group by transaction_type, year, quarter
                            order by year asc;""", (select_quarter, select_type))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'quarter', 'Transaction Type', 'Transaction Amount'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

class map_transaction:
     # map - transaction
    def district_wise_top10_transaction_count():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, district, sum(transaction_count) as transaction_count
                            from map_transaction
                            
                            group by state, district
                            order by transaction_count desc
                            limit 10;""")
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'District', 'Transaction Count'])
        data.reset_index(drop=True, inplace=True)
        data.index += 1
        data = data.rename_axis('S.No')
        return data
    
    def district_wise_top10_transaction_amount():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, district, sum(transaction_amount) as transaction_amount
                            from map_transaction
                            
                            group by state, district
                            order by transaction_amount desc;""")
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'District', 'Transaction Amount'])
        data.reset_index(drop=True, inplace=True)
        data.index += 1
        data = data.rename_axis('S.No')
        return data
     
    def selectstate_district_wise_transaction_count(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, district, sum(transaction_count) as transaction_count 
                            from map_transaction
                            where state=%s
                            group by district, state
                            order by transaction_count desc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'District', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_district_wise_transaction_amount(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, district, sum(transaction_amount) as transaction_amount 
                            from map_transaction
                            where state=%s
                            group by district, state
                            order by transaction_amount desc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'District', 'Transaction Amount'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_district_wise_transaction_count(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, district, sum(transaction_count) as transaction_count 
                            from map_transaction
                            where year=%s
                            group by district, state
                            order by transaction_count desc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State','Year', 'District', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['State']=data['State'].str.title()
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_district_wise_transaction_amount(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, district, sum(transaction_count) as transaction_count 
                            from map_transaction
                            where year=%s
                            group by district, state
                            order by transaction_count desc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'District', 'Transaction Count'], index=i)
        data['Transaction Count']=data['Transaction Count'].apply(lambda x: round(x, 0))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selectquarter_district_wise_transaction_count(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, district, sum(transaction_count) as transaction_count
                            from map_transaction
                            where year=%s and quarter=%s
                            group by district, state
                            order by transaction_count desc;""", (select_year,select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'District', 'Transaction Count'], index=i)
        data['Transaction Count']=data['Transaction Count'].apply(lambda x: round(x, 0))
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data['State']=data['State'].str.title()
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data 

    def selectyear_selectquarter_district_wise_transaction_amount(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, district, sum(transaction_count) as transaction_count, sum(transaction_amount) as transaction_amount 
                            from map_transaction
                            where year=%s and quarter=%s
                            group by district, state
                            order by transaction_amount desc;""", (select_year,select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'District', 'Transaction Count', 'Transaction Amount'], index=i)
        data['Transaction Amount']=data['Transaction Amount'].apply(lambda x: round(x, 0))
        data = data.rename_axis('S.No')
        data['State']=data['State'].str.title()
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(int(x))))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_district_wise_transaction_count(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, district, sum(transaction_count) as transaction_count 
                            from map_transaction
                            where state=%s and year=%s
                            group by district, year, state
                            order by year asc, transaction_count desc;""", (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'District', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_district_wise_transaction_amount(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, district, sum(transaction_amount) as transaction_amount 
                            from map_transaction
                            where state=%s and year=%s
                            group by district, year, state
                            order by transaction_amount desc
                            limit 10;""", (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'District', 'Transaction Amount'], index=i)
        data['State']=data['State'].str.title()
        data['Transaction Amount'] = data['Transaction Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectquarter_district_wise_transaction_count(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, district, sum(transaction_count) as transaction_count 
                            from map_transaction
                            where state=%s and quarter=%s
                            group by district
                            order by transaction_count desc;""", (select_state, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Quarter', 'District', 'Transaction Count'], index=i)
        data['State']=data['State'].str.title()
        data = data.rename_axis('S.No')
        data['Transaction'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectquarter_district_wise_transaction_amount(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, district, sum(transaction_amount) as transaction_amount 
                            from map_transaction
                            where state=%s and quarter=%s
                            group by district, quarter, state
                            order by transaction_amount desc
                       limit 10;""", (select_state, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Quarter', 'District', 'Transaction Amount'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data['State']=data['State'].str.title()
        data = data.rename_axis('S.No')
        data['Transaction Amt'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_selectquarter_district_wise_transaction_count(select_state, select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, district, sum(transaction_count) as transaction_count 
                            from map_transaction
                            where state=%s and year=%s and quarter=%s
                            group by district, quarter, year, state
                            order by transaction_count desc;""", (select_state, select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'District', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['State']=data['State'].str.title()
        data['Formatted Value'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_selectquarter_district_wise_transaction_amount(select_state, select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, district, sum(transaction_amount) as transaction_amount 
                            from map_transaction
                            where state=%s and year=%s and quarter=%s
                            group by district, quarter, year, state
                            order by year, quarter asc, transaction_amount desc;""", (select_state, select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'District', 'Transaction Amount'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

class top_transaction:

    def pincodewise_top10_transaction_count():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, pincode, sum(transaction_count) as transaction_count
                            from top_transaction
                            
                            group by state, pincode
                            order by transaction_count desc
                            limit 10;""")
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Pincode', 'Transaction Count'])
        data.reset_index(drop=True, inplace=True)
        data.index += 1
        data = data.rename_axis('S.No')
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['District and State'] = data['District'] + '@ ' + data['State'] 
        return data
    
    def pincodewise_top10_transaction_amount():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, pincode, sum(transaction_amount) as transaction_amount
                            from top_transaction                            
                            group by state, pincode
                            order by transaction_amount desc
                            limit 10;""")
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Pincode', 'Transaction Amount'])
        data.reset_index(drop=True, inplace=True)
        data.index += 1
        data = data.rename_axis('S.No')
        data['State']=data['State'].str.title()
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['District and State'] = data['District'] + ' District @ ' + data['State'] 
        return data

    def selectstate_selectquarter_pincodewise_top10_transaction_count(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state,quarter, pincode, sum(transaction_count) as transaction_count
                            from top_transaction
                            where state=%s and quarter=%s
                            group by state, pincode, quarter
                            order by transaction_count desc
                            limit 10;""",(select_state,select_quarter))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Quarter', 'Pincode', 'Transaction Count'])
        data.reset_index(drop=True, inplace=True)
        data.index += 1
        data = data.rename_axis('S.No')
        data['State']=data['State'].str.title()
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['District and State'] = data['District'] + ' District @ ' + data['State'] 
        return data
    
    def selectstate_selectquarter_pincodewise_top10_transaction_amount(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state,quarter, pincode, sum(transaction_amount) as transaction_amount
                            from top_transaction
                            where state=%s and quarter=%s
                            group by state, pincode, quarter
                            order by transaction_amount desc
                            limit 10;""",(select_state,select_quarter))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Quarter', 'Pincode', 'Transaction Amount'])
        data.reset_index(drop=True, inplace=True)
        data.index += 1
        data = data.rename_axis('S.No')
        data['State']=data['State'].str.title()
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['District and State'] = data['District'] + ' District @ ' + data['State'] 
        return data

    def selectstate_pincodewise_top10_transaction_count(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, pincode, sum(transaction_count) as transaction_count
                            from top_transaction
                            where state=%s
                            group by state, pincode
                            order by transaction_count desc
                            limit 10;""",(select_state,))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Pincode', 'Transaction Count'])
        data.reset_index(drop=True, inplace=True)
        data.index += 1
        data = data.rename_axis('S.No')
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['District_State'] = data['District'] + '@(' + data['State'] + ')'
        return data
    
    def selectyear_pincodewise_top10_transaction_count(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, pincode, sum(transaction_count) as transaction_count
                            from top_transaction
                            where year=%s
                            group by state, pincode
                            order by transaction_count desc
                            limit 10;""",(select_year,))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Pincode', 'Transaction Count'])
        data.reset_index(drop=True, inplace=True)
        data.index += 1
        data = data.rename_axis('S.No')
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['State']=data['State'].str.title()
        data['District and State'] = data['District'] + ' District @ ' + data['State'] 
        return data
    
        
    def selectyear_pincodewise_top10_transaction_amount(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, pincode, sum(transaction_amount) as transaction_amount
                            from top_transaction
                            where year=%s
                            group by state, pincode
                            order by transaction_amount desc
                            limit 10;""",(select_year,))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Pincode', 'Transaction Amount'])
        data['Transaction Amount']=data['Transaction Amount'].apply(lambda x: round(x, 0))
        data.reset_index(drop=True, inplace=True)
        data.index += 1
        data = data.rename_axis('S.No')
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['State']=data['State'].str.title()
        data['District and State'] = data['District'] + ' District @ ' + data['State'] 
        data['Transaction Amt']=data['Transaction Amount'].apply(lambda x: state.convert(str(int(x))) )
        return data
    
    def selectstate_selectyear_pincode_wise_transaction_count(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year,pincode, sum(transaction_count) as transaction_count
                            from top_transaction
                            where state=%s and year=%s
                            group by state, pincode, year
                            order by transaction_count desc
                            limit 10;""",(select_state, select_year))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State','Year', 'Pincode', 'Transaction Count'])
        data['State']=data['State'].str.title()
        data.reset_index(drop=True, inplace=True)
        data.index += 1
        data = data.rename_axis('S.No')
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['District and State'] = data['District'] + ' District @ '  + data['State'] 
        return data
    
    def selectstate_selectyear_pincode_wise_transaction_amount(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year,pincode, sum(transaction_amount) as transaction_amount
                            from top_transaction
                            where state=%s and year=%s
                            group by state, pincode, year
                            order by transaction_amount desc
                            limit 10;""",(select_state, select_year))
        s = cursor.fetchall()
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State','Year', 'Pincode', 'Transaction Amount'])
        data['State']=data['State'].str.title()
        data.reset_index(drop=True, inplace=True)
        data.index += 1
        data = data.rename_axis('S.No')
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['District and State'] = data['District'] + ' District @ '  + data['State'] 
        return data
    
    
    def selectyear_selectquarter_statewise_top10_transaction(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(transaction_count) as transaction_count, sum(transaction_amount) as transaction_amount 
                            from top_transaction
                            where year=%s and quarter=%s
                            group by quarter, year, state
                            order by transaction_amount desc
                            limit 10;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Transaction Count', 'Transaction Amount'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Count'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data['Amount'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data['Avg. Transaction Value'] = data['Transaction Amount'] // data['Transaction Count']
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selectquarter_districtwise_top10_transaction(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, district, transaction_count, transaction_amount
                            from map_transaction
                            where year=%s and quarter=%s
                            group by transaction_amount, transaction_count, district, quarter, year, state
                            order by transaction_amount desc
                            limit 10;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'District', 'Transaction Count', 'Transaction Amount'], index=i)
        data['Transaction Amount'] = data['Transaction Amount'].apply(
            lambda x: int(round(x, 0)))
        data = data.rename_axis('S.No')
        data['Count'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data['Amount'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
        data['Avg. Transaction Value'] = data['Transaction Amount'] // data['Transaction Count']
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        data['District_State'] = data['District'] + '@(' + data['State'] + ')'
        return data

    def selectyear_selectquarter_pincodewise_top10_transaction_count(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, pincode, sum(transaction_count) as transaction_count
                                                   from top_transaction
                            where year=%s and quarter=%s
                            group by pincode, state
                            order by transaction_count desc
                            limit 10;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Pincode', 'Transaction Count'], index=i)
        data['Count'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))        
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['State']=data['State'].str.title()
        data['District and State'] =  data['District'] + ' District @ ' + data['State'] 
        return data

    def selectyear_selectquarter_pincodewise_top10_transaction_amount(select_year, select_quarter):
            connection = mysql.connector.connect(
                                            host='localhost',
                                            user='root',
                                            password='Kimch!811',
                                            database='PhonePe_Data'
                                        )
            cursor = connection.cursor()
            cursor.execute(f"""select state, year, quarter, pincode, sum(transaction_count) as transaction_count, sum(transaction_amount) as transaction_amount
                                from top_transaction
                                where year=%s and quarter=%s
                                group by pincode, state
                                order by transaction_amount desc
                                limit 10;""", (select_year, select_quarter))
            s = cursor.fetchall()
            i = [i for i in range(1, len(s)+1)]
            pd.set_option('display.max_columns', None)
            data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Pincode', 'Transaction Count', 'Transaction Amount'], index=i)
            data['Transaction Amount'] = data['Transaction Amount'].apply(lambda x: int(round(x, 0)))
            data = data.rename_axis('S.No')
            data['Count'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
            data['Amount'] = data['Transaction Amount'].apply(lambda x: state.convert(str(x)))
            data['Avg. Transaction Value'] = data['Transaction Amount'] // data['Transaction Count']
            data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
            data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
            data['State']=data['State'].str.title()
            data['District and State'] =  data['District'] + ' District @ ' + data['State'] 
            return data

    def selectstate_selectyear_selectquarter_districtwise_top10_transaction_count(select_state, select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                        )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, district, transaction_count
                            from map_transaction
                            where state=%s and year=%s and quarter=%s
                            group by transaction_count, district, quarter, year, state
                            order by transaction_count desc
                            limit 10;""", (select_state, select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'District', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Count'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_selectquarter_pincodewise_top10_transaction_count(select_state, select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                        )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, pincode, sum(transaction_count) as transaction_count
                                                    from top_transaction
                            where state=%s and year=%s and quarter=%s
                            group by pincode, quarter, year, state
                            order by transaction_count desc
                            limit 10;""", (select_state, select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Pincode', 'Transaction Count'], index=i)
        data = data.rename_axis('S.No')
        data['Count'] = data['Transaction Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['State']=data['State'].str.title()
        data['District and State'] = data['District'] + ' District @' + data['State'] 
        return data

    def selectstate_selectyear_selectquarter_pincodewise_top10_transaction_amount(select_state, select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                        )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, pincode, sum(transaction_amount) as transaction_amount
                                                    from top_transaction
                            where state=%s and year=%s and quarter=%s
                            group by pincode, quarter, year, state
                            order by transaction_amount desc
                            limit 10;""", (select_state, select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'Pincode', 'Transaction Amount'], index=i)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['State']=data['State'].str.title()
        data['District and State'] = data['District'] + ' District @' + data['State'] 
        return data

#3. USERS
class aggregated_user:
    def state_wise_user_count():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, sum(user_count) as user_count 
                            from aggregated_user
                            group by state
                            order by state asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'User Count'], index=i)
               
        data = data.sort_values(by='User Count', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def stateandyear_wise_user_count():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, sum(user_count) as user_count 
                            from aggregated_user
                            group by state, year
                            order by state asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State','Year','User Count'], index=i)
               
        data = data.sort_values(by='User Count', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data


    def selectstate_year_wise_user_count(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, sum(user_count) as user_count 
                                from aggregated_user
                                where state=%s
                                group by year, state
                                order by year asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_quarter_wise_user_count(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, sum(user_count) as user_count 
                            from aggregated_user
                            where state=%s
                            group by quarter, state
                            order by quarter asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame( s, columns=['State', 'Quarter', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_brand_wise_user_count(select_state):
        connection =mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, brands, sum(user_count) as user_count 
                            from aggregated_user
                            where state=%s
                            group by brands, state
                            order by case when brands = 'Others' then 1 else 0 end, user_count desc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_year_quarter_wise_user_count(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(user_count) as user_count 
                            from aggregated_user
                            where state=%s
                            group by quarter, year, state
                            order by year, quarter asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'Quarter', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_quarter_wise_user_count(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(user_count) as user_count 
                            from aggregated_user
                            where state=%s and year=%s
                            group by quarter, year, state
                            order by quarter asc;""", (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_brand_wise_user_count(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
            
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, brands, sum(user_count) as user_count 
                            from aggregated_user
                            where state=%s and year=%s
                            group by brands, year, state
                            order by case when brands = 'Others' then 1 else 0 end, user_count desc;""", (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectquarter_year_wise_user_count(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(user_count) as user_count 
                            from aggregated_user
                            where state=%s and quarter=%s
                            group by quarter, year, state
                            order by year asc;""", (select_state, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectquarter_brand_wise_user_count(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, brands, sum(user_count) as user_count 
                            from aggregated_user
                            where state=%s and quarter=%s
                            group by brands, quarter, state
                            order by case when brands = 'Others' then 1 else 0 end, user_count desc;""", (select_state, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'quarter', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_selectquarter_brand_wise_user_count(select_state, select_year, select_quarter):
        connection =mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, brands, user_count 
                            from aggregated_user
                            where state=%s and year=%s and quarter=%s
                            order by case when brands = 'Others' then 1 else 0 end, user_count desc;""", (select_state, select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_quarter_brand_wise_user_count(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, brands, user_count 
                            from aggregated_user
                            where state=%s and year=%s
                            order by quarter asc, case when brands = 'Others' then 1 else 0 end, user_count desc;""", (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectquarter_year_brand_wise_user_count(select_state, select_quarter):
        connection =mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, brands, user_count 
                            from aggregated_user
                            where state=%s and quarter=%s
                            order by year, case when brands = 'Others' then 1 else 0 end, user_count desc;""", (select_state, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    # year - wise
    def year_wise_user_count():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, sum(user_count) as user_count 
                                from aggregated_user
                                group by year
                                order by year asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['Year', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def year_quarter_wise_user_count():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(user_count) as user_count 
                            from aggregated_user
                            group by quarter, year
                            order by year, quarter asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['Year', 'Quarter', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def year_brand_wise_user_count():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, brands, sum(user_count) as user_count 
                            from aggregated_user
                            group by brands, year
                            order by year asc, case when brands = 'Others' then 1 else 0 end, user_count desc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data
    
    def quarter_brand_wise_user_count():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select quarter, brands, sum(user_count) as user_count 
                            from aggregated_user
                            group by brands, quarter
                            order by quarter asc, case when brands = 'Others' then 1 else 0 end, user_count desc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['quarter', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def state_wise_user_percentage():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, sum(user_percentage) as user_percentage 
                                from aggregated_user
                                group by state
                                order by user_percentage desc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame( s, columns=['State', 'User Percentage'], index=i)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data
    
    def selectyear_state_wise_user_count(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, sum(user_count) as user_count 
                                from aggregated_user
                                where year=%s
                                group by state
                                order by state asc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'Year', 'User Count'], index=i)
               
        data = data.sort_values(by='User Count', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_state_wise_user_count(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, sum(user_count) as user_count 
                                from aggregated_user
                                where quarter=%s
                                group by quarter, state
                                order by state asc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'quarter', 'User Count'], index=i)
               
        data = data.sort_values(by='User Count', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectbrand_state_wise_user_count(brand_option):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, brands, sum(user_count) as user_count 
                                from aggregated_user
                                where brands=%s
                                group by brands, state
                                order by state asc;""", (brand_option,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'User Brand', 'User Count'], index=i)
               
        data = data.sort_values(by='User Count', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_quarter_wise_user_count(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(user_count) as user_count 
                            from aggregated_user
                            where year=%s
                            group by quarter, year
                            order by quarter asc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'quarter', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_brand_wise_user_count(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, brands, sum(user_count) as user_count 
                            from aggregated_user
                            where year=%s
                            group by brands, year
                            order by case when brands = 'Others' then 1 else 0 end, user_count desc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_quarter_brand_wise_user_count(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, brands, sum(user_count) as user_count 
                            from aggregated_user
                            where year=%s
                            group by brands, quarter, year
                            order by quarter asc, case when brands = 'Others' then 1 else 0 end, user_count desc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'quarter', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selectstate_brand_wise_user_count(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, brands, sum(user_count) as user_count 
                                from aggregated_user
                                where state=%s and year=%s
                                group by brands, year, state
                                order by case when brands = 'Others' then 1 else 0 end, user_count desc;""", (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selectstate_quarter_brand_wise_user_count(select_state, select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, brands, sum(user_count) as user_count 
                                from aggregated_user
                                where state=%s and year=%s and quarter=%s
                                group by brands, quarter, year, state
                                order by case when brands = 'Others' then 1 else 0 end, user_count desc;""", (select_state, select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selectquarter_state_wise_user_count(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(user_count) as user_count 
                            from aggregated_user
                            where year=%s and quarter=%s
                            group by quarter, year, state
                            order by state asc;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'User Count'], index=i)
               
        data = data.sort_values(by='User Count', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selectquarter_brand_wise_user_count(select_year, select_quarter):
        connection = mysql.connector.connect(
                                            host='localhost',
                                            user='root',
                                            password='Kimch!811',
                                            database='PhonePe_Data'
                                           )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, brands, sum(user_count) as user_count 
                            from aggregated_user
                            where year=%s and quarter=%s
                            group by brands, quarter, year
                            order by case when brands = 'Others' then 1 else 0 end, user_count desc;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'quarter', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    # quarter - wise
    def quarter_wise_user_count():
        connection =mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select quarter, sum(user_count) as user_count 
                                from aggregated_user
                                group by quarter
                                order by quarter asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['Quarter', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_year_wise_user_count(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(user_count) as user_count 
                            from aggregated_user
                            where quarter=%s
                            group by quarter, year
                            order by year asc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'quarter', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_brand_wise_user_count(select_quarter):
        connection = mysql.connector.connect(
                                            host='localhost',
                                            user='root',
                                            password='Kimch!811',
                                            database='PhonePe_Data'
                                           )
        cursor = connection.cursor()
        cursor.execute(f"""select quarter, brands, sum(user_count) as user_count 
                            from aggregated_user
                            where quarter=%s
                            group by brands, quarter
                            order by case when brands = 'Others' then 1 else 0 end, user_count desc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['quarter', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_year_brand_wise_user_count(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, brands, sum(user_count) as user_count 
                            from aggregated_user
                            where quarter=%s
                            group by brands, quarter, year
                            order by year asc, case when brands = 'Others' then 1 else 0 end, user_count desc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'quarter', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data


    # brand - wise
    def brand_wise_user_count():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select brands, sum(user_count) as user_count 
                            from aggregated_user
                            group by brands
                            order by case when brands = 'Others' then 1 else 0 end, user_count desc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectbrand_state_wise_user_count(brand_option):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, brands, sum(user_count) as user_count 
                            from aggregated_user
                            where brands=%s
                            group by brands, state
                            order by state asc;""", (brand_option,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'User Brand', 'User Count'], index=i)
               
        data = data.sort_values(by='User Count', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectbrand_year_wise_user_count(brand_option):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, brands, sum(user_count) as user_count 
                            from aggregated_user
                            where brands=%s
                            group by brands, year
                            order by year asc;""", (brand_option,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectbrand_quarter_wise_user_count(brand_option):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select quarter, brands, sum(user_count) as user_count 
                            from aggregated_user
                            where brands=%s
                            group by brands, quarter
                            order by user_count asc;""", (brand_option,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['quarter', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectbrand_year_quarter_wise_user_count(brand_option):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, brands, sum(user_count) as user_count 
                            from aggregated_user
                            where brands=%s
                            group by brands, quarter, year
                            order by year, quarter asc;""", (brand_option,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'quarter', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectbrand_year_wise_user_count(select_state, brand_option):
        connection =mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, brands, sum(user_count) as user_count 
                            from aggregated_user
                            where state=%s and brands=%s
                            group by brands, year, state
                            order by year asc;""", (select_state, brand_option))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectbrand_quarter_wise_user_count(select_state, brand_option):
        connection =mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, brands, sum(user_count) as user_count 
                            from aggregated_user
                            where state=%s and brands=%s
                            group by brands, quarter, state
                            order by quarter asc;""", (select_state, brand_option))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'quarter', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectbrand_year_quarter_wise_user_count(select_state, brand_option):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, brands, sum(user_count) as user_count 
                            from aggregated_user
                            where state=%s and brands=%s
                            group by brands, quarter, year, state
                            order by year, quarter asc;""", (select_state, brand_option))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selectbrand_state_wise_user_count(select_year, brand_option):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, brands, sum(user_count) as user_count 
                            from aggregated_user
                            where year=%s and brands=%s
                            group by brands, year, state
                            order by state asc;""", (select_year, brand_option))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'User Brand', 'User Count'], index=i)
               
        data = data.sort_values(by='User Count', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selectbrand_quarter_wise_user_count(select_year, brand_option):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, brands, sum(user_count) as user_count 
                            from aggregated_user
                            where year=%s and brands=%s
                            group by brands, quarter, year
                            order by quarter asc;""", (select_year, brand_option))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'quarter', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_selectbrand_state_wise_user_count(select_quarter, brand_option):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, brands, sum(user_count) as user_count 
                            from aggregated_user
                            where quarter=%s and brands=%s
                            group by brands, quarter, state
                            order by state asc;""", (select_quarter, brand_option))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'quarter', 'User Brand', 'User Count'], index=i)
               
        data = data.sort_values(by='User Count', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_selectbrand_year_wise_user_count(select_quarter, brand_option):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, brands, sum(user_count) as user_count 
                            from aggregated_user
                            where quarter=%s and brands=%s
                            group by brands, quarter, year
                            order by year asc;""", (select_quarter, brand_option))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'quarter', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_selectbrand_quarter_wise_user_count(select_state, select_year, brand_option):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, brands, sum(user_count) as user_count 
                            from aggregated_user
                            where state=%s and year=%s and brands=%s
                            group by brands, quarter, year, state
                            order by quarter asc;""", (select_state, select_year, brand_option))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectquarter_selectbrand_year_wise_user_count(select_state, select_quarter, brand_option):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, brands, sum(user_count) as user_count 
                            from aggregated_user
                            where state=%s and quarter=%s and brands=%s
                            group by brands, quarter, year, state
                            order by year asc;""", (select_state, select_quarter, brand_option))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selectquarter_selectbrand_state_wise_user_count(select_year, select_quarter, brand_option):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, brands, sum(user_count) as user_count 
                            from aggregated_user
                            where year=%s and quarter=%s and brands=%s
                            group by brands, quarter, year, state
                            order by state asc;""", (select_year, select_quarter, brand_option))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=[
                            'State', 'Year', 'quarter', 'User Brand', 'User Count'], index=i)
               
        data = data.sort_values(by='User Count', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_selectquarter_selectbrand_wise_user_count(select_state, select_year, select_quarter, brand_option):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, brands, sum(user_count) as user_count 
                        from aggregated_user
                        where state=%s and year=%s and quarter=%s and brands=%s
                        group by brands, quarter, year, state;""", (select_state, select_year, select_quarter, brand_option))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'User Brand', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['User Count'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

class map_user:
    def state_wise_registerUsers():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, sum(registerUsers) as registerUsers 
                                from map_user
                                group by state
                                order by state asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Registered Users'], index=i)
               
        data = data.sort_values(by='Registered Users', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def state_wise_appOpens():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, sum(appOpens) as appOpens 
                                from map_user
                                group by state
                                order by state asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'App Opens'], index=i)
               
        data = data.sort_values(by='App Opens', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data
    
    def state_wise_registerUsers():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, sum(registerUsers) as registerUsers 
                                from map_user
                                group by state
                                order by state asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Registered Users'], index=i)
               
        data = data.sort_values(by='Registered Users', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def year_wise_registerUsers():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, sum(registerUsers) as registerUsers 
                                from map_user
                                group by year
                                order by year asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['Year', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Register'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def year_wise_appOpens():
        connection =mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, sum(appOpens) as appOpens 
                                from map_user
                                group by year
                                order by year asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['App'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def year_quarter_wise_registerUsers():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(registerUsers) as registerUsers 
                                from map_user
                                group by quarter, year
                                order by year, quarter asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'quarter', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Register'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def year_quarter_wise_appOpens():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(appOpens) as appOpens 
                                from map_user
                                group by quarter, year
                                order by year, quarter asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'quarter', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['App'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def district_wise_registerUsers():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, district, sum(registeredUsers) as registerUsers 
                                from map_user
                                group by state, district
                                order by registerUsers desc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(s, columns=['State', 'District','Registered Users'], index=i)
               
        data = data.sort_values(by='Registered Users', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data
    
    def quarter_wise_registerUsers():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select quarter, sum(registerUsers) as registerUsers 
                                from map_user
                                group by quarter
                                order by quarter asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['quarter', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Register'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def quarter_wise_appOpens():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select quarter, sum(appOpens) as appOpens 
                                from map_user
                                group by quarter
                                order by quarter asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['quarter', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['App'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select quarter, sum(appOpens) as appOpens 
                                from map_user
                                group by quarter
                                order by quarter asc;""")
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['quarter', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['App'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_state_wise_registerUsers(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, sum(registerUsers) as registerUsers 
                                from map_user
                                where year=%s
                                group by year, state
                                order by state asc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Registered Users'], index=i)
               
        data = data.sort_values(by='Registered Users', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_state_wise_appOpens(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, sum(appOpens) as appOpens 
                                from map_user
                                where year=%s
                                group by year, state
                                order by state asc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'App Opens'], index=i)
               
        data = data.sort_values(by='App Opens', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_state_wise_registerUsers(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, sum(registerUsers) as registerUsers 
                                from map_user
                                where quarter=%s
                                group by quarter, state
                                order by state asc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'quarter', 'Registered Users'], index=i)
               
        data = data.sort_values(by='Registered Users', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_state_wise_appOpens(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, sum(appOpens) as appOpens 
                                from map_user
                                where quarter=%s
                                group by quarter, state
                                order by state asc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'quarter', 'App Opens'], index=i)
               
        data = data.sort_values(by='App Opens', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_year_wise_registerUsers(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, sum(registerUsers) as registerUsers 
                                from map_user
                                where state=%s
                                group by year, state
                                order by year asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Register'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_year_wise_appOpens(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, sum(appOpens) as appOpens 
                                from map_user
                                where state=%s
                                group by year, state
                                order by year asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['App'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_quarter_wise_registerUsers(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, sum(registerUsers) as registerUsers 
                            from map_user
                            where state=%s
                            group by quarter, state
                            order by quarter asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'quarter', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Register'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_quarter_wise_appOpens(select_state):
        connection = mysql.connector.connect(
                                            host='localhost',
                                            user='root',
                                            password='Kimch!811',
                                            database='PhonePe_Data'
                                           )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, sum(appOpens) as appOpens 
                                from map_user
                                where state=%s
                                group by quarter, state
                                order by quarter asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'quarter', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['App'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_year_quarter_wise_registerUsers(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(registerUsers) as registerUsers 
                            from map_user
                            where state=%s
                            group by quarter, year, state
                            order by year, quarter asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Register'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_year_quarter_wise_appOpens(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(appOpens) as appOpens 
                                from map_user
                                where state=%s
                                group by quarter, year, state
                                order by year, quarter asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['App'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_quarter_wise_registerUsers(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(registerUsers) as registerUsers 
                            from map_user
                            where state=%s and year=%s
                            group by quarter, year, state
                            order by quarter asc;""", (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Register'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_quarter_wise_appOpens(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(appOpens) as appOpens 
                                from map_user
                                where state=%s and year=%s
                                group by quarter, year, state
                                order by quarter asc;""", (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['App'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectquarter_year_wise_registerUsers(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(registerUsers) as registerUsers 
                            from map_user
                            where state=%s and quarter=%s
                            group by quarter, year, state
                            order by year asc;""", (select_state, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Register'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectquarter_year_wise_appOpens(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
            
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(appOpens) as appOpens 
                            from map_user
                            where state=%s and quarter=%s
                            group by quarter, year, state
                            order by year asc;""", (select_state, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['App'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_quarter_wise_registerUsers(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(registerUsers) as registerUsers 
                            from map_user
                            where year=%s
                            group by quarter, year
                            order by quarter asc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'quarter', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Register'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_quarter_wise_appOpens(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(appOpens) as appOpens 
                                from map_user
                                where year=%s
                                group by quarter, year
                                order by quarter asc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'quarter', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['App'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selectquarter_state_wise_registerUsers(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(registerUsers) as registerUsers 
                                from map_user
                                where year=%s and quarter=%s
                                group by quarter, year, state
                                order by state asc;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'Registered Users'], index=i)
               
        data = data.sort_values(by='Registered Users', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selectquarter_state_wise_appOpens(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(appOpens) as appOpens 
                                from map_user
                                where year=%s and quarter=%s
                                group by quarter, year, state
                                order by state asc;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'quarter', 'Year', 'App Opens'], index=i)
               
        data = data.sort_values(by='App Opens', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_year_wise_registerUsers(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(registerUsers) as registerUsers 
                            from map_user
                            where quarter=%s
                            group by quarter, year
                            order by year asc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'quarter', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Register'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_year_wise_appOpens(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(appOpens) as appOpens 
                            from map_user
                            where quarter=%s
                            group by quarter, year
                            order by year asc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'quarter', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['App'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_district_wise_registerUsers(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, district, sum(registerUsers) as registerUsers 
                                from map_user
                                where state=%s
                                group by district, state
                                order by registerUsers desc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'District', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_district_wise_appOpens(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, district, sum(appOpens) as appOpens 
                                from map_user
                                where state=%s
                                group by district, state
                                order by appOpens desc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'District', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_district_wise_registerUsers(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, district, sum(registerUsers) as registerUsers 
                                from map_user
                                where state=%s and year=%s
                                group by district, year, state
                                order by year asc, registerUsers desc;""", (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'District', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_district_wise_appOpens(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, district, sum(appOpens) as appOpens 
                                from map_user
                                where state=%s and year=%s
                                group by district, year, state
                                order by year asc, appOpens desc;""", (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'District', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectquarter_district_wise_registerUsers(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, district, sum(registerUsers) as registerUsers 
                                from map_user
                                where state=%s and quarter=%s
                                group by district, quarter, state
                                order by quarter asc, registerUsers desc;""", (select_state, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'quarter', 'District', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectquarter_district_wise_appOpens(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, district, sum(appOpens) as appOpens 
                                from map_user
                                where state=%s and quarter=%s
                                group by district, quarter, state
                                order by quarter asc, appOpens desc;""", (select_state, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'quarter', 'District', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_selectquarter_district_wise_registerUsers(select_state, select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, district, sum(registerUsers) as registerUsers 
                                from map_user
                                where state=%s and year=%s and quarter=%s
                                group by district, quarter, year, state
                                order by year, quarter asc, registerUsers desc;""", (select_state, select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'District', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_selectquarter_district_wise_appOpens(select_state, select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, district, sum(appOpens) as appOpens 
                                from map_user
                                where state=%s and year=%s and quarter=%s
                                group by district, quarter, year, state
                                order by year, quarter asc, appOpens desc;""", (select_state, select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'District', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data
    
    def selectyear_state_wise_registerUsers(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, sum(registerUsers) as registerUsers 
                                from map_user
                                where year=%s
                                group by year, state
                                order by state asc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Registered Users'], index=i)
               
        data = data.sort_values(by='Registered Users', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_state_wise_appOpens(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, sum(appOpens) as appOpens 
                                from map_user
                                where year=%s
                                group by year, state
                                order by state asc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'App Opens'], index=i)
               
        data = data.sort_values(by='App Opens', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_state_wise_registerUsers(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, sum(registerUsers) as registerUsers 
                                from map_user
                                where quarter=%s
                                group by quarter, state
                                order by state asc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'quarter', 'Registered Users'], index=i)
               
        data = data.sort_values(by='Registered Users', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_state_wise_appOpens(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, sum(appOpens) as appOpens 
                                from map_user
                                where quarter=%s
                                group by quarter, state
                                order by state asc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'quarter', 'App Opens'], index=i)
               
        data = data.sort_values(by='App Opens', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_year_wise_registerUsers(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, sum(registerUsers) as registerUsers 
                                from map_user
                                where state=%s
                                group by year, state
                                order by year asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Register'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_year_wise_appOpens(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, sum(appOpens) as appOpens 
                                from map_user
                                where state=%s
                                group by year, state
                                order by year asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['App'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_quarter_wise_registerUsers(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, sum(registerUsers) as registerUsers 
                            from map_user
                            where state=%s
                            group by quarter, state
                            order by quarter asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'quarter', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Register'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_quarter_wise_appOpens(select_state):
        connection = mysql.connector.connect(
                                            host='localhost',
                                            user='root',
                                            password='Kimch!811',
                                            database='PhonePe_Data'
                                           )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, sum(appOpens) as appOpens 
                                from map_user
                                where state=%s
                                group by quarter, state
                                order by quarter asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'quarter', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['App'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_year_quarter_wise_registerUsers(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(registerUsers) as registerUsers 
                            from map_user
                            where state=%s
                            group by quarter, year, state
                            order by year, quarter asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Register'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_year_quarter_wise_appOpens(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(appOpens) as appOpens 
                                from map_user
                                where state=%s
                                group by quarter, year, state
                                order by year, quarter asc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['App'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_quarter_wise_registerUsers(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(registerUsers) as registerUsers 
                            from map_user
                            where state=%s and year=%s
                            group by quarter, year, state
                            order by quarter asc;""", (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Register'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_quarter_wise_appOpens(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(appOpens) as appOpens 
                                from map_user
                                where state=%s and year=%s
                                group by quarter, year, state
                                order by quarter asc;""", (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['App'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectquarter_year_wise_registerUsers(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(registerUsers) as registerUsers 
                            from map_user
                            where state=%s and quarter=%s
                            group by quarter, year, state
                            order by year asc;""", (select_state, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Register'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectquarter_year_wise_appOpens(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
            
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(appOpens) as appOpens 
                            from map_user
                            where state=%s and quarter=%s
                            group by quarter, year, state
                            order by year asc;""", (select_state, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['App'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_quarter_wise_registerUsers(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(registerUsers) as registerUsers 
                            from map_user
                            where year=%s
                            group by quarter, year
                            order by quarter asc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'quarter', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Register'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_quarter_wise_appOpens(select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(appOpens) as appOpens 
                                from map_user
                                where year=%s
                                group by quarter, year
                                order by quarter asc;""", (select_year,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'quarter', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['App'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selectquarter_state_wise_registerUsers(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(registerUsers) as registerUsers 
                                from map_user
                                where year=%s and quarter=%s
                                group by quarter, year, state
                                order by state asc;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'Registered Users'], index=i)
               
        data = data.sort_values(by='Registered Users', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selectquarter_state_wise_appOpens(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(appOpens) as appOpens 
                                from map_user
                                where year=%s and quarter=%s
                                group by quarter, year, state
                                order by state asc;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'quarter', 'Year', 'App Opens'], index=i)
               
        data = data.sort_values(by='App Opens', ascending=False)
        data = data.rename_axis('S.No')
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_year_wise_registerUsers(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(registerUsers) as registerUsers 
                            from map_user
                            where quarter=%s
                            group by quarter, year
                            order by year asc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'quarter', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Register'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectquarter_year_wise_appOpens(select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select year, quarter, sum(appOpens) as appOpens 
                            from map_user
                            where quarter=%s
                            group by quarter, year
                            order by year asc;""", (select_quarter,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['Year', 'quarter', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['App'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_district_wise_registerUsers(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, district, sum(registerUsers) as registerUsers 
                                from map_user
                                where state=%s
                                group by district, state
                                order by registerUsers desc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'District', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_district_wise_appOpens(select_state):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, district, sum(appOpens) as appOpens 
                                from map_user
                                where state=%s
                                group by district, state
                                order by appOpens desc;""", (select_state,))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'District', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_district_wise_registerUsers(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, district, sum(registerUsers) as registerUsers 
                                from map_user
                                where state=%s and year=%s
                                group by district, year, state
                                order by year asc, registerUsers desc;""", (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'District', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_district_wise_appOpens(select_state, select_year):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, district, sum(appOpens) as appOpens 
                                from map_user
                                where state=%s and year=%s
                                group by district, year, state
                                order by year asc, appOpens desc;""", (select_state, select_year))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'District', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectquarter_district_wise_registerUsers(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, district, sum(registerUsers) as registerUsers 
                                from map_user
                                where state=%s and quarter=%s
                                group by district, quarter, state
                                order by quarter asc, registerUsers desc;""", (select_state, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'quarter', 'District', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectquarter_district_wise_appOpens(select_state, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, quarter, district, sum(appOpens) as appOpens 
                                from map_user
                                where state=%s and quarter=%s
                                group by district, quarter, state
                                order by quarter asc, appOpens desc;""", (select_state, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'quarter', 'District', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_selectquarter_district_wise_registerUsers(select_state, select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, district, sum(registerUsers) as registerUsers 
                                from map_user
                                where state=%s and year=%s and quarter=%s
                                group by district, quarter, year, state
                                order by year, quarter asc, registerUsers desc;""", (select_state, select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'District', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_selectquarter_district_wise_appOpens(select_state, select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, district, sum(appOpens) as appOpens 
                                from map_user
                                where state=%s and year=%s and quarter=%s
                                group by district, quarter, year, state
                                order by year, quarter asc, appOpens desc;""", (select_state, select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'District', 'App Opens'], index=i)
        data = data.rename_axis('S.No')
        data['Formatted Value'] = data['App Opens'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

class top_user:
    def pincodewise_top10_user_count():
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, pincode, sum(registeredUsers) as registeredUsers
                            from top_user
                            group by state, pincode
                            order by registeredUsers desc
                            limit 10;""", ())
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Pincode', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Users'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data
    
    def selectyear_selectquarter_statewise_top10_user(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, sum(registeredUsers) as registeredUsers
                            from top_user
                            where year=%s and quarter=%s
                            group by quarter, year, state
                            order by registeredUsers desc
                            limit 10;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'Registered Users'], index=i)
        data = data.rename_axis('S.No')
        data['Users'] = data['Registered Users'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectyear_selectquarter_districtwise_top10_user(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, district, registeredUsers
                            from map_user
                            where year=%s and quarter=%s
                            group by registeredUsers, district, quarter, year, state
                            order by registeredUsers desc
                            limit 10;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'District', 'registeredUsers'], index=i)
        data = data.rename_axis('S.No')
        data['Users'] = data['registeredUsers'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        data['District_State'] = data['District'] + '@(' + data['State'] + ')'
        return data

    def selectyear_selectquarter_pincodewise_top10_user(select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, pincode, sum(registeredUsers) as registeredUsers
                            from top_user
                            where year=%s and quarter=%s
                            group by pincode, quarter, year, state
                            order by registeredUsers desc
                            limit 10;""", (select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'Pincode', 'registeredUsers'], index=i)
        data = data.rename_axis('S.No')
        data['Users'] = data['registeredUsers'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['Pincode_District_State'] = data['Pincode'] + '@(' + data['District'] + ' -@' + data['State'] + ')'
        return data

    def selectstate_selectyear_selectquarter_districtwise_top10_user(select_state, select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, district, registeredUsers
                            from map_user
                            where state=%s and year=%s and quarter=%s
                            group by registeredUsers, district, quarter, year, state
                            order by registeredUsers desc
                            limit 10;""", (select_state, select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'quarter', 'District', 'registeredUsers'], index=i)
        data = data.rename_axis('S.No')
        data['Users'] = data['registeredUsers'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        return data

    def selectstate_selectyear_selectquarter_pincodewise_top10_user(select_state, select_year, select_quarter):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select state, year, quarter, pincode, sum(registeredUsers) as registeredUsers
                            from map_user
                            where state=%s and year=%s and quarter=%s
                            group by pincode, quarter, year, state
                            order by registeredUsers desc
                            limit 10;""", (select_state, select_year, select_quarter))
        s = cursor.fetchall()
        i = [i for i in range(1, len(s)+1)]
        pd.set_option('display.max_columns', None)
        data = pd.DataFrame(
            s, columns=['State', 'Year', 'Quarter', 'Pincode', 'User Count'], index=i)
        data = data.rename_axis('S.No')
        data['User'] = data['registeredUsers'].apply(lambda x: state.convert(str(x)))
        data.index = data.index.map(lambda x: '{:^{}}'.format(x, 10))
        data['District'] = data['Pincode'].apply(lambda x: state.find_district(x))
        data['Pincode_District'] = data['Pincode'] + '@(' + data['District'] + ')'
        return data

#4. TOP CHARTS
class top_charts:
    def top_chart_transaction_amount(table_name):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        #plot_1
        query1= f'''SELECT state, SUM(transaction_amount) AS transaction_amount
                    FROM {table_name}
                    GROUP BY state
                    ORDER BY transaction_amount DESC
                    LIMIT 10;'''

        cursor.execute(query1)
        table_1= cursor.fetchall()
        connection.commit()

        df_1= pd.DataFrame(table_1, columns=("state", "transaction_amount"))

        col1,col2= st.columns(2)
        with col1:

            fig_amount= px.bar(df_1, x="state", y="transaction_amount", title="TOP 10 OF TRANSACTION AMOUNT", hover_name= "state",
                                color_discrete_sequence=px.colors.sequential.Aggrnyl, height= 650,width= 600)
            st.plotly_chart(fig_amount)

        #plot_2
        query2= f'''SELECT state, SUM(transaction_amount) AS transaction_amount
                    FROM {table_name}
                    GROUP BY state
                    ORDER BY transaction_amount
                    LIMIT 10;'''

        cursor.execute(query2)
        table_2= cursor.fetchall()
        connection.commit()

        df_2= pd.DataFrame(table_2, columns=("state", "transaction_amount"))
        
        with col2:
            fig_amount_2= px.bar(df_2, x="state", y="transaction_amount", title="LAST 10 OF TRANSACTION AMOUNT", hover_name= "state",
                                color_discrete_sequence=px.colors.sequential.Aggrnyl_r, height= 650,width= 600)
            st.plotly_chart(fig_amount_2)

        #plot_3
        query3= f'''SELECT state, AVG(transaction_amount) AS transaction_amount
                    FROM {table_name}
                    GROUP BY state
                    ORDER BY transaction_amount;'''

        cursor.execute(query3)
        table_3= cursor.fetchall()
        connection.commit()

        df_3= pd.DataFrame(table_3, columns=("state", "transaction_amount"))

        fig_amount_3= px.bar(df_3, y="state", x="transaction_amount", title="AVERAGE OF TRANSACTION AMOUNT", hover_name= "state", orientation= "h",
                            color_discrete_sequence=px.colors.sequential.Bluered_r, height= 800,width= 1000)
        st.plotly_chart(fig_amount_3)

    def top_chart_transaction_count(table_name):
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()

        #plot_1
        query1= f'''SELECT state, SUM(transaction_count) AS transaction_count
                    FROM {table_name}
                    GROUP BY state
                    ORDER BY transaction_count DESC
                    LIMIT 10;'''

        cursor.execute(query1)
        table_1= cursor.fetchall()
        connection.commit()

        df_1= pd.DataFrame(table_1, columns=("state", "transaction_count"))

        col1,col2= st.columns(2)
        with col1:
            fig_amount= px.bar(df_1, x="state", y="transaction_count", title="TOP 10 OF TRANSACTION COUNT", hover_name= "state",
                                color_discrete_sequence=px.colors.sequential.Aggrnyl, height= 650,width= 600)
            st.plotly_chart(fig_amount)

        #plot_2
        query2= f'''SELECT state, SUM(transaction_count) AS transaction_count
                    FROM {table_name}
                    GROUP BY state
                    ORDER BY transaction_count
                    LIMIT 10;'''

        cursor.execute(query2)
        table_2= cursor.fetchall()
        connection.commit()

        df_2= pd.DataFrame(table_2, columns=("state", "transaction_count"))

        with col2:
            fig_amount_2= px.bar(df_2, x="state", y="transaction_count", title="LAST 10 OF TRANSACTION COUNT", hover_name= "state",
                                color_discrete_sequence=px.colors.sequential.Aggrnyl_r, height= 650,width= 600)
            st.plotly_chart(fig_amount_2)

        #plot_3
        query3= f'''SELECT state, AVG(transaction_count) AS transaction_count
                    FROM {table_name}
                    GROUP BY state
                    ORDER BY transaction_count;'''

        cursor.execute(query3)
        table_3= cursor.fetchall()
        connection.commit()

        df_3= pd.DataFrame(table_3, columns=("state", "transaction_count"))

        fig_amount_3= px.bar(df_3, y="state", x="transaction_count", title="AVERAGE OF TRANSACTION COUNT", hover_name= "state", orientation= "h",
                            color_discrete_sequence=px.colors.sequential.Bluered_r, height= 800,width= 1000)
        st.plotly_chart(fig_amount_3)

#sql connection
    def top_chart_registerUsers(table_name, state):
        connection = mysql.connector.connect(
                                            host='localhost',
                                            user='root',
                                            password='Kimch!811',
                                            database='PhonePe_Data'
                                        )
        cursor = connection.cursor()

        #plot_1
        query1= f'''SELECT district, SUM(registereduser) AS registereduser
                    FROM {table_name}
                    WHERE state= '{state}'
                    GROUP BY district
                    ORDER BY registereduser DESC
                    LIMIT 10;'''

        cursor.execute(query1)
        table_1= cursor.fetchall()
        connection.commit()

        df_1= pd.DataFrame(table_1, columns=("district", "registereduser"))

        col1,col2= st.columns(2)
        with col1:
            fig_amount= px.bar(df_1, x="district", y="registereduser", title="TOP 10 OF REGISTERED USER", hover_name= "district",
                                color_discrete_sequence=px.colors.sequential.Aggrnyl, height= 650,width= 600)
            st.plotly_chart(fig_amount)

        #plot_2
        query2= f'''SELECT district, SUM(registereduser) AS registereduser
                    FROM {table_name}
                    WHERE state= '{state}'
                    GROUP BY district
                    ORDER BY registereduser
                    LIMIT 10;'''

        cursor.execute(query2)
        table_2= cursor.fetchall()
        connection.commit()

        df_2= pd.DataFrame(table_2, columns=("district", "registereduser"))

        with col2:
            fig_amount_2= px.bar(df_2, x="district", y="registereduser", title="LAST 10 REGISTERED USER", hover_name= "district",
                                color_discrete_sequence=px.colors.sequential.Aggrnyl_r, height= 650,width= 600)
            st.plotly_chart(fig_amount_2)

        #plot_3
        query3= f'''SELECT district, AVG(registereduser) AS registereduser
                    FROM {table_name}
                    WHERE state= '{state}'
                    GROUP BY district
                    ORDER BY registereduser;'''

        cursor.execute(query3)
        table_3= cursor.fetchall()
        connection.commit()

        df_3= pd.DataFrame(table_3, columns=("district", "registereduser"))

        fig_amount_3= px.bar(df_3, y="district", x="registereduser", title="AVERAGE OF REGISTERED USER", hover_name= "district", orientation= "h",
                            color_discrete_sequence=px.colors.sequential.Bluered_r, height= 800,width= 1000)
        st.plotly_chart(fig_amount_3)

#sql connection
    def top_chart_appopens(table_name, state):
        connection = mysql.connector.connect(
                                            host='localhost',
                                            user='root',
                                            password='Kimch!811',
                                            database='PhonePe_Data'
                                        )
        cursor = connection.cursor()

        #plot_1
        query1= f'''SELECT district, SUM(appopens) AS appopens
                    FROM {table_name}
                    WHERE state= '{state}'
                    GROUP BY district
                    ORDER BY appopens DESC
                    LIMIT 10;'''

        cursor.execute(query1)
        table_1= cursor.fetchall()
        connection.commit()

        df_1= pd.DataFrame(table_1, columns=("district", "appopens"))


        col1,col2= st.columns(2)
        with col1:

            fig_amount= px.bar(df_1, x="district", y="appopens", title="TOP 10 OF APPOPENS", hover_name= "district",
                                color_discrete_sequence=px.colors.sequential.Aggrnyl, height= 650,width= 600)
            st.plotly_chart(fig_amount)

        #plot_2
        query2= f'''SELECT district, SUM(appopens) AS appopens
                    FROM {table_name}
                    WHERE state= '{state}'
                    GROUP BY district
                    ORDER BY appopens
                    LIMIT 10;'''

        cursor.execute(query2)
        table_2= cursor.fetchall()
        connection.commit()

        df_2= pd.DataFrame(table_2, columns=("district", "appopens"))

        with col2:

            fig_amount_2= px.bar(df_2, x="district", y="appopens", title="LAST 10 APPOPENS", hover_name= "district",
                                color_discrete_sequence=px.colors.sequential.Aggrnyl_r, height= 650,width= 600)
            st.plotly_chart(fig_amount_2)

        #plot_3
        query3= f'''SELECT district, AVG(appopens) AS appopens
                    FROM {table_name}
                    WHERE state= '{state}'
                    GROUP BY district
                    ORDER BY appopens;'''

        cursor.execute(query3)
        table_3= cursor.fetchall()
        connection.commit()

        df_3= pd.DataFrame(table_3, columns=("district", "appopens"))

        fig_amount_3= px.bar(df_3, y="district", x="appopens", title="AVERAGE OF APPOPENS", hover_name= "district", orientation= "h",
                            color_discrete_sequence=px.colors.sequential.Bluered_r, height= 800,width= 1000)
        st.plotly_chart(fig_amount_3)

#sql connection
    def top_chart_registerUserss(table_name):
        connection = mysql.connector.connect(
                                            host='localhost',
                                            user='root',
                                            password='Kimch!811',
                                            database='PhonePe_Data'
                                        )
        cursor = connection.cursor()

        #plot_1
        query1= f'''SELECT state, SUM(registeredusers) AS registeredusers
                    FROM {table_name}
                    GROUP BY state
                    ORDER BY registeredusers DESC
                    LIMIT 10;'''

        cursor.execute(query1)
        table_1= cursor.fetchall()
        connection.commit()

        df_1= pd.DataFrame(table_1, columns=("state", "registeredusers"))
        
        col1,col2= st.columns(2)
        with col1:

            fig_amount= px.bar(df_1, x="state", y="registeredusers", title="TOP 10 OF REGISTERED USERS", hover_name= "state",
                                color_discrete_sequence=px.colors.sequential.Aggrnyl, height= 650,width= 600)
            st.plotly_chart(fig_amount)

        #plot_2
        query2= f'''SELECT state, SUM(registeredusers) AS registeredusers
                    FROM {table_name}
                    GROUP BY state
                    ORDER BY registeredusers
                    LIMIT 10;'''

        cursor.execute(query2)
        table_2= cursor.fetchall()
        connection.commit()

        df_2= pd.DataFrame(table_2, columns=("state", "registeredusers"))

        with col2:

            fig_amount_2= px.bar(df_2, x="state", y="registeredusers", title="LAST 10 REGISTERED USERS", hover_name= "state",
                                color_discrete_sequence=px.colors.sequential.Aggrnyl_r, height= 650,width= 600)
            st.plotly_chart(fig_amount_2)

        #plot_3
        query3= f'''SELECT state, AVG(registeredusers) AS registeredusers
                    FROM {table_name}
                    GROUP BY state
                    ORDER BY registeredusers;'''

        cursor.execute(query3)
        table_3= cursor.fetchall()
        connection.commit()

        df_3= pd.DataFrame(table_3, columns=("state", "registeredusers"))

        fig_amount_3= px.bar(df_3, y="state", x="registeredusers", title="AVERAGE OF REGISTERED USERS", hover_name= "state", orientation= "h",
                            color_discrete_sequence=px.colors.sequential.Bluered_r, height= 800,width= 1000)
        st.plotly_chart(fig_amount_3)
    
#PLOTLY
class plotly:

    def geo_map(data, locations_column, color_column, title, title_x=0.5, title_y=0.93):
        min_value = data[color_column].min()
        max_value = data[color_column].max()
        fig = px.choropleth_mapbox(
            data,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations=locations_column,
            color=color_column,
            hover_name="State",
            mapbox_style="carto-positron",
            center={"lat": 24, "lon": 79},
            color_continuous_scale=px.colors.diverging.PuOr,
            color_continuous_midpoint=0,
            zoom=3.6,
            range_color=(min_value, max_value),  
            title=title,
            width=800, 
            height=800
        )
        fig.update_geos(fitbounds='locations', visible=False)
        fig.update_layout(
            title=title,
            title_x=title_x,
            title_y=title_y,
            title_font=dict(size=24)
        )
        fig.update_layout(coloraxis_colorbar=dict(title=' ', showticklabels=True),title={
        'font': {'size': 24}
                            },hoverlabel_font={'size': 18})
        st.plotly_chart(fig, use_container_width=True)


    
#Data_Insights TAB
with Data_Insights: 
    col1, col2, col3 =st.columns([1,0.2,3])
    with col1:
        custom_styles = {
                        "container": {"padding": "0!important", "background-color": "#f0f0f0"},
                        "icon": {"color": "violet", "font-size": "12px"},
                        "nav-link": {"font-size": "13px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "blue"},
                    }         
        option=option_menu("Data Insights",
                                options=["Insurance Analysis","Transaction Analysis", "User Analysis", "Top Charts"],
                                menu_icon='bar-chart',
                                icons=['umbrella', 'toggles', 'circle', 'trophy'],
                                default_index=1,
                                styles=custom_styles)

    with col3:
        #Insurance Analysis:
        if option=="Insurance Analysis":
            st.write("")
            select = st.radio(
                    "Select Analysis Type",
                    ["Premium Count", "Premium Amount"], horizontal = True,
                    format_func=lambda option: "Premium Count" if option == "Premium Count" else "Premium Amount"
                )
            st.write("")
            st.write("")
            if select == "Premium Count":
                analysis = st.selectbox(
                        'Select Analysis',
                        ['Select one', 'State-wise Insurance Analysis', 'Year-wise Insurance Analysis', 'Quarter-wise Insurance Analysis']
                    )
                if analysis != 'Select one':
                    st.write(f'You selected {analysis}')

            elif select == "Premium Amount":
                analysis = st.selectbox(
                        'Select Analysis',
                        ['Select one', 'State-wise Insurance Amount Analysis', 'Year-wise Insurance Amount Analysis', 'Quarter-wise Insurance Amount Analysis']
                    )
                if analysis != 'Select one':
                        st.write(f'You selected {analysis}')

        #Transaction Analysis:
        elif option=="Transaction Analysis":
            st.write("")
            select = st.radio(
                    "Select Analysis Type",
                    ["Transaction Count", "Transaction Amount"], horizontal = True,
                    format_func=lambda option: "Transaction Count" if option == "Transaction Count" else "Transaction Amount"
                )
            st.write("")
            st.write("")
            if select == "Transaction Count":
                analysis = st.selectbox(
                    'Select Analysis',
                    ['Select one', 'State-wise Transaction Count Analysis', 'Year-wise Transaction Count Analysis', 'Quarter-wise Transaction Count Analysis', 'Transaction_Typewise Transaction Count Analysis']
                )
                if analysis != 'Select one':
                    st.write(f'You selected {analysis}')

            elif select == "Transaction Amount":
                analysis = st.selectbox(
                    'Select Analysis',
                    ['Select one', 'State-wise Transaction Amount Analysis', 'Year-wise Transaction Amount Analysis', 'Quarter-wise Transaction Amount Analysis', 'Transaction_Typewise Transaction Amount Analysis']
                )
                if analysis != 'Select one':
                    st.write(f'You selected {analysis}')
        
        elif option=="User Analysis":
            st.write("")
            st.write("")
            st.write("")
            analysis = st.selectbox(
                    'Select Analysis',
                    ['Select one', 'State-wise User Analysis', 'Year-wise User Analysis', 'Quarter-wise User Analysis', 'UsersByBrand']
                )
            if analysis != 'Select one':
                    st.write(f'You selected {analysis}')

        #Top Charts
        elif option=="Top Charts":
            button_style = """
                    <style>
                        .stButton > button {
                            background-color: lightblue;
                            color: black;  /* Optional: Set text color */
                            font-weight: bold;  /* Optional: Set font weight */
                        }
                    </style>
                """

            st.markdown(button_style, unsafe_allow_html=True)
            st.button("All India")
            question= st.selectbox("Select the Question",[
                "1. What is the average premium amount for insurance transactions on PhonePe, and how does it compare across different quarters?",
                "2. Which transaction category accounts for the highest number of transactions on PhonePe?",
                "3. Which states contribute the most to transaction volumes on PhonePe in terms of total transaction amount?",
                "4. What are the top 10 districts by transaction amount within each state on PhonePe?",
                "5. Which are the top 10 pincode areas that generate the highest transaction amounts on PhonePe?",
                "6. What is the average transaction amount and how does it vary across different transaction types on PhonePe?",
                "7. What is the trend in total transaction volume on PhonePe over the past year?", 
                "8. Which brands have the highest user count on PhonePe?",
                "9. What is the distribution of transaction amounts for different types of transactions on PhonePe?",
                "10. Which regions or cities exhibit the highest growth rate in terms of new users on PhonePe?"])
                                                                     
            
 #INSURANCE ANALYSIS          
    #Display part(Insurance Analysis-State-wise-Insurance Analysis)
    if option=="Insurance Analysis" and select=="Premium Count" and analysis=="State-wise Insurance Analysis":
        button_style = """
                <style>
                    .stButton > button {
                        background-color: lightblue;
                        color: black;  /* Optional: Set text color */
                        font-weight: bold;  /* Optional: Set font weight */
                    }
                </style>
            """

        st.markdown(button_style, unsafe_allow_html=True)
        st.button("All India")
        col1,col2=st.columns([4,2])
        with col1:  
            state_wise_premium_count = aggregated_insurance.state_wise_premium_count()
            fig1=px.bar(state_wise_premium_count, x='State', y='Premium Count', title=f"State-wise Insurance Policies", color_discrete_sequence=px.colors.sequential.YlGnBu_r)
            fig1.update_layout(width=600, height=700)
            st.plotly_chart(fig1)
        with col2: 
            st.title(":blue[Insurance]")
            st.markdown(f'<p style="font-size: 16px; font-weight: bold;">All India Insurance Policies Purchased (Nos.)</p>', unsafe_allow_html=True)
            df=pd.DataFrame()
            df['State']=state_wise_premium_count['State']
            df['Premium Count']=state_wise_premium_count['Premium Count']
            total_premium= df['Premium Count'].sum()
            formatted_total_premium = "{:,}".format(total_premium)
            st.markdown(f'<p style="font-size: 24px; color: blue; font-weight: bold;">{formatted_total_premium}</p>', unsafe_allow_html=True)
            sorted_df = df.sort_values(by='Premium Count', ascending=False)
            sorted_df.reset_index(drop=True, inplace=True)
            sorted_df.index += 1
            top_10_states = sorted_df.head(10)
            st.write("<h3 style='text-align: center;'>Top 10 States by Premium Count</h3>", unsafe_allow_html=True)
            st.dataframe(top_10_states)
        
        st.write("")
        df = aggregated_insurance.state_wise_premium_count()
        plotly.geo_map(df, 'State','Premium Count', 'Geo Insights of State wise Premium Count')
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            advanced_filters = st.checkbox(':blue[ADVANCED SEARCH]')
            
            st.write("")
        if advanced_filters:
                col1, col2, col3 = st.columns(3)
                with col1:
                    select_state=st.selectbox('Select State: ', state.ins_state_list())
                with col2:
                    year_list = ['Select One']
                    year_list.extend(state.ins_year_list())
                    select_year = st.selectbox('Select Year:             ', year_list)
                with col3:
                    select_quarter = st.selectbox(
                        'Select Quarter: ', ['Select One', '1', '2', '3', '4'])
                st.write('')

        if advanced_filters:
            #CASE 1
            if  select_state and select_year == 'Select One' and select_quarter == 'Select One':
                col1, col2 = st.columns(2)
                        
                selectstate_year_wise_premium_count = aggregated_insurance.selectstate_year_wise_premium_count(select_state)
                selectstate_quarter_wise_premium_count = aggregated_insurance.selectstate_quarter_wise_premium_count(select_state)
                selectstate_year_quarter_wise_premium_count = aggregated_insurance.selectstate_year_quarter_wise_premium_count(select_state)

                with col1:
                    fig_line = px.line(selectstate_year_wise_premium_count, x='Year', y='Premium Count', title=f'{select_state}: Premium Distribution by Year')
                    fig_line.update_layout(width=450, height=400)
                    st.plotly_chart(fig_line)
                with col2:
                    fig_pie = px.pie(selectstate_quarter_wise_premium_count, values='Premium Count',names='Quarter', title=f'{select_state}: Premium Distribution by Quarter')
                    fig_pie.update_layout(width=450, height=400)
                    st.plotly_chart(fig_pie)
                    
                col1, col2 = st.columns(2)
                with col1:
                    fig_bar_grouped = px.bar(selectstate_year_quarter_wise_premium_count, 
                            x='Quarter', y='Premium Count', 
                            color='Year', barmode='group',
                            title=f'{select_state}: Premium Distribution by Year & Quarter')
                    fig_bar_grouped.update_layout(width=500, height=450)
                    st.plotly_chart(fig_bar_grouped)
                
                with col2:
                    st.write("")
                    df=pd.DataFrame()
                    df=aggregated_insurance.selectstate_year_wise_premium_count(select_state)
                    result=df['Premium Count'].sum()
                    st.markdown(f'<p style="font-size: 16px;  font-weight: bold; ">Total Premium  for {select_state} :</p>', unsafe_allow_html=True)
                    st.markdown(f'<p style="font-size: 20px; color: blue; font-weight: bold;">Rs.{result}</p>', unsafe_allow_html=True)
                    st.write("")
                    st.markdown(f'<p style="font-size: 16px; font-weight: bold; text-align: center;">Top 10 Postal Codes by Premium Counts for {select_state}</p>', unsafe_allow_html=True)
                    df=top_insurance.selectstate_pincodewise_top10_insurance(select_state)
                    df['State']=df['State'].str.title()
                    columns_to_display = ['State', 'District', 'Pincode', 'Premium Count']
                    st.dataframe(df[columns_to_display])


            #CASE 2                                    
            if  select_state and select_year != 'Select One' and select_quarter == 'Select One':
                col1,col2=st.columns(2)
                with col1:
                    selectstate_selectyear_quarter_wise_premium_count = aggregated_insurance.selectstate_selectyear_quarter_wise_premium_count(select_state, select_year)
                    fig_pie = px.pie(selectstate_selectyear_quarter_wise_premium_count, values='Premium Count', names='Quarter',
                                                title=f'{select_state}: Premium Distribution by Quarter for {select_year}')
                    fig_pie.update_layout(width=400, height=400)
                    st.plotly_chart(fig_pie)
                with col2:
                    st.write("")
                    st.markdown(f'<p style="font-size: 16px; font-weight: bold; text-align: center;">Top 10 Postal Codes by Premium Counts for {select_state} - {select_year}</p>', unsafe_allow_html=True)
                    df=top_insurance.selectstate_selectyear_pincodewise_top10_insurance(select_state, select_year)
                    df['State']=df['State'].str.title()
                    columns_to_display = ['State', 'Year', 'District', 'Pincode', 'Premium Count']
                    st.dataframe(df[columns_to_display])


            #CASE 3
            if  select_state and select_year == 'Select One' and select_quarter != 'Select One':
                col1,col2=st.columns(2)
                with col1:
                    selectstate_selectquarter_year_wise_premium_count = aggregated_insurance.selectstate_selectquarter_year_wise_premium_count(select_state, select_quarter)
                    fig_pie = px.pie(selectstate_selectquarter_year_wise_premium_count, values='Premium Count', names='Year',
                                                title=f'{select_state}: Premium Distribution by Year for Quarter{select_quarter}')
                    fig_pie.update_layout(width=400, height=400)
                    st.plotly_chart(fig_pie)
                with col2:
                    st.write("")
                    st.markdown(f'<p style="font-size: 16px; font-weight: bold; text-align: center;">Top 10 Postal Codes by Premium Counts for {select_state} - Quarter{select_quarter}</p>', unsafe_allow_html=True)
                    df=top_insurance.selectstate_selectquarter_pincodewise_top10_insurance(select_state, select_quarter)
                    df['State']=df['State'].str.title()
                    columns_to_display = ['State', 'Quarter', 'District', 'Pincode', 'Premium Count']
                    st.dataframe(df[columns_to_display])

            
            #CASE 4
            if  select_state and select_year != 'Select One' and select_quarter != 'Select One':
                col1,col2=st.columns(2)
                with col1:
                    st.write("")
                    st.markdown(f'<p style="font-size: 16px; font-weight: bold; text-align: center;">Premium Count for  {select_state} - {select_year} - Q{select_quarter}</p>', unsafe_allow_html=True)
                    selectstate_selectyear_quarter_wise_premium_count = aggregated_insurance.selectstate_selectyear_quarter_wise_premium_count(select_state, select_year)
                    df= pd.DataFrame(selectstate_selectyear_quarter_wise_premium_count)
                    df['State']=df['State'].str.title()
                    result=df[df['Quarter']==select_quarter]
                    st.write(result)
                with col2:
                    st.write("")
                    st.markdown(f'<p style="font-size: 16px; font-weight: bold; text-align: center;">Top 10 Postal Codes by Premium Counts for {select_state} -{select_year} - Quarter {select_quarter}</p>', unsafe_allow_html=True)
                    df=top_insurance.selectstate_selectyear_selectquarter_pincodewise_top10_insurance(select_state, select_year,select_quarter)
                    df['State']=df['State'].str.title()
                    columns_to_display = ['State', 'Year', 'Quarter', 'District', 'Pincode', 'Premium Count']
                    st.dataframe(df[columns_to_display])

    #Display part(Insurance Analysis-State-wise-Premium Amount)
    if option=="Insurance Analysis" and select=="Premium Amount" and analysis=="State-wise Insurance Amount Analysis":
        button_style = """
                <style>
                    .stButton > button {
                        background-color: lightblue;
                        color: black;  /* Optional: Set text color */
                        font-weight: bold;  /* Optional: Set font weight */
                    }
                </style>
            """

        st.markdown(button_style, unsafe_allow_html=True)
        st.button("All India")
        col1,col2=st.columns([4,2])
        with col1:  
            state_wise_premium_amount = aggregated_insurance.state_wise_premium_amount()
            fig1=px.bar(state_wise_premium_amount, x='State', y='Premium Amount', title=f"State-wise Insurance Policies", color_discrete_sequence=px.colors.sequential.YlGnBu_r)
            fig1.update_layout(width=600, height=700)
            st.plotly_chart(fig1)
        with col2: 
            st.title(":blue[Insurance]")
            df=pd.DataFrame()
            df['State']=state_wise_premium_amount['State']
            df['Premium Amount']=state_wise_premium_amount['Premium Amount']
            total_premium= df['Premium Amount'].sum()
            formatted_total_premium = "{:,}".format(total_premium)
            st.markdown(f'<p style="font-size: 20px;  font-weight: bold;">Total Premium Value: ₹{formatted_total_premium}</p>', unsafe_allow_html=True)
            avg_premium= df['Premium Amount'].mean()
            formatted_avg_premium = "{:,.2f}".format(avg_premium)
            st.markdown(f'<p style="font-size: 20px; font-weight: bold;">Average Premium Value: ₹{formatted_avg_premium}</p>', unsafe_allow_html=True)
            sorted_df = df.sort_values(by='Premium Amount', ascending=False)
            sorted_df.reset_index(drop=True, inplace=True)
            sorted_df.index += 1
            top_10_states = sorted_df.head(10)
            st.write("<h3 style='text-align: center;'>Top 10 States by Policy Amount</h3>", unsafe_allow_html=True)
            st.dataframe(top_10_states)
        
        st.write("")
        state_wise_premium_amount = aggregated_insurance.state_wise_premium_amount()
        plotly.geo_map(state_wise_premium_amount, 'State',
                    'Premium Amount', 'Geo Insights of State wise Premium Amount')
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            advanced_filters = st.checkbox(':blue[ADVANCED SEARCH]')
            
            st.write("")
        if advanced_filters:
                col1, col2, col3 = st.columns(3)  
                with col1:
                    select_state=st.selectbox('Select State: ', state.ins_state_list())              
                with col2:
                    year_list = ['Select One']
                    year_list.extend(state.ins_year_list())
                    select_year = st.selectbox('Select Year:             ', year_list)
                with col3:
                    select_quarter = st.selectbox(
                        'Select Quarter: ', ['Select One', '1', '2', '3', '4'])
                st.write('')

        if advanced_filters:
            
            #CASE 1
            if  select_state and select_year == 'Select One' and select_quarter == 'Select One':
                col1, col2 = st.columns(2)
                        
                selectstate_year_wise_premium_amount = aggregated_insurance.selectstate_year_wise_premium_amount(select_state)
                selectstate_quarter_wise_premium_amount = aggregated_insurance.selectstate_quarter_wise_premium_amount(select_state)
                selectstate_year_quarter_wise_premium_amount = aggregated_insurance.selectstate_year_quarter_wise_premium_amount(select_state)

                with col1:
                    fig_line = px.line(selectstate_year_wise_premium_amount, x='Year', y='Premium Amount', title=f'{select_state}: Premium Amount Distribution by Year')
                    fig_line.update_layout(width=450, height=400)
                    st.plotly_chart(fig_line)
                with col2:
                    fig_pie = px.pie(selectstate_quarter_wise_premium_amount, values='Premium Amount',names='Quarter', title=f'{select_state}: Premium Amount Distribution by Quarter')
                    fig_pie.update_layout(width=500, height=400)
                    st.plotly_chart(fig_pie)
                    
                col1, col2 = st.columns(2)
                with col1:
                    fig_bar_grouped = px.bar(selectstate_year_quarter_wise_premium_amount, 
                            x='Quarter', y='Premium Amount', 
                            color='Year', barmode='group',
                            title=f'{select_state}: Premium Amount Distribution by Year & Quarter')
                    fig_bar_grouped.update_layout(width=450, height=450)
                    st.plotly_chart(fig_bar_grouped)
                
                with col2:
                    st.write("")
                    df=pd.DataFrame()
                    df=aggregated_insurance.selectstate_year_wise_premium_amount(select_state)
                    result=df['Premium Amount'].sum()
                    st.markdown(f'<p style="font-size: 16px; font-weight: bold;">Total Premium Value for {select_state} :</p>', unsafe_allow_html=True)
                    st.write(f"₹{result}")
                    df=top_insurance.selectstate_pincodewise_top10_premium_amount(select_state)
                    st.markdown(f'<p style="font-size: 16px; font-weight: bold; text-align: center;">Top 10 Postal Codes by Premium Value for {select_state}</p>', unsafe_allow_html=True)
                    df=top_insurance.selectstate_pincodewise_top10_premium_amount(select_state)
                    df['State']=df['State'].str.title()
                    columns_to_display = ['State', 'District', 'Pincode', 'Premium Amount']
                    st.dataframe(df[columns_to_display])


            #CASE 2                                    
            if  select_year != 'Select One' and select_quarter == 'Select One':
                col1,col2=st.columns(2)
                with col1:
                    selectstate_selectyear_quarter_wise_premium_amount = aggregated_insurance.selectstate_selectyear_quarter_wise_premium_amount(select_state, select_year)
                    fig_pie = px.pie(selectstate_selectyear_quarter_wise_premium_amount, values='Premium Amount', names='Quarter',
                                                title=f'{select_state}: Premium Value Distribution by Quarter for {select_year}')
                    fig_pie.update_layout(width=400, height=400)
                    st.plotly_chart(fig_pie)
                with col2:
                    st.write("")
                    st.markdown(f'<p style="font-size: 16px; font-weight: bold; text-align: center;">Top 10 Postal Codes by Premium Value for {select_state} - {select_year}</p>', unsafe_allow_html=True)
                    df=top_insurance.selectstate_selectyear_pincodewise_top10_premium_amount(select_state, select_year)
                    df['State']=df['State'].str.title()
                    columns_to_display = ['State', 'Year', 'District', 'Pincode', 'Premium Amount']
                    st.dataframe(df[columns_to_display])


            #CASE 3
            if  select_year == 'Select One' and select_quarter != 'Select One':
                col1,col2=st.columns(2)
                with col1:
                    selectstate_selectquarter_year_wise_premium_amount = aggregated_insurance.selectstate_selectquarter_year_wise_premium_amount(select_state, select_quarter)
                    fig_pie = px.pie(selectstate_selectquarter_year_wise_premium_amount, values='Premium Amount', names='Year',
                                                title=f'{select_state}: Premium Distribution by Year for Quarter{select_quarter}')
                    fig_pie.update_layout(width=400, height=400)
                    st.plotly_chart(fig_pie)
                with col2:
                    st.write("")
                    st.markdown(f'<p style="font-size: 16px; font-weight: bold; text-align: center;">Top 10 Postal Codes by Premium value for {select_state} - Quarter{select_quarter}</p>', unsafe_allow_html=True)
                    df=top_insurance.selectstate_selectquarter_pincodewise_top10_premium_amount(select_state, select_quarter)
                    df['State']=df['State'].str.title()
                    columns_to_display = ['State', 'Quarter', 'District', 'Pincode', 'Premium Amount']
                    st.dataframe(df[columns_to_display])

            
            #CASE 4
            if  select_state and select_year != 'Select One' and select_quarter != 'Select One':
                col1,col2=st.columns(2)
                with col1:
                    st.write("")
                    st.markdown(f"Premium Amount for {select_state}-{select_year}-Quarter {select_quarter}")
                    selectstate_selectyear_quarter_wise_premium_amount = aggregated_insurance.selectstate_selectyear_quarter_wise_premium_amount(select_state, select_year)
                    df= pd.DataFrame(selectstate_selectyear_quarter_wise_premium_amount)
                    df['State']=df['State'].str.title()
                    result=df[df['Quarter']==select_quarter]
                    st.write(result)
                with col2:
                    st.write("")
                    st.markdown(f'<p style="font-size: 16px; font-weight: bold; text-align: center;">Top 10 Postal Codes by Premium value for {select_state} -{select_year} Quarter{select_quarter}</p>', unsafe_allow_html=True)
                    df=top_insurance.selectstate_selectyear_selectquarter_pincodewise_top10_premium_amount(select_state, select_year,select_quarter)
                    df['State']=df['State'].str.title()
                    columns_to_display = ['State', 'Year', 'Quarter', 'District', 'Pincode', 'Premium Amount']
                    st.dataframe(df[columns_to_display])
  
    #Display part(Insurance Analysis-Year-wise-Premium Count)
    if option=="Insurance Analysis" and select=="Premium Count" and analysis=="Year-wise Insurance Analysis":
        button_style = """
                <style>
                    .stButton > button {
                        background-color: lightblue;
                        color: black;  /* Optional: Set text color */
                        font-weight: bold;  /* Optional: Set font weight */
                    }
                </style>
            """

        st.markdown(button_style, unsafe_allow_html=True)
        st.button("All India")
        col1,col2=st.columns(2)
        with col1:
            year_wise_premium_count = aggregated_insurance.year_wise_premium_count()
            fig1=px.bar(year_wise_premium_count, x=['2020','2021','2022','2023'], y='Premium Count', title=f"Year-wise Premium Count details", color_discrete_sequence=px.colors.sequential.Plasma)
            fig1.update_xaxes(title_text='Year')
            fig1.update_layout(width=450, height=400)
            x_values = year_wise_premium_count['Year'].astype(float)  
            y_values = year_wise_premium_count['Premium Count'].astype(float)
            m, b = np.polyfit(x_values, y_values, 1)  
            trend_line = m * x_values + b
            fig1.add_trace(go.Scatter(x=x_values, y=trend_line, mode='lines', name='Trend Line'))
            fig1.update_layout(showlegend=True)
            st.plotly_chart(fig1)
        with col2:
            year_quarter_wise_premium_count = aggregated_insurance.year_quarter_wise_premium_count()
            Quarter=year_quarter_wise_premium_count['Quarter'].unique().tolist()
            fig2 = px.bar(year_quarter_wise_premium_count, x='Quarter', y='Premium Count', color='Year',
                                           barmode='group', title='Year - Quarter wise Premium Count (Grouped Bar)')
            fig2.update_layout(xaxis_title='Quarter', yaxis_title='Premium Count')
            fig2.update_layout(width=500, height=400)
            st.plotly_chart(fig2)

        
        with col1:
            select_year=st.slider("Select a Year", 2020, 2023, 2020)
            df=aggregated_insurance.selectyear_state_wise_premium_count(select_year)
            plotly.geo_map(df, 'State','Premium Count', f'Geo Insights for the year {select_year} State wise Premium Count')            

        
            
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            advanced_filters = st.checkbox(':blue[ADVANCED SEARCH]')
            
            st.write("")
        if advanced_filters:
                col1, col2, col3 = st.columns(3)
                with col1:
                    year_list = ['Select One']
                    year_list.extend(state.ins_year_list())
                    select_year = st.selectbox('Select Year:             ', year_list)
                with col3:
                    select_quarter = st.selectbox(
                        'Select Quarter: ', ['Select One', '1', '2', '3', '4'])
                st.write('')

        if advanced_filters:
            #CASE 1
            if  select_year != 'Select One'and select_quarter == 'Select One':
                col1, col2 = st.columns([4,2])
                        
                selectyear_state_wise_premium_count = aggregated_insurance.selectyear_state_wise_premium_count(select_year)
                selectyear_quarter_wise_premium_count = aggregated_insurance.selectyear_quarter_wise_premium_count(select_year)
                
                with col1:
                    fig1=px.bar(selectyear_state_wise_premium_count, x='State', y='Premium Count', title=f"State-wise Premium Count for the year - {select_year}", color_discrete_sequence=px.colors.sequential.Sunsetdark_r)
                    fig1.update_layout(width=700, height=600)
                    st.plotly_chart(fig1)
                with col2:
                    st.title(":blue[Insurance]")
                    df=aggregated_insurance.year_wise_premium_count()
                    result=df[df['Year']==select_year]
                    filtered_result = result.iloc[0]['Premium Count']  
                    st.markdown(f'<p style="font-size: 16px; font-weight: bold;">All India Insurance Policies Purchased for the year - {select_year} (Nos.)</p>', unsafe_allow_html=True)
                    st.markdown(f'<p style="font-size: 20px; color: blue; font-weight: bold;">Rs.{filtered_result}</p>', unsafe_allow_html=True)
                  
                    st.write("")
                    fig_pie = px.pie(selectyear_quarter_wise_premium_count, values='Premium Count',names='Quarter', title=f'{select_year}: Premium Distribution by Quarter')
                    fig_pie.update_layout(width=400, height=400)
                    st.plotly_chart(fig_pie)
                    

                    
                col1, col2, col3= st.columns([1.5,2,1])
                with col1:
                    st.write("")
                    st.markdown(f'<p style="font-size: 16px; font-weight: bold;">Top 10 States by Premium Count for {select_year}</p>', unsafe_allow_html=True)
                    df= aggregated_insurance.selectyear_state_wise_premium_count(select_year)
                    df['State']=df['State'].str.title()
                    columns_to_display = ['State','Premium Count']
                    st.dataframe(df[columns_to_display])
                    
                
                with col2:
                    st.write("")
                    st.markdown(f'<p style="font-size: 16px; font-weight: bold; text-align: center;">Top 10 Postal Codes by Premium Counts for {select_year}</p>', unsafe_allow_html=True)
                    df=top_insurance.selectyear_pincodewise_top10_insurance(select_year)
                    columns_to_display = ['Pincode', 'Premium Count', 'District and State']
                    st.dataframe(df[columns_to_display])
                                  
                with col3:
                    st.write("")
                    st.markdown(f'<p style="font-size: 16px; font-weight: bold; text-align: center;">Top 10 Districts </p>', unsafe_allow_html=True)
                    df=map_insurance.selectyear_district_wise_premium_count(select_year)
                    df['District']=df['District'].str.title()
                    columns_to_display = ['District']
                    st.dataframe(df[columns_to_display])


            #CASE 2      
            elif  select_year != 'Select One' and select_quarter != 'Select One':
                col1,col2=st.columns([4,1.5])
                with col1:
                    df=aggregated_insurance.selectyear_selectquarter_state_wise_premium_count(select_year, select_quarter)    
                    fig = px.bar(
                                    df,   x='State',
                                    y='Premium Count',
                                    color='Quarter',  
                                    title=f'Statewise Premium Count for Q{select_quarter}-{select_year}',
                                    labels={'State': 'State', 'Premium Count': 'Premium Count', 'Quarter': 'Quarter'}
                                )
                    fig.update_layout(width=750, height=600)
                    st.plotly_chart(fig)
                    
                with col2:
                    st.write("")
                    custom_styles = {
                        "container": {"padding": "0!important", "background-color": "#9dc5e4"},
                        "icon": {"color": "red", "font-size": "12px"},
                        "nav-link": {"font-size": "10px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "green"},
                    }         
                    option=option_menu("Top 10",
                                options=["States","Districts", "Pincodes"],
                                menu_icon='trophy',
                                default_index=0, orientation='horizontal',
                                styles=custom_styles)
                    if option== 'States':         
                        
                        df= aggregated_insurance.selectyear_selectquarter_state_wise_premium_count(select_year, select_quarter)
                        df['State']=df['State'].str.title()
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['State','Premium Count']
                        st.dataframe(df[columns_to_display].head(10))
                        

                    elif option== 'Districts':         
                        
                        df= map_insurance.selectyear_selectquarter_district_wise_premium_count(select_year, select_quarter)
                        df['District']=df['District'].str.title()
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['District']
                        st.dataframe(df[columns_to_display].head(10))

                    elif option== 'Pincodes':         
                        
                        df= top_insurance.selectyear_selectquarter_pincodewise_top10_insurance(select_year, select_quarter)
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['Pincode', 'Premium Count']
                        st.dataframe(df[columns_to_display].head(10))

    #Display part(Insurance Analysis-Year-wise-Premium Amount)
    if option=="Insurance Analysis" and select=="Premium Amount" and analysis=="Year-wise Insurance Amount Analysis":
        button_style = """
                <style>
                    .stButton > button {
                        background-color: lightblue;
                        color: black;  /* Optional: Set text color */
                        font-weight: bold;  /* Optional: Set font weight */
                    }
                </style>
            """

        st.markdown(button_style, unsafe_allow_html=True)
        st.button("All India")
        col1,col2=st.columns(2)
        with col1:
            year_wise_premium_amount = aggregated_insurance.year_wise_premium_amount()
            fig1=px.bar(year_wise_premium_amount, x=['2020','2021','2022','2023'], y='Premium Amount', title=f"Year-wise Premium Amount details", color_discrete_sequence=px.colors.sequential.Plasma)
            fig1.update_xaxes(title_text='Year')
            fig1.update_layout(width=450, height=400)
            x_values = year_wise_premium_amount['Year'].astype(float)  
            y_values = year_wise_premium_amount['Premium Amount'].astype(float)
            m, b = np.polyfit(x_values, y_values, 1)  
            trend_line = m * x_values + b
            fig1.add_trace(go.Scatter(x=x_values, y=trend_line, mode='lines', name='Trend Line'))
            fig1.update_layout(showlegend=True)
            st.plotly_chart(fig1)
        with col2:
            year_quarter_wise_premium_amount = aggregated_insurance.year_quarter_wise_premium_amount()
            Quarter=year_quarter_wise_premium_amount['Quarter'].unique().tolist()
            fig2 = px.bar(year_quarter_wise_premium_amount, x='Quarter', y='Premium Amount', color='Year',
                                           barmode='group', title='Year - Quarter wise Premium Amount (Grouped Bar)')
            fig2.update_layout(xaxis_title='Quarter', yaxis_title='Premium Amount')
            fig2.update_layout(width=500, height=400)
            st.plotly_chart(fig2)

        
        with col1:
            select_year=st.slider("Select a Year", 2020, 2023, 2020)
            df=aggregated_insurance.selectyear_state_wise_premium_amount(select_year)
            plotly.geo_map(df, 'State','Premium Amount', f'Geo Insights for the year {select_year} State wise Premium Amount')            

        
            
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            advanced_filters = st.checkbox(':blue[ADVANCED SEARCH]')
            
            st.write("")
        if advanced_filters:
                col1, col2, col3 = st.columns(3)
                with col1:
                    year_list = ['Select One']
                    year_list.extend(state.ins_year_list())
                    select_year = st.selectbox('Select Year:             ', year_list)
                with col3:
                    select_quarter = st.selectbox(
                        'Select Quarter: ', ['Select One', '1', '2', '3', '4'])
                st.write('')

        if advanced_filters:
            #CASE 1
            if  select_year != 'Select One'and select_quarter == 'Select One':
                col1, col2 = st.columns([4,2])
                        
                selectyear_state_wise_premium_amount = aggregated_insurance.selectyear_state_wise_premium_amount(select_year)
                selectyear_quarter_wise_premium_amount = aggregated_insurance.selectyear_quarter_wise_premium_amount(select_year)
                
                with col1:
                    fig1=px.bar(selectyear_state_wise_premium_amount, x='State', y='Premium Amount', title=f"State-wise Premium Amount for the year - {select_year}", color_discrete_sequence=px.colors.sequential.Sunsetdark_r)
                    fig1.update_layout(width=700, height=600)
                    st.plotly_chart(fig1)
                with col2:
                    st.title(":blue[Insurance]")
                    df=aggregated_insurance.year_wise_premium_amount()
                    result=df[df['Year']==select_year]
                    filtered_result = result.iloc[0]['Premium Amount']  
                    st.markdown(f'<p style="font-size: 16px; font-weight: bold;">All India Insurance Premium Value for the year - {select_year} (Nos.)</p>', unsafe_allow_html=True)
                    st.markdown(f'<p style="font-size: 20px; color: blue; font-weight: bold;">Rs.{filtered_result}</p>', unsafe_allow_html=True)
                  
                    st.write("")
                    fig_pie = px.pie(selectyear_quarter_wise_premium_amount, values='Premium Amount',names='Quarter', title=f'{select_year}: Premium Value Distribution by Quarter')
                    fig_pie.update_layout(width=400, height=400)
                    st.plotly_chart(fig_pie)
                    

                    
                col1, col2, col3= st.columns([1.5,2,1])
                with col1:
                    st.write("")
                    st.markdown(f'<p style="font-size: 16px; font-weight: bold;">Top 10 States by Premium Amount for {select_year}</p>', unsafe_allow_html=True)
                    df= aggregated_insurance.selectyear_state_wise_premium_amount(select_year)
                    df['State']=df['State'].str.title()
                    columns_to_display = ['State','Premium Amount']
                    st.dataframe(df[columns_to_display])
                    
                
                with col2:
                    st.write("")
                    st.markdown(f'<p style="font-size: 16px; font-weight: bold; text-align: center;">Top 10 Postal Codes </p>', unsafe_allow_html=True)
                    df=top_insurance.selectyear_pincodewise_top10_premium_amount(select_year)
                    columns_to_display = ['Pincode', 'Premium Amount']
                    st.dataframe(df[columns_to_display])
                                  
                with col3:
                    st.write("")
                    st.markdown(f'<p style="font-size: 16px; font-weight: bold; text-align: center;">Top 10 Districts </p>', unsafe_allow_html=True)
                    df=map_insurance.selectyear_district_wise_premium_amount(select_year)
                    df['District']=df['District'].str.title()
                    columns_to_display = ['District']
                    st.dataframe(df[columns_to_display])


            #CASE 2      
            elif  select_year != 'Select One' and select_quarter != 'Select One':
                col1,col2=st.columns([3,1.2])
                with col1:
                    df=aggregated_insurance.selectyear_selectquarter_state_wise_premium_amount(select_year, select_quarter)    
                    fig = px.bar(
                                    df,   x='State',
                                    y='Premium Amount',
                                    color='Quarter',  
                                    title=f'Statewise Premium Amount for Q{select_quarter}-{select_year}',
                                    labels={'State': 'State', 'PremiumAmount': 'Premium Amount', 'Quarter': 'Quarter'}
                                )
                    fig.update_layout(width=700, height=600)
                    st.plotly_chart(fig)
                    
                with col2:
                    st.write("")
                    custom_styles = {
                        "container": {"padding": "0!important", "background-color": "#9dc5e4"},
                        "icon": {"color": "red", "font-size": "12px"},
                        "nav-link": {"font-size": "10px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "green"},
                    }         
                    option=option_menu("Top 10",
                                options=["States","Districts", "Pincodes"],
                                menu_icon='trophy',
                                default_index=0, orientation='horizontal',
                                styles=custom_styles)
                    if option== 'States':         
                        
                        df= aggregated_insurance.selectyear_selectquarter_state_wise_premium_amount(select_year, select_quarter)
                        df['State']=df['State'].str.title()
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['State','Premium Amount']
                        st.dataframe(df[columns_to_display].head(10))
                        

                    elif option== 'Districts':         
                        
                        df= map_insurance.selectyear_selectquarter_district_wise_premium_amount(select_year, select_quarter)
                        df['District']=df['District'].str.title()
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['District']
                        st.dataframe(df[columns_to_display].head(10))

                    elif option== 'Pincodes':         
                        
                        df= top_insurance.selectyear_selectquarter_pincodewise_top10_insurance(select_year, select_quarter)
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['Pincode', 'Premium Amount']
                        st.dataframe(df[columns_to_display].head(10))
      
    #Display part(Insurance Analysis-Quarter-wise-Premium Count)
    if option=="Insurance Analysis" and select=="Premium Count" and analysis=="Quarter-wise Insurance Analysis":
        button_style = """
                <style>
                    .stButton > button {
                        background-color: lightblue;
                        color: black;  /* Optional: Set text color */
                        font-weight: bold;  /* Optional: Set font weight */
                    }
                </style>
            """

        st.markdown(button_style, unsafe_allow_html=True)
        st.button("All India")
        col1,col2=st.columns([3,2])
        with col1:
            year_quarter_wise_premium_count = aggregated_insurance.year_quarter_wise_premium_count()
            fig1=px.bar(year_quarter_wise_premium_count, x='Quarter', y='Premium Count',
                                            title='Quarter-wise Premium Count Details',
                                            color='Year',  
                                            color_continuous_scale='Viridis')
            fig1.update_layout(width=600, height=400)
            st.plotly_chart(fig1)
        with col2:                        
            year_quarter_wise_premium_count = aggregated_insurance.year_quarter_wise_premium_count()
            Quarter=year_quarter_wise_premium_count['Quarter'].unique().tolist()
            fig2=px.line(year_quarter_wise_premium_count, x='Quarter', y='Premium Count',
                                    color='Year', title='Year - Quarter wise Premium Count')
            fig2.update_layout(width=400, height=400)
            st.plotly_chart(fig2)

        col1,col2=st.columns([2,3])
        with col1:
            select_quarter=st.slider("Select a Quarter", 1, 4, 1)
        df=aggregated_insurance.selectquarter_state_wise_premium_count(select_quarter)
        plotly.geo_map(df, 'State','Premium Count', f'Geo Insights for the Quarter{select_quarter} - Premium Count')
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            advanced_filters = st.checkbox(':blue[ADVANCED SEARCH]')
            
            st.write("")
        if advanced_filters:
                col1, col2, col3 = st.columns(3)
                with col1:
                    select_quarter = st.selectbox(
                        'Select Quarter: ', ['Select One', '1', '2', '3', '4'])
                
                with col3:
                    year_list = ['Select One']
                    year_list.extend(state.ins_year_list())
                    select_year = st.selectbox('Select Year:             ', year_list)
                st.write('')

        if advanced_filters:
            #CASE 1
            if  select_quarter != 'Select One' and select_year == 'Select One':
                col1, col2 = st.columns([4,2])
                        
                df = aggregated_insurance.selectquarter_year_wise_premium_count(select_quarter)
                               
                with col1:
                    fig1=px.bar(df, x=df['Year'].unique().astype(str), y='Premium Count', title=f"Year-wise Premium Count for the Quarter - {select_quarter}", color_discrete_sequence=px.colors.sequential.Sunsetdark_r)
                    fig1.update_layout(width=400, height=450, xaxis=dict(title='Year'))
                    x_values = np.array(df['Year']).astype(float)
                    y_values = np.array(df['Premium Count']).astype(float)
                    m, b = np.polyfit(x_values, y_values, 1)  
                    trend_line = m * x_values + b
                    fig1.add_trace(go.Scatter(x=x_values, y=trend_line, mode='lines', name='Trend Line'))
                    fig1.update_layout(showlegend=True)
                    st.plotly_chart(fig1)

                with col2:
                    st.write(f"Quarter {select_quarter}")
                    custom_styles = {
                        "container": {"padding": "0!important", "background-color": "#9dc5e4"},
                        "icon": {"color": "red", "font-size": "12px"},
                        "nav-link": {"font-size": "10px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "green"},
                    }         
                    option=option_menu("Top 10",
                                options=["States","Districts", "Pincodes"],
                                menu_icon='trophy',
                                default_index=0, orientation='horizontal',
                                styles=custom_styles)
                    if option== 'States':         
                        
                        df= aggregated_insurance.selectquarter_state_wise_premium_count(select_quarter)
                        df['State']=df['State'].str.title()
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['State','Premium Count']
                        st.dataframe(df[columns_to_display].head(10))
                        

                    elif option== 'Districts':         
                        
                        df= map_insurance.selectquarter_district_wise_premium_count(select_quarter)
                        df['District']=df['District'].str.title()
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['District']
                        st.dataframe(df[columns_to_display].head(10))

                    elif option== 'Pincodes':         
                        
                        df= top_insurance.selectquarter_pincodewise_top10_insurance(select_quarter)
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['Pincode', 'Premium Count']
                        st.dataframe(df[columns_to_display].head(10))

            #CASE 2
            if  select_quarter != 'Select One' and select_year != 'Select One':
                col1,col2=st.columns([4,1.5])
                with col1:
                    df=aggregated_insurance.selectyear_selectquarter_state_wise_premium_count(select_year, select_quarter)    
                    fig = px.bar(
                                    df,   x='State',
                                    y='Premium Count',
                                    color='Quarter',  
                                    title=f'Statewise Premium Count for Q{select_quarter}-{select_year}',
                                    labels={'State': 'State', 'Premium Count': 'Premium Count', 'Quarter': 'Quarter'}
                                )
                    fig.update_layout(width=750, height=600)
                    st.plotly_chart(fig)
                    
                with col2:
                    st.write("")
                    custom_styles = {
                        "container": {"padding": "0!important", "background-color": "#9dc5e4"},
                        "icon": {"color": "red", "font-size": "12px"},
                        "nav-link": {"font-size": "10px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "green"},
                    }         
                    option=option_menu("Top 10",
                                options=["States","Districts", "Pincodes"],
                                menu_icon='trophy',
                                default_index=0, orientation='horizontal',
                                styles=custom_styles)
                    if option== 'States':         
                        
                        df= aggregated_insurance.selectyear_selectquarter_state_wise_premium_count(select_year, select_quarter)
                        df['State']=df['State'].str.title()
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['State','Premium Count']
                        st.dataframe(df[columns_to_display].head(10))
                        

                    elif option== 'Districts':         
                        
                        df= map_insurance.selectyear_selectquarter_district_wise_premium_count(select_year, select_quarter)
                        df['District']=df['District'].str.title()
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['District']
                        st.dataframe(df[columns_to_display].head(10))

                    elif option== 'Pincodes':         
                        
                        df= top_insurance.selectyear_selectquarter_pincodewise_top10_insurance(select_year, select_quarter)
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['Pincode', 'Premium Count']
                        st.dataframe(df[columns_to_display].head(10))

    #Display part(Insurance Analysis-Quarter-wise-Premium Amount)
    if option=="Insurance Analysis" and select=="Premium Amount" and analysis=="Quarter-wise Insurance Amount Analysis":
        button_style = """
                <style>
                    .stButton > button {
                        background-color: lightblue;
                        color: black;  /* Optional: Set text color */
                        font-weight: bold;  /* Optional: Set font weight */
                    }
                </style>
            """

        st.markdown(button_style, unsafe_allow_html=True)
        st.button("All India")
        col1,col2=st.columns([3,2])
        with col1:
            year_quarter_wise_premium_amount = aggregated_insurance.year_quarter_wise_premium_amount()
            fig1=px.bar(year_quarter_wise_premium_amount, x='Quarter', y='Premium Amount',
                                            title='Quarter-wise Premium Amount Details',
                                            color='Year',  
                                            color_continuous_scale='Viridis')
            fig1.update_layout(width=600, height=400)
            st.plotly_chart(fig1)
        with col2:                        
            year_quarter_wise_premium_amount = aggregated_insurance.year_quarter_wise_premium_amount()
            Quarter=year_quarter_wise_premium_amount['Quarter'].unique().tolist()
            fig2=px.line(year_quarter_wise_premium_amount, x='Quarter', y='Premium Amount',
                                    color='Year', title='Year - Quarter wise Premium Amount')
            fig2.update_layout(width=400, height=400)
            st.plotly_chart(fig2)

        col1,col2=st.columns([2,3])
        with col1:
            select_quarter=st.slider("Select a Quarter", 1, 4, 1)
        df=aggregated_insurance.selectquarter_state_wise_premium_amount(select_quarter)
        plotly.geo_map(df, 'State','Premium Amount', f'Geo Insights for the Quarter{select_quarter} - Premium Amount')
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            advanced_filters = st.checkbox(':blue[ADVANCED SEARCH]')
            
            st.write("")
        if advanced_filters:
                col1, col2, col3 = st.columns(3)
                with col1:
                    select_quarter = st.selectbox(
                        'Select Quarter: ', ['Select One', '1', '2', '3', '4'])
                
                with col3:
                    year_list = ['Select One']
                    year_list.extend(state.ins_year_list())
                    select_year = st.selectbox('Select Year:             ', year_list)
                st.write('')

        if advanced_filters:
            #CASE 1
            if  select_quarter != 'Select One' and select_year == 'Select One':
                col1, col2 = st.columns([4,2])
                        
                df = aggregated_insurance.selectquarter_year_wise_premium_amount(select_quarter)
                               
                with col1:
                    fig1=px.bar(df, x=df['Year'].unique().astype(str), y='Premium Amount', title=f"Year-wise Premium Amount for the Quarter - {select_quarter}", color_discrete_sequence=px.colors.sequential.Sunsetdark_r)
                    fig1.update_layout(width=400, height=450, xaxis=dict(title='Year'))
                    x_values = np.array(df['Year']).astype(float)
                    y_values = np.array(df['Premium Amount']).astype(float)
                    m, b = np.polyfit(x_values, y_values, 1)  
                    trend_line = m * x_values + b
                    fig1.add_trace(go.Scatter(x=x_values, y=trend_line, mode='lines', name='Trend Line'))
                    fig1.update_layout(showlegend=True)
                    st.plotly_chart(fig1)

                with col2:
                    st.write(f"Quarter {select_quarter}")
                    custom_styles = {
                        "container": {"padding": "0!important", "background-color": "#9dc5e4"},
                        "icon": {"color": "red", "font-size": "12px"},
                        "nav-link": {"font-size": "10px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "green"},
                    }         
                    option=option_menu("Top 10",
                                options=["States","Districts", "Pincodes"],
                                menu_icon='trophy',
                                default_index=0, orientation='horizontal',
                                styles=custom_styles)
                    if option== 'States':         
                        
                        df= aggregated_insurance.selectquarter_state_wise_premium_amount(select_quarter)
                        df['State']=df['State'].str.title()
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['State','Premium Amount']
                        st.dataframe(df[columns_to_display].head(10))
                        

                    elif option== 'Districts':         
                        
                        df= map_insurance.selectquarter_district_wise_premium_amount(select_quarter)
                        df['District']=df['District'].str.title()
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['District']
                        st.dataframe(df[columns_to_display].head(10))

                    elif option== 'Pincodes':         
                        
                        df= top_insurance.selectquarter_pincodewise_top10_premium_amount(select_quarter)
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['Pincode', 'Premium Amount']
                        st.dataframe(df[columns_to_display].head(10))

            #CASE 2
            if  select_quarter != 'Select One' and select_year != 'Select One':
                col1,col2=st.columns([4,1.5])
                with col1:
                    df=aggregated_insurance.selectyear_selectquarter_state_wise_premium_amount(select_year, select_quarter)    
                    fig = px.bar(
                                    df,   x='State',
                                    y='Premium Amount',
                                    color='Quarter',  
                                    title=f'Statewise Premium Amount for Q{select_quarter}-{select_year}',
                                    labels={'State': 'State', 'Premium Amount': 'Premium Amount', 'Quarter': 'Quarter'}
                                )
                    fig.update_layout(width=750, height=600)
                    st.plotly_chart(fig)
                    
                with col2:
                    st.write("")
                    custom_styles = {
                        "container": {"padding": "0!important", "background-color": "#9dc5e4"},
                        "icon": {"color": "red", "font-size": "12px"},
                        "nav-link": {"font-size": "10px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "green"},
                    }         
                    option=option_menu("Top 10",
                                options=["States","Districts", "Pincodes"],
                                menu_icon='trophy',
                                default_index=0, orientation='horizontal',
                                styles=custom_styles)
                    if option== 'States':         
                        
                        df= aggregated_insurance.selectyear_selectquarter_state_wise_premium_amount(select_year, select_quarter)
                        df['State']=df['State'].str.title()
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['State','Premium Amount']
                        st.dataframe(df[columns_to_display].head(10))
                        

                    elif option== 'Districts':         
                        
                        df= map_insurance.selectyear_selectquarter_district_wise_premium_amount(select_year, select_quarter)
                        df['District']=df['District'].str.title()
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['District']
                        st.dataframe(df[columns_to_display].head(10))

                    elif option== 'Pincodes':         
                        
                        df= top_insurance.selectyear_selectquarter_pincodewise_top10_premium_amount(select_year, select_quarter)
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['Pincode', 'Premium Amount']
                        st.dataframe(df[columns_to_display].head(10))


#TRANSACTION ANALYSIS              
    #Display part(Transaction Analysis-State-wise-Transaction Count)
    if option=="Transaction Analysis" and select=="Transaction Count" and analysis=="State-wise Transaction Count Analysis":
        button_style = """
                <style>
                    .stButton > button {
                        background-color: lightblue;
                        color: black;  /* Optional: Set text color */
                        font-weight: bold;  /* Optional: Set font weight */
                    }
                </style>
            """

        st.markdown(button_style, unsafe_allow_html=True)
        st.button("All India")
        st.title(":blue[Transaction]")
        df=aggregated_transaction.state_wise_transaction_count()
        result=df['Transaction Count'].sum()
        formatted_result = "{:,}".format(result)                    
        st.markdown(    f'<div style="text-align: center;">'
                        f'<p style="font-size: 24px; font-weight: bold;">All PhonePe transactions (UPI + Cards + Wallets) :</p>'
                        f'<p style="font-size: 22px; color: blue; font-weight: bold;">{formatted_result}</p>'
                        f'</div>',
                        unsafe_allow_html=True
                    )
        st.write("")
        col1,col2=st.columns([4,2])
        with col1:  
            state_wise_transaction_count = aggregated_transaction.state_wise_transaction_count()
            fig1=px.bar(state_wise_transaction_count, x='State', y='Transaction Count', title=f"All India - State-wise Transaction Count details",
                          color_discrete_sequence=px.colors.sequential.YlOrRd_r)
            fig1.update_layout(width=600, height=700)
            st.plotly_chart(fig1)
        with col2: 

            custom_styles = {
                "container": {"padding": "0!important", "background-color": "#9dc5e4"},
                "icon": {"color": "red", "font-size": "12px"},
                "nav-link": {"font-size": "10px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "green"},
            }         
            option=option_menu("Top 10 Tranasctions",
                        options=["States","Districts", "Pincodes"],
                        menu_icon='trophy',
                        default_index=0, orientation='horizontal',
                        styles=custom_styles)
            if option== 'States':      
                df = aggregated_transaction.state_wise_transaction_count()
                df.reset_index(drop=True, inplace=True)
                df.index += 1
                top_10_states = df.head(10)
                st.dataframe(top_10_states)

            elif option== 'Districts':         
                df= map_transaction.district_wise_top10_transaction_count()
                df['District']=df['District'].str.title()
                df['State']=df['State'].str.title()
                df.reset_index(drop=True, inplace=True)
                df.index+=1
                columns_to_display = ['District', 'State']
                st.dataframe(df[columns_to_display].head(10))

            elif option== 'Pincodes':         
                df= top_transaction.pincodewise_top10_transaction_count()
                df.reset_index(drop=True, inplace=True)
                df.index+=1
                columns_to_display = ['Pincode', 'District and State']
                st.dataframe(df[columns_to_display].head(10))
           
        
        st.write("")
        state_wise_transaction_count = aggregated_transaction.state_wise_transaction_count()
        plotly.geo_map(state_wise_transaction_count, 'State',
                    'Transaction Count', 'Geo Insights of State wise Transaction Count')
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            state_list=['Select One']
            state_list.extend(state.ins_state_list())
            select_state=st.selectbox('Select State:       ', state_list)
        
        
        #CASE 1
        if  select_state != 'Select One':            
            df1=aggregated_transaction.selectstate_year_wise_transaction_count(select_state)
            df2=aggregated_transaction.selectstate_quarter_wise_transaction_count(select_state)
            df3=aggregated_transaction.selectstate_type_wise_transaction_count(select_state)
            df4=aggregated_transaction.selectstate_year_quarter_wise_transaction_count(select_state)
            df5=aggregated_transaction.selectstate_year_type_wise_transaction_count(select_state)
            df6=aggregated_transaction.selectstate_quarter_type_wise_transaction_count(select_state)   
            st.write("")
            df=pd.DataFrame(df5)
            result=df['Transaction Count'].sum()
            formatted_result = "{:,}".format(result) 
            st.markdown(    f'<div style="text-align: center;">'
                            f'<p style="font-size: 24px; font-weight: bold;">Total Transaction of State - {select_state} :</p>'
                            f'<p style="font-size: 22px; color: blue; font-weight: bold;">{formatted_result}</p>'
                            f'</div>',
                            unsafe_allow_html=True
                        )

            col1, col2,col3 = st.columns(3)
            with col1:
                fig_line = px.line(df1, x='Year', y='Transaction Count', title=f'Transaction Distribution by Year')
                fig_line.update_layout(width=450, height=400)
                st.plotly_chart(fig_line)
            with col2:
                fig_pie = px.pie(df2, values='Transaction Count',names='Quarter', title=f'Transaction Distribution by Quarter')
                fig_pie.update_layout(width=450, height=400)
                st.plotly_chart(fig_pie)
            with col3:
                fig_bar_grouped = px.bar(df4, 
                        x='Quarter', y='Transaction Count', 
                        color='Year', barmode='group',
                        title=f'Transaction Distribution by Year & Quarter')
                fig_bar_grouped.update_layout(width=450, height=400)
                st.plotly_chart(fig_bar_grouped)
                
                
            col1, col2, col3= st.columns(3)
            with col1:
                fig1 = px.bar(df3,
                                x='Transaction Type', 
                                y='Transaction Count',   
                                text='Transaction Count',  
                                color='Transaction Type',  
                                color_discrete_sequence=px.colors.qualitative.Pastel,                                 
                                title='Type-wise Transaction Count')          
                fig1.update_xaxes(title='Transaction Type')
                fig1.update_layout(width=500, height=500)
                st.plotly_chart(fig1)
                
                
            with col2:
                fig_bar_grouped = px.bar(df5, 
                        x='Transaction Type', y='Transaction Count', 
                        color='Year', barmode='group',
                        title=f'Transaction Distribution by Year & Transaction Type')
                fig_bar_grouped.update_layout(width=450, height=500)
                st.plotly_chart(fig_bar_grouped)

            with col3:
                fig_bar_grouped = px.bar(df6, 
                        x='Transaction Type', y='Transaction Count', 
                        color='Quarter', barmode='group',
                        title=f'Transaction Distribution by Quarter & Transaction Type')
                fig_bar_grouped.update_layout(width=450, height=500)
                st.plotly_chart(fig_bar_grouped)

            
                
                
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                advanced_filters = st.checkbox(':blue[ADVANCED SEARCH]')
                
            
            if advanced_filters:
                col1, col2, col3 = st.columns(3)
                with col1:
                    year_list = ['Select One']
                    year_list.extend(state.ins_year_list())
                    select_year = st.selectbox('Select Year:             ', year_list)
                with col2:
                    select_quarter = st.selectbox(
                        'Select Quarter: ', ['Select One', '1', '2', '3', '4'])
                with col3:
                    type_list = ['Select One']
                    type_list.extend(state.type_list())
                    select_type = st.selectbox('Select Type:             ', type_list)
                    
                st.write('')
            
                #CASE 2                                    
                if  select_state != 'Select One' and select_year != 'Select One' and select_quarter == 'Select One' and select_type == 'Select One':

                    col1,col2, col3=st.columns([2,1,2])
                    with col1:
                        st.title(f'{select_state}')
                        df1=aggregated_transaction.selectstate_selectyear_quarter_type_wise_transaction_count(select_state,select_year)
                        fig_1 = px.bar(df1, x='Transaction Type', y='Transaction Count',  color='Quarter', barmode='group', 
                                         title=f'Transaction Distribution by Quarter & Transaction Types - {select_year}',
                                                    color_discrete_sequence=px.colors.qualitative.Set1_r)
                        fig_1.update_layout(width=700, height=600)
                        st.plotly_chart(fig_1)
                    with col3:
                        st.write("")
                        st.write("")
                        st.write("")
                        st.write("")
                        custom_styles = {
                        "container": {"padding": "0!important", "background-color": "#9dc5e4"},
                        "icon": {"color": "red", "font-size": "12px"},
                        "nav-link": {"font-size": "10px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "green"},
                        }         
                        option=option_menu(f"{select_state}-({select_year}): Top 10",
                                    options=["Districts", "Pincodes"],
                                    menu_icon='trophy',
                                    default_index=0, orientation='horizontal',
                                    styles=custom_styles)
                    

                        if option== 'Districts':         
                            df= map_transaction.selectstate_selectyear_district_wise_transaction_count(select_state, select_year)
                            df['District']=df['District'].str.title()
                            df.reset_index(drop=True, inplace=True)
                            df.index+=1
                            columns_to_display = ['District', 'Transaction Count']
                            st.dataframe(df[columns_to_display].head(10))
                        elif option== 'Pincodes':      
                            df= top_transaction.selectstate_selectyear_pincode_wise_transaction_count(select_state, select_year)
                            df.reset_index(drop=True, inplace=True)
                            df.index+=1
                            columns_to_display = ['Pincode',  'District and State']
                            st.dataframe(df[columns_to_display].head(10))

                    col1,col2=st.columns(2)
                    with col1:
                        df1=aggregated_transaction.selectstate_selectyear_quarter_wise_transaction_count(select_state,select_year)
                        fig_pie = px.pie(df1, values='Transaction Count', names='Quarter',
                                                    title=f'{select_state}: Transaction Distribution by Quarter - {select_year}',
                                                    color_discrete_sequence=px.colors.qualitative.G10_r)
                        fig_pie.update_layout(width=500, height=500)
                        st.plotly_chart(fig_pie)
                    with col2:
                        df2=aggregated_transaction.selectstate_selectyear_type_wise_transaction_count(select_state,select_year)
                        fig_pie = px.pie(df2, values='Transaction Count', names='Transaction Type',
                                                    title=f'{select_state}: Transaction Distribution by Types - {select_year}',
                                                    color_discrete_sequence=px.colors.qualitative.Pastel)
                        fig_pie.update_layout(width=500, height=500)
                        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
                        st.plotly_chart(fig_pie)


                #CASE 3
                if  select_state != 'Select One' and select_year == 'Select One' and select_quarter != 'Select One' and select_type=='Select One':
                    col1,col2,col3=st.columns([2,0.2,2.5])
                    with col1:
                        df1 = aggregated_transaction.selectstate_selectquarter_year_wise_transaction_count(select_state, select_quarter)
                        fig_pie = px.pie(df1, values='Transaction Count', names='Year',
                                                    title=f'{select_state}: Transaction Distribution by Year - Quarter{select_quarter}',
                                                    color_discrete_sequence=px.colors.qualitative.Pastel)
                        fig_pie.update_layout(width=500, height=500)
                        st.plotly_chart(fig_pie)
                    with col3:
                        df2=aggregated_transaction.selectstate_selectquarter_type_wise_transaction_count(select_state,select_quarter)
                        fig_pie = px.pie(df2, values='Transaction Count', names='Transaction Type',
                                                    title=f'{select_state}: Transaction Distribution by Transaction Types - Quarter{select_quarter}',
                                                    color_discrete_sequence=px.colors.qualitative.T10_r)
                        fig_pie.update_layout(width=700, height=500)
                        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
                        st.plotly_chart(fig_pie)
                    col1,col2, col3=st.columns([2,1,2])
                    with col1:
                        df1=aggregated_transaction.selectstate_selectquarter_year_type_wise_transaction_count(select_state,select_quarter)
                        fig_2 = px.bar(df1, x='Transaction Type', y='Transaction Count', color='Year', 
                                        barmode='stack', title='Transaction Distribution by Transaction Types & Year',
                                        color_discrete_sequence=px.colors.qualitative.Vivid_r)
                        fig_2.update_layout(width=700, height=600)
                        st.plotly_chart(fig_2)

                    with col3:
                        st.write("")
                        st.write("")
                        st.write("")
                        custom_styles = {
                        "container": {"padding": "0!important", "background-color": "#9dc5e4"},
                        "icon": {"color": "red", "font-size": "12px"},
                        "nav-link": {"font-size": "10px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "green"},
                        }         
                        option=option_menu(f"{select_state}-Q{select_quarter}: Top 10",
                                    options=["Districts", "Pincodes"],
                                    menu_icon='trophy',
                                    default_index=0, orientation='horizontal',
                                    styles=custom_styles)
                    

                        if option== 'Districts':         
                            df= map_transaction.selectstate_selectquarter_district_wise_transaction_count(select_state, select_quarter)
                            df['District']=df['District'].str.title()
                            df.reset_index(drop=True, inplace=True)
                            df.index+=1
                            columns_to_display = ['District', 'State']
                            st.dataframe(df[columns_to_display].head(10))
                        elif option== 'Pincodes':      
                            df= top_transaction.selectstate_selectquarter_pincodewise_top10_transaction_count(select_state, select_quarter)
                            df.reset_index(drop=True, inplace=True)
                            df.index+=1
                            columns_to_display = ['Pincode', 'District and State']
                            st.dataframe(df[columns_to_display].head(10))
                        
                
                #CASE 4
                if  select_state != 'Select One' and select_year == 'Select One' and select_quarter == 'Select One' and select_type !='Select One':
                    col1,col2=st.columns(2)
                    with col1:
                        df1 = aggregated_transaction.selectstate_selecttype_year_wise_transaction_count(select_state, select_type)
                        fig_pie = px.pie(df1, values='Transaction Count', names='Year',
                                                    title=f'{select_state}: Transaction Distribution by Year{select_type}',
                                                    color_discrete_sequence=px.colors.qualitative.Pastel)
                        fig_pie.update_layout(width=500, height=500)
                        st.plotly_chart(fig_pie)
                    with col2:
                        df2=aggregated_transaction.selectstate_selecttype_quarter_wise_transaction_count(select_state,select_type)
                        fig_pie = px.pie(df2, values='Transaction Count', names='Quarter',
                                                    title=f'{select_state}: Transaction Distribution by Quarter- Type: {select_type}',
                                                    color_discrete_sequence=px.colors.qualitative.T10_r)
                        fig_pie.update_layout(width=500, height=500)
                        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
                        st.plotly_chart(fig_pie)
                    col1,col2  =st.columns(2)
                    with col1:
                        df1=aggregated_transaction.selectstate_selecttype_year_quarter_wise_transaction_count(select_state,select_type)
                        fig_2 = px.bar(df1, x='Quarter', y='Transaction Count', color='Year', 
                                        barmode='stack', title='Transaction Distribution by Year & Quarter',
                                        color_discrete_sequence=px.colors.qualitative.Pastel2_r)
                        fig_2.update_layout(width=500, height=400)
                        st.plotly_chart(fig_2)
                    with col2:
                        fig_line = px.line(df1, x='Quarter', y='Transaction Count', color='Year', 
                                        line_group='Year', title='Transaction Trends by Quarter and Year',
                                        color_discrete_sequence=px.colors.qualitative.Pastel2_r)
                        fig_line.update_layout(width=500, height=400)
                        st.plotly_chart(fig_line)

                    

                #CASE 5
                if  select_state != 'Select One' and select_year != 'Select One' and select_quarter != 'Select One' and select_type =='Select One':
                    col1,col2,col3=st.columns([2,0.2,1])
                    with col1:
                        df1 = aggregated_transaction.selectstate_selectyear_selectquarter_type_wise_transaction_count(select_state, 
                                                                                                                      select_year, select_quarter)
                        fig_bar = px.bar(df1, x='Transaction Count', y='Transaction Type',
                                                    title=f'{select_state}: Transaction Distribution by Types',orientation='h',
                                                    color_discrete_sequence=px.colors.qualitative.Pastel)
                        fig_bar.update_layout(width=700, height=500)
                        st.plotly_chart(fig_bar)
                    with col3:
                        st.write("")
                        st.write("")
                        st.write("")
                        custom_styles = {
                        "container": {"padding": "0!important", "background-color": "#9dc5e4"},
                        "icon": {"color": "red", "font-size": "12px"},
                        "nav-link": {"font-size": "10px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "green"},
                        }         
                        option=option_menu(f"{select_state}-{select_year}-Q{select_quarter}: Top 10",
                                    options=["Districts", "Pincodes"],
                                    menu_icon='trophy',
                                    default_index=0, orientation='horizontal',
                                    styles=custom_styles)                

                        if option== 'Districts':         
                            df= map_transaction.selectstate_selectyear_selectquarter_district_wise_transaction_count(select_state, select_year, select_quarter)
                            df['District']=df['District'].str.title()
                            df.reset_index(drop=True, inplace=True)
                            df.index+=1
                            columns_to_display = ['District', 'State']
                            st.dataframe(df[columns_to_display].head(10))
                        elif option== 'Pincodes':      
                            df= top_transaction.selectstate_selectyear_selectquarter_pincodewise_top10_transaction_count(select_state, select_year, select_quarter)
                            df.reset_index(drop=True, inplace=True)
                            df.index+=1
                            columns_to_display = ['Pincode', 'District and State']
                            st.dataframe(df[columns_to_display].head(10))
                #CASE 6
                if  select_state != 'Select One' and select_year != 'Select One' and select_quarter == 'Select One' and select_type !='Select One':
                    col1,col2=st.columns([3,1.2])
                    with col1:
                        df1 = aggregated_transaction.selectstate_selectyear_selecttype_quarter_wise_transaction_count(select_state, 
                                                                                                                      select_year, select_type)
                        fig_bar = px.bar(df1, x='Transaction Count', y='Quarter',
                                                    title=f'{select_state}: Transaction Distribution by Quarter({select_type})',orientation='h',
                                                    color_discrete_sequence=px.colors.qualitative.D3_r)
                        fig_bar.update_layout(width=500, height=300)
                        st.plotly_chart(fig_bar)
                    with col2:
                        st.write("")
                        st.markdown(f'{select_state}-{select_year}: {select_type}')
                        df=df1.copy()
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['Quarter', 'Transaction Count']
                        st.dataframe(df[columns_to_display].head(10))


                #CASE 7
                if  select_state != 'Select One' and select_year == 'Select One' and select_quarter != 'Select One' and select_type !='Select One':
                    col1,col2=st.columns([3,1.2])
                    with col1:
                        df1 = aggregated_transaction.selectstate_selectquarter_selecttype_year_wise_transaction_count(select_state, 
                                                                                                                      select_quarter, select_type)
                        fig_bar = px.bar(df1, x='Transaction Count', y='Year',
                                                    title=f'{select_state}: Transaction Distribution by Year)',orientation='h',
                                                    color_discrete_sequence=px.colors.qualitative.Dark24)
                        fig_bar.update_layout(width=700, height=400)
                        st.plotly_chart(fig_bar)
                    with col2:
                        st.write("")
                        st.write("")
                        st.markdown(f'{select_state}-Quarter{select_quarter}: {select_type}')
                        df=df1.copy()
                        df['Year'] = df['Year'].astype(str)
                        df['Year']=df['Year'].str.replace(",", "")
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['Year', 'Transaction']
                        st.dataframe(df[columns_to_display].head(10))


                #CASE 8
                if  select_state != 'Select One' and select_year != 'Select One' and select_quarter != 'Select One' and select_type !='Select One':
                    col1,col2=st.columns([3,1.2])
                    with col1:
                        df1 = aggregated_transaction.selectstate_selectyear_selectquarter_selecttype_wise_transaction_count(select_state,select_year, select_quarter, select_type)
                        result=df1['Transaction Count'].sum()
                        st.subheader("Total Transaction")
                        st.markdown(f'State:{select_state} - {select_year}-Q{select_quarter} ({select_type}): {result}')                                                                                           
         
    #Display part(Transaction Analysis-State-wise-Transaction Amount)
    if option=="Transaction Analysis" and select=="Transaction Amount" and analysis=="State-wise Transaction Amount Analysis": 
        button_style = """
                <style>
                    .stButton > button {
                        background-color: lightblue;
                        color: black;  /* Optional: Set text color */
                        font-weight: bold;  /* Optional: Set font weight */
                    }
                </style>
            """

        st.markdown(button_style, unsafe_allow_html=True)
        st.button("All India")
        st.title(":blue[Transaction]")
        df=aggregated_transaction.state_wise_transaction_amount()
        result1=df['Transaction Amount'].sum()
        formatted_result1 = state.convert(str(result1))  
        st.write(":blue[All PhonePe transactions (UPI + Cards + Wallets)]")
        connection = mysql.connector.connect(
                                        host='localhost',
                                        user='root',
                                        password='Kimch!811',
                                        database='PhonePe_Data'
                                       )
        cursor = connection.cursor()
        cursor.execute(f"""select sum(transaction_amount) as transaction_amount, 
                            sum(transaction_amount)/sum(transaction_count) as avg_transaction  
                            from aggregated_transaction;""")
        s = cursor.fetchall()
        result=s[0]
        result1 = round(result[1], 0)
        formatted_result2 = state.convert(str(int(result1))) 
        col1,col2=st.columns([2,1]) 
        with col1:              
            st.markdown(    #f'<div style="text-align: center;">'
                            f'<p style="font-size: 24px; font-weight: bold;">Total payment value :</p>'
                            f'<p style="font-size: 22px; color: blue; font-weight: bold;">₹{formatted_result1}</p>'
                            f'</div>',
                            unsafe_allow_html=True
                        )
        with col2:
            st.markdown(    #f'<div style="text-align: center;">'
                            f'<p style="font-size: 24px; font-weight: bold;">Avg. transaction value :</p>'
                            f'<p style="font-size: 22px; color: blue; font-weight: bold;">₹{formatted_result2}</p>'
                            f'</div>',
                            unsafe_allow_html=True
                        )
        st.write("")
        col1,col2=st.columns([4,2])
        with col1:  
            df = aggregated_transaction.state_wise_transaction_amount()
            fig1=px.bar(df, x='State', y='Transaction Amount', title=f"All India - State-wise Transaction Amount details",
                          color_discrete_sequence=px.colors.sequential.YlOrRd_r)
            fig1.update_layout(width=600, height=700)
            st.plotly_chart(fig1)
        with col2: 
            st.write("")
            st.write("")
            custom_styles = {
                "container": {"padding": "0!important", "background-color": "#9dc5e4"},
                "icon": {"color": "red", "font-size": "12px"},
                "nav-link": {"font-size": "10px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "green"},
            }         
            option=option_menu("Top 10 Tranasctions",
                        options=["States","Districts", "Pincodes"],
                        menu_icon='trophy',
                        default_index=0, orientation='horizontal',
                        styles=custom_styles)
            if option== 'States':      
                
                df.reset_index(drop=True, inplace=True)
                df.index += 1
                col=['State', 'Transaction Amount', 'Average Transaction']
                st.dataframe(df[col])

            elif option== 'Districts':         
                df= map_transaction.district_wise_top10_transaction_amount()
                df['District']=df['District'].str.title()
                df['State']=df['State'].str.title()
                df.reset_index(drop=True, inplace=True)
                df.index+=1
                columns_to_display = ['District', 'State']
                st.dataframe(df[columns_to_display].head(10))

            elif option== 'Pincodes':         
                df= top_transaction.pincodewise_top10_transaction_amount()
                df.reset_index(drop=True, inplace=True)
                df.index+=1
                columns_to_display = ['Pincode', 'District and State']
                st.dataframe(df[columns_to_display].head(10))
           
        
        st.write("")
        state_wise_transaction_amount = aggregated_transaction.state_wise_transaction_amount()
        plotly.geo_map(state_wise_transaction_amount, 'State',
                    'Transaction Amount', 'Geo Insights of State wise Transaction Amount')
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            state_list=['Select One']
            state_list.extend(state.ins_state_list())
            select_state=st.selectbox('Select State:       ', state_list)
        
        
        #CASE 1
        if  select_state != 'Select One':            
            df1=aggregated_transaction.selectstate_year_wise_transaction_amount(select_state)
            df2=aggregated_transaction.selectstate_quarter_wise_transaction_amount(select_state)
            df3=aggregated_transaction.selectstate_type_wise_transaction_amount(select_state)
            df4=aggregated_transaction.selectstate_year_quarter_wise_transaction_amount(select_state)
            df5=aggregated_transaction.selectstate_year_type_wise_transaction_amount(select_state)
            df6=aggregated_transaction.selectstate_quarter_type_wise_transaction_amount(select_state)   
            st.write("")
            df=pd.DataFrame(df5)
            col1,col2=st.columns([2,1])
            with col1:
                result=df1['Transaction Amount'].sum()
                result2=df1['Average Transaction'].mean()
                formatted_result = state.convert(str(result))
                formatted_result2 = state.convert(str(int(result2)))
                st.markdown(    f'<p style="font-size: 24px; font-weight: bold;">{select_state} Total payment value : :</p>'
                                f'<p style="font-size: 22px; color: blue; font-weight: bold;">₹{formatted_result}</p>'
                                f'</div>',
                                unsafe_allow_html=True
                            )
            with col2:
                st.markdown(    f'<p style="font-size: 24px; font-weight: bold;">{select_state} Avg.payment value :  :</p>'
                                f'<p style="font-size: 22px; color: blue; font-weight: bold;">₹{formatted_result2}</p>'
                                f'</div>',
                                unsafe_allow_html=True
                            )

            col1, col2,col3 = st.columns(3)
            with col1:
                fig_line = px.line(df1, x='Year', y='Transaction Amount', title=f'Transaction Distribution by Year')
                fig_line.update_layout(width=450, height=400)
                st.plotly_chart(fig_line)
            with col2:
                fig_pie = px.pie(df2, values='Transaction Amount',names='Quarter', title=f'Transaction Distribution by Quarter')
                fig_pie.update_layout(width=450, height=400)
                st.plotly_chart(fig_pie)
            with col3:
                fig_bar_grouped = px.bar(df4, 
                        x='Quarter', y='Transaction Amount', 
                        color='Year', barmode='group',
                        title=f'Transaction Distribution by Year & Quarter')
                fig_bar_grouped.update_layout(width=450, height=400)
                st.plotly_chart(fig_bar_grouped)
                
                
            col1, col2, col3= st.columns(3)
            with col1:
                fig1 = px.bar(df3,
                                x='Transaction Type', 
                                y='Transaction Amount',   
                                text='Transaction Amount',  
                                color='Transaction Type',  
                                color_discrete_sequence=px.colors.qualitative.Pastel,                                 
                                title='Type-wise Transaction Amount')          
                fig1.update_xaxes(title='Transaction Type')
                fig1.update_layout(width=500, height=500)
                st.plotly_chart(fig1)
                
                
            with col2:
                fig_bar_grouped = px.bar(df5, 
                        x='Transaction Type', y='Transaction Amount', 
                        color='Year', barmode='group',
                        title=f'Transaction Distribution by Year & Transaction Type')
                fig_bar_grouped.update_layout(width=450, height=500)
                st.plotly_chart(fig_bar_grouped)

            with col3:
                fig_bar_grouped = px.bar(df6, 
                        x='Transaction Type', y='Transaction Amount', 
                        color='Quarter', barmode='group',
                        title=f'Transaction Distribution by Quarter & Transaction Type')
                fig_bar_grouped.update_layout(width=450, height=500)
                st.plotly_chart(fig_bar_grouped)

            
                
                
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                advanced_filters = st.checkbox(':blue[ADVANCED SEARCH]')
                
            
            if advanced_filters:
                col1, col2, col3 = st.columns(3)
                with col1:
                    year_list = ['Select One']
                    year_list.extend(state.ins_year_list())
                    select_year = st.selectbox('Select Year:             ', year_list)
                with col2:
                    select_quarter = st.selectbox(
                        'Select Quarter: ', ['Select One', '1', '2', '3', '4'])
                with col3:
                    type_list = ['Select One']
                    type_list.extend(state.type_list())
                    select_type = st.selectbox('Select Type:             ', type_list)
                    
                st.write('')
            
                #CASE 2                                    
                if  select_state != 'Select One' and select_year != 'Select One' and select_quarter == 'Select One' and select_type == 'Select One':

                    col1,col2, col3=st.columns([2,1,2])
                    with col1:
                        st.title(f'{select_state}')
                        df1=aggregated_transaction.selectstate_selectyear_quarter_type_wise_transaction_amount(select_state,select_year)
                        fig_1 = px.bar(df1, x='Transaction Type', y='Transaction Amount',  color='Quarter', barmode='group', 
                                         title=f'Transaction Distribution by Quarter & Transaction Types - {select_year}',
                                                    color_discrete_sequence=px.colors.qualitative.Set1_r)
                        fig_1.update_layout(width=700, height=600)
                        st.plotly_chart(fig_1)
                    with col3:
                        st.write("")
                        st.write("")
                        st.write("")
                        st.write("")
                        custom_styles = {
                        "container": {"padding": "0!important", "background-color": "#9dc5e4"},
                        "icon": {"color": "red", "font-size": "12px"},
                        "nav-link": {"font-size": "10px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "green"},
                        }         
                        option=option_menu(f"{select_state}-({select_year}): Top 10",
                                    options=["Districts", "Pincodes"],
                                    menu_icon='trophy',
                                    default_index=0, orientation='horizontal',
                                    styles=custom_styles)
                    

                        if option== 'Districts':         
                            df= map_transaction.selectstate_selectyear_district_wise_transaction_amount(select_state, select_year)
                            df['District']=df['District'].str.title()
                            df.reset_index(drop=True, inplace=True)
                            df.index+=1
                            columns_to_display = ['District', 'Transaction Amt']
                            st.dataframe(df[columns_to_display].head(10))
                        elif option== 'Pincodes':      
                            df= top_transaction.selectstate_selectyear_pincode_wise_transaction_amount(select_state, select_year)
                            df.reset_index(drop=True, inplace=True)
                            df.index+=1
                            columns_to_display = ['Pincode',  'District and State']
                            st.dataframe(df[columns_to_display].head(10))

                    col1,col2=st.columns(2)
                    with col1:
                        df1=aggregated_transaction.selectstate_selectyear_quarter_wise_transaction_amount(select_state,select_year)
                        fig_pie = px.pie(df1, values='Transaction Amount', names='Quarter',
                                                    title=f'{select_state}: Transaction Distribution by Quarter - {select_year}',
                                                    color_discrete_sequence=px.colors.qualitative.G10_r)
                        fig_pie.update_layout(width=500, height=500)
                        st.plotly_chart(fig_pie)
                    with col2:
                        df2=aggregated_transaction.selectstate_selectyear_type_wise_transaction_amount(select_state,select_year)
                        fig_pie = px.pie(df2, values='Transaction Amount', names='Transaction Type',
                                                    title=f'{select_state}: Transaction Distribution by Types - {select_year}',
                                                    color_discrete_sequence=px.colors.qualitative.Pastel)
                        fig_pie.update_layout(width=500, height=500)
                        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
                        st.plotly_chart(fig_pie)


                #CASE 3
                if  select_state != 'Select One' and select_year == 'Select One' and select_quarter != 'Select One' and select_type=='Select One':
                    col1,col2,col3=st.columns([2,0.2,2.5])
                    with col1:
                        df1 = aggregated_transaction.selectstate_selectquarter_year_wise_transaction_amount(select_state, select_quarter)
                        fig_pie = px.pie(df1, values='Transaction Amount', names='Year',
                                                    title=f'{select_state}: Transaction Distribution by Year - Quarter{select_quarter}',
                                                    color_discrete_sequence=px.colors.qualitative.Pastel)
                        fig_pie.update_layout(width=500, height=500)
                        st.plotly_chart(fig_pie)
                    with col3:
                        df2=aggregated_transaction.selectstate_selectquarter_type_wise_transaction_amount(select_state,select_quarter)
                        fig_pie = px.pie(df2, values='Transaction Amount', names='Transaction Type',
                                                    title=f'{select_state}: Transaction Distribution by Transaction Types - Quarter{select_quarter}',
                                                    color_discrete_sequence=px.colors.qualitative.T10_r)
                        fig_pie.update_layout(width=700, height=500)
                        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
                        st.plotly_chart(fig_pie)
                    col1,col2, col3=st.columns([2,1,2])
                    with col1:
                        df1=aggregated_transaction.selectstate_selectquarter_year_type_wise_transaction_amount(select_state,select_quarter)
                        fig_2 = px.bar(df1, x='Transaction Type', y='Transaction Amount', color='Year', 
                                        barmode='stack', title='Transaction Distribution by Transaction Types & Year',
                                        color_discrete_sequence=px.colors.qualitative.Vivid_r)
                        fig_2.update_layout(width=700, height=600)
                        st.plotly_chart(fig_2)

                    with col3:
                        st.write("")
                        st.write("")
                        st.write("")
                        custom_styles = {
                        "container": {"padding": "0!important", "background-color": "#9dc5e4"},
                        "icon": {"color": "red", "font-size": "12px"},
                        "nav-link": {"font-size": "10px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "green"},
                        }         
                        option=option_menu(f"{select_state}-Q{select_quarter}: Top 10",
                                    options=["Districts", "Pincodes"],
                                    menu_icon='trophy',
                                    default_index=0, orientation='horizontal',
                                    styles=custom_styles)
                    

                        if option== 'Districts':         
                            df= map_transaction.selectstate_selectquarter_district_wise_transaction_amount(select_state, select_quarter)
                            df['District']=df['District'].str.title()
                            df.reset_index(drop=True, inplace=True)
                            df.index+=1
                            columns_to_display = ['District', 'State']
                            st.dataframe(df[columns_to_display].head(10))
                        elif option== 'Pincodes':      
                            df= top_transaction.selectstate_selectquarter_pincodewise_top10_transaction_amount(select_state, select_quarter)
                            df.reset_index(drop=True, inplace=True)
                            df.index+=1
                            columns_to_display = ['Pincode', 'District and State']
                            st.dataframe(df[columns_to_display].head(10))
                        
                
                #CASE 4
                if  select_state != 'Select One' and select_year == 'Select One' and select_quarter == 'Select One' and select_type !='Select One':
                    col1,col2=st.columns(2)
                    with col1:
                        df1 = aggregated_transaction.selectstate_selecttype_year_wise_transaction_amount(select_state, select_type)
                        fig_pie = px.pie(df1, values='Transaction Amount', names='Year',
                                                    title=f'{select_state}: Transaction Distribution by Year{select_type}',
                                                    color_discrete_sequence=px.colors.qualitative.Pastel)
                        fig_pie.update_layout(width=500, height=500)
                        st.plotly_chart(fig_pie)
                    with col2:
                        df2=aggregated_transaction.selectstate_selecttype_quarter_wise_transaction_amount(select_state,select_type)
                        fig_pie = px.pie(df2, values='Transaction Amount', names='Quarter',
                                                    title=f'{select_state}: Transaction Distribution by Quarter- Type: {select_type}',
                                                    color_discrete_sequence=px.colors.qualitative.T10_r)
                        fig_pie.update_layout(width=500, height=500)
                        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
                        st.plotly_chart(fig_pie)
                    col1,col2  =st.columns(2)
                    with col1:
                        df1=aggregated_transaction.selectstate_selecttype_year_quarter_wise_transaction_amount(select_state,select_type)
                        fig_2 = px.bar(df1, x='Quarter', y='Transaction Amount', color='Year', 
                                        barmode='stack', title='Transaction Distribution by Year & Quarter',
                                        color_discrete_sequence=px.colors.qualitative.Pastel2_r)
                        fig_2.update_layout(width=500, height=400)
                        st.plotly_chart(fig_2)
                    with col2:
                        fig_line = px.line(df1, x='Quarter', y='Transaction Amount', color='Year', 
                                        line_group='Year', title='Transaction Trends by Quarter and Year',
                                        color_discrete_sequence=px.colors.qualitative.Pastel2_r)
                        fig_line.update_layout(width=500, height=400)
                        st.plotly_chart(fig_line)

                    

                #CASE 5
                if  select_state != 'Select One' and select_year != 'Select One' and select_quarter != 'Select One' and select_type =='Select One':
                    col1,col2,col3=st.columns([2,0.2,1])
                    with col1:
                        df1 = aggregated_transaction.selectstate_selectyear_selectquarter_type_wise_transaction_amount(select_state, 
                                                                                                                      select_year, select_quarter)
                        fig_bar = px.bar(df1, x='Transaction Amount', y='Transaction Type',
                                                    title=f'{select_state}: Transaction Distribution by Types',orientation='h',
                                                    color_discrete_sequence=px.colors.qualitative.Pastel)
                        fig_bar.update_layout(width=700, height=500)
                        st.plotly_chart(fig_bar)
                    with col3:
                        st.write("")
                        st.write("")
                        st.write("")
                        custom_styles = {
                        "container": {"padding": "0!important", "background-color": "#9dc5e4"},
                        "icon": {"color": "red", "font-size": "12px"},
                        "nav-link": {"font-size": "10px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "green"},
                        }         
                        option=option_menu(f"{select_state}-{select_year}-Q{select_quarter}: Top 10",
                                    options=["Districts", "Pincodes"],
                                    menu_icon='trophy',
                                    default_index=0, orientation='horizontal',
                                    styles=custom_styles)                

                        if option== 'Districts':         
                            df= map_transaction.selectstate_selectyear_selectquarter_district_wise_transaction_amount(select_state, select_year, select_quarter)
                            df['District']=df['District'].str.title()
                            df.reset_index(drop=True, inplace=True)
                            df.index+=1
                            columns_to_display = ['District', 'State']
                            st.dataframe(df[columns_to_display].head(10))
                        elif option== 'Pincodes':      
                            df= top_transaction.selectstate_selectyear_selectquarter_pincodewise_top10_transaction_amount(select_state, select_year, select_quarter)
                            df.reset_index(drop=True, inplace=True)
                            df.index+=1
                            columns_to_display = ['Pincode', 'District and State']
                            st.dataframe(df[columns_to_display].head(10))

                #CASE 6
                if  select_state != 'Select One' and select_year != 'Select One' and select_quarter == 'Select One' and select_type !='Select One':
                    col1,col2=st.columns([3,1.2])
                    with col1:
                        df1 = aggregated_transaction.selectstate_selectyear_selecttype_quarter_wise_transaction_amount(select_state, 
                                                                                                                      select_year, select_type)
                        fig_bar = px.bar(df1, x='Transaction Amount', y='Quarter',
                                                    title=f'{select_state}: Transaction Distribution by Quarter({select_type})',orientation='h',
                                                    color_discrete_sequence=px.colors.qualitative.D3_r)
                        fig_bar.update_layout(width=500, height=300)
                        st.plotly_chart(fig_bar)
                    with col2:
                        st.write("")
                        st.markdown(f'{select_state}-{select_year}: {select_type}')
                        df=df1.copy()
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['Quarter', 'Transaction Amount']
                        st.dataframe(df[columns_to_display].head(10))


                #CASE 7
                if  select_state != 'Select One' and select_year == 'Select One' and select_quarter != 'Select One' and select_type !='Select One':
                    col1,col2=st.columns([3,1.2])
                    with col1:
                        df1 = aggregated_transaction.selectstate_selectquarter_selecttype_year_wise_transaction_amount(select_state, 
                                                                                                                      select_quarter, select_type)
                        fig_bar = px.bar(df1, x='Transaction Amount', y='Year',
                                                    title=f'{select_state}: Transaction Distribution by Year)',orientation='h',
                                                    color_discrete_sequence=px.colors.qualitative.Dark24)
                        fig_bar.update_layout(width=700, height=400)
                        st.plotly_chart(fig_bar)
                    with col2:
                        st.write("")
                        st.write("")
                        st.markdown(f'{select_state}-Quarter{select_quarter}: {select_type}')
                        df=df1.copy()
                        df['Year'] = df['Year'].astype(str)
                        df['Year']=df['Year'].str.replace(",", "")
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['Year', 'Transaction Amount']
                        st.dataframe(df[columns_to_display].head(10))


                #CASE 8
                if  select_state != 'Select One' and select_year != 'Select One' and select_quarter != 'Select One' and select_type !='Select One':
                    col1,col2=st.columns([3,1.2])
                    with col1:
                        df1 = aggregated_transaction.selectstate_selectyear_selectquarter_selecttype_wise_transaction_amount(select_state,select_year, select_quarter, select_type)
                        result=df1['Transaction Amount'].sum()
                        st.subheader("Total Transaction")
                        st.markdown(f'State:{select_state} - {select_year}-Q{select_quarter} ({select_type}): {result}')                                                                                           
                 
    #Display part(Transaction Analysis-Year-wise-Transaction Count)
    if option=="Transaction Analysis" and select=="Transaction Count" and analysis=="Year-wise Transaction Count Analysis":
        button_style = """
                <style>
                    .stButton > button {
                        background-color: lightblue;
                        color: black;  /* Optional: Set text color */
                        font-weight: bold;  /* Optional: Set font weight */
                    }
                </style>
            """

        st.markdown(button_style, unsafe_allow_html=True)
        st.button("All India")
        col1,col2,col3=st.columns(3)
        with col1:
            df = aggregated_transaction.year_wise_transaction_count()
            fig1=px.bar(df, x=['2018', '2019', '2020', '2021', '2022', '2023'], y='Transaction Count', title=f"Year-wise Transaction Count details", color_discrete_sequence=px.colors.sequential.Plasma)
            fig1.update_xaxes(title='Year')
            fig1.update_layout(width=600, height=400)
            x_values = np.array(df['Year']).astype(float)
            y_values = np.array(df['Transaction Count']).astype(float)
            m, b = np.polyfit(x_values, y_values, 1)  
            trend_line = m * x_values + b
            fig1.add_trace(go.Scatter(x=x_values, y=trend_line, mode='lines', name='Trend Line'))
            fig1.update_layout(showlegend=True)
            fig1.update_layout(width=500, height=400)
            st.plotly_chart(fig1)
        with col2: 
            df2 = aggregated_transaction.year_quarter_wise_transaction_count()
            fig2 = px.bar(df2, x='Transaction Count', y='Year', color='Quarter', orientation='h',
                                           barmode='group', title='Year - Quarter wise Transaction Count (Grouped Bar)')
            fig2.update_layout(width=400, height=400)
            st.plotly_chart(fig2)
        with col3:
            df3 = aggregated_transaction.year_type_wise_transaction_count()
            fig_line = px.line(df3, x='Year', y='Transaction Count', color='Transaction Type', title=f'Transaction Type by Year')
            fig_line.update_layout(width=450, height=400)
            st.plotly_chart(fig_line)
        with col1:
            select_year=st.slider("Select a Year", 2018, 2023, 2020)
        df=aggregated_transaction.selectyear_state_wise_transaction_count(select_year)
        plotly.geo_map(df, 'State','Transaction Count', f'Geo Insights for the year {select_year} State wise Transaction Count')            


        
        col1, col2 = st.columns([4,2])
        
                
        selectyear_state_wise_transaction_count = aggregated_transaction.selectyear_state_wise_transaction_count(select_year)
        selectyear_quarter_wise_transaction_count = aggregated_transaction.selectyear_quarter_wise_transaction_count(select_year)
        
        with col1:
            st.title(f"{select_year}")
            fig1=px.bar(selectyear_state_wise_transaction_count, x='State', y='Transaction Count', title=f"State-wise Transaction Count for the year - {select_year}", color_discrete_sequence=px.colors.sequential.Sunsetdark_r)
            fig1.update_layout(width=700, height=620)
            st.plotly_chart(fig1)
        with col2:
            st.write("")
            st.write("")
            st.title(":blue[Transaction]")
            df=aggregated_transaction.year_wise_transaction_count()
            result=df[df['Year']==select_year]
            filtered_result = result.iloc[0]['Transaction Count']  
            formatted_total_premium = "{:,}".format(filtered_result)
            st.markdown(f'<p style="font-size: 16px; font-weight: bold;">All India transaction Policies Purchased for the year - {select_year} (Nos.)</p>', unsafe_allow_html=True)
            st.markdown(f'<p style="font-size: 20px; color: blue; font-weight: bold;">{formatted_total_premium}</p>', unsafe_allow_html=True)
        with col2:
            st.write("")
            custom_styles = {
                "container": {"padding": "0!important", "background-color": "#9dc5e4"},
                "icon": {"color": "red", "font-size": "12px"},
                "nav-link": {"font-size": "10px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "green"},
            }         
            option=option_menu(f"{select_year} - Top 10",
                        options=["States","Districts", "Pincodes"],
                        menu_icon='trophy',
                        default_index=2, orientation='horizontal',
                        styles=custom_styles)
            if option== 'States':         
                
                df= aggregated_transaction.selectyear_state_wise_transaction_count(select_year)
                df['State']=df['State'].str.title()
                df.reset_index(drop=True, inplace=True)
                df.index+=1
                columns_to_display = ['State','Transaction Count']
                st.dataframe(df[columns_to_display].head(10))
                

            elif option== 'Districts':         
                
                df= map_transaction.selectyear_district_wise_transaction_count(select_year)
                df['District']=df['District'].str.title()
                df.reset_index(drop=True, inplace=True)
                df.index+=1
                columns_to_display = ['District', 'State']
                st.dataframe(df[columns_to_display].head(10))

            elif option== 'Pincodes':         
                
                df= top_transaction.selectyear_pincodewise_top10_transaction_count(select_year)
                df.reset_index(drop=True, inplace=True)
                df.index+=1
                columns_to_display = ['Pincode', 'District and State']
                st.dataframe(df[columns_to_display].head(10))

        col1, col2, col3 = st.columns(3)
        df1=aggregated_transaction.selectyear_quarter_wise_transaction_count(select_year)
        df2=aggregated_transaction.selectyear_type_wise_transaction_count(select_year)
        df3=aggregated_transaction.selectyear_quarter_type_wise_transaction_count(select_year)
        with col1:
            st.write("")
            fig_pie = px.pie(df1, values='Transaction Count',names='Quarter',color_discrete_sequence=px.colors.sequential.amp_r, title=f'{select_year}: Transaction Distribution by Quarter')
            fig_pie.update_layout(width=400, height=400)
            st.plotly_chart(fig_pie)
                        
        with col2:
            st.write("")
            fig_pie = px.pie(df2, values='Transaction Count',names='Transaction Type', title=f'{select_year}: Transaction Distribution by Type',
                                color_discrete_sequence=px.colors.sequential.Agsunset_r)
            fig_pie.update_layout(width=400, height=400)
            st.plotly_chart(fig_pie)
            
        with col3:
            fig1=px.bar(df3, x='Transaction Type', y='Transaction Count', color='Quarter', title=f"Quarter and Type-wise transaction Count for the year - {select_year}", color_discrete_sequence=px.colors.sequential.Sunsetdark_r)
            fig1.update_layout(width=400, height=400)
            st.plotly_chart(fig1)

             
            
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            advanced_filters = st.checkbox(':blue[ADVANCED SEARCH]')
            
            st.write("")
        if advanced_filters:
                col1, col2 = st.columns(2)

                with col1:
                    select_quarter = st.selectbox(
                        'Select Quarter: ', ['Select One', '1', '2', '3', '4'])
                
                with col2:
                    type_list = ['Select One']
                    type_list.extend(state.type_list())
                    select_type = st.selectbox('Select Type:             ', type_list)
                st.write('')

        if advanced_filters:
            #CASE 1
            if  select_quarter != 'Select One' and select_type == 'Select One':
                st.title(f"{select_year} - Q{select_quarter}")
                col1,col2=st.columns([4,1.5])
                with col1:
                    df=aggregated_transaction.selectyear_selectquarter_state_wise_transaction_count(select_year, select_quarter)    
                    fig = px.bar(
                                    df,   x='State',
                                    y='Transaction Count',
                                    color='State',  
                                    title=f'Statewise Transaction Count for Q{select_quarter}-{select_year}',
                                    labels={'State': 'State', 'Transaction Count': 'Transaction Count', 'Quarter': 'Quarter'}
                                )
                    fig.update_layout(width=750, height=600)
                    st.plotly_chart(fig)   
                with col2:
                    st.write("")
                    custom_styles = {
                        "container": {"padding": "0!important", "background-color": "#9dc5e4"},
                        "icon": {"color": "red", "font-size": "12px"},
                        "nav-link": {"font-size": "10px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "green"},
                    }         
                    option=option_menu(f"{select_year} Q{select_quarter}- Top 10",
                                options=["States","Districts", "Pincodes"],
                                menu_icon='trophy',
                                default_index=2, orientation='horizontal',
                                styles=custom_styles)
                    if option== 'States':         
                        
                        df= aggregated_transaction.selectyear_selectquarter_state_wise_transaction_count(select_year, select_quarter)
                        df['State']=df['State'].str.title()
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['State','Transaction Count']
                        st.dataframe(df[columns_to_display].head(10))
                        

                    elif option== 'Districts':         
                        
                        df= map_transaction.selectyear_selectquarter_district_wise_transaction_count(select_year,select_quarter)
                        df['District']=df['District'].str.title()
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['District','State']
                        st.dataframe(df[columns_to_display].head(10))

                    elif option== 'Pincodes':         
                        
                        df= top_transaction.selectyear_selectquarter_pincodewise_top10_transaction_count(select_year,select_quarter)
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['Pincode', 'District and State']
                        st.dataframe(df[columns_to_display].head(10))
                st.write("")
                df=aggregated_transaction.selectyear_selectquarter_type_wise_transaction_count(select_year, select_quarter)
                fig1 = px.bar(df, x='Transaction Count', 
                                y='Transaction Type',   
                                text='Transaction Count',  
                                color='Transaction Type',  
                                color_discrete_sequence=px.colors.qualitative.Pastel,  
                                orientation='h',  
                                title=f'Type-wise Transaction Count - {select_year}- Q{select_quarter}')          
                fig1.update_xaxes(title='Transaction Count')
                fig1.update_layout(width=800, height=400)
                st.plotly_chart(fig1)


                
            #CASE 2      
            elif   select_quarter == 'Select One' and select_type != 'Select One':
                col1,col2=st.columns([4,1.5])
                with col1:
                    st.title(f"{select_year}")
                    df=aggregated_transaction.selectyear_selecttype_state_wise_transaction_count(select_year, select_type)    
                    fig = px.bar(
                                    df,   x='State',
                                    y='Transaction Count',
                                    color='State',  
                                    title=f'Statewise Transaction Count for {select_year} - {select_type}',
                                    labels={'State': 'State', 'Transaction Count': 'Transaction Count', 'Transaction Type': 'Tranasction Type'}
                                )
                    fig.update_layout(width=900, height=600)
                    st.plotly_chart(fig)
                    
                
                with col2:
                    st.write("")
                    st.write("")
                    st.markdown(f"Transction Type wise Top 10 state for {select_year} - {select_type}") 
                    df.reset_index(drop=True, inplace=True)
                    df.index+=1
                    columns_to_display = ['State','Transaction Count']
                    st.dataframe(df[columns_to_display].head(10))

                st.write("")
                df=aggregated_transaction.selectyear_selecttype_quarter_wise_transaction_count(select_year, select_type)
                fig1 = px.bar(df, x='Transaction Count', 
                                y='Quarter',   
                                text='Transaction Count',  
                                color='Quarter',  
                                color_discrete_sequence=px.colors.qualitative.Pastel,  
                                orientation='h',  
                                title=f'Quarter-wise Transaction Count - Year {select_year}- {select_type}')          
                fig1.update_layout(width=500, height=300)
                st.plotly_chart(fig1)
            
            #CASE 3     
            elif   select_quarter != 'Select One' and select_type != 'Select One':
                col1,col2=st.columns([4,1.5])
                with col1:
                    st.title(f"{select_year}-Q{select_quarter}-{select_type}")
                    df=aggregated_transaction.selectyear_selectquarter_selecttype_state_wise_transaction_count(select_year, select_quarter, select_type)    
                    fig = px.bar(
                                    df,   x='State',
                                    y='Transaction Count',
                                    color='State',  
                                    title=f'Statewise Transaction Count for {select_year} -Q{select_quarter}: {select_type}',
                                     )
                    fig.update_layout(width=900, height=600)
                    st.plotly_chart(fig)
                with col2:
                    st.write("")
                    st.write("")
                    st.write("")
                    st.write("")
                    df.reset_index(drop=True, inplace=True)
                    df.index+=1
                    st.markdown("Top 10 state")
                    columns_to_display = ['State', 'Transaction Count']
                    st.dataframe(df[columns_to_display])
                        
    #Display part(Transaction Analysis-Year-wise-Transaction Amount)    
    if option=="Transaction Analysis" and select=="Transaction Amount" and analysis=="Year-wise Transaction Amount Analysis":
        button_style = """
                <style>
                    .stButton > button {
                        background-color: lightblue;
                        color: black;  /* Optional: Set text color */
                        font-weight: bold;  /* Optional: Set font weight */
                    }
                </style>
            """
        st.markdown(button_style, unsafe_allow_html=True)
        st.button("All India")
        col1,col2,col3=st.columns(3)
        with col1:
            df = aggregated_transaction.year_wise_transaction_amount()
            fig1=px.bar(df, x=['2018', '2019', '2020', '2021', '2022', '2023'], y='Transaction Amount', title=f"Year-wise Transaction Amount details", color_discrete_sequence=px.colors.sequential.Plasma)
            fig1.update_xaxes(title='Year')
            fig1.update_layout(width=600, height=400)
            x_values = np.array(df['Year']).astype(float)
            y_values = np.array(df['Transaction Amount']).astype(float)
            m, b = np.polyfit(x_values, y_values, 1)  
            trend_line = m * x_values + b
            fig1.add_trace(go.Scatter(x=x_values, y=trend_line, mode='lines', name='Trend Line'))
            fig1.update_layout(showlegend=True)
            fig1.update_layout(width=500, height=400)
            st.plotly_chart(fig1)
        with col2: 
            df2 = aggregated_transaction.year_quarter_wise_transaction_amount()
            fig2 = px.bar(df2, x='Transaction Amount', y='Year', color='Quarter', orientation='h',
                                           barmode='group', title='Year - Quarter wise Transaction Amount (Grouped Bar)')
            fig2.update_layout(width=400, height=400)
            st.plotly_chart(fig2)
        with col3:
            df3 = aggregated_transaction.year_type_wise_transaction_amount()
            fig_line = px.line(df3, x='Year', y='Transaction Amount', color='Transaction Type', title=f'Trend - Year & Transaction Type wise')
            fig_line.update_layout(width=450, height=400)
            st.plotly_chart(fig_line)
        with col1:
            select_year=st.slider("Select a Year", 2018, 2023, 2020)
        df=aggregated_transaction.selectyear_state_wise_transaction_amount(select_year)
        plotly.geo_map(df, 'State','Transaction Amount', f'Geo Insights for the year {select_year} State wise Transaction Amount')            


        
        col1, col2 = st.columns([4,2])
        
                
        selectyear_state_wise_transaction_amount = aggregated_transaction.selectyear_state_wise_transaction_amount(select_year)
        selectyear_quarter_wise_transaction_amount = aggregated_transaction.selectyear_quarter_wise_transaction_amount(select_year)
        
        with col1:
            st.title(f"{select_year}")
            fig1=px.bar(selectyear_state_wise_transaction_amount, x='State', y='Transaction Amount', title=f"State-wise Transaction Amount for the year - {select_year}", color_discrete_sequence=px.colors.sequential.Sunsetdark_r)
            fig1.update_layout(width=700, height=620)
            st.plotly_chart(fig1)
        with col2:
            st.write("")
            st.write("")
            st.title(":blue[Transaction]")
            df=aggregated_transaction.year_wise_transaction_amount()
            result=df[df['Year']==select_year]
            filtered_result = result.iloc[0]['Transaction Amount']  
            formatted_total_premium = state.convert(str(int(filtered_result)))
            st.markdown(f'<p style="font-size: 16px; font-weight: bold;">All India total payment value for the year - {select_year} (Nos.)</p>', unsafe_allow_html=True)
            st.markdown(f'<p style="font-size: 20px; color: blue; font-weight: bold;">Rs.{formatted_total_premium}</p>', unsafe_allow_html=True)
        with col2:
            st.write("")
            custom_styles = {
                "container": {"padding": "0!important", "background-color": "#9dc5e4"},
                "icon": {"color": "red", "font-size": "12px"},
                "nav-link": {"font-size": "10px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "green"},
            }         
            option=option_menu(f"{select_year} - Top 10",
                        options=["States","Districts", "Pincodes"],
                        menu_icon='trophy',
                        default_index=2, orientation='horizontal',
                        styles=custom_styles)
            if option== 'States':         
                
                df= aggregated_transaction.selectyear_state_wise_transaction_amount(select_year)
                df['State']=df['State'].str.title()
                df.reset_index(drop=True, inplace=True)
                df.index+=1
                columns_to_display = ['State','Transaction Amount']
                st.dataframe(df[columns_to_display].head(10))
                

            elif option== 'Districts':         
                
                df= map_transaction.selectyear_district_wise_transaction_amount(select_year)
                df['District']=df['District'].str.title()
                df.reset_index(drop=True, inplace=True)
                df.index+=1
                df['State']=df['State'].str.title()
                columns_to_display = ['District', 'State']
                st.dataframe(df[columns_to_display].head(10))

            elif option== 'Pincodes':         
                
                df= top_transaction.selectyear_pincodewise_top10_transaction_amount(select_year)
                df.reset_index(drop=True, inplace=True)
                df.index+=1
                columns_to_display = ['Pincode', 'District and State']
                st.dataframe(df[columns_to_display].head(10))

        col1, col2, col3 = st.columns(3)
        df1=aggregated_transaction.selectyear_quarter_wise_transaction_amount(select_year)
        df2=aggregated_transaction.selectyear_type_wise_transaction_amount(select_year)
        df3=aggregated_transaction.selectyear_quarter_type_wise_transaction_amount(select_year)
        with col1:
            st.write("")
            fig_pie = px.pie(df1, values='Transaction Amount',names='Quarter',color_discrete_sequence=px.colors.sequential.amp_r, title=f'{select_year}: Transaction Distribution by Quarter')
            fig_pie.update_layout(width=400, height=400)
            st.plotly_chart(fig_pie)
                        
        with col2:
            st.write("")
            fig_pie = px.pie(df2, values='Transaction Amount',names='Transaction Type', title=f'{select_year}: Transaction Distribution by Type',
                                color_discrete_sequence=px.colors.sequential.Agsunset_r)
            fig_pie.update_layout(width=400, height=400)
            st.plotly_chart(fig_pie)
            
        with col3:
            fig1=px.bar(df3, x='Transaction Type', y='Transaction Amount', color='Quarter', title=f"Quarter and Type-wise transaction Amount for the year - {select_year}", color_discrete_sequence=px.colors.sequential.Sunsetdark_r)
            fig1.update_layout(width=400, height=400)
            st.plotly_chart(fig1)

             
            
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            advanced_filters = st.checkbox(':blue[ADVANCED SEARCH]')
            
            st.write("")
        if advanced_filters:
                col1, col2 = st.columns(2)

                with col1:
                    select_quarter = st.selectbox(
                        'Select Quarter: ', ['Select One', '1', '2', '3', '4'])
                
                with col2:
                    type_list = ['Select One']
                    type_list.extend(state.type_list())
                    select_type = st.selectbox('Select Type:             ', type_list)
                st.write('')

        if advanced_filters:
            #CASE 1
            if  select_quarter != 'Select One' and select_type == 'Select One':
                st.title(f"{select_year} - Q{select_quarter}")
                col1,col2=st.columns([4,1.5])
                with col1:
                    df=aggregated_transaction.selectyear_selectquarter_state_wise_transaction_amount(select_year, select_quarter)    
                    fig = px.bar(
                                    df,   x='State',
                                    y='Transaction Amount',
                                    color='State',  
                                    title=f'Statewise Transaction Amount for Q{select_quarter}-{select_year}',
                                    labels={'State': 'State', 'Transaction Amount': 'Transaction Amount', 'Quarter': 'Quarter'}
                                )
                    fig.update_layout(width=850, height=700)
                    st.plotly_chart(fig)   
                with col2:
                    st.write("")
                    custom_styles = {
                        "container": {"padding": "0!important", "background-color": "#9dc5e4"},
                        "icon": {"color": "red", "font-size": "12px"},
                        "nav-link": {"font-size": "10px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "green"},
                    }         
                    option=option_menu(f"{select_year} Q{select_quarter}- Top 10",
                                options=["States","Districts", "Pincodes"],
                                menu_icon='trophy',
                                default_index=2, orientation='horizontal',
                                styles=custom_styles)
                    if option== 'States':         
                        
                        df= aggregated_transaction.selectyear_selectquarter_state_wise_transaction_amount(select_year, select_quarter)
                        df['State']=df['State'].str.title()
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['State','Transaction Amount']
                        st.dataframe(df[columns_to_display].head(10))
                        

                    elif option== 'Districts':         
                        
                        df= map_transaction.selectyear_selectquarter_district_wise_transaction_amount(select_year,select_quarter)
                        df['District']=df['District'].str.title()
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['District','State']
                        st.dataframe(df[columns_to_display].head(10))

                    elif option== 'Pincodes':         
                        
                        df= top_transaction.selectyear_selectquarter_pincodewise_top10_transaction_amount(select_year,select_quarter)
                        df.reset_index(drop=True, inplace=True)
                        df.index+=1
                        columns_to_display = ['Pincode', 'District and State']
                        st.dataframe(df[columns_to_display].head(10))
                st.write("")
                df=aggregated_transaction.selectyear_selectquarter_type_wise_transaction_amount(select_year, select_quarter)
                fig1 = px.bar(df, x='Transaction Amount', 
                                y='Transaction Type',   
                                text='Transaction Amount',  
                                color='Transaction Type',  
                                color_discrete_sequence=px.colors.qualitative.Pastel,  
                                orientation='h',  
                                title=f'Type-wise Transaction Amount - {select_year}- Q{select_quarter}')          
                fig1.update_xaxes(title='Transaction Amount')
                fig1.update_layout(width=800, height=400)
                st.plotly_chart(fig1)


                
            #CASE 2      
            elif   select_quarter == 'Select One' and select_type != 'Select One':
                col1,col2=st.columns([4,1.5])
                with col1:
                    st.title(f"{select_year}")
                    df=aggregated_transaction.selectyear_selecttype_state_wise_transaction_amount(select_year, select_type)    
                    fig = px.bar(
                                    df,   x='State',
                                    y='Transaction Amount',
                                    color='State',  
                                    title=f'Statewise Transaction Amount for {select_year} - {select_type}',
                                    labels={'State': 'State', 'Transaction Amount': 'Transaction Amount', 'Transaction Type': 'Tranasction Type'}
                                )
                    fig.update_layout(width=900, height=600)
                    st.plotly_chart(fig)
                    
                
                with col2:
                    st.write("")
                    st.write("")
                    st.markdown(f"Transction Type wise Top 10 state for {select_year} - {select_type}") 
                    df.reset_index(drop=True, inplace=True)
                    df.index+=1
                    columns_to_display = ['State','Transaction Amount']
                    st.dataframe(df[columns_to_display].head(10))

                st.write("")
                df=aggregated_transaction.selectyear_selecttype_quarter_wise_transaction_amount(select_year, select_type)
                fig1 = px.bar(df, x='Transaction Amount', 
                                y='Quarter',   
                                text='Transaction Amount',  
                                color='Quarter',  
                                color_discrete_sequence=px.colors.qualitative.Pastel,  
                                orientation='h',  
                                title=f'Quarter-wise Transaction Amount - Year {select_year}- {select_type}')          
                fig1.update_layout(width=500, height=300)
                st.plotly_chart(fig1)
            
            #CASE 3     
            elif   select_quarter != 'Select One' and select_type != 'Select One':
                col1,col2=st.columns([4,1.5])
                with col1:
                    st.title(f"{select_year}-Q{select_quarter}-{select_type}")
                    df=aggregated_transaction.selectyear_selectquarter_selecttype_state_wise_transaction_amount(select_year, select_quarter, select_type)    
                    fig = px.bar(
                                    df,   x='State',
                                    y='Transaction Amount',
                                    color='State',  
                                    title=f'Statewise Transaction Amount for {select_year} -Q{select_quarter}: {select_type}',
                                     )
                    fig.update_layout(width=900, height=600)
                    st.plotly_chart(fig)
                with col2:
                    st.write("")
                    st.write("")
                    st.write("")
                    st.write("")
                    df.reset_index(drop=True, inplace=True)
                    df.index+=1
                    st.markdown("Top 10 state")
                    columns_to_display = ['State', 'Transaction Amount']
                    st.dataframe(df[columns_to_display])
                                      
    #Display part(Transaction Analysis-Quarter-wise-Transaction Count)
    if option=="Transaction Analysis" and select=="Transaction Count" and analysis=="Quarter-wise Transaction Count Analysis":
        button_style = """
                <style>
                    .stButton > button {
                        background-color: lightblue;
                        color: black;  /* Optional: Set text color */
                        font-weight: bold;  /* Optional: Set font weight */
                    }
                </style>
            """

        st.markdown(button_style, unsafe_allow_html=True)
        st.button("All India")
        
        col1,col2,col3=st.columns([3,1,2])
        with col1:
            quarter_wise_transaction_count = aggregated_transaction.quarter_wise_transaction_count()
            fig1=px.bar(quarter_wise_transaction_count, x='Quarter', y='Transaction Count',
                                            title='Quarter-wise Transaction Count Details',
                                            color='Transaction Count',  
                                            color_continuous_scale='Viridis')
            fig1.update_layout(width=600, height=400)
            st.plotly_chart(fig1)
        with col3:                        
            st.write("")
            st.write("")
            st.write("")
            st.title(":blue[Insurance]")
            st.markdown(f'<p style="font-size: 16px; font-weight: bold;">All India Insurance Policies Purchased by Quarters(Nos.)</p>', unsafe_allow_html=True)
            df=pd.DataFrame(aggregated_transaction.quarter_wise_transaction_count())
            columns_to_display=['Quarter', 'Transaction Count']
            st.dataframe(df[columns_to_display])

        col1,col2=st.columns([2,1.2])
        with col1:                             
            quarter_type_wise_transaction_count = aggregated_transaction.quarter_type_wise_transaction_count()
            fig3= px.bar(quarter_type_wise_transaction_count, x='Quarter', y='Transaction Count',
                                                                color='Transaction Type', barmode='stack',
                                                                title='Quarter - Type wise Transaction Count')
            fig3.update_layout(width=600, height=400)
            st.plotly_chart(fig3)

        with col2:
            year_quarter_wise_transaction_count = aggregated_transaction.year_quarter_wise_transaction_count()
            Quarter=year_quarter_wise_transaction_count['Quarter'].unique().tolist()
            fig2=px.line(year_quarter_wise_transaction_count, x='Quarter', y='Transaction Count',
                                    color='Year', title='Year - Quarter wise Transaction Count')
            fig2.update_layout(width=400, height=400)
            st.plotly_chart(fig2)
        col1,col2=st.columns(2)
        with col1:
            select_quarter=st.slider("Select a Quarter", 1, 4, 1)
        df=aggregated_transaction.selectquarter_state_wise_transaction_count(select_quarter)
        plotly.geo_map(df, 'State','Transaction Count', f'Geo Insights for the Q{select_quarter} State wise Transaction Count')

    #Display part(Transaction Analysis-Quarter-wise-Transaction Amount)
    if option=="Transaction Analysis" and select=="Transaction Amount" and analysis=="Quarter-wise Transaction Amount Analysis":
        button_style = """
                <style>
                 .stButton > button {
                        background-color: lightblue;
                        color: black;  /* Optional: Set text color */
                        font-weight: bold;  /* Optional: Set font weight */
                    }
                </style>
            """

        st.markdown(button_style, unsafe_allow_html=True)
        st.button("All India")
        
        col1,col2,col3=st.columns([3,1,2])
        with col1:
            quarter_wise_transaction_amount = aggregated_transaction.quarter_wise_transaction_amount()
            fig1=px.bar(quarter_wise_transaction_amount, x='Quarter', y='Transaction Amount',
                                            title='Quarter-wise Transaction Amount Details',
                                            color='Transaction Amount',  
                                            color_continuous_scale='Viridis')
            fig1.update_layout(width=600, height=400)
            st.plotly_chart(fig1)
        with col3:                        
            st.write("")
            st.write("")
            st.write("")
            st.title(":blue[Insurance]")
            st.markdown(f'<p style="font-size: 16px; font-weight: bold;">All India Insurance Payment Value by Quarters(Nos.)</p>', unsafe_allow_html=True)
            df=pd.DataFrame(aggregated_transaction.quarter_wise_transaction_amount())
            columns_to_display=['Quarter', 'Transaction Amount']
            st.dataframe(df[columns_to_display])

        col1,col2=st.columns([2,1.2])
        with col1:                             
            quarter_type_wise_transaction_amount = aggregated_transaction.quarter_type_wise_transaction_amount()
            fig3= px.bar(quarter_type_wise_transaction_amount, x='Quarter', y='Transaction Amount',
                                                                color='Transaction Type', barmode='stack',
                                                                title='Quarter - Type wise Transaction Amount')
            fig3.update_layout(width=600, height=400)
            st.plotly_chart(fig3)

        with col2:
            year_quarter_wise_transaction_amount = aggregated_transaction.year_quarter_wise_transaction_amount()
            Quarter=year_quarter_wise_transaction_amount['Quarter'].unique().tolist()
            fig2=px.line(year_quarter_wise_transaction_amount, x='Quarter', y='Transaction Amount',
                                    color='Year', title='Year - Quarter wise Transaction Amount')
            fig2.update_layout(width=400, height=400)
            st.plotly_chart(fig2)
        col1,col2=st.columns(2)
        with col1:
            select_quarter=st.slider("Select a Quarter", 1, 4, 1)
        df=aggregated_transaction.selectquarter_state_wise_transaction_amount(select_quarter)
        plotly.geo_map(df, 'State','Transaction Amount', f'Geo Insights for the Q{select_quarter} State wise Transaction Amount')

    #Display part(Transaction Analysis-TransactionTywe-wise-Transaction Count)
    if option=="Transaction Analysis" and select=="Transaction Count" and analysis=="Transaction_Typewise Transaction Count Analysis":
        button_style = """
                <style>
                    .stButton > button {
                        background-color: lightblue;
                        color: black;  /* Optional: Set text color */
                        font-weight: bold;  /* Optional: Set font weight */
                    }
                </style>
            """

        st.markdown(button_style, unsafe_allow_html=True)
        st.button("All India")
        
        col1,col2,col3=st.columns([3,1,2])
        with col1:
            type_wise_transaction_count = aggregated_transaction.type_wise_transaction_count()
            fig1 = px.bar(type_wise_transaction_count,
                                x='Transaction Count', 
                                y='Transaction Type',   
                                text='Transaction Count',  
                                color='Transaction Type',  
                                color_discrete_sequence=px.colors.qualitative.Pastel,  
                                orientation='h',  
                                title='Type-wise Transaction Count')          
            fig1.update_xaxes(title='Transaction Count')
            fig1.update_layout(width=600, height=400)
            st.plotly_chart(fig1)
        with col3:  
                              
            st.write("")
            st.write("")
            st.write("")
            st.title(":blue[Insurance]")
            st.markdown(f'<p style="font-size: 16px; font-weight: bold;">All India Insurance Policies Purchased by Transaction Type(Nos.)</p>', unsafe_allow_html=True)
            df=pd.DataFrame(aggregated_transaction.type_wise_transaction_count())
            columns_to_display=['Transaction Type', 'Transaction Count']
            st.dataframe(df[columns_to_display])

        col1,col2=st.columns([2,1.2])
        with col1:                             
            quarter_type_wise_transaction_count = aggregated_transaction.quarter_type_wise_transaction_count()
            fig3= px.bar(quarter_type_wise_transaction_count, x='Transaction Type', y='Transaction Count',
                                                                color='Quarter', barmode='stack',
                                                                title='Transaction Type - Quarter wise Transaction Count')
            fig3.update_layout(width=600, height=400)
            st.plotly_chart(fig3)

        with col2:
            df= aggregated_transaction.year_type_wise_transaction_count()
            fig3= px.bar(df, x='Transaction Type', y='Transaction Count',
                                                                color='Year', barmode='stack',
                                                                title='Transaction Type - Year wise Transaction Count')
            fig3.update_layout(width=600, height=400)
            st.plotly_chart(fig3)
           
    #Display part(Transaction Analysis-TransactionTywe-wise-Transaction Amount)
    if option=="Transaction Analysis" and select=="Transaction Amount" and analysis=="Transaction_Typewise Transaction Amount Analysis":
        button_style = """
                <style>
                    .stButton > button {
                        background-color: lightblue;
                        color: black;  /* Optional: Set text color */
                        font-weight: bold;  /* Optional: Set font weight */  amount
                    }
                </style>
            """

        st.markdown(button_style, unsafe_allow_html=True)
        st.button("All India")
        
        col1,col2,col3=st.columns([3,1,2])
        with col1:
            type_wise_transaction_amount = aggregated_transaction.type_wise_transaction_amount()
            fig1 = px.bar(type_wise_transaction_amount,
                                x='Transaction Amount', 
                                y='Transaction Type',   
                                text='Transaction Amount',  
                                color='Transaction Type',  
                                color_discrete_sequence=px.colors.qualitative.Pastel,  
                                orientation='h',  
                                title='Type-wise Transaction Amount')          
            fig1.update_xaxes(title='Transaction Amount')
            fig1.update_layout(width=600, height=400)
            st.plotly_chart(fig1)
        with col3:                        
            st.write("")
            st.write("")
            st.write("")
            st.title(":blue[Insurance]")
            st.markdown(f'<p style="font-size: 16px; font-weight: bold;">All India Insurance Policies Payment Value by Transaction Type(Nos.)</p>', unsafe_allow_html=True)
            df=pd.DataFrame(aggregated_transaction.type_wise_transaction_amount())
            columns_to_display=['Transaction Type', 'Transaction Amount']
            st.dataframe(df[columns_to_display])

        col1,col2=st.columns([2,1.2])
        with col1:                             
            quarter_type_wise_transaction_amount = aggregated_transaction.quarter_type_wise_transaction_amount()
            fig3= px.bar(quarter_type_wise_transaction_amount, x='Transaction Type', y='Transaction Amount',
                                                                color='Quarter', barmode='stack',
                                                                title='Transaction Type - Quarter wise Transaction Amount')
            fig3.update_layout(width=600, height=400)
            st.plotly_chart(fig3)

        with col2:
            df= aggregated_transaction.year_type_wise_transaction_amount()
            fig3= px.bar(df, x='Transaction Type', y='Transaction Amount',
                                                                color='Year', barmode='stack',
                                                                title='Transaction Type - Year wise Transaction Amount')
            fig3.update_layout(width=600, height=400)
            st.plotly_chart(fig3)
        
    
#User Analysis          
    #Display part(User Analysis-State-wise-User Count)
    if option=="User Analysis" and  analysis=="State-wise User Analysis":
        button_style = """
                <style>
                    .stButton > button {
                        background-color: lightblue;
                        color: black;  /* Optional: Set text color */
                        font-weight: bold;  /* Optional: Set font weight */
                    }
                </style>
            """

        st.markdown(button_style, unsafe_allow_html=True)
        st.button("All India Users")

        st.write("")
        state_wise_user_count= aggregated_user.state_wise_user_count()
        plotly.geo_map(state_wise_user_count, 'State',
                    'User Count', 'Geo Insights of State wise User Count')
        
        col1,col2=st.columns(2)
        with col1:  
            state_wise_user_count = aggregated_user.state_wise_user_count()
            fig1=px.bar(state_wise_user_count, x='State', y='User Count', title=f"State-wise User Count details", color_discrete_sequence=px.colors.sequential.Mint_r)
            fig1.update_layout(width=600, height=800)
            st.plotly_chart(fig1) 
        with col2:
            df=map_user.state_wise_appOpens()
            fig1=px.bar(df, x='State', y='App Opens', title=f"State-wise App Opens Count details", color_discrete_sequence=px.colors.sequential.algae_r)
            fig1.update_layout(width=600, height=800)
            st.plotly_chart(fig1) 
        
        col1,col2,col3=st.columns([0.2,0.6,0.2])
        with col2:
            st.write("")    
            st.write("")                           

            custom_styles = {
                "container": {"padding": "0!important", "background-color": "#9dc5e4"},
                "icon": {"color": "red", "font-size": "12px"},
                "nav-link": {"font-size": "10px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "green"},
            }         
            option=option_menu("Top 10 Users",
                        options=["States","Districts", "Pincodes"],
                        menu_icon='trophy',
                        default_index=0, orientation='horizontal',
                        styles=custom_styles)
            if option== 'States':      
                df=pd.DataFrame(aggregated_user.state_wise_user_count())
                sorted_df = df.sort_values(by='User Count', ascending=False)
                sorted_df.reset_index(drop=True, inplace=True)
                sorted_df.index += 1
                top_10_states = sorted_df.head(10)
                st.dataframe(top_10_states)

            elif option== 'Districts':         
                df= map_user.district_wise_registerUsers()
                df['District']=df['District'].str.title()
                df['State']=df['State'].str.title()
                df.reset_index(drop=True, inplace=True)
                df.index+=1
                columns_to_display = ['District', 'State', 'Registered Users']
                st.dataframe(df[columns_to_display].head(10))

            elif option== 'Pincodes':         
                df= top_user.pincodewise_top10_user_count()
                df.reset_index(drop=True, inplace=True)
                df.index+=1
                columns_to_display = ['Pincode', 'Registered Users']
                st.dataframe(df[columns_to_display].head(10))

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            advanced_filters = st.checkbox(':blue[ADVANCED SEARCH]')
            
            st.write("")
        if advanced_filters:
            col1, col2, col3 = st.columns(3)
            with col1:
                select_state=st.selectbox('Select State: ', state.ins_state_list())
            if select_state:
                col1,col2=st.columns(2)
                with col1:  
                    df1 = aggregated_user.selectstate_year_wise_user_count(select_state)
                    fig1=px.bar(df1, x=['2018','2019','2020','2021','2022'], y='User Count', title=f"{select_state}: Year-wise User Count details", color_discrete_sequence=px.colors.sequential.Mint_r)
                    fig1.update_layout(width=450, height=500)
                    st.plotly_chart(fig1) 
                with col2:
                    df2 = aggregated_user.selectstate_quarter_wise_user_count(select_state)
                    fig1=px.bar(df2, x='Quarter', y='User Count', title=f"{select_state}: Quarter-wise User Count details", color_discrete_sequence=px.colors.sequential.Magenta_r)
                    fig1.update_layout(width=450, height=500)
                    st.plotly_chart(fig1)  
                

                with col1:
                    df3 = aggregated_user.selectstate_brand_wise_user_count(select_state)
                    fig1=px.bar(df3, x='User Brand', y='User Count', title=f"{select_state}: UserBrand-wise User Count details", color_discrete_sequence=px.colors.sequential.Cividis_r)
                    fig1.update_layout(width=450, height=500)
                    st.plotly_chart(fig1)

                with col2:
                    st.write("")    
                    st.write("")       
                    df4 = aggregated_user.selectstate_year_quarter_wise_user_count(select_state)                    
                    fig3= px.bar(df4, x='Quarter', y='User Count',
                                                                        color='Year', barmode='stack',
                                                                        title=f'Year - Quarter wise User Count for {select_state}')
                    fig3.update_layout(width=450, height=500)
                    st.plotly_chart(fig3)
                
    #Display part(User Analysis-Year-wise-User Count)
    if option=="User Analysis" and  analysis=="Year-wise User Analysis":
        button_style = """
                <style>
                    .stButton > button {
                        background-color: lightblue;
                        color: black;  /* Optional: Set text color */
                        font-weight: bold;  /* Optional: Set font weight */
                    }
                </style>
            """

        st.markdown(button_style, unsafe_allow_html=True)
        st.button("All India Users")
        col1,col2=st.columns([1,2])
        with col1:
            df = aggregated_user.year_wise_user_count()
            df['User Count'] = df['User Count'].astype(float)
            fig1 = px.bar(df, x='Year', y='User Count',
                            title='Year-wise User Count',
                            color_discrete_sequence=px.colors.sequential.Mint_r)
            fig1.update_layout(width=550, height=400, xaxis_title='Year')
            x_values = np.array(df['Year'])
            y_values = np.array(df['User Count'])
            m, b = np.polyfit(x_values, y_values, 1)  
            trend_line = m * x_values + b
            fig1.add_trace(go.Scatter(x=x_values, y=trend_line, mode='lines', name='Trend Line'))
            fig1.update_layout(showlegend=True)
            st.plotly_chart(fig1)
        
        with col2:
            df4= aggregated_user.year_brand_wise_user_count()
            fig1 = px.bar(df4, x='User Brand', y='User Count', color='Year',
               title='Year-Brand- wise User Count Line Graph')
            fig1.update_layout(width=800, height=400)
            st.plotly_chart(fig1)
            
        col1,col2=st.columns([1,2])
        with col1:
            df2 = aggregated_user.year_quarter_wise_user_count()
            fig1 = px.line(df2, x='Year', y='User Count', color='Quarter',
               title='Year-Quarter - wise User Count Line Graph')
            fig1.update_layout(width=400, height=400)
            st.plotly_chart(fig1)
        with col2:
            st.write("")
            st.write("")
            st.write("<h3> Year-wise User Count </h3>", unsafe_allow_html=True)
            df=pd.DataFrame(aggregated_user.year_wise_user_count())
            df_new = df.groupby('Year')['User Count'].sum().reset_index()
            df_new['Year']=df_new['Year'].astype(str)
            df_new.index+=1
            st.dataframe(df_new)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            advanced_filters = st.checkbox(':blue[ADVANCED SEARCH]')
        if advanced_filters:
            col1, col2, col3 = st.columns(3)
            with col1:
                select_year=st.selectbox('Select Year: ', aggregated_user.year_wise_user_count()['Year'].unique())
            if select_year:
                col1,col2=st.columns(2)
                with col1:
                    df2 = aggregated_user.selectyear_state_wise_user_count(int(select_year))
                    fig1=px.bar(df2, x='State', y='User Count', title=f"{select_year}: State-wise User Count details", color_discrete_sequence=px.colors.sequential.Magenta_r)
                    fig1.update_layout(width=450, height=500)
                    st.plotly_chart(fig1) 

                with col2:
                    df2 = aggregated_user.selectyear_quarter_wise_user_count(int(select_year))
                    fig1=px.bar(df2, x='quarter', y='User Count', title=f"{select_year}: Quarter-wise User Count details", color_discrete_sequence=px.colors.sequential.Magenta_r)
                    fig1.update_layout(width=450, height=500)
                    st.plotly_chart(fig1)  
                
                with col1:
                    df2 = aggregated_user.selectyear_brand_wise_user_count(int(select_year))
                    fig1=px.bar(df2, x='User Brand', y='User Count', title=f"{select_year}: Brand-wise User Count details", color_discrete_sequence=px.colors.sequential.Magenta_r)
                    fig1.update_layout(width=450, height=500)
                    st.plotly_chart(fig1)  
                with col2:
                    df2 = aggregated_user.selectyear_quarter_brand_wise_user_count(int(select_year))
                    fig1=px.bar(df2, x='User Brand', y='User Count', color='quarter', title=f"{select_year}: State-wise User Count details", color_discrete_sequence=px.colors.sequential.Magenta_r)
                    fig1.update_layout(width=450, height=500)
                    st.plotly_chart(fig1)  

    #Display part(User Analysis-Quarter-wise-User Count)
    if option=="User Analysis" and  analysis=="Quarter-wise User Analysis":
        button_style = """
                <style>
                    .stButton > button {
                        background-color: lightblue;
                        color: black;  /* Optional: Set text color */
                        font-weight: bold;  /* Optional: Set font weight */
                    }
                </style>
            """

        st.markdown(button_style, unsafe_allow_html=True)
        st.button("All India Users")
        col1,col2,col3=st.columns([2,1,2])
        with col1:
            df = aggregated_user.quarter_wise_user_count()
            fig1 = px.bar(df, x='Quarter', y='User Count', color='Quarter',
                            title='Quarter-wise User Count',
                            color_discrete_sequence=px.colors.sequential.Inferno_r)
            fig1.update_layout(width=400, height=400)
            st.plotly_chart(fig1)
        
        with col2:
            st.write("")
            st.write("")
            st.write("")
            df = aggregated_user.quarter_wise_user_count()
            sorted_df = df.sort_values(by='User Count', ascending=False)
            sorted_df.reset_index(drop=True, inplace=True)
            sorted_df.index += 1
            coloumn_to_display=['Quarter', 'User Count']
            
            st.write("<h3>User Count By Quarters</h3>", unsafe_allow_html=True)
            st.dataframe(df[coloumn_to_display])
        with col3:
            df2 = aggregated_user.year_quarter_wise_user_count()
            fig1 = px.bar(df2, x='Quarter', y='User Count', color='Year',
            title='Year-Quarter - wise User Count Line Graph')
            fig1.update_layout(width=400, height=400)
            st.plotly_chart(fig1)
      
        
        df4= aggregated_user.quarter_brand_wise_user_count()
        fig1 = px.bar(df4, x='User Brand', y='User Count', color='quarter',
            title='Quarter-Brand- wise User Count Line Graph')
        fig1.update_layout(width=800, height=400)
        st.plotly_chart(fig1)

        col1, col2, col3, col4 = st.columns(4) 
        with col1:
            advanced_filters = st.checkbox(':blue[ADVANCED SEARCH]') 
        if advanced_filters:
            col1, col2, col3 = st.columns(3)
            with col1:
                select_quarter=st.selectbox('Select Quarter: ', aggregated_user.quarter_wise_user_count()['Quarter'].unique())
            if select_quarter:
                col1,col2=st.columns([2,1])
                with col1:
                    df2 = aggregated_user.selectquarter_state_wise_user_count(int(select_quarter))
                    fig1=px.bar(df2, x='State', y='User Count', title=f"{select_quarter}: State-wise User Count details", color_discrete_sequence=px.colors.sequential.Magenta_r)
                    fig1.update_layout(width=750, height=600)
                    st.plotly_chart(fig1) 

                with col2:
                    df2 = aggregated_user.selectquarter_year_wise_user_count(int(select_quarter))
                    fig1=px.bar(df2, x='User Count', y='Year', orientation='h', title=f"{select_quarter}: Year-wise User Count details", color_discrete_sequence=px.colors.sequential.Magenta_r)
                    fig1.update_layout(width=450, height=400)
                    st.plotly_chart(fig1)  
                
                with col1:
                    df2 = aggregated_user.selectquarter_brand_wise_user_count(int(select_quarter))
                    fig1=px.bar(df2, x='User Brand', y='User Count', title=f"{select_quarter}: Brand-wise User Count details", color_discrete_sequence=px.colors.sequential.Magenta_r)
                    fig1.update_layout(width=450, height=500)
                    st.plotly_chart(fig1)  
                with col2:
                    df2 = aggregated_user.selectquarter_year_brand_wise_user_count(int(select_quarter))
                    fig1=px.bar(df2, x='User Brand', y='User Count', color='Year', title=f"{select_quarter}: State-wise User Count details", color_discrete_sequence=px.colors.sequential.Magenta_r)
                    fig1.update_layout(width=450, height=500)
  
    #Display part(User Analysis-Brand-wise-User Count)
    if option=="User Analysis" and  analysis=="UsersByBrand":
        button_style = """
                <style>
                    .stButton > button {
                        background-color: lightblue;
                        color: black;  /* Optional: Set text color */
                        font-weight: bold;  /* Optional: Set font weight */
                    }
                </style>
            """

        st.markdown(button_style, unsafe_allow_html=True)
        st.button("All India Users")
        col1,col2=st.columns([4,2])
        with col1:
            brand_wise_user_count = aggregated_user.brand_wise_user_count()
            fig1 = px.pie(brand_wise_user_count, values='User Count', names='User Brand', 
                            title='Brand-wise User Count Pie Chart')
            fig1.update_layout(width=600, height=600)
            st.plotly_chart(fig1)
        
        with col2:
            brand_wise_user_count = aggregated_user.brand_wise_user_count()
            df=pd.DataFrame({'Brand': brand_wise_user_count['User Brand'], 
                             'User Count': brand_wise_user_count['User Count']})
            sorted_df = df.sort_values(by='User Count', ascending=False)
            sorted_df.reset_index(drop=True, inplace=True)
            sorted_df.index += 1
            top_10_states = sorted_df.head(10)
            st.write("<h3>Top 10 Brands By User Count</h3>", unsafe_allow_html=True)
            st.dataframe(top_10_states)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            advanced_filters = st.checkbox(':blue[ADVANCED SEARCH]')
        if advanced_filters:
            col1, col2, col3 = st.columns(3)
            with col1:
                select_brand=st.selectbox('Select Brand: ', aggregated_user.brand_wise_user_count()['User Brand'].unique())
            if select_brand:
                col1,col2=st.columns(2)
                with col1:
                    df2 = aggregated_user.selectbrand_state_wise_user_count(select_brand)
                    fig1=px.bar(df2, x='State', y='User Count', color='User Brand', title=f"{select_brand}: State-wise User Count details", color_discrete_sequence=px.colors.sequential.Magenta_r)
                    fig1.update_layout(width=450, height=500)
                    st.plotly_chart(fig1) 

                with col2:
                    df2 = aggregated_user.selectbrand_year_wise_user_count(select_brand)
                    fig1=px.bar(df2, x='User Count', y='Year', orientation='h', color='Year',title=f"{select_brand}: Year-wise User Count details", color_discrete_sequence=px.colors.sequential.Magenta_r)
                    fig1.update_layout(width=600, height=400)
                    st.plotly_chart(fig1)  
                
                col1,col2=st.columns(2)
                
                with col1:
                    df2 = aggregated_user.selectbrand_quarter_wise_user_count(select_brand)
                    fig1=px.bar(df2, x='quarter', y='User Count', title=f"{select_brand}: Quarter-wise User Count details", color_discrete_sequence=px.colors.sequential.Magenta_r)
                    fig1.update_layout(width=400, height=500)
                    st.plotly_chart(fig1)  
                with col2:
                    df2 = aggregated_user.selectbrand_year_quarter_wise_user_count(select_brand)
                    fig1=px.bar(df2, x='quarter', y='User Count', color='Year', title=f"{select_brand}: Year-Quarter wise User Count details", color_discrete_sequence=px.colors.sequential.Magenta_r)
                    fig1.update_layout(width=450, height=500)
                    st.plotly_chart(fig1)  

            
#Top Charts
    if option=="Top Charts":
        if question=="1. What is the average premium amount for insurance transactions on PhonePe, and how does it compare across different quarters?":
            st.write()
            col1, col2=st.columns([1,2])
            with col2:
                st.write("")
                df = pd.DataFrame(aggregated_insurance.year_quarter_wise_premium_amount())
                avg_premium_by_quarter = df.groupby('Quarter')['Premium Amount'].mean().reset_index()
                st.header("Average Premium Amount for Insurance Transactions by Quarter on PhonePe")
                fig = px.bar(avg_premium_by_quarter, x='Quarter', y='Premium Amount', 
                             color='Quarter',
                            color_continuous_scale='YlOrRd',
                            labels={'Quarter': 'Quarter', 'Premium Amount': 'Average Premium Amount (INR)'})
                fig.update_layout(width=500, height=500, xaxis_title='Quarter', yaxis_title='Average Premium Amount (INR)')
                st.plotly_chart(fig)
    
        
        if question=="2. Which transaction category accounts for the highest number of transactions on PhonePe?":
            col1, col2=st.columns([1,2])
            with col2:
                df = aggregated_transaction.type_wise_transaction_count()
                fig1 = px.bar(df,
                                x='Transaction Count', 
                                y='Transaction Type',   
                                text='Transaction Count',  
                                color='Transaction Type',  
                                color_discrete_sequence=px.colors.qualitative.Pastel,  
                                orientation='h',  
                                title='Distribution of Transaction Counts by Category')      
            
                fig1.update_layout(yaxis_title='Transaction Category')
                fig1.update_layout(width=800, height=450)
                st.plotly_chart(fig1)

        if question =="3. Which states contribute the most to transaction volumes on PhonePe in terms of total transaction amount?":            
            col1, col2=st.columns([2,1])
            with col1:
                df = aggregated_transaction.state_wise_transaction_amount()
                fig1=px.bar(df, x='State', y='Transaction Amount', title=f"All India - State-wise Transaction Amount details",
                            color_discrete_sequence=px.colors.sequential.YlOrRd_r)
                fig1.update_layout(width=700, height=600)
                st.plotly_chart(fig1)
            with col2:
                st.write("")
                st.write("")
                st.header("Top 10 States by Payment Value")
                df = aggregated_transaction.state_wise_transaction_amount()
                st.write("")
                df.reset_index(drop=True, inplace=True)
                df.index += 1
                col=['State', 'Transaction Amount', 'Average Transaction']
                st.dataframe(df[col].head(10))

        if question=="4. What are the top 10 districts by transaction amount within each state on PhonePe?":
            st.write()
            col1, col2=st.columns([1,2])
            with col2:
                df= map_transaction.district_wise_top10_transaction_amount()
                st.header("Top Districts by Transaction Amount within Each State:")
                df['District']=df['District'].str.title()
                df2 = df.groupby('State').apply(lambda x: x.nlargest(1, 
                                        'Transaction Amount')).reset_index(drop=True)
                df2.reset_index(drop=True, inplace=True)
                df2.index += 1
                st.dataframe(df2)
                

        if question=="5. Which are the top 10 pincode areas that generate the highest transaction amounts on PhonePe?":
            st.write()
            col1, col2=st.columns([1,2])
            with col2:
                st.header("Top 10 postal codes by Transaction Amount")
                df= top_transaction.pincodewise_top10_transaction_amount()
                df.reset_index(drop=True, inplace=True)
                df.index+=1
                columns_to_display = ['Pincode', 'District and State']
                st.dataframe(df[columns_to_display].head(10))

        if question=="6. What is the average transaction amount and how does it vary across different transaction types on PhonePe?":
            st.write()
            col1, col2=st.columns([1,2])
            with col2:
                st.write("")
                df = pd.DataFrame(aggregated_transaction.type_wise_transaction_amount())
                avg_transaction_amount_by_type = df.groupby('Transaction Type')['Transaction Amount'].mean().reset_index()
                avg_transaction_amount_by_type = avg_transaction_amount_by_type.sort_values(by='Transaction Amount', ascending=False)
                fig = px.bar(avg_transaction_amount_by_type, x='Transaction Amount', y='Transaction Type', orientation='h', 
                        title='Average Transaction Amount Across Different Transaction Types on PhonePe',
                        labels={'Transaction Amount': 'Average Transaction Amount', 'Transaction Type': 'Transaction Type'},
                        color='Transaction Amount', color_continuous_scale='viridis')
                fig.update_layout(width=700, height=400)
                st.plotly_chart(fig)

   
        if question=="7. What is the trend in total transaction volume on PhonePe over the past year?":
            st.write()
            col1, col2=st.columns([1,2])
            with col2:
                df = aggregated_transaction.year_wise_transaction_count()
                fig1=px.bar(df, x=['2018', '2019', '2020', '2021', '2022', '2023'], y='Transaction Count', title=f"Total Transaction Volume on PhonePe over years", color_discrete_sequence=px.colors.sequential.Plasma)
                fig1.update_xaxes(title='Year')
                x_values = np.array(df['Year']).astype(float)
                y_values = np.array(df['Transaction Count']).astype(float)
                m, b = np.polyfit(x_values, y_values, 1)  
                trend_line = m * x_values + b
                fig1.add_trace(go.Scatter(x=x_values, y=trend_line, mode='lines', name='Trend Line'))
                fig1.update_layout(showlegend=True)
                fig1.update_layout(width=650, height=500)
                st.plotly_chart(fig1)

        if question=="8. Which brands have the highest user count on PhonePe?":
            st.write()
            col1, col2=st.columns([1,2])
            with col2:
                st.write("")
                df = pd.DataFrame(aggregated_user.brand_wise_user_count())
                df2 = df.groupby('User Brand')['User Count'].sum().reset_index()
                df2.index+=1
                st.header("User Brand Engagement Analysis on PhonePe")
                st.write("Total User Count by Brand:")
                fig = px.bar(df2, x='User Brand', y='User Count',
                            labels={'User Brand': 'Brand', 'User Count': 'Total User Count'},
                            color='User Brand', color_discrete_sequence=px.colors.qualitative.Dark24)
                fig.update_layout(width=800, height=600, xaxis_title='Brand', yaxis_title='Total User Count')
                st.plotly_chart(fig)

        if question=="9. What is the distribution of transaction amounts for different types of transactions on PhonePe?":
            st.write()
            col1, col2=st.columns([1,2])
            with col2:
                st.write("")
                df = aggregated_transaction.type_wise_transaction_amount()
                fig = px.box(df, x='Transaction Type', y='Transaction Amount',
                            title='Distribution of Transaction Amounts by Transaction Type on PhonePe',
                            labels={'Transaction Type': 'Transaction Type', 'Transaction Amount': 'Transaction Amount'})
                fig.update_layout(width=800, height=600)
                st.plotly_chart(fig)

        if question=="10. Which regions or cities exhibit the highest growth rate in terms of new users on PhonePe?":
            st.write()
            df=pd.DataFrame(aggregated_user.stateandyear_wise_user_count())
            df = df.dropna()

            df['User_Count_Prev_Year'] = df.groupby('State')['User Count'].shift(1)
            df['Growth_Rate'] = ((df['User Count'] - df['User_Count_Prev_Year']) / df['User_Count_Prev_Year']) * 100
            df['Growth_Rate'] = df['Growth_Rate'].abs()
            highest_growth_states = df.groupby('State')['Growth_Rate'].max().sort_values(ascending=False).reset_index()
            st.header('States with the Highest Growth Rate in User Counts on PhonePe')
            fig = px.bar(highest_growth_states, x='State', y='Growth_Rate',
                        title='Highest Growth Rate in User Counts by State',
                        labels={'State': 'State', 'Growth_Rate': 'Growth Rate (%)'},
                        color='Growth_Rate', color_continuous_scale='Viridis')
            fig.update_layout(width=1000, height=600)
            st.plotly_chart(fig)


#Exit TAB
with Exit:
    st.success(':red[Thank you for your time. Exiting the application]')
    st.balloons()
