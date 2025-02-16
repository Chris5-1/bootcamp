def opening():
    print("\nNilai Siswa-Siswi SMA")
    print("="*50)

    print("1. Tampilkan data nilai siswa")
    print("2. Tambahkan data nilai siswa")
    print("3. Perubahan pada data nilai siswa")
    print("4. Hapus data nilai siswa")
    print("5. Exit/Keluar dari aplikasi")

#=============================================================

data_siswa = [
    {
        'NIS': 'XP001',
        'Nama': 'Alexander Smith',
        'Kelas Angka': '10',
        'Kelas Huruf': 'A',
        'Jurusan': 'IPA',
        'Nilai Rata-Rata': 87,
        'Jenis Kelamin': 'Laki-laki'
    },
    {
        'NIS': 'XP002',
        'Nama': 'Benjamin Taylor',
        'Kelas Angka': '10',
        'Kelas Huruf': 'B',
        'Jurusan': 'IPS',
        'Nilai Rata-Rata': 82,
        'Jenis Kelamin': 'Laki-laki'
    },
    {
        'NIS': 'XP003',
        'Nama': 'Catherine Davis',
        'Kelas Angka': '10',
        'Kelas Huruf': 'A',
        'Jurusan': 'IPA',
        'Nilai Rata-Rata': 90,
        'Jenis Kelamin': 'Perempuan'
    },
    {
        'NIS': 'XP004',
        'Nama': 'Diana Roberts',
        'Kelas Angka': '10',
        'Kelas Huruf': 'C',
        'Jurusan': 'IPS',
        'Nilai Rata-Rata': 85,
        'Jenis Kelamin': 'Perempuan'
    },
    {
        'NIS': 'XP005',
        'Nama': 'Emily Clark',
        'Kelas Angka': '10',
        'Kelas Huruf': 'B',
        'Jurusan': 'IPA',
        'Nilai Rata-Rata': 88,
        'Jenis Kelamin': 'Laki-laki'
    },
    {
        'NIS': 'XP006',
        'Nama': 'Frank Williams',
        'Kelas Angka': '10',
        'Kelas Huruf': 'A',
        'Jurusan': 'IPS',
        'Nilai Rata-Rata': 80,
        'Jenis Kelamin': 'Laki-laki'
    },
    {
        'NIS': 'XP007',
        'Nama': 'Grace Miller',
        'Kelas Angka': '10',
        'Kelas Huruf': 'C',
        'Jurusan': 'IPA',
        'Nilai Rata-Rata': 91,
        'Jenis Kelamin': 'Perempuan'
    },
    {
        'NIS': 'XP008',
        'Nama': 'Henry Wilson',
        'Kelas Angka': '12',
        'Kelas Huruf': 'B',
        'Jurusan': 'IPS',
        'Nilai Rata-Rata': 83,
        'Jenis Kelamin': 'Laki-laki'
    },
    {
        'NIS': 'XP009',
        'Nama': 'Isabella Moore',
        'Kelas Angka': '12',
        'Kelas Huruf': 'A',
        'Jurusan': 'IPA',
        'Nilai Rata-Rata': 89,
        'Jenis Kelamin': 'Perempuan'
    },
    {
        'NIS': 'XP010',
        'Nama': 'James Anderson',
        'Kelas Angka': '11',
        'Kelas Huruf': 'C',
        'Jurusan': 'IPS',
        'Nilai Rata-Rata': 84,
        'Jenis Kelamin': 'Laki-laki'
    },
]

#=============================================================

def validasi_nis(nis):
    if len(nis) != 5:
        print("NIS harus terdiri dari 2 huruf dan 3 angka")
    else:
        if not nis.startswith("XP"):    #if word[0:2] == "XP":
            print("NIS harus diawali dengan 'XP'")
        else:
            try:
                int(nis[2:])
                print("NIS valid!")
                return True
            except ValueError:
                print("NIS tidak valid!!")

def coba_kelas_gabungan(kelas_gabungan):
    try:
        if len(kelas_gabungan) != 3 or not kelas_gabungan[:2].isdigit() or not (kelas_gabungan[2].isalpha() ):
            print("Format kelas tidak valid. Harus terdiri dari 2 angka kelas dan 1 huruf bagian kelas(contoh: 10A)")
            return False
        else:
            return True
    except ValueError:
        print("Input tidak valid.")
        return False
    except KeyboardInterrupt:
        print("\nInput dibatalkan oleh user.")
        return False
    except Exception as e:
        print(f"Terjadi error lain: {e}")
        return False

