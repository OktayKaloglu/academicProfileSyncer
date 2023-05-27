from enum import Enum


class CourseCodeSelector(str, Enum):
    IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY = "div > div.vc_col-sm-9 > h1"
    EGE_UNIVERSITY = "#wrapper > div > div > div > div > div > div > table:nth-child(5) > tbody > tr > td:nth-child(1)"
    DOKUZ_EYLUL_UNIVERSITY = "body > div.main-wrapper > div.container > div.span-18.last > table:nth-child(3) > tbody > tr > td > table > tbody > tr:nth-child(2) > td:nth-child(1)"
    YASAR_UNIVERSITY = "#main-content > div > div > div > div > div > h3"
    IZMIR_KATIP_CELEBI_UNIVERSITY = "#main-wrapper > section.content-container > section > div > div > div > div > div.row.form-group > div > div > div > table > tbody > tr:nth-child(6) > td:nth-child(1) > h4 > span > span > strong"
    IZMIR_EKONOMI_UNIVERSITY = "body > main > div:nth-child(3) > div > div.col-xs-12.col-sm-12.col-md-8.col-lg-9.text-primary-color-content > h1"


class CourseNameSelector(str, Enum):
    IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY = "div > div.vc_col-sm-9 > h2"
    EGE_UNIVERSITY = "#wrapper > div > div > div > div > div > div > table:nth-child(5) > tbody > tr > td:nth-child(2)"
    DOKUZ_EYLUL_UNIVERSITY = (
        "body > div.main-wrapper > div.container > div.span-24.slider-area-inner > p"
    )
    YASAR_UNIVERSITY = "#main-content > div > div > div > div > div > h3"
    IZMIR_KATIP_CELEBI_UNIVERSITY = "#main-wrapper > section.content-container > section > div > div > div > div > div.row.form-group > div > div > div > table > tbody > tr:nth-child(6) > td:nth-child(2) > h4 > span > span > strong"
    IZMIR_EKONOMI_UNIVERSITY = "#course_name"
