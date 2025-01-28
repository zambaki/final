# IP Intelligence Toplayıcı

**Proje Adı:** IP Intelligence Toplayıcı  
**Öğrenci Adı ve Numarası:** Emre Can Telli 2320191027
**Teslim Tarihi:** 28.01.2025  

---

## Proje Tanımı

Bu projenin amacı, gelen IP adreslerini güvenlik risklerine göre ayırt ederek değerlendirmek ve potansiyel tehditleri daha hızlı tespit etmektir.

### Çözülen Güvenlik Problemleri:

1. **Kötü Amaçlı IP'lerin Tespiti**
   - Kötü niyetli faaliyetlerde bulunan IP adreslerini belirler (botnet, spam, DDoS vb.).
   - IP reputation kontrolleri ile riskli bağlantılardan kaçınılabilir.

2. **Saldırı Analizi**
   - Saldırı anında veya sonrasında, IP adresi hakkında detaylı bilgi sunar (coğrafi konum, ASN, WHOIS bilgileri).
   - Saldırı kaynakları daha hızlı tespit edilir.

3. **Tehdit İstihbaratı**
   - Şüpheli IP adreslerini değerlendirme ve filtreleme imkânı sunar.
   - Tehdit veri tabanlarıyla entegrasyon yaparak proaktif güvenlik sağlar.

4. **Risk Değerlendirmesi**
   - Belirli bir IP’nin güvenilirliği hakkında risk skorları oluşturur.
   - Potansiyel tehditler önceden fark edilir.

### Hedef Kitle ve Kullanım Alanları
- **Siber Güvenlik Ekipleri**
- **Kurumsal Şirketler**
- **Küçük İşletmeler**
- **Bağımsız Araştırmacılar ve Etik Hackerlar**

---

## Kullanılan Teknolojiler

### Programlama Dili
- **Python**

### Gerekli Kütüphaneler ve Sürmeleri

1. **Veri Toplama ve API İletişimi**
   - `requests` (v2.31.0): API çağrıları ve HTTP istekleri için.
   - `json` (Standart Kütüphane): JSON verilerini işlemek için.

2. **Veri Analizi ve Manipülasyonu**
   - `pandas` (v2.0.3): IP adreslerinden gelen verileri tablolar halinde düzenlemek için.
   - `numpy` (v1.25.1): Matematiksel hesaplamalar ve veri manipülasyonu için.

3. **IP ve Ağ Analizi**
   - `ipwhois` (v1.2.0): WHOIS sorguları ve ASN analizi yapmak için.
   - `geoip2` (v4.7.0): IP adreslerinin coğrafi konumunu bulmak için.

4. **Risk ve Reputation Analizi**
   - **AbuseIPDB API:** IP reputation kontrolleri için `requests` ile entegre edilir.
   - `virustotal-api` (v1.1.11): VirusTotal API’sini kullanarak IP’lerin güvenilirliğini kontrol etmek için.

5. **Haritalama ve Görselleştirme**
   - `folium` (v0.14.0): IP adreslerinin coğrafi konumlarını haritada görselleştirmek için.
   - `matplotlib` (v3.8.0): Grafik ve görselleştirme için.

6. **Diğer Kullanışlı Kütüphaneler**
   - `argparse` (Standart Kütüphane): Komut satırı argümanlarını işlemek için.
   - `logging` (Standart Kütüphane): Hata ve bilgi mesajlarını loglamak için.

---

## Çalışma Ortamı Gereksinimleri

- **Python Sürümü:** 3.8 veya üstü.
- **Paket Yönetimi:** `pip` veya `conda`.
- **Editör:** VS Code veya Spyder (isteğe bağlı olarak değiştirilebilir).
- **İşletim Sistemi:** Linux, Windows veya macOS. (Linux tercih edilir.)

### Sanal Ortam Tavsiyesi
Bir sanal ortam oluşturup projeyi bu ortamda yürütmek en iyi yaklaşımdır:

```bash
python -m venv ip-intelligence
source ip-intelligence/bin/activate  # Windows'da: ip-intelligence\Scripts\activate
pip install requests pandas numpy ipwhois geoip2 folium matplotlib
```

7.  **API Anahtarları ve Erişimler:**

-   AbuseIPDB API: AbuseIPDB sitesinden ücretsiz veya ücretli bir API anahtarı alınmalı.
-   VirusTotal API: VirusTotal’dan kayıt olup bir API anahtarı edinmelisiniz.
-   MaxMind GeoIP: IP lokasyon verisi için bir lisans anahtarı gereklidir.
