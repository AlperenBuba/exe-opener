# EXE Opener

Linux üzerinde Windows `.exe` dosyalarını Wine ile çalıştırmak için basit bir grafik arayüz. Sürükle-bırak, son açılanlar ve canlı log desteği sunar.

## Özellikler

- Wine ile `.exe` çalıştırma
- Dosya seçici ile `.exe` seçme
- Sürükle-bırak desteği (`tkinterdnd2`)
- Son 10 dosya geçmişi
- Canlı Wine çıktısı (siyah terminal benzeri panel)
- Log kaydetme
- Eksik bağımlılıkları PolicyKit (`pkexec`) ile grafiksel kurma

## Platform Desteği

| Platform | Çalıştırma | Derleme |
|----------|-----------|---------|
| Linux (Debian/Ubuntu) | ✅ `python3 main.py` | ✅ `build.sh` |
| Windows | ✅ Doğrudan EXE çalıştırır (Wine'siz) | ❌ |
| macOS | ❌ Test edilmedi | ❌ |

## Gereksinimler

- Python 3.8+
- Wine (Linux, yoksa script ilk çalışmada kurmayı önerir)
- `python3-tk` (yoksa script otomatik kurar)

## Kullanım

### Kaynaktan çalıştırma

```bash
python3 main.py
```

### Linux için tek dosya binary derleme

```bash
./build.sh
# Çıktı: dist/EXEOpener
```

Binary'i `/usr/local/bin/` gibi bir yola kopyalayıp sistem genelinde kullanabilirsiniz:

```bash
sudo cp dist/EXEOpener /usr/local/bin/exe-opener
```

`.exe` dosyalarını bu uygulamayla açmak için dosya ilişkilendirmesi yapabilirsiniz:

```bash
# Linux (GNOME/KDE)
xdg-mime default exe-opener.desktop application/x-ms-dos-executable
```

## Bağımlılıklar

Program ilk çalıştırmada eksik bağımlılıkları otomatik olarak kurmayı dener:

| Bileşen | Kaynak | Açıklama |
|---------|--------|----------|
| `python3-tk` | `apt` (pkexec ile) | Grafik arayüz |
| `tkinterdnd2` | `pip` | Sürükle-bırak desteği |
| `wine` | `apt` (pkexec ile) | EXE çalıştırma |
| `pyinstaller` | `pip` | Derleme (opsiyonel) |

## Proje Yapısı

```
exe-opener/
├── main.py              — Ana uygulama
├── build.sh             — Derleme betiği
├── README.md            — Bu dosya
├── LICENSE              — MIT lisansı
└── .gitignore
```

## Lisans

MIT