def coba_kelas_angka(kelas_angka):
    try:
        int(kelas_angka)
        return True
    except ValueError:
        print("Input harus berupa angka. Masukkan ulang")
        return 
    except KeyboardInterrupt:
        print("\nInput dibatalkan oleh user.")
        return 
    except Exception as e:
        print(f"Terjadi error lain: {e}") 
        return
    
def coba_kelas_huruf(kelas_huruf):
    if len(kelas_huruf) != 1 or not kelas_huruf.isalpha():
        print("Kelas huruf harus terdiri dari tepat 1 huruf. Silahkan masukkan ulang")
        return True
    
def coba_jurusan(jurusan):
    if jurusan not in ["IPA", "IPS"]:
        print("Input tidak valid. Masukkan antara 'IPA' atau 'IPS'")
        return True

def coba_jenis_kelamin(jenis_kelamin):
    if jenis_kelamin in ["laki-laki", "laki-lak", "laki-la", "laki-l","laki-","lk", "laki", "lak", "lki", "l", "la"]:
        return "Laki-laki"
    elif jenis_kelamin in ["perempuan", "pr", "perempua", "perempu", "peremp", "perem", "pere", "per", "pe", "p"]:
        return "Perempuan"
    else:
        print("Jenis kelamin tidak valid. Harap masukkan 'laki-laki(laki/lk)' atau 'perempuan(pr)'")
        return True
#=============================================================

def tampilkan_menu():
    while True:
        opening()
        
        try:
            pilihan_menu = int(input("Masukkan pilihan yang anda inginkan(Angka 1-5): "))
        except ValueError:
            print("Input tidak valid, Harap masukkan angka 1-5.")
        except KeyboardInterrupt:
            print("\nInput dibatalkan oleh user.")
        except Exception as e:
            print(f"Terjadi error lain: {e}")

        if pilihan_menu == 1:  
            print("\n")
            cari_data()
        elif pilihan_menu == 2:
            print("\n")
            create_menu()
        elif pilihan_menu == 3:
            print("\n")
            update_menu()
        elif pilihan_menu == 4:
            print("\n")
            delete_menu()
        elif pilihan_menu == 5:
            print("Anda memilih keluar dari aplikasi ini")
            exit()
        else:
            print("\n")
            print("Input tidak valid, harap masukkan angka 1-5")

#=============================================================

def cari_data(): #READ MENU
    while True:
        print("===========Read Menu========: ")
        print("\n1. Menampilkan semua data siswa")
        print("2. Mencari data siswa dengan filter")
        print("3. Kembali ke menu utama")
        pilihan_data = input("Masukkan pilihan anda(input berupa angka 1, 2, atau 3): ").strip()
    
        try:
            pilihan_data = int(pilihan_data)
        except ValueError:
            print("Input tidak valid. SIlahkan masukkan angka 1,2, atau 3")
            return

        if pilihan_data not in [1, 2, 3]:
            print("Input tidak valid. Silahkan masukkan angka 1, 2, atau 3")
            continue

        if pilihan_data == 1:
            print("Anda memilih untuk menampilkan semua data siswa")
            tampilkan_data_siswa()
        elif pilihan_data == 2:
            print("Anda memilih untuk mencari data siswa dengan filter")
            filter_data()
        elif pilihan_data == 3:
            return

#=============================================================

def tampilkan_data_siswa():
    if not data_siswa:
        print("Data tidak ada. Kembali ke menu utama.")
        return
    print("\n========Data Nilai Siswa========")
    for urutan, siswa in enumerate(data_siswa, 1):
        print(f"{urutan}. NIS: {siswa["NIS"]}, Nama: {siswa["Nama"]}, Kelas: {siswa["Kelas Angka"]}{siswa["Kelas Huruf"]}, Jurusan: {siswa["Jurusan"]}, Nilai Rata-Rata: {siswa["Nilai Rata-Rata"]}, Jenis Kelamin: {siswa["Jenis Kelamin"]}")

#=============================================================

