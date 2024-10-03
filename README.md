## Proyek Analisis Data: [E-Commerce Public Dataset]

Proyek ini bertujuan untuk menganalisis distribusi jumlah pelanggan dan pesanan berdasarkan data pesanan. Analisis meliputi distribusi pelanggan berdasarkan negara bagian dan tren pesanan per bulan. Dashboard ini dibuat menggunakan Streamlit untuk visualisasi hasil analisis.

## Hasil Analisis
- **Distribusi Jumlah Pelanggan di Setiap Negara Bagian**: Negara bagian dengan jumlah pelanggan terbanyak adalah SP dengan 41.746 pelanggan.
- **Jumlah Pesanan yang Diterima per Bulan**: Bulan dengan jumlah pesanan terbanyak adalah November 2017 dengan 7.404 pesanan.

## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```
## Setup Environment - Shell/Terminal
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run dashboard.py
```
