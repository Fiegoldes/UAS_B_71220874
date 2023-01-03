print ("*"*6, "Kredit Keaktifan Mahasiswa", "*"*6)
print ("(Student Activities Credit)")
print ("1. Menambahkan Kegiatan")  
print ("2. Menampilkan Jumlah Poin")
print ("3. Keluar")
print ("-"*30)
choice = int (input ("Silahkan masukkan pilihan yang anda :"))
if choice==1 :
    vid = input ("Nama Kegiatan :")
    vad = input ("Tanggal Kegiatan :")
    print ("Pilihan Kategori Kegiatan : \n- Prestasi \n- Organisasi \n- Kepanitiaan \n- Rekognisi")
    vod = input ("Masukkan Kategori Kegiatan :")
    print ("Kegiatan berhasil ditambahkan.")
elif choice==2 :
    print ("-"*30)
    print ("Nama Kegiatan      Tanggal      Katergori       Poin")
            # if vod == [Prestasi] :
                # print (f"{vid}      {vad}       {vod}       30")
            # elif vod == [Organisasi] :
                # print (f"{vid}      {vad}       {vod}       10")
            # elif vod == [Kepanitiaan] :
                # print (f"{vid}      {vad}       {vod}       5")
            # elif vod == [Rekognisi]   :
                # print (f"{vid}      {vad}       {vod}       2")
            # else :
                # print ("ERROR!")


