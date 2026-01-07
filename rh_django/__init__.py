import pymysql

# 1. ESTA LÍNEA DEBE IR PRIMERO:
# Le dice a Django: "Usa pymysql en lugar de mysqlclient"
pymysql.install_as_MySQLdb()

# 2. AHORA SÍ podemos importar MySQLdb (porque la línea 1 lo simuló)
import MySQLdb

# 3. PARCHE DE VERSIÓN (Para engañar a Django 4.2 / 5.0)
# Si la versión detectada es muy vieja, la forzamos a una aceptable.
try:
    if MySQLdb.version_info < (2, 2, 2):
        MySQLdb.version_info = (2, 2, 2, 'final', 0)
        MySQLdb.__version__ = '2.2.2'
except AttributeError:
    pass
