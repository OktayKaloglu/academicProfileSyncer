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
    GEBZE_TEKNIK_UNIVERSITY = "https://abl.gtu.edu.tr/ects/?dil=tr&duzey=ucuncu&modul=lisans_derskatalogu&bolum=104&tip=lisans"
    ANKARA_UNIVERSITY = "http://bbs.ankara.edu.tr/Ders_Plani.aspx?bno=4358&bot=1992"
    BASKENT_UNIVERSITY = "http://truva.baskent.edu.tr/bilgipaketi/?dil=TR&menu=akademik&inner=katalog&birim=682"
    ISTANBUL_UNIVERSITY_CERRAHPASA = "https://ebs.iuc.edu.tr/home/dersprogram/?id=1092"
    MARMARA_UNIVERSITY = "https://meobs.marmara.edu.tr/Mufredat/DersListesi?organizasyonId=97&organizasyonProgramId=78&programMufredatId=4199&mufredatTurId=932001&birimOrganizasyonId=0"


class SpecialBaseURLEnding(str, Enum):
    DOKUZ_EYLUL_UNIVERSITY = "/ders-katalog/2021-2022/tr/"
    IZMIR_EKONOMI_UNIVERSITY = "/tr/"
    BILKENT_UNIVERSITY = "/"
    ANKARA_UNIVERSITY = "/"
