# Mengimpor tkinter untuk membuat GUI
import tkinter as tk

# Mengimpor modul font dari tkinter (meskipun tidak digunakan dalam kode ini)
from tkinter import font

# Mengimpor modul time untuk operasi waktu
import time

# Mengimpor threading untuk menjalankan tugas secara paralel
import threading

# Mengimpor random untuk memilih teks sampel secara acak
import random


# Mendefinisikan kelas utama untuk app
class TypeSpeedGUI:
    def __init__(self):
        # Membuat jendela utama
        self.root = tk.Tk()
        # Mengatur judul jendela
        self.root.title("Aplikasi Tes Kecepatan Mengetik")
        # Mengatur ukuran jendela menjadi 1024x768 piksel
        self.root.geometry("1024x768")

        # Daftar teks sampel untuk latihan mengetik
        self.texts = [
            "Saya sangat suka belajar pemrograman Python.",
            "Kecepatan mengetik sangat penting untuk programmer.",
            "Berlatih setiap hari membuat kita semakin mahir.",
            "Indonesia adalah negara kepulauan terbesar di dunia.",
        ]

        # Membuat frame utama untuk menampung semua widget
        self.frame = tk.Frame(self.root)
        # Memasang frame agar mengisi ruang yang tersedia
        self.frame.pack(expand=True, fill="both")

        # Membuat dan mengkonfigurasi label penjelasan dengan metrik kecepatan mengetik
        explanation_text = """
Pengukuran Kecepatan:
- CPS (Character Per Second) = Jumlah karakter per detik
- CPM (Character Per Minute) = Jumlah karakter per menit
- WPS (Words Per Second) = Jumlah kata per detik
- WPM (Words Per Minute) = Jumlah kata per menit

Catatan: 1 kata dianggap setara dengan 5 karakter
        """
        # Membuat label untuk teks penjelasan
        self.explanation = tk.Label(
            self.frame, text=explanation_text, font=("Helvetica", 12), justify=tk.LEFT
        )
        # Memasang label penjelasan dengan padding
        self.explanation.pack(pady=10)

        # Membuat label untuk teks sampel dengan pemilihan acak
        self.sample_label = tk.Label(
            self.frame,
            text=random.choice(self.texts),
            wraplength=900,
            font=("Helvetica", 18),
        )
        # Memasang label teks sampel
        self.sample_label.pack(pady=20)

        # Membuat kolom input teks
        self.input_entry = tk.Text(
            self.frame, height=4, width=50, font=("Helvetica", 16)
        )
        # Memasang kolom input
        self.input_entry.pack(pady=20)

        # Membuat label untuk menampilkan metrik kecepatan mengetik
        self.speed_label = tk.Label(
            self.frame,
            text="Kecepatan: \n0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPM",
            font=("Helvetica", 18),
        )
        # Memasang label kecepatan
        self.speed_label.pack(pady=20)

        # Membuat tombol reset
        self.reset_button = tk.Button(
            self.frame, text="Mulai Ulang", command=self.reset, font=("Helvetica", 16)
        )
        # Memasang tombol reset
        self.reset_button.pack(pady=20)

        # Menginisialisasi variabel pelacakan
        self.running = False  # Melacak apakah tes sedang berjalan
        self.time = 0.001  # Menginisialisasi timer
        self.speed = 0  # Menginisialisasi kecepatan
        self.counter = 0  # Menginisialisasi penghitung
        # Menyimpan teks sampel saat ini
        self.content_text = self.sample_label.cget("text")

        # Mengikat event penekanan tombol ke fungsi start
        self.input_entry.bind("<KeyPress>", self.start)

    # Fungsi untuk menangani awal tes mengetik
    def start(self, event):
        # Memeriksa apakah tes belum berjalan
        if not self.running:
            # Mengabaikan tombol modifier (shift, ctrl, alt)
            if not event.keycode in [16, 17, 18]:
                self.running = True
                # Memulai thread penghitung waktu
                t = threading.Thread(target=self.time_thread)
                t.start()
        # Memeriksa apakah tombol Enter ditekan
        if event.keycode == 13:
            self.check_text()

    # Fungsi untuk menangani waktu dan perhitungan kecepatan
    def time_thread(self):
        while self.running:
            try:
                # Jeda selama 0.1 detik
                time.sleep(0.1)
                # Memperbarui penghitung waktu
                self.time += 0.1
                self.counter += 1
                # Memperbarui kecepatan setiap detik (10 * 0.1s)
                if self.counter % 10 == 0:
                    # Menghitung karakter per detik
                    self.speed = len(self.input_entry.get("1.0", "end-1c")) / max(
                        self.time, 0.001
                    )
                    #                     self.input_entry.get("1.0", "end-1c"):

                    # Mengambil semua teks yang diketik oleh pengguna dari kolom input.

                    # "1.0" adalah indeks awal (baris 1, kolom 0).

                    # "end-1c" adalah indeks akhir, dikurangi 1 karakter untuk menghindari newline (\n) yang otomatis ditambahkan oleh widget Text.
                    # Menghitung berbagai metrik kecepatan
                    cps = self.speed
                    cpm = cps * 60
                    wps = cps / 5
                    wpm = wps * 60
                    # Memperbarui label kecepatan
                    self.speed_label.config(
                        text=f"Kecepatan: \n{cps:.2f} CPS\n{cpm:.2f} CPM\n{wps:.2f} WPS\n{wpm:.2f} WPM"
                    )
            except Exception as e:
                print(f"Error: {e}")
                self.running = False

    # Fungsi untuk memeriksa apakah teks yang diketik cocok dengan teks sampel
    def check_text(self):
        # Mengambil teks yang diketik dan menghapus spasi di akhir
        typed_text = self.input_entry.get("1.0", "end-1c").strip()
        # Membandingkan dengan teks sampel
        if typed_text == self.content_text:
            # Menghentikan tes
            self.running = False
            # Menampilkan metrik kecepatan akhir
            self.speed_label.config(
                text=f"Kecepatan Akhir: \n{self.speed:.2f} CPS\n{self.speed*60:.2f} CPM\n"
                + f"{self.speed/5:.2f} WPS\n{self.speed*60/5:.2f} WPM"
            )

    # Fungsi untuk reset teks
    def reset(self):
        # Mereset semua variabel pelacakan
        self.running = False
        self.time = 0.001
        self.speed = 0
        self.counter = 0
        # Mereset label kecepatan
        self.speed_label.config(
            text="Kecepatan: \n0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPM"
        )
        # Memilih teks acak baru
        self.sample_label.config(text=random.choice(self.texts))
        # Membersihkan kolom input
        self.input_entry.delete("1.0", tk.END)
        # Memperbarui teks konten
        self.content_text = self.sample_label.cget("text")


# Fungsi untuk memulai aplikasi kecepatan mengetik
def game():
    # Membuat instance TypeSpeedGUI dan memulai loop utama
    TypeSpeedGUI().root.mainloop()


# Memeriksa apakah script dijalankan secara langsung
if __name__ == "__main__":
    # Memulai permainan
    game()
