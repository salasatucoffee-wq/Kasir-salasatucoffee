# Cara mendapatkan APK Salasatu Kasir

1. Buat akun GitHub (gratis) lalu buat repository baru, misalnya `salasatu-kasir`.
2. Unggah SEMUA isi folder ini ke repository, termasuk folder `.github` dan `www`.
   Di web GitHub: Add file > Upload files. Pastikan `.github/workflows/build-apk.yml` ikut terunggah.
3. Buka tab **Actions**. Workflow "Build APK" jalan otomatis (sekitar 5 menit).
   Kalau tidak jalan: pilih "Build APK" > Run workflow.
4. Setelah centang hijau, buka run tersebut, bagian **Artifacts**, unduh `salasatu-kasir-apk`.
5. Ekstrak zip-nya, kirim `app-debug.apk` ke tablet, buka, izinkan "Instal dari sumber tidak dikenal".

## Menghubungkan printer
1. Nyalakan printer, pasangkan lewat Pengaturan > Bluetooth tablet (PIN biasanya 0000 atau 1234).
2. Buka aplikasi > Owner > Pengaturan > Printer struk > Pilih printer.
3. Pilih lebar kertas (58 mm atau 80 mm), lalu tekan Tes cetak.
- Printer harus mendukung ESC/POS lewat Bluetooth klasik. Kalau printer CD335 Anda versi USB atau LAN, beri tahu saya.

## Unduh laporan PDF
Owner > Laporan harian atau Rekap bulanan > Unduh PDF. Lembar bagikan Android muncul, pilih Simpan ke File/Drive atau kirim lewat WhatsApp.

Catatan:
- Ini APK debug: bisa dipasang langsung. Untuk Google Play Store perlu APK/AAB bertanda tangan.
- targetSdk sengaja 30 agar Bluetooth printer tidak minta izin runtime tambahan di Android 12 ke atas.
- Data tersimpan di tablet itu saja (tidak sinkron antar perangkat).