def filter_data():
    print("Pilih filter:")
    print("1. Berdasarkan NIS")
    print("2. Berdasarkan Nama")
    print("3. Berdasarkan Gabungan Kelas (2 Angka dan 1 Huruf)")
    print("4. Berdasarkan Kelas Angka")
    print("5. Berdasarkan Kelas Huruf")
    print("6. Berdasarkan Jurusan")
    print("7. Berdasarkan Jenis kelamin")
    print("8. Kembali ke menu sebelumnya")

    if not data_siswa:
        print("Data tidak ada. Kembali ke menu utama.")
        return
    
    while True:
        try:
            pilihan_filter = int(input("Masukkan filter yang anda inginkan(Angka 1-8): "))
        except ValueError:
            print("Input tidak valid, Harap masukkan angka 1-8.")
            continue
        except KeyboardInterrupt:
            print("\nInput dibatalkan oleh user.")
            continue
        except Exception as e:
            print(f"Terjadi error lain: {e}")
            continue

        if pilihan_filter not in range(1, 9):
            print("Pilihan filter tidak valid. Silahkan masukkan angka 1-8.\n")
            continue
        break

    if pilihan_filter == 1:
        nis = input("Masukkan NIS (format: XP diikuti 3 angka): ").strip().upper()
        print("\n")
        validasi_nis(nis)
        hasil_filter = [siswa for siswa in data_siswa if siswa['NIS'].upper() == nis]

    elif pilihan_filter == 2:
        nama = input("Masukkan nama siswa: ").strip().lower()
        hasil_filter = [siswa for siswa in data_siswa if nama in siswa['Nama'].lower()]

    elif pilihan_filter == 3:
        while True:
            kelas_gabungan = input("Masukkan kelas gabungan (contoh: 10A): ").strip().upper()
            if coba_kelas_gabungan(kelas_gabungan) == True:
                break
            else:
                continue
        hasil_filter = [siswa for siswa in data_siswa if f"{siswa['Kelas Angka']}{siswa['Kelas Huruf']}".upper() == kelas_gabungan]
    
    elif pilihan_filter == 4:
        while True:
            kelas_angka = input("Masukkan kelas angka(contoh: 10): ").strip()
            if coba_kelas_angka(kelas_angka) == True:
                break
            else:
                continue
        hasil_filter = [siswa for siswa in data_siswa if siswa['Kelas Angka'] == kelas_angka] 

    elif pilihan_filter == 5:
        while True:
            kelas_huruf = input("Masukkan kelas huruf(contoh A): ").strip().upper()
            if coba_kelas_huruf(kelas_huruf)== True:
                continue
            else:
                break
        hasil_filter = [siswa for siswa in data_siswa if siswa['Kelas Huruf'].upper() == kelas_huruf]

    elif pilihan_filter == 6:
        while True:
            jurusan = input("Masukkan jurusan(contoh IPA atau IPS): ").strip().upper()
            if coba_jurusan(jurusan) == True:
                continue
            else:
                break
        hasil_filter = [siswa for siswa in data_siswa if siswa['Jurusan'].upper() == jurusan]

    elif pilihan_filter == 7:
        while True:
            jenis_kelamin = input("Masukkan jenis kelamin(laki-laki(laki/lk)' atau 'perempuan(pr)): ").strip().lower()
            if coba_jenis_kelamin(jenis_kelamin) == True:
                continue
            else:
                jenis_kelamin = coba_jenis_kelamin(jenis_kelamin)
                break
        hasil_filter = [siswa for siswa in data_siswa if siswa['Jenis Kelamin'] == jenis_kelamin]

    elif pilihan_filter == 8:
        return

    if hasil_filter:
        print("Data ada")
        for siswa in hasil_filter:
            print(f"NIS: {siswa['NIS']}, Nama: {siswa['Nama']}, Kelas: {siswa['Kelas Angka']}{siswa['Kelas Huruf']}, Jurusan: {siswa['Jurusan']}, Nilai Rata-Rata: {siswa['Nilai Rata-Rata']}, Jenis Kelamin: {siswa['Jenis Kelamin']}")
    else:
        print("Data tidak ada")
        cari_data()
        return

#=============================================================

