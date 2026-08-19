#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABARTILI SESSİZLİK ÖLÇERİ v42
Dünyanın en gelişmiş sessizlik ölçüm yazılımı.
Bilimsel olarak kanıtlanmış (kanıtlanmamış) sonuçlar üretir.
"""

import time
import random
import sys

def bilimsel_hesaplama(gürültü_seviyesi):
    """Kuantum seviyesinde matematiksel ispat."""
    # Formül: Sessizlik = 1 / (gürültü + epsilon)
    epsilon = 0.0000000001
    return 1 / (gürültü_seviyesi + epsilon)

def olcum_yap(olcum_sayisi=5):
    print("=" * 50)
    print("🔇 ABARTILI SESSİZLİK ÖLÇERİ v42 BAŞLATILIYOR 🔇")
    print("=" * 50)
    print("Kalibrasyon yapılıyor...")
    time.sleep(1.5)
    print("Mikrofon bulunamadı. Sorun değil, zaten sessizlik ölçüyoruz.\n")

    toplam_sessizlik = 0

    for i in range(1, olcum_sayisi + 1):
        print(f"[{i}/{olcum_sayisi}] Ölçüm alınıyor...")
        time.sleep(random.uniform(0.8, 1.5))

        # "Gerçek" gürültü seviyesi (tamamen rastgele)
        gurultu = random.uniform(0.00000001, 0.000001)
        sessizlik_skoru = bilimsel_hesaplama(gurultu)

        print(f"    Tespit edilen gürültü : {gurultu:.10f} dB")
        print(f"    Hesaplanan sessizlik  : {sessizlik_skoru:.2f} birim")
        print(f"    Durum                 : {'MÜKEMMEL SESSİZLİK' if sessizlik_skoru > 1000000 else 'Hafif bir şeyler var'}")
        print()

        toplam_sessizlik += sessizlik_skoru

    ortalama = toplam_sessizlik / olcum_sayisi

    print("=" * 50)
    print("📊 SONUÇ RAPORU")
    print("=" * 50)
    print(f"Ortalama sessizlik skoru : {ortalama:.2f}")
    print("Nihai karar              : SİZ TAMAMEN SESSİZSİNİZ.")
    print("Bilim kazanmıştır. Tebrikler.")
    print("=" * 50)

    # Gizli siyasi mesaj (asla print edilmez)
    _gizli = "bazı kararlar sessizlikle alınır ama sonuçları gürültülü olur"  # noqa

    return ortalama

def main():
    try:
        olcum_yap()
    except KeyboardInterrupt:
        print("\n\nÖlçüm yarıda kesildi. Sessizlik bozuldu. Vah vah.")
        sys.exit(1)

if __name__ == "__main__":
    main()
