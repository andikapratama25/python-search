# python-search

**Sequential and Binary Search**


  Sequential search adalah metode pencarian berurutan yang melibatkan memeriksa setiap elemen dalam daftar secara berurutan sampai elemen yang dicari ditemukan atau mencapai akhir daftar. Dimulai dari elemen pertama, elemen-elemen diurutkan satu per satu hingga elemen yang dicari ditemukan atau mencapai akhir daftar. Sequential search efektif digunakan untuk daftar yang tidak terurut atau memiliki jumlah elemen yang relatif kecil.
  
 Binary search adalah metode pencarian yang hanya berlaku pada daftar yang sudah diurutkan secara terurut meningkat. Metode ini membagi daftar menjadi dua bagian dan memeriksa apakah elemen yang dicari berada di setengah kiri atau setengah kanan daftar. Jika elemen yang dicari lebih besar dari elemen tengah daftar, maka hanya setengah kanan daftar yang perlu diperiksa. Jika lebih kecil, hanya setengah kiri yang perlu diperiksa. Binary search secara berulang membagi daftar menjadi setengahnya hingga elemen yang dicari ditemukan atau daftar menjadi kosong. Binary search sangat efisien untuk daftar yang besar karena setiap iterasi mengurangi jumlah kemungkinan pencarian sebesar setengah. Dalam pemilihan metode pencarian antara sequential search dan binary search, penting untuk mempertimbangkan apakah daftar sudah diurutkan, jumlah elemen dalam daftar, dan kompleksitas waktu yang diinginkan. Sequential search lebih sederhana dan efektif untuk daftar yang tidak terurut atau memiliki jumlah elemen yang kecil, sedangkan binary search sangat efisien untuk daftar yang sudah diurutkan dan memiliki jumlah elemen yang besar.


**Percobaan 10 atau binary_search_rotation.py**

  untuk mencari indeks rotasi terkecil dalam suatu array yang telah diputar. Pada baris pertama fungsi binary_search_rotation(data) diinisialisasi dengan dua variabel low dan high. low diatur ke nilai 0, yang merupakan indeks pertama dalam array, dan high diatur ke nilai len(data) - 1, yang merupakan indeks terakhir dalam array. Selanjutnya, dilakukan loop while yang berjalan selama low kurang dari high. Di dalam loop, dihitung nilai tengah (mid) dengan membagi jumlah low dan high lalu dibagi 2 menggunakan operator //. Kemudian dilakukan pengecekan apakah nilai data[mid] lebih besar dari data[high]. Jika iya, itu berarti indeks rotasi terkecil berada di sebelah kanan mid. Maka low diupdate menjadi mid + 1 untuk mencari di sebelah kanan. Jika nilai data[mid] tidak lebih besar dari data[high], itu berarti indeks rotasi terkecil berada di sebelah kiri atau mungkin mid itu sendiri adalah indeks rotasi terkecil. Maka high diupdate menjadi mid untuk mencari di sebelah kiri. Pada baris terakhir, fungsi binary_search_rotation dipanggil untuk mencari indeks rotasi terkecil dalam list my_list. Hasilnya disimpan dalam variabel rotation_index. Terakhir, nilai rotation_index dicetak menggunakan print dengan format string untuk memberikan output yang informatif.
  
  
**Percobaan 11 atau binary_search_most_frequent.py**

  untuk mencari elemen yang paling sering muncul dalam sebuah array terurut. Fungsi ini menggunakan algoritma pencarian biner untuk menemukan elemen dengan jumlah kemunculan terbanyak. Pada setiap iterasi, fungsi menghitung jumlah kemunculan elemen tengah saat ini dan memperbarui variabel max_count dan most_frequent jika jumlah tersebut lebih besar dari yang sebelumnya. Fungsi juga mencari elemen dengan kemunculan yang sama di sebelah kiri dan kanan elemen tengah. Proses pencarian berlanjut dengan membatasi area pencarian ke kiri atau kanan tergantung pada hasil perbandingan jumlah kemunculan dengan 1. Pencarian berhenti ketika tidak ada elemen lain yang sama dengan elemen tengah. Setelah selesai, fungsi mengembalikan elemen yang paling sering muncul dalam array. Pada contoh yang diberikan, dengan array [2, 2, 2, 4, 4, 6, 6, 6, 6, 8, 8, 8, 8, 8], elemen yang paling sering muncul adalah 8. Nilai ini kemudian dicetak menggunakan pernyataan print untuk dihasilkan.


**Percobaan 12 atau binary_search_name_list.py**

  pencarian biner untuk mencari nilai target dalam sebuah daftar data yang terurut. Inisialisasikan variabel low dengan nilai 0 sebagai indeks awal daftar dan high dengan nilai len(data) - 1 sebagai indeks akhir.
Selama low masih kurang dari atau sama dengan high, lakukan langkah-langkah berikut:
Hitung indeks tengah mid dengan menggunakan rumus (low + high) // 2.
Jika nilai pada indeks mid sama dengan nilai target, kembalikan mid sebagai indeks di mana target ditemukan.
Jika nilai pada indeks mid lebih kecil dari nilai target, perbarui low menjadi mid + 1 untuk mencari di separuh atas sisa daftar.
Jika nilai pada indeks mid lebih besar dari nilai target, perbarui high menjadi mid - 1 untuk mencari di separuh bawah sisa daftar.
Jika nilai target tidak ditemukan dalam daftar, kembalikan -1 untuk menandakan bahwa nilai tersebut tidak ditemukan.
Pada contoh yang diberikan, program meminta pengguna untuk memasukkan sebuah nama yang ingin dicari dalam daftar ['Alice', 'Bob', 'Charlie', 'Emma', 'Frank', 'George']. Fungsi binary_search kemudian dipanggil dengan daftar dan nama target sebagai argumen. Jika indeks yang dikembalikan bukan -1, artinya nama tersebut ditemukan, dan program mencetak indeks tempat nama tersebut ditemukan. Jika indeks yang dikembalikan adalah -1, program mencetak pesan yang menandakan bahwa nama tersebut tidak ditemukan.
