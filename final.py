import requests
from ipwhois import IPWhois


def check_ip_reputation_free(ip):
    """
    IP'nin abuse durumunu ücretsiz ve authentication gerektirmeyen API ile kontrol eder.
    """
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()

        # Abuse bilgisi olmadan reputation kontrolü:
        if "bogon" in data:
            return {"blacklisted": True, "reason": "Bogon IP detected"}
        if "org" in data and any(word in data["org"].lower() for word in ["vpn", "proxy", "hosting"]):
            return {"blacklisted": True, "reason": "Possible hosting or proxy"}
        return {"blacklisted": False}
    except Exception as e:
        print(f"Reputation kontrol hatası: {e}")
        return {"blacklisted": False}


def get_geolocation(ip):
    """
    IP'nin coğrafi konum bilgilerini getirir (ücretsiz API kullanır).
    """
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        return {
            "country": data.get("country"),
            "region": data.get("region"),
            "city": data.get("city"),
            "asn": data.get("org"),
        }
    except Exception as e:
        print(f"Geolokasyon hatası: {e}")
        return None


def analyze_asn_route(ip):
    """
    IP'nin ASN ve rota bilgilerini analiz eder (ipwhois kullanır).
    """
    try:
        obj = IPWhois(ip)
        result = obj.lookup_rdap(asn_methods=["whois", "http"])
        asn = result.get("asn")
        asn_description = result.get("asn_description")
        return {"asn": asn, "asn_description": asn_description}
    except Exception as e:
        print(f"ASN analiz hatası: {e}")
        return None


def calculate_trust_score(ip):
    """
    Tüm analizlerden güvenilirlik oranını hesaplar.
    """
    score = 100

    reputation = check_ip_reputation_free(ip)
    if reputation["blacklisted"]:
        score -= 30  # Kara liste durumu varsa puan düşür.

    geolocation = get_geolocation(ip)
    if geolocation and geolocation.get("country") != "TR":
        score -= 20  # IP yurtdışındaysa puan kesintisi.

    asn_info = analyze_asn_route(ip)
    if asn_info and asn_info.get("asn") not in ["9121", "15924", "3376"]:  # Örnek ASN'ler
        score -= 10  # Beklenen ASN değilse puan düşür.

    return max(score, 0)  # Puanın negatif olmamasını sağla.


if __name__ == "__main__":
    ip_address = input("IP Adresi Girin: ").strip()
    trust_score = calculate_trust_score(ip_address)
    print(f"IP: {ip_address} Güvenilirlik Oranı: {trust_score}%")