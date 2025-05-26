

# Projek IoT_Kelompok4
#📷 Smart Home Camera System (Face Detection via Web)

## 🧠 Deskripsi Proyek

Proyek ini merupakan sistem kamera rumah pintar berbasis **ESP32-CAM** yang mampu melakukan **deteksi wajah** dan **live video streaming** langsung ke browser melalui jaringan Wi-Fi. Sistem ini dirancang untuk mendukung *Sustainable Development Goal (SDG) 11*: *Sustainable Cities and Communities*, dengan menciptakan teknologi rumah yang lebih cerdas, aman, dan terhubung.

---

## 🎯 Tujuan

- Mendeteksi wajah secara real-time menggunakan kamera ESP32-CAM.
- Menampilkan hasil deteksi wajah dan video langsung melalui Web UI.
- Membangun sistem kamera rumah hemat biaya, efisien, dan mudah diakses via jaringan lokal.

---

## 🔧 Komponen

| Komponen      | Keterangan                        |
|---------------|-----------------------------------|
| ESP32-CAM     | Modul mikroprosesor dengan kamera |
| Wi-Fi Router  | Koneksi lokal antara ESP dan browser |
| Web Browser   | Untuk mengakses Web UI streaming  |
| Power Supply  | 5V untuk ESP32-CAM (via USB TTL atau adaptor) |

---

## 🌐 Platform

- **ESP32-CAM Web Server (built-in Arduino firmware)**
- Akses via **browser lokal** (contoh: `http://192.168.X.X`)
- Tampilan UI: tombol untuk streaming, face detection, pengaturan kamera, dsb.

---

## ⚙️ Fitur

- 🔁 Real-time **video streaming** via jaringan Wi-Fi.
- 👤 **Face Detection** secara otomatis.
- 🎛️ Pengaturan kamera langsung di Web UI (flip, brightness, quality, dll).
- 💡 Mode hemat daya dan efisien bandwidth.

---

## 💡 Kontribusi terhadap SDG 11

> *"Make cities and human settlements inclusive, safe, resilient and sustainable."*

Dengan menyediakan sistem pengawasan rumah yang **hemat biaya**, **terintegrasi**, dan **mudah digunakan**, proyek ini berkontribusi terhadap:
- Keamanan hunian berbasis teknologi cerdas.
- Peningkatan kualitas hidup masyarakat urban.
- Pemanfaatan teknologi IoT untuk lingkungan berkelanjutan.

---

## 🚀 Cara Kerja

1. ESP32-CAM dikonfigurasi melalui Arduino IDE.
2. Sistem otomatis terhubung ke jaringan Wi-Fi.
3. IP address lokal dicetak ke Serial Monitor.
4. Pengguna mengakses IP melalui browser.
5. Web UI menampilkan video stream dan hasil deteksi wajah.

---

## 📦 Instalasi & Upload

1. Hubungkan ESP32-CAM ke PC (menggunakan USB-TTL).
2. Pilih board: `AI Thinker ESP32-CAM`.
3. Gunakan partition scheme: `Huge APP (3MB No OTA)`.
4. Upload sketch `CameraWebServer.ino`.
5. Buka Serial Monitor dan salin IP lokal.
6. Akses dari browser → aktifkan streaming dan face detection.

---

## 📸 Demo Tampilan UI

![ESP32-CAM UI Screenshot](https://raw.githubusercontent.com/espressif/esp32-camera/master/examples/CameraWebServer/server_files/capture.jpg)

---

## 📚 Referensi

- [ESP32-CAM CameraWebServer Example](https://github.com/espressif/esp32-camera/tree/master/examples/CameraWebServer)
- [Arduino-ESP32 Core](https://github.com/espressif/arduino-esp32)
- [SDG 11 – United Nations](https://sdgs.un.org/goals/goal11)

---

## ✍️ Penulis

Proyek ini dibuat oleh [Christo.Z.A Dan Aom.R],.