def create_menu():
    while True:
        print("===========Create Menu========: ")
        print("1. Membuat data baru " )
        print("2. Kembali ke menu awal")

        try:   
            pilihan_create = int(input("Masukkan pilihan (1/2): ").strip())
        except ValueError:
            print("Input harus berupa angka 1 atau 2")
        except KeyboardInterrupt:
            print("\nInput dibatalkan oleh user")
        except Exception as e:
            print(f"Terjadi error lain: {e}")

        if pilihan_create not in [1, 2]:
            print("Input harus berupa angka 1 atau 2")
            continue

        if pilihan_create == 1:
            while True: 
                nis = input("Masukkan NIS (format: XP diikuti 3 angka): ").strip().upper()
                print("\n")
                if validasi_nis(nis) == True:
                    break

            duplikasi = False
            for siswa in data_siswa:
                if siswa['NIS'] == nis:
                    duplikasi = True

            if duplikasi:
                print("NIS sudah ada dalam data. Silahkan Masukkan NIS yang berbeda\n")
                continue
            
            nama = input("Masukkan nama: ").strip()
            
            while True:
                kelas_angka = input("Masukkan kelas angka(contoh: 10): ").strip()
                if coba_kelas_angka(kelas_angka) == True:
                    break
                else:
                    continue

            while True:
                kelas_huruf = input("Masukkan huruf kelas(contohnya A atau B): ").strip().upper()
                if coba_kelas_huruf(kelas_huruf)== True:
                    continue
                else:
                    break

            while True:
                jurusan = input("Masukkan jrusan(contohnya IPA atau IPS): ").strip().upper()
                if coba_jurusan(jurusan) == True:
                    continue
                else:
                    break

            while True:
                nilai = input("Masukkan nilai rata-rata: ").strip()
                nilai = nilai.replace(',', '.')
                try:
                    nilai = float(nilai)
                    if 0 <= nilai <= 100:
                        break
                    else:
                        print("Input nilai harus 0-100!!!!!!!!!!!!!")
                except ValueError:
                    print("Input harus berupa angka! Coba lagi.")
                except KeyboardInterrupt:
                    print("\nInput dibatalkan oleh user.")
                except Exception as e:
                    print(f"Terjadi error lain: {e}")

            while True:
                jenis_kelamin = input("Masukkan jenis kelamin(laki-laki(laki/lk)' atau 'perempuan(pr)): ").strip().lower()
                if coba_jenis_kelamin(jenis_kelamin) == True:
                    continue
                else:
                    jenis_kelamin = coba_jenis_kelamin(jenis_kelamin)
                    break

            print("\nData yang diinput")
            print(f"NIS: {nis}")
            print(f"Kelas: {kelas_angka}{kelas_huruf}")
            print(f"Jurusan: {jurusan}")
            print(f"Nilai Rata-Rata: {nilai}")
            print(f"Jenis Kelamin: {jenis_kelamin}")

            save_data = input("Apakah anda ingin menyimpan datanya ke dalam list anda(Y/N)? ").strip().lower()

            if save_data in ["y", "ye", "yes", "ys"]:
                siswa_baru = {
                    'NIS': nis,
                    'Nama' : nama,
                    'Kelas Angka': kelas_angka,
                    'Kelas Huruf': kelas_huruf,
                    'Jurusan': jurusan,
                    'Nilai Rata-Rata': nilai,
                    'Jenis Kelamin': jenis_kelamin
                    }
                data_siswa.append(siswa_baru)
                print("Data berhasil disimpan")
                tampilkan_data_siswa()
                
            elif save_data in ["n", "no"]:
                print("Data gagal disimpan\n")
                continue
                
            else:
                print("Masukkan Y untuk simpan data dan N untuk membuang data")

        if pilihan_create == 2:
            return #balik ke menu utama

#=============================================================

