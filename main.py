from database import create_connection, define_database_name
from selenium.webdriver.common.by import By
from proxy_generator import ProxyGenerator


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args,
                                                                 **kwargs)
        return cls._instances[cls]


if __name__ == '__main__':
    db_path = define_database_name("runtime")
    create_connection(db_path)
    a = ProxyGenerator()
    a.set_logger(enable=False)
    proxy_works = a.FreeProxies()
    if not proxy_works:
        print("nope")
    session = a.get_session()
    a._check_proxy(a._proxies)
