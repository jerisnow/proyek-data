import pandas as pd
import seaborn as sns
import streamlit as st

sns.set(style='dark')
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('E-Commerce Public Dashboard')
st.write('Visualization & Explanatory Analysis')

select_option = st.sidebar.selectbox(
    'Select an option:',
    ('Tingkat Kepuasan Pelanggan', 'Lokasi Geografis Pelanggan', 'Monthly Purchase Trend', 'Payment Method Trend'),
    index=0,
    key=None,
)

# Load data
customers_df = pd.read_csv("https://raw.githubusercontent.com/jerisnow/proyek-data/main/data/customers_dataset.csv")
orders_df = pd.read_csv("https://raw.githubusercontent.com/jerisnow/proyek-data/main/data/orders_dataset.csv")
tingkat_kepuasan_pelanggan = pd.read_csv("https://raw.githubusercontent.com/jerisnow/proyek-data/dsh/dashboard/tingkat_kepuasan_pelanggan.csv")
payment_method_trend = pd.read_csv("https://raw.githubusercontent.com/jerisnow/proyek-data/dsh/dashboard/payment_method.csv")

with st.sidebar:
    # Title
    st.title("Athirah Naura R.")

if select_option == 'Tingkat Kepuasan Pelanggan':
    st.header('Tingkat Kepuasan Pelanggan')
    st.write('Pertanyaan 1: Bagaimana tingkat kepuasan pelanggan berbeda-beda berdasarkan lokasi geografis mereka?')
    st.write(tingkat_kepuasan_pelanggan)

    st.bar_chart(tingkat_kepuasan_pelanggan, x='customer_state', y='review_score')
    
    tab1, tab2 = st.tabs(["Insight Output", "Kesimpulan"])
    tab1.write("Insight dari output analisis tersebut adalah sebagai berikut: Terlihat bahwa  kepuasan pelanggan berbeda-beda di setiap negara bagian. Beberapa negara bagian memiliki  kepuasan pelanggan yang tinggi dengan peringkat rata-rata di atas 4, sementara negara bagian lainnya memiliki kepuasan pelanggan yang  rendah dengan peringkat di bawah 4. Perbedaan  kepuasan pelanggan dapat dikaitkan dengan faktor-faktor yang berbeda-beda di setiap wilayah, seperti layanan pengiriman, kualitas produk, dan interaksi pelanggan. Dengan memahami perbedaan dalam kepuasan pelanggan maka dapat memudahkan dalam pengidentifikasian area potensial dimana layanan yang perlu ditingkatkan atau strategi pemasaran yang lebih dikembangkan. Analisis ini  memberikan wawasan mengenai area di mana peningkatan layanan dan peningkatan pengalaman pelanggan diperlukan untuk meningkatkan kepuasan pelanggan.")
    tab2.write("Berdasarkan analisis tingkat kepuasan pelanggan berdasarkan lokasi geografis, dapat disimpulkan bahwa persepsi pelanggan terhadap layanan perusahaan bervariasi di berbagai negara bagian. Ditemukan bahwa beberapa negara bagian memiliki tingkat kepuasan yang tinggi dengan skor ulasan rata-rata di atas 4, sementara yang lain memiliki tingkat kepuasan yang lebih rendah dengan skor ulasan di bawah 4. Perbedaan ini menunjukkan bahwa ada faktor-faktor tertentu di setiap wilayah yang mempengaruhi pengalaman pelanggan. Analisis ini memberikan wawasan tentang area mana yang mungkin memerlukan perbaikan layanan atau peningkatan strategi pemasaran untuk meningkatkan kepuasan pelanggan.")
               
elif select_option == 'Lokasi Geografis Pelanggan':
    st.header('Lokasi Geografis Pelanggan')
    st.write('Pertanyaan 2: Bagaimana hubungan antara lokasi geografis pelanggan dengan frekuensi pembelian?')
    st.write(pd.DataFrame(customers_df['customer_state'].value_counts()))
    table_2 = pd.DataFrame(customers_df['customer_state'].value_counts())

    st.bar_chart(table_2)

    tab1, tab2 = st.tabs(["Insight Output", "Kesimpulan"])
    tab1.write("Insight dari output analisis tersebut adalah sebagai berikut: Negara bagian São Paulo (SP) memiliki jumlah pelanggan tertinggi dan jauh lebih tinggi dibandingkan  negara bagian lain. Hal ini menunjukkan bahwa São Paulo memiliki pangsa pasar yang besar dalam operasional perusahaan. Negara bagian memiliki potensi pasar yang besar, dengan banyak pelanggan seperti São Paulo (SP), Rio de Janeiro (RJ), dan Minas Gerais (MG). Dengan membandingkan jumlah pelanggan di berbagai negara bagian, perusahaan dapat mengevaluasi kinerja penjualan  di setiap wilayah. Memudahkan dalam merencanakan strategi pemasaran yang lebih efektif dan mengoptimalkan alokasi sumber daya.")
    tab2.write("Berdasarkan analisis grafik distribusi pelanggan berdasarkan negara bagian, dapat disimpulkan bahwa São Paulo (SP) menjadi negara bagian dengan jumlah pelanggan tertinggi, dengan jumlah yang jauh lebih besar dibandingkan dengan negara bagian lainnya. Hal ini menunjukkan dominasi pasar yang signifikan di São Paulo dan menegaskan posisinya sebagai pusat bisnis utama di Brasil. Selain itu, negara bagian seperti Rio de Janeiro (RJ) dan Minas Gerais (MG) juga menunjukkan potensi pasar yang besar dengan jumlah pelanggan yang signifikan.")

