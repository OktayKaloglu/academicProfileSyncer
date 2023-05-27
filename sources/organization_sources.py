from enum import Enum


class OrganizationSource(str, Enum):
    """University source list"""

    EGE_UNIVERSITY = "https://ebp.ege.edu.tr/DereceProgramlari/Detay/1/31/2626/932001"
    DOKUZ_EYLUL_UNIVERSITY = (
        "https://debis.deu.edu.tr/ders-katalog/2021-2022/tr/bolum_1210_tr.html"
    )
    IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITESI = "https://ceng.iyte.edu.tr/tr/egitim/lisans-programi/lisans-egitim-plani-2018-ve-sonrasi/"
    YASAR_UNIVERSITY = "https://ce.yasar.edu.tr/dersler/"
    IZMIR_KATIP_CELEBI_UNIVERSITY = (
        "https://ceng.ikcu.edu.tr/S/16843/lisans-ogretim-plani"
    )
    IZMIR_EKONOMI_UNIVERSITY = "https://ce.ieu.edu.tr/tr/curr"


class SpecialBaseURLEnding(str, Enum):
    DOKUZ_EYLUL_UNIVERSITY = "/ders-katalog/2021-2022/tr/"
    IZMIR_EKONOMI_UNIVERSITY = "/tr/"
