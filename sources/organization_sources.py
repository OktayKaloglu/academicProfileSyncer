from enum import Enum
from typing import NamedTuple


class OrganizationSource(str, Enum):
    """University source list"""

    EGE_UNIVERSITY = "https://ebp.ege.edu.tr/DereceProgramlari/Detay/1/31/2626/932001"
    DOKUZ_EYLUL_UNIVERSITY = (
        "https://debis.deu.edu.tr/ders-katalog/2021-2022/tr/bolum_1210_tr.html"
    )
    IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY = "https://ceng.iyte.edu.tr/tr/egitim/lisans-programi/lisans-egitim-plani-2018-ve-sonrasi/"
    YASAR_UNIVERSITY = "https://ce.yasar.edu.tr/dersler/"
    IZMIR_KATIP_CELEBI_UNIVERSITY = (
        "https://ceng.ikcu.edu.tr/S/16843/lisans-ogretim-plani"
    )
    IZMIR_EKONOMI_UNIVERSITY = "https://ce.ieu.edu.tr/tr/curr"
    BOGAZICI_UNIVERSITY = "https://www.cmpe.boun.edu.tr/courses/undergraduate"
    BILKENT_UNIVERSITY = "https://catalog.bilkent.edu.tr/dep/dc11.html"
    ORTA_DOGU_TEKNIK_UNIVERSITY = "https://ceng.metu.edu.tr/tr/ogretim-programi"
    ISTANBUL_TEKNIK_UNIVERSITY = (
        "https://ninova.itu.edu.tr/tr/dersler/bilgisayar-bilisim-fakultesi/"
    )
    YEDITEPE_UNIVERSITY = (
        "https://eng.yeditepe.edu.tr/tr/bilgisayar-muhendisligi-bolumu/dersler"
    )
    GALATASARAY_UNIVERSITY = "https://ects.gsu.edu.tr/tr/program/programmedetails/12"
    BAHCESEHIR_UNIVERSITY = "https://akts.bau.edu.tr/bilgipaketi/index/ogrenimprogrami/program_kodu/04012101/menu_id/p_33/tip/L/ln/tr/print/1"
    YILDIZ_TEKNIK_UNIVERSITY = (
        "http://www.bologna.yildiz.edu.tr/index.php?r=program/view&id=196&aid=3"
    )
    ISTANBUL_BILGI_UNIVERSITY = (
        "https://ects.bilgi.edu.tr/Department/Curriculum?catalog_departmentId=138530"
    )


class SpecialBaseURLEnding(str, Enum):
    DOKUZ_EYLUL_UNIVERSITY = "/ders-katalog/2021-2022/tr/"
    IZMIR_EKONOMI_UNIVERSITY = "/tr/"
    BILKENT_UNIVERSITY = "/"
