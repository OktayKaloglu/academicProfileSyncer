from enum import Enum


class InstructorNameSelector(str, Enum):
    IZMIR_YUKSEK_TEKNOLOJI_UNIVERSITY = "div > div.wpb_column.vc_col-sm-3 > div.iyte_ins-ass > div.stm-teacher-bio.stm-teacher-bio_trainer > div > div > div.stm-teacher-bio__title > a"
    EGE_UNIVERSITY = "#wrapper > div > div > div > div > div > div > p:nth-child(17)"
    DOKUZ_EYLUL_UNIVERSITY = "body > div.main-wrapper > div.container > div.span-18.last > table:nth-child(12) > tbody > tr:nth-child(2) > td > p"
    YASAR_UNIVERSITY = (
        "#main-content > div > div > div > div > div > ul > li:nth-child(1) > strong"
    )
    IZMIR_KATIP_CELEBI_UNIVERSITY = "#main-wrapper > section.content-container > section > div > div > div > div > div.row.form-group > div > div > div > table > tbody > tr:nth-child(6) > td:nth-child(9) > h4 > span > span > strong"
    IZMIR_EKONOMI_UNIVERSITY = "#coordinator_list > li > a"
