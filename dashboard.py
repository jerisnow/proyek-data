import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import streamlit as st
import urllib
from func import DataAnalyzer, BrazilMapPlotter

sns.set(style='dark')
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('E-Commerce Public Dashboard')

select_option = st.sidebar.selectbox(
    'Select an option:',
    ('Overview', 'Customer Analysis', 'Product Analysis', 'Trend Analysis')
)

# Load data
customers_df = pd.read_csv('D:/Bangkit Academy 2024/Proyek Analisis Data/submission/data/customers_dataset.csv')
geoloc_df = pd.read_csv('D:/Bangkit Academy 2024/Proyek Analisis Data/submission/data/geolocation_dataset.csv')
order_items = pd.read_csv('D:/Bangkit Academy 2024/Proyek Analisis Data/submission/data/order_items_dataset.csv')
order_pays = pd.read_csv('D:/Bangkit Academy 2024/Proyek Analisis Data/submission/data/order_payments_dataset.csv')
order_review = pd.read_csv('D:/Bangkit Academy 2024/Proyek Analisis Data/submission/data/order_reviews_dataset.csv')
orders_df = pd.read_csv('D:/Bangkit Academy 2024/Proyek Analisis Data/submission/data/orders_dataset.csv')
product_category = pd.read_csv('D:/Bangkit Academy 2024/Proyek Analisis Data/submission/data/product_category_name_translation.csv')
products_df = pd.read_csv('D:/Bangkit Academy 2024/Proyek Analisis Data/submission/data/products_dataset.csv')
sellers_df = pd.read_csv('D:/Bangkit Academy 2024/Proyek Analisis Data/submission/data/sellers_dataset.csv')
all_df = pd.read_csv('D:/Bangkit Academy 2024/Proyek Analisis Data/submission/data/all_df.csv')

with st.sidebar:
    # Title
    st.title("Athirah Naura R.")
merged_data = orders_df.merge(order_review[['order_id', 'review_score']], on='order_id')

merged_data = merged_data.merge(customers_df[['customer_id', 'customer_state']], on='customer_id')

average_review_score_by_state = merged_data.groupby('customer_state')['review_score'].mean().reset_index()

plt.figure(figsize=(10, 6))
customers_df['customer_state'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Hubungan antara Lokasi Geografis Pelanggan dengan Frekuensi Pembelian')
plt.xlabel('Lokasi Geografis')
plt.ylabel('Frekuensi Pembelian')
plt.xticks(rotation=45)
plt.show()

table_2 = pd.DataFrame(customers_df['customer_state'].value_counts())

orders_df['order_purchase_timestamp'] = pd.to_datetime(orders_df['order_purchase_timestamp'])

monthly_purchase = orders_df.resample('M', on='order_purchase_timestamp').size()

merged_data_2 = orders_df.merge(order_pays[['order_id', 'payment_type']], on='order_id')

merged_data_2['order_purchase_timestamp'] = pd.to_datetime(merged_data_2['order_purchase_timestamp'])

merged_data_2['order_month'] = merged_data_2['order_purchase_timestamp'].dt.to_period('M')
payment_method_trend = merged_data_2.groupby(['order_month', 'payment_type']).size().unstack(fill_value=0)

if select_option == 'Overview':
    st.header('Overview')
    st.write('This page provides an overview of the E-Commerce Public dataset.')
    st.write(all_df)

elif select_option == 'Customer Analysis':
    st.header('Customer Analysis')
    st.write('This page provides analysis of customer-related data.')

    st.subheader('Customer Distribution by State')
    st.bar_chart(table_2)

elif select_option == 'Product Analysis':
    st.header('Product Analysis')
    st.write('This page provides analysis of product-related data.')

    st.subheader('Product Categories')
    category_counts = product_category['product_category_name'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=category_counts.index, y=category_counts.values)
    plt.xticks(rotation=90)
    plt.xlabel('Product Category')
    plt.ylabel('Number of Products')
    st.pyplot()

elif select_option == 'Trend Analysis':
    st.header('Trend Analysis')

    st.subheader('Monthly Purchase Trend')
    st.line_chart(monthly_purchase)

    st.subheader('Payment Method Trend')
    st.line_chart(payment_method_trend)