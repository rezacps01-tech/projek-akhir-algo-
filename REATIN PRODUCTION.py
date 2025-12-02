import csv
import pandas as pd
import os
from tabulate import tabulate

def login():
    os.system('cls')
    teks = """
    
██████╗ ███████╗ █████╗ ████████╗██╗███╗   ██╗    ██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║████╗  ██║    ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
██████╔╝█████╗  ███████║   ██║   ██║██╔██╗ ██║    ██████╔╝██████╔╝██║   ██║██║  ██║██║   ██║██║        ██║   ██║██║   ██║██╔██╗ ██║
██╔══██╗██╔══╝  ██╔══██║   ██║   ██║██║╚██╗██║    ██╔═══╝ ██╔══██╗██║   ██║██║  ██║██║   ██║██║        ██║   ██║██║   ██║██║╚██╗██║
██║  ██║███████╗██║  ██║   ██║   ██║██║ ╚████║    ██║     ██║  ██║╚██████╔╝██████╔╝╚██████╔╝╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                                                                   """
    print(teks)
    print("===========[LOGIN]============")

    username = input("Masukkan Username:")
    password = input("Masukkan Password:")

    user = []
    with open('user.csv','r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            user.append({'username': row[0], 'password': row[1], 'role': row[2]})

    for i in user:
        if i['username'] == username and i['password'] == password:
            if i['role'] == 'owner':
                print("Selamat Datang Owner")
                input("Klik Enter Untuk Melanjutkan")
                return menu_owner(username)
            else:
                print(f"Selamat Datang, {i['username']}")
                input("Klik Enter Untuk Melanjutkan")
                return menu_kasir(username)

    print("Username atau password salah!")
    input("Klik Enter Untuk Melanjutkan")
    return login()


def kelola_produk(role, username):
    os.system('cls')
    data_produk = pd.read_csv('data_pupuk.csv')
    data_produk.index += 1

   
    print("==== KELOLA PRODUK ====")
    print("1. Tambahkan Produk")
    print("2. Hapus Produk")
    print("3. Info Produk")
    print("4. Kembali")

  

    pilihan = input("Pilih menu (1/2/3/4): ")
    if pilihan == "1":
        tambahkan_produk(data_produk)
    elif pilihan == "2":
        hapus_produk(data_produk)
    elif pilihan == "3":
        info_produk(data_produk)
    elif pilihan == "4":
        os.system('cls')
        if role == "owner":
            menu_owner(username)
        else:
            menu_kasir(username)
    else:
        input("Masukkan input yang benar. Tekan enter untuk melanjutkan")
        kelola_produk(role, username)


def tambahkan_produk(data_produk):
    os.system('cls')
    print("=== TAMBAH PRODUK ===")
    print("Ketik 0 untuk kembali ke menu sebelumnya\n")

    while True:
        try:
            nama_produk = input("Masukkan nama produk: ").capitalize()
            if nama_produk == "0":     
                return        
                     
            kategori_produk = input("Masukkan kategori produk: ")
            harga_produk = float(input("Masukkan harga produk: "))
            stok_produk = float(input("Masukkan stok produk: "))
            deskripsi_produk = input("Masukkan deskripsi produk: ")

            if (data_produk['Nama_Produk'] == nama_produk).any():
                print("Produk sudah ada, masukkan produk lain.")
                input("Klik enter untuk melanjutkan")
                continue

            menambahkan_produk = pd.DataFrame({
                "Nama_Produk": [nama_produk],
                "Kategori": [kategori_produk],
                "Harga": [harga_produk],
                "Stok(kg)": [stok_produk],
                "Deskripsi": [deskripsi_produk]
            })

            data_produk = pd.concat([data_produk, menambahkan_produk], ignore_index=True)
            data_produk.to_csv("data_pupuk.csv", index=False)

            print("Produk berhasil ditambahkan")
            break
        except ValueError:
            print("Input tidak valid!!")
    input("Klik enter untuk melanjutkan")


def hapus_produk(data_produk):
    os.system('cls')
    print("ketik 0 untuk kembali\n")
    print(tabulate(data_produk, headers='keys', tablefmt='fancy_grid'))

    
    while True:
        try:
            index_produk = int(input("Masukkan index produk yang ingin dihapus: "))

            if index_produk == 0:
                return
            
            if 1 <= index_produk <= len(data_produk):
                data_produk = data_produk.drop(data_produk.index[index_produk - 1])
                data_produk.to_csv('data_pupuk.csv', index=False)
                print("Produk berhasil dihapus")
                break
            else:
                print("Index tidak valid!!")
        except ValueError:
            print("Input tidak valid!! Masukkan angka")
    input("Klik enter untuk melanjutkan")



def info_produk(data_produk):
    os.system('cls')
    data_produk.index += 0
    print("==== INFO PRODUK ====\n")
    print(tabulate(data_produk, headers='keys', tablefmt='fancy_grid'))
    input("\nTekan Enter untuk kembali")




def catatan_penjualan(username):
    os.system('cls')
    produk = pd.read_csv('data_pupuk.csv')
    penjualan = pd.read_csv('data_penjualan.csv')

    tampilkan_produk = produk.copy()
    tampilkan_produk.index += 1
    kolom_tertentu = tampilkan_produk[['Nama_Produk', 'Kategori', 'Harga', 'Stok(kg)', 'Deskripsi']]
    print(tabulate(kolom_tertentu, headers='keys', tablefmt='fancy_grid'))

    print("\nketik 0 untuk kembali")

    while True:
        try:
            jumlah_jenis = int(input("\nJumlah jenis produk yang ingin dibeli: "))

            if jumlah_jenis == 0:
                return
            
            if jumlah_jenis <= 0 or jumlah_jenis > len(produk):
                print("Jumlah jenis tidak valid!")
                continue

            keranjang = []
            total_belanja = 0
            total_keuntungan = 0

            for i in range(jumlah_jenis):
                print(f"\nPembelian ke-{i+1}")
                while True:
                    try:
                        nomor_produk = int(input("Masukkan nomor produk: ")) - 1
                        if nomor_produk < 0 or nomor_produk >= len(produk):
                            print("Nomor produk tidak valid!")
                            continue

                        jumlah = float(input("Masukkan jumlah (kg): "))
                        if jumlah <= 0:
                            print("Jumlah harus lebih besar dari 0!")
                            continue

                        stok = produk.iloc[nomor_produk]['Stok(kg)']
                        if jumlah > stok:
                            print(f"Stok tidak cukup! Stok tersedia: {stok}")
                            continue

                        nama = produk.iloc[nomor_produk]['Nama_Produk']
                        harga = produk.iloc[nomor_produk]['Harga']
                        keuntungan_per_kg = float(produk.iloc[nomor_produk]['Harga'])
                        subtotal = jumlah * harga
                        subtotal_keuntungan = jumlah * keuntungan_per_kg

                        keranjang.append({
                            'produk': nama,
                            'jumlah': jumlah,
                            'harga': harga,
                            'subtotal': subtotal,
                            'keuntungan' : subtotal_keuntungan
                        })

                        total_belanja += subtotal
                        total_keuntungan += subtotal_keuntungan


                        produk.at[nomor_produk, 'Stok(kg)'] = stok - jumlah
                        break
                    except ValueError:
                        print("Input tidak valid!")
            os.system('cls')

            print("\n=== STRUK PEMBELIAN ===")
            print(f"Kasir: {username}")
            for i in keranjang:
                print(f"\nProduk: {i['produk']}")
                print(f"Jumlah: {i['jumlah']} kg")
                print(f"Harga: Rp {i['harga']:,.0f}")
                print(f"Subtotal: Rp {i['subtotal']:,.0f}")
            print(f"\nTotal Pembelian: Rp {total_belanja:,.0f}")

            for item in keranjang:
                new_row = pd.DataFrame({
                    'tanggal': [pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")],
                    'produk': [item['produk']],
                    'jumlah': [item['jumlah']],
                    'harga': [item['harga']],
                    'total': [item['subtotal']],
                    'keuntungan': [item['keuntungan']]
                })
                penjualan = pd.concat([penjualan, new_row], ignore_index=True)

            produk.to_csv('data_pupuk.csv', index=False)
            penjualan.to_csv('data_penjualan.csv', index=False)

            print("\nTotal Pembelian:", total_belanja)
            input("Tekan Enter untuk melanjutkan")
            break

        except ValueError:
            print("Input tidak valid!")


def kelola_akun_kasir():
    os.system('cls')
    akun_kasir = pd.read_csv('user.csv')
    akun_kasir.index += 1
    print(tabulate(akun_kasir, headers='keys', tablefmt='fancy_grid'))

    print("==== KELOLA AKUN KASIR ====")
    print("1. Tambahkan Akun Kasir")
    print("2. Hapus Akun Kasir")
    print("3. kembali")

    pilihan = input("Pilihan Menu (1/2/3): ")

    if pilihan == '1':
        tambahkan_akun_kasir()
    elif pilihan == '2':
        hapus_akun_kasir()
    elif pilihan == '3':
        return
    else:
        print("Pilihan tidak valid!")
        input("Klik enter untuk melanjutkan")
        kelola_akun_kasir()


def tambahkan_akun_kasir():
    os.system('cls')
    akun_kasir = pd.read_csv('user.csv')
    print("\nketik 0 untuk kembali")
    
    username = input("Masukkan username baru: ")

    if username == "0":
        return
    
    password = input("Masukkan password baru: ")

    if (akun_kasir['username'] == username).any():
        print("Akun sudah ada!")
        input("Klik enter untuk melanjutkan")
        return

    new_row = pd.DataFrame({
        'username': [username],
        'password': [password],
        'role': ['kasir']
    })

    akun_kasir = pd.concat([akun_kasir, new_row], ignore_index=True)
    akun_kasir.to_csv('user.csv', index=False)

    print("Akun kasir berhasil ditambahkan!")
    input("Klik enter untuk melanjutkan")


def hapus_akun_kasir():
    os.system('cls')
    akun_kasir = pd.read_csv('user.csv')
    akun_kasir.index += 1
    print(tabulate(akun_kasir, headers='keys', tablefmt='fancy_grid'))
    print("\nKetik 0 untuk kembali") 

    while True:
        try:
            index_hapus = int(input("Masukkan index akun kasir yang ingin dihapus: "))
            if index_hapus == 0:
                return
            
            if 1 <= index_hapus <= len(akun_kasir):
                akun_kasir = akun_kasir.drop(akun_kasir.index[index_hapus - 1])
                akun_kasir.to_csv('user.csv', index=False)
                print("Akun kasir berhasil dihapus!")
                break
            else:
                print("Index tidak valid!")
        except ValueError:
            print("Input tidak valid! Harus angka.")

        input("Klik enter untuk melanjutkan")


def laporan_keuntungan():
    while True:
        os.system('cls')
        print("==== LAPORAN KEUNTUNGAN ====")
        print("1. Laporan keuntungan Produk")
        print("2. Laporan Per Periode")
        print("3. total Keseluruhan")
        print("4. Kembali")

        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            penjualan = pd.read_csv('data_penjualan.csv')

            laporan = penjualan.groupby('produk').agg({
                'jumlah': 'sum',
                'keuntungan': 'sum'
            }).reset_index()

            laporan.index += 1
            print(tabulate(laporan, headers='keys', tablefmt='fancy_grid'))

        elif pilihan == '2':
            penjualan = pd.read_csv('data_penjualan.csv')

            print("\nFormat tanggal: DD-MM-YYYY")

            try:
                start_str = input("Tanggal awal: ")
                end_str = input("Tanggal akhir: ")

                start_date = pd.to_datetime(start_str, format='%d-%m-%Y')
                end_date = pd.to_datetime(end_str, format='%d-%m-%Y')

                filtered = penjualan[
                    (pd.to_datetime(penjualan['tanggal']) >= start_date) &
                    (pd.to_datetime(penjualan['tanggal']) <= end_date)
                ]

                if len(filtered) == 0:
                    print("Tidak ada transaksi pada periode tersebut.")
                else:
                    laporan = filtered.groupby(filtered["tanggal"]).agg({
                        'keuntungan': 'sum'
                    }).reset_index()

                    laporan.index += 1
                    print(tabulate(laporan, headers='keys', tablefmt='fancy_grid'))
                    print("Total Keuntungan:", laporan['keuntungan'].sum())

            except ValueError:
                print("Format tanggal salah!")

        elif pilihan == '3':
            penjualan = pd.read_csv('data_penjualan.csv')
            total = penjualan['keuntungan'].sum()
            print("Total Keuntungan Keseluruhan:", total)

        elif pilihan == '4':
            return

        input("\nTekan Enter untuk melanjutkan")


def lihat_data_penjualan():
    os.system('cls')
    print("==== DATA PENJUALAN ====\n")

    try:
        data = pd.read_csv('data_penjualan.csv')

        if data.empty:
            print("Belum ada data penjualan.")
        else:
            data.index += 1
            print(tabulate(data, headers='keys', tablefmt='fancy_grid'))
    except ValueError:
        print("File data_penjualan.csv tidak ditemukan!")

    input("\nTekan Enter untuk kembali")



    


def keluar():
    os.system('cls')
    print("Anda telah keluar. Terima kasih!")
    exit()


def menu_kasir(username):
    while True:
        os.system('cls')
        print(f"===================== MENU UTAMA (Kasir: {username}) =====================")
        print("1. Catatan Penjualan")
        print("2. kelola produk")
        print("3. Keluar")

        pilihan = input("Pilih Menu (1/2/3): ")

        if  pilihan == "1":
            catatan_penjualan(username)
        elif pilihan == "2":
            kelola_produk("kasir",username)
        elif pilihan == "3":
            keluar()
        else:
            print("Pilihan tidak valid!")
            input("Klik enter untuk melanjutkan")


def menu_owner(username):
    while True:
        os.system('cls')
        print(f"===================== MENU UTAMA (Owner: {username}) =====================")
        print("1. Kelola produk")
        print("2. Catatan penjualan")
        print("3. Laporan keuntungan")
        print("4. Kelola akun kasir")
        print("5. Lihat data penjualan")
        print("6. Keluar")

        pilihan = input("Pilih menu (1/2/3/4/5): ")


        if pilihan == '1':
            kelola_produk("owner", username)
        elif pilihan == '2':
            catatan_penjualan(username)
        elif pilihan == '3':
            laporan_keuntungan()
        elif pilihan == '4':
            kelola_akun_kasir()
        elif pilihan == '5':
            lihat_data_penjualan()
        elif pilihan == '6':
            keluar()
        else:
            print("Pilihan tidak valid!")
            input("\nTekan Enter untuk melanjutkan")


login()

