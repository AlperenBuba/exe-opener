# 🍷 EXE Opener

> 🐧 Linux üzerinde Windows `.exe` dosyalarını **Wine** ile çalıştırmak için basit ve kullanışlı grafik arayüz.

---

## 📋 Platform Desteği

| Platform | Durum |
|----------|-------|
| 🐧 Linux (Debian/Ubuntu) | ✅ Destekleniyor |
| 🪟 Windows | ✅ Destekleniyor |
| 🐍 Python | 3.8+ |

---

## ✨ Özellikler

- 🍷 **Wine otomatik kurulum** — Sisteminizde Wine yoksa kurulumu sizin yerinize yapar
- 📂 **Dosya seçici** — `.exe` dosyanızı grafiksel olarak seçin
- 🖱️ **Sürükle-bırak** — `.exe` dosyasını doğrudan pencereye bırakın
- 🕘 **Son açılanlar** — Son 10 dosyayı hızla açın
- 🖥️ **Canlı log paneli** — Wine çıktısını anlık olarak siyah terminalde görüntüleyin
- 💾 **Log kaydet** — Paneldeki çıktıyı dosyaya kaydedin

---

## 🚀 Kullanım

### 🐍 Kaynaktan çalıştırma

```bash
git clone https://github.com/alperenmsl/exe-opener.git
cd exe-opener
python3 main.py
```

### 📦 Derlenmiş sürüm

#### 🐧 Linux için derleme

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
# Çıktı: dist/EXEOpener
sudo cp dist/linux/EXEOpener /usr/local/bin/exe-opener
```

#### 🪟 Windows için derleme (Wine ile)

```bash
wine python -m pip install pyinstaller
wine python -m PyInstaller --onefile --windowed --name "EXEOpener" main.py
# Çıktı: dist/windows/EXEOpener.exe
```

---

## 🔧 Bağımlılıklar

Program ilk çalıştırmada eksik bağımlılıkları **otomatik** olarak kurar:

| Bileşen | Kaynak | Amaç |
|---------|--------|------|
| 🐍 `python3-tk` | `apt` | Grafik arayüz |
| 📦 `tkinterdnd2` | `pip` | Sürükle-bırak desteği |
| 🍷 `wine` | `apt` | EXE çalıştırma |
| 🔨 `pyinstaller` | `pip` | Derleme (opsiyonel) |

---

## 📁 Proje Yapısı

```
exe-opener/
├── 🐍 main.py            — Ana uygulama dosyası
├── 📘 README.md          — Bu dosya
├── 🚫 .gitignore
├── 🐚 build.sh           — Linux derleme betiği
└── 📦 dist/
    ├── 🐧 linux/
    │   └── EXEOpener     — Linux çalıştırılabiliri
    └── 🪟 windows/
        └── EXEOpener.exe — Windows çalıştırılabiliri
```

---

## 📄 Lisans

**MIT** — İstediğiniz gibi kullanın, değiştirin, dağıtın. 🎉
