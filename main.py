from database import create_connection, define_database_name
from navigator import Navigator

if __name__ == '__main__':
    db_path = define_database_name("runtime")
    create_connection(db_path)
    # a = ProxyGenerator()
    # a.set_logger(enable=False)
    # proxy_works = a.FreeProxies()
    # if not proxy_works:
    #    print("nope")
    # session = a.get_session()
    # a._check_proxy(a._proxies)
    a = Navigator()
    a.set_logger(enable=True)
    # a.use_proxy()
    b = a.search_organization("https://ebp.ege.edu.tr/DereceProgramlari/Detay/1/31/2626/932001")
    # EGE_UNIVERSITY = "https://ebp.ege.edu.tr/DereceProgramlari/Detay/1/31/2626/932001"
