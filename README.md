# EXE Opener - Wine Launcher

> Linux üzerinde Windows `.exe` dosyalarini Wine ile calistirmak icin basit ve kullanisli grafik arayuz.

| Platform | Durum |
|----------|-------|
| Linux (Debian/Ubuntu) | Destekleniyor |
| Windows | Yalnizca kaynak koddan calisir (Wine yok) |
| Python | 3.8+ |

---

## Ozellikler

- **Wine otomatik kurulum** -- Sisteminizde Wine yoksa kurulumu sizin yerinize yapar
- **Dosya secici** -- `.exe` dosyanizi grafiksel olarak secin
- **Surukle-birak** -- `.exe` dosyasini dogrudan pencereye birakin
- **Son acilanlar** -- Son 10 dosyayi hizlica acin
- **Canli log paneli** -- Wine ciktisini anlik olarak siyah terminalde goruntuleyin
- **Log kaydet** -- Paneldeki ciktiyi dosyaya kaydedin

---

## Kullanim

### Kaynaktan calistirma

```bash
git clone https://github.com/alperenmsl/exe-opener.git
cd exe-opener
python3 main.py
```

### Derlenmis surum

#### Linux icin derleme

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
# Cikti: dist/main
sudo cp dist/main /usr/local/bin/exe-opener
```

#### Windows icin derleme

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "EXEOpener" main.py
# Cikti: dist/EXEOpener.exe
```

Not: Windows uzerinde calistirildiginda Wine degil, dogrudan `.exe` dosyasini calistirir.

---

## Bagimliliklar

Program ilk calistirmada eksik bagimliliklari otomatik olarak kurar:

| Bilesen | Kaynak | Amac |
|---------|--------|------|
| `python3-tk` | apt | Grafik arayuz |
| `tkinterdnd2` | pip | Surukle-birak destegi |
| `wine` | apt | EXE calistirma |
| `pyinstaller` | pip | Derleme (opsiyonel) |

---

## Proje Yapisi

```
exe-opener/
  main.py      -- Ana uygulama dosyasi
  README.md    -- Bu dosya
  .gitignore
```

---

## Lisans

MIT
