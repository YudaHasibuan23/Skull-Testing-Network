<p align="center"><img src="https://firebasestorage.googleapis.com/v0/b/yudahasibuann23.appspot.com/o/Desain%20tanpa%20judul%20(1).png?alt=media&token=18224a1b-d413-4fd7-9553-af6aa04f16c4"</p>

# Skull Testing 

Alat untuk memantau, menganalisis, dan membatasi bandwidth (upload/download) perangkat di jaringan lokal Anda tanpa akses fisik atau administratif.<br>
```Skull Testing``` menggunakan [ARP spoofing](https://en.wikipedia.org/wiki/ARP_spoofing) dan [traffic shaping](https://en.wikipedia.org/wiki/Traffic_shaping) untuk membatasi bandwidth host di jaringan.


## Syarat:
- Linux distribution
- Python 3 or greater

Kemungkinan paket python yang hilang akan diinstal selama proses instalasi.

## Installasi

```bash
git clone https://github.com/YudaHasibuan23/Skull-Testing-Network
cd Skull-Testing-Network
sudo python3 setup.py install
```

## Use

Tipe ```evillimiter``` or ```python3 bin/evillimiter``` Untuk Menjalanakan Tools.


#### Argumen Baris Perintah

| Argument | Explanation |
| -------- | ----------- |
| ```-h``` | Menampilkan pesan bantuan yang mencantumkan semua argumen baris perintah |
| ```-i [Interface Name]``` | Menentukan antarmuka jaringan (diselesaikan jika tidak ditentukan)|
| ```-g [Gateway IP Address]``` | menentukan alamat IP gateway (diselesaikan jika tidak ditentukan)|
| ```-m [Gateway MAC Address]``` | Menentukan alamat MAC gateway (diselesaikan jika tidak ditentukan)|
| ```-n [Netmask Address]``` | Menentukan netmask (diselesaikan jika tidak ditentukan)|
| ```-f``` | Menghapus konfigurasi iptables dan tc saat ini. Memastikan bahwa paket ditangani dengan benar.|
| ```--colorless``` | Menonaktifkan keluaran berwarna |

#### ```evillimiter``` Commands

| Command | Explanation |
| ------- | ----------- |
| ```scan (--range [IP Range])``` | Memindai jaringan Anda untuk mencari host online. Salah satu hal pertama yang harus dilakukan setelah memulai.<br>```--range``` memungkinkan Anda menentukan rentang IP khusus.<br>Misalnya: ```scan --range 192.168.178.1-192.168.178.40 ``` atau cukup ```scan``` untuk memindai seluruh subnet.
| ```hosts (--force)``` | Menampilkan semua host/perangkat yang dipindai sebelumnya dan informasi dasar. Menampilkan ID untuk setiap host yang diperlukan untuk interaksi.<br>```--force``` memaksa tabel untuk ditampilkan, meskipun tabel tersebut tidak sesuai dengan terminal.
| ```limit [ID1,ID2,...] [Rate] (--upload) (--download)``` | Membatasi bandwidth host yang terkait dengan ID tertentu. Tarif menentukan kecepatan internet.<br>```--upload``` hanya membatasi lalu lintas keluar.<br>```--download``` hanya membatasi lalu lintas masuk.<br>Tarif yang valid: ```bit ```, ```kbit```, ```mbit```, ```gbit```<br>Misalnya: ```batas 4,5,6 200kbit``` atau ``` batasi semua 1gbit```
| ```block [ID1,ID2,...] (--upload) (--download)``` | Memblokir koneksi internet host yang terkait dengan ID tertentu.<br>```--upload``` hanya membatasi lalu lintas keluar <br>```--download``` hanya membatasi lalu lintas masuk.
| ```free [ID1,ID2,...]``` | Membatalkan/Membuka blokir host yang terkait dengan ID tertentu. Menghapus semua batasan lebih lanjut.
| ```add [IP] (--mac [MAC])``` | Menambahkan host khusus ke daftar host. Alamat MAC akan diselesaikan secara otomatis atau dapat ditentukan secara manual.<br>Misalnya: ```tambahkan 192.168.178.24``` atau ```tambahkan 192.168.1.50 --mac 1c:fc:bc:2d:a6: 37```
| ```monitor (--interval [time in ms])``` | Memantau penggunaan bandwidth dari host yang terbatas (penggunaan saat ini, total bandwidth yang digunakan, ...).<br>```--interval``` menyetel interval setelah informasi bandwidth disegarkan dalam milidetik (default 500 md).< br> Misalnya: ```monitor --interval 1000```
| ```analyze [ID1,ID2,...] (--duration [time in s])``` | Menganalisis lalu lintas host tanpa batasan untuk menentukan siapa yang menggunakan berapa banyak bandwidth.<br>```--duration``` specifies the duration of the analysis in seconds (default 30s).<br>For example: ```analyze 2,3 --duration 120```
| ```watch``` | Sbagaimana status tontonan saat ini. Fitur jam tangan mendeteksi ketika host terhubung kembali dengan alamat IP yang berbeda.
| ```watch add [ID1,ID2,...]``` | Menambahkan host tertentu ke daftar pantauan.<br>Misalnya: ```watch add 6,7,8```
| ```watch remove [ID1,ID2,...]``` | Rmenghapus host tertentu dari daftar pantauan.<br>Misalnya: ```watch remove all```
| ```watch set [Attribute] [Value]``` | Cmengubah pengaturan jam tangan saat ini. Atribut berikut dapat diubah:<br>```range``` adalah rentang IP yang akan dipindai untuk menyambung kembali.<br>```interval``` adalah waktu tunggu di antara setiap pemindaian jaringan (dalam hitungan detik).<br>Misalnya: ```watch set interval 120```
| ```clear``` | Membersihkan Terminal Pada Linux.
| ```quit``` | Keluar Terminal.
| ```?```, ```help``` |menampilkan informasi perintah yang mirip dengan ini.

## Restrictions

- **Membatasi koneksi IPv4 saja**, karena [spoofing ARP](https://en.wikipedia.org/wiki/ARP_spoofing) memerlukan paket ARP yang hanya ada di jaringan IPv4.

<a href="https://instagram.com/yuda.hasibuan23" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="rishav_chanda" height="30" width="40" /></a>