elif select_option == 'Monthly Purchase Trend':
    st.header('Monthly Purchase Trend')
    st.write('Pertanyaan 3: Bagaimana tren pembelian bulanan dari waktu ke waktu?')
    
    orders_df['order_purchase_timestamp'] = pd.to_datetime(orders_df['order_purchase_timestamp'])
    monthly_purchase = orders_df.resample('M', on='order_purchase_timestamp').size()
    st.write(monthly_purchase)
    st.subheader('Tren Pembelian Bulanan')
    st.line_chart(monthly_purchase)

    tab1, tab2 = st.tabs(["Insight Output", "Kesimpulan"])
    tab1.write("Insight dari output analisis tersebut adalah sebagai berikut: Tren penjualan menunjukkan peningkatan yang signifikan dari September 2016 hingga November 2017. Setelah mencapai puncaknya pada November 2017, terjadi penurunan jumlah pembelian, meskipun masih ada fluktuasi yang terjadi hingga akhir periode analisis pada Oktober 2018. Penurunan yang signifikan setelah November 2017 dapat menjadi perhatian untuk mengevaluasi faktor-faktor yang mempengaruhi, seperti perubahan musiman, strategi pemasaran, atau kondisi pasar.")
    tab2.write("Dari output analisis tersebut, dapat dilihat bahwa terdapat tren kenaikan jumlah pembelian setiap bulan dari awal periode (September 2016) hingga puncaknya pada November 2017. Setelah itu, terjadi penurunan jumlah pembelian, meskipun masih relatif tinggi, dan fluktuasi jumlah pembelian terjadi hingga akhir periode analisis pada Oktober 2018. Penurunan yang signifikan terjadi setelah puncak pada November 2017, kemungkinan dipengaruhi oleh faktor-faktor musiman atau perubahan dalam strategi pemasaran atau kondisi pasar.")

elif select_option == 'Payment Method Trend':
    st.header('Payment Method Trend')
    st.write('Pertanyaan 4: Bagaimana tren penggunaan metode pembayaran yang berbeda, berubah dari waktu ke waktu?')
    st.write(payment_method_trend)
    st.line_chart(payment_method_trend)

    tab1, tab2 = st.tabs(["Insight Output", "Kesimpulan"])
    tab1.write("Insight dari output analisis tersebut adalah: Penggunaan kartu kredit (credit_card) merupakan metode pembayaran yang paling umum digunakan dari bulan ke bulan, diikuti oleh metode pembayaran voucher dan boleto. Tren penggunaan metode pembayaran boleto, kartu kredit, dan voucher cenderung meningkat dari waktu ke waktu, menunjukkan peningkatan dalam aktivitas pembelian secara keseluruhan. Penggunaan metode pembayaran debit card relatif stabil sepanjang waktu, dengan sedikit variasi dalam jumlah transaksi. Metode pembayaran not_defined hanya muncul pada bulan-bulan tertentu dan jumlahnya tidak signifikan, sehingga dapat diabaikan dalam analisis tren pembayaran.")
    tab2.write("Tren penggunaan metode pembayaran dari waktu ke waktu menunjukkan bahwa penggunaan kartu kredit (credit_card) cenderung meningkat secara signifikan dari bulan ke bulan. Selain itu, penggunaan metode pembayaran boleto dan voucher juga mengalami peningkatan yang cukup signifikan. Meskipun demikian, penggunaan metode pembayaran debit card relatif stabil, sementara metode pembayaran not_defined muncul dalam jumlah yang sangat sedikit. Kesimpulannya, terdapat kecenderungan menuju penggunaan metode pembayaran elektronik seperti kartu kredit, yang menunjukkan pergeseran preferensi konsumen terhadap pembayaran online.")
