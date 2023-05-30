from enum import Enum


class Blacklist(list, Enum):
    EGE_UNIVERSITY = ["DersOgretimPlaniPdf", "sayfa"]
    DOKUZ_EYLUL_UNIVERSITY = [
        "havuz",
        "index",
        ".pdf",
        "bolum_1210_eng.html",
        "bolum_1210_tr.html",
        "tr-",
    ]
    IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY = [
        "lidya",
        "kisiler",
        "arastirma",
        "egitim",
        "iletisim",
        "education",
        "hakkinda",
        "fakulte-dersleri",
        "math",
    ]
    YASAR_UNIVERSITY = [
        "kadro",
        "ders-plani",
        "progCourses",
        "mufredat",
        "arastirma",
        "lisans-form",
        "program-ciktilari",
        "program-yeterlilikleri",
        "konferans",
        "calistay",
        "paneller",
        "bolum-seminerleri",
        "egitim-seminerleri",
        "tarihce",
        "misyon",
        "altyapi",
        "etkinlikler",
        "category",
        "fotografvideo",
        "iletisim",
    ]
    IZMIR_KATIP_CELEBI_UNIVERSITY = []
    IZMIR_EKONOMI_UNIVERSITY = [
        "news",
        "web",
        "gamedev",
        "iletisim",
        "phone_book",
        "sss",
        "bologna",
        "staj",
        "academic_pub",
        "arastirma",
        "projeler",
        "mudek",
        "yandal",
        "cift-anadal",
        "hakkimizda",
        "misyon",
        "vizyon" "egitim-amaclari",
        "erasmus",
        "academic_personal",
        "curr",
        "pool",
        "onkosul-zinrici",
        "eur-ace-bachelor",
        "lisansustu_tezler",
        "mezunlarimizdan",
        "ozel_hukuk",
        "lojistik_yonetimi",
    ]
    BOGAZICI_UNIVERSITY = [
        "undergraduate",
        "login",
        "department",
        "prospective",
        "history",
        "faculty",
        "researchers",
        "assistants",
        "graduate",
        "swe",
        "node",
        "people",
        "content",
    ]
    BILKENT_UNIVERSITY = []
    ORTA_DOGU_TEKNIK_UNIVERSITY = [
        "konum",
        "people",
        "assistants",
        "node",
        "arastirma",
        "yazilim",
        "tez",
        "tezsiz",
        "aday",
        "dersler",
        "ogretim",
        "genel",
        "ders-listesi",
    ]
    ISTANBUL_TEKNIK_UNIVERSITY = [
        "Login",
        "yardim",
        "hakkinda",
        "herkese",
        "tum",
        "insaat",
        "mimarlik",
        "makina",
        "elektrik",
        "maden",
        "kimya",
        "gemi",
        "fen",
        "isletme",
        "ucak",
        "denizcilik",
        "tekstil",
        "turk",
        "yabanci",
        "fen-bilimleri",
        "sosyal",
        "enstitusu",
        "beb",
        "itukktc",
        "guzel",
        "avrasya",
    ]