def update_menu():

    while True:
        print("========Update Data========")
        print("1. Update data siswa")
        print("2. Kembali ke menu awal")

        try:
            pilihan_update = int(input("Masukkan pilihan (1/2): ").strip())
        except ValueError:
            print("Input harus berupa angka 1 atau 2")
            continue
        except KeyboardInterrupt:
            print("\nInput dibatalkan oleh user")
            continue
        except Exception as e:
            print(f"Terjadi error lain: {e}")
            continue

        if pilihan_update not in [1, 2]:
            print("Input harus berupa angka 1 atau 2")
            continue

        if pilihan_update == 1:
            while True:
                nis = input("Masukkan NIS (format: XP diikuti 3 angka): ").strip().upper()
                print("\n")
                if validasi_nis(nis) == True:
                    break

        if pilihan_update == 2:
            print("Kembali ke menu utama")
            return
                
        data_sama = False
        for urutan, siswa in enumerate(data_siswa):
            if siswa['NIS'] == nis:
                data_sama = True
                break

        if data_sama == False:
            print("Data tidak ditemukan")
            continue
        else:
            data_ketemu = data_siswa[urutan]

        for key, value in data_ketemu.items():
            print(f"{key}: {value}")

        lanjut_update = input("\nApakah anda ingin melanjutkan ubah data(Y/N)? ").strip().lower()
        if lanjut_update in ["y", "ye", "ys", "yes"]:
            print("Melanjutkan perubahan data")
        else:
            print("Perubahan data dibatalkan")
            return #balik ke menu utama

        daftar_kolom = ["Nama", "Kelas Angka", "Kelas Huruf", "Jurusan", "Nilai Rata-Rata", "Jenis Kelamin"]

        while True:
            input_update = input(f"Masukkan nama kolom yang ingin diubah {", ".join(daftar_kolom)}: ").title()
            if input_update not in daftar_kolom:
                print("Kolom tidak valid. Masukkan dari daftar(", daftar_kolom, ")")
                continue
            else:
                print(f"Mengubah data '{input_update}' dari NIS {nis}")
                break

        while True:
            input_baru = input(f"Masukkan data baru yang ingin diubah dari kolom {input_update}: ").strip()

            if input_update == "Kelas Angka":
                if coba_kelas_angka(input_baru):
                    break
                else:
                    continue
            
            elif input_update == "Kelas Huruf":
                if coba_kelas_huruf(input_baru):
                    continue
                else:
                    break

            elif input_update == "Jurusan":
                if coba_jurusan(input_baru) :
                    continue
                else:
                    break

            elif input_update == "Nilai Rata-Rata":
                input_baru = input_baru.replace(',', '.')
                try:
                    input_baru = float(input_baru)
                    nilai = float(nilai)
                    if 0 <= nilai <= 100:
                        break
                    else:
                        print("Input nilai harus 0-100!!!!!!!!!!!!!")
                except ValueError:
                    print("Input harus berupa angka! Coba lagi.")
                except KeyboardInterrupt:
                    print("\nInput dibatalkan oleh user.")
                except Exception as e:
                    print(f"Terjadi error lain: {e}")

            elif input_update == "Jenis Kelamin":
                if coba_jenis_kelamin(input_baru) == True:
                    continue
                else:
                    input_baru = coba_jenis_kelamin(input_baru)
                    break

            else:
                break
                
        konfirmasi = input(f"Apakah Anda yakin ingin mengubah kolom '{input_update}' di list anda?? (Y/N): ").strip().lower()
        if konfirmasi in ["y", "ye", "ys", "yes"]:
            data_siswa[urutan][input_update] = input_baru
            print("\nData berhasil diupdate")
            for key, value in data_ketemu.items():
                print(f"{key}: {value}")
            tampilkan_data_siswa()
        else:
            print("\nData gagal diupdate")

#=============================================================

def delete_menu():
    while True:
        print("========Delete Data========")
        print("1. Hapus data siswa")
        print("2. Kembali ke menu awal")

        try:
            pilihan_delete = int(input("Masukkan pilihan (1/2): ").strip())
        except ValueError:
            print("Input harus berupa angka 1 atau 2")
            continue
        except KeyboardInterrupt:
            print("\nInput dibatalkan oleh user")
            continue
        except Exception as e:
            print(f"Terjadi error lain: {e}")
            continue

        if pilihan_delete not in [1, 2]:
            print("Input harus berupa angka 1 atau 2")
            continue

        if pilihan_delete == 1:
            while True:
                nis = input("Masukkan NIS (format: XP diikuti 3 angka): ").strip().upper()
                print("\n")
                if validasi_nis(nis) == True:
                    break

        if pilihan_delete == 2:
            print("Kembali ke menu utama")
            return
        
        data_sama = False
        for urutan, siswa in enumerate(data_siswa):
            if siswa['NIS'] == nis:
                data_sama = True
                break

        if data_sama == False:
            print("Data tidak ditemukan")
            continue
        else:
            data_ketemu = data_siswa[urutan]

        for key, value in data_ketemu.items():
            print(f"{key}: {value}")

        lanjut_delete = input("Apakah anda ingin menghapus data(Y/N)? ").strip().lower()
        if lanjut_delete in ["y", "ye", "ys", "yes"]:
            print("Data berhasil dihapus")
            data_siswa.pop(urutan)
            tampilkan_data_siswa()
        else:
            print("penghapusan data dibatalkan")
            continue

#=============================================================

tampilkan_menu()