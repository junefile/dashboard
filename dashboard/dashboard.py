import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load all_data
all_data = pd.read_csv('dashboard/all_data.csv')

# Konversi kolom order_purchase_timestamp ke format datetime
all_data['order_purchase_timestamp'] = pd.to_datetime(all_data['order_purchase_timestamp'], errors='coerce')

# Menambahkan kolom baru: tahun dari order_purchase_timestamp
all_data['order_purchase_year'] = all_data['order_purchase_timestamp'].dt.year

with st.sidebar:
    # Menambahkan logo 
    st.image('dashboard/logo.png')

# Sidebar untuk filter berdasarkan tahun dan state
st.sidebar.header("Filter Data")
selected_year = st.sidebar.selectbox("Pilih Tahun", sorted(all_data['order_purchase_year'].dropna().unique()))
selected_state = st.sidebar.selectbox("Pilih Negara Bagian (State)", all_data['customer_state'].unique())

# Filter data berdasarkan tahun dan state yang dipilih
filtered_data = all_data[(all_data['order_purchase_year'] == selected_year) & 
                         (all_data['customer_state'] == selected_state)]

# Tampilkan informasi hasil filter
st.write(f"### Data Pesanan untuk Tahun {selected_year} dan Negara Bagian {selected_state}")
st.write(f"Jumlah Pesanan: {len(filtered_data)}")


# Grafik 1: Jumlah Pesanan Per Bulan (untuk melihat tren penjualan puncak)
st.write("#### Tren Penjualan per Bulan")
monthly_orders = filtered_data.groupby(filtered_data['order_purchase_timestamp'].dt.to_period('M')).size().reset_index(name='jumlah_pesanan')
monthly_orders['order_purchase_timestamp'] = monthly_orders['order_purchase_timestamp'].astype(str)  # Agar plot bisa berjalan dengan baik

plt.figure(figsize=(10, 6))
sns.lineplot(x='order_purchase_timestamp', y='jumlah_pesanan', data=monthly_orders, marker='o')
plt.xticks(rotation=45)
plt.title(f'Tren Pesanan Bulanan di {selected_state} pada Tahun {selected_year}', fontsize=16)
plt.xlabel('Bulan')
plt.ylabel('Jumlah Pesanan')
st.pyplot(plt)

# Grafik 2: Demografi Pelanggan berdasarkan Kota
st.write("#### Demografi Pelanggan berdasarkan Kota")
city_counts = filtered_data['customer_city'].value_counts().reset_index()
city_counts.columns = ['customer_city', 'jumlah_pelanggan']

plt.figure(figsize=(10, 6))
sns.barplot(x='jumlah_pelanggan', y='customer_city', data=city_counts.head(10), color='royalblue')#palette='viridis')
plt.title(f'Konsentrasi Pelanggan di {selected_state} pada Tahun {selected_year}', fontsize=16)
plt.xlabel('Jumlah Pelanggan')
plt.ylabel('Kota')
st.pyplot(plt)

# Informasi tambahan tentang demografi pelanggan di negara bagian
total_customers = filtered_data['customer_unique_id'].nunique()
st.write(f"#### Jumlah Total Pelanggan Unik di {selected_state} pada Tahun {selected_year}: {total_customers}")



# Display judul ringkasan data
st.title("Ringkasan Data")


# Ringkasan data: Jumlah Pesanan per State
order_count_by_state = all_data.groupby('customer_state')['order_id'].count().reset_index()
order_count_by_state.columns = ['customer_state', 'jumlah_order']

plt.figure(figsize=(10, 5))
plt.bar(order_count_by_state['customer_state'], order_count_by_state['jumlah_order'], color='royalblue')
plt.xticks(rotation=45)
plt.xlabel('State Pelanggan')
plt.ylabel('Jumlah Order')
plt.title('Jumlah Order Berdasarkan State Pelanggan')
st.pyplot(plt)


# Ringkasan data: Tren Jumlah Pesanan per Bulan
all_data['order_year_month'] = all_data['order_purchase_timestamp'].dt.to_period('M').astype(str)
order_trend = all_data.groupby('order_year_month')['order_id'].count().reset_index()
order_trend.columns = ['order_year_month', 'jumlah_order']

plt.figure(figsize=(10, 5))
plt.plot(order_trend['order_year_month'], order_trend['jumlah_order'], marker='o', color='royalblue')
plt.xticks(rotation=45)
plt.xlabel('Tahun-Bulan')
plt.ylabel('Jumlah Order')
plt.title('Tren Jumlah Order Per Bulan')
st.pyplot(plt)


# Menampilkan ringkasan data
st.write(f"Jumlah total pesanan: {all_data['order_id'].nunique()}")
st.write(f"Jumlah pelanggan unik: {all_data['customer_unique_id'].nunique()}")