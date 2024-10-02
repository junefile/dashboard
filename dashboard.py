import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Mengatur judul 
st.title('Dashboard Analisis E-commerce')

data = {
    'order_month': ['2017-09', '2017-10', '2017-11', '2017-12', '2018-01', '2018-02',
                    '2018-03', '2018-04', '2018-05', '2018-06', '2018-07', '2018-08'],
    'order_count': [5342, 6285, 7404, 6102, 5650, 4950, 6100, 5823, 5893, 5021, 5110, 4892]
}

# Membuat DataFrame dari data
df = pd.DataFrame(data)

# Menambah kolom tahun berdasarkan kolom order_month
df['year'] = df['order_month'].apply(lambda x: x.split('-')[0])

# Sidebar untuk filter tahun
selected_year = st.sidebar.selectbox(
    'Pilih Tahun',
    df['year'].unique()
)

# Menampilkan data sesuai tahun yang dipilih
filtered_data = df[df['year'] == selected_year]

# Tampilkan hasil filter di dashboard dengan tampilan yang lebih rapi
st.markdown(f"### Data Pesanan untuk Tahun {selected_year}:", unsafe_allow_html=True)

# Tambahkan informasi jumlah data
st.write(f"Jumlah data pesanan untuk tahun {selected_year}: **{filtered_data.shape[0]}**")

# Tampilkan DataFrame dengan styling yang lebih sederhana
styled_df = (
    filtered_data
    .style
    .set_table_attributes('style="width: 100%; border-collapse: collapse;"')
    .set_properties(**{
        'text-align': 'center',
        'border': '1px solid #ccc',
        'background-color': '#f9f9f9',
        'padding': '10px'
    })
    .set_table_styles(
        [{
            'selector': 'th',
            'props': [('background-color', '#e0e0e0'), ('font-weight', 'bold')]
        }]
    )
    .set_caption("Tabel di atas menunjukkan jumlah pesanan per bulan untuk tahun yang dipilih.")
)

# Menampilkan dataframe yang telah distyling
st.dataframe(styled_df, use_container_width=True)

# Memberikan penjelasan tambahan jika diperlukan
st.markdown("""
### Penjelasan:
- **Data Pesanan**: Tabel ini menunjukkan jumlah pesanan yang diterima setiap bulannya untuk tahun yang dipilih.
""")

# Analisis jumlah pesanan per bulan
st.subheader("Jumlah Pesanan per Bulan")
st.write("Jumlah pesanan yang diterima per bulan terbanyak pada bulan **November 2017** dengan 7.404 pesanan.")

# Visualisasi jumlah pesanan per bulan
plt.figure(figsize=(10, 6))
sns.barplot(x='order_month', y='order_count', data=filtered_data)
plt.xticks(rotation=45)
plt.title(f'Jumlah Pesanan per Bulan untuk Tahun {selected_year}')
st.pyplot(plt)

# Data hasil analisis
customers_by_state = {
    'State': ['SP', 'RJ', 'MG', 'RS', 'PR'],
    'Customer Count': [41746, 17089, 13865, 6888, 6323]
}
orders_by_month = {
    'Month': ['2017-01', '2017-02', '2017-03', '2017-11', '2017-12'],
    'Order Count': [1500, 2000, 3000, 7404, 5000]
}

# Convert to DataFrame
customers_df = pd.DataFrame(customers_by_state)
orders_df = pd.DataFrame(orders_by_month)


# Analisis 1: Distribusi pelanggan berdasarkan negara bagian
st.header('Distribusi Pelanggan Berdasarkan Negara Bagian')
st.write('Berdasarkan analisis, negara bagian dengan pelanggan terbanyak adalah SP dengan jumlah 41.746 pelanggan.')

# Barplot untuk distribusi pelanggan berdasarkan negara bagian
st.subheader('Top 5 Negara Bagian dengan Pelanggan Terbanyak')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Customer Count', y='State', data=customers_df, palette='Blues_d', ax=ax)
st.pyplot(fig)

# Analisis 2: Tren jumlah pesanan per bulan
st.header('Tren Jumlah Pesanan per Bulan')
st.write('Berdasarkan analisis, jumlah pesanan yang diterima per bulan terbanyak terjadi pada November 2017 dengan 7.404 pesanan.')

# Lineplot untuk tren jumlah pesanan per bulan
st.subheader('Jumlah Pesanan per Bulan')
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='Month', y='Order Count', data=orders_df, marker='o', ax=ax)
plt.xticks(rotation=45)
plt.title('Tren Jumlah Pesanan per Bulan')
st.pyplot(fig)
