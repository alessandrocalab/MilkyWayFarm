

import oracledb
from python.env.getDotEnv import get_env_required

def get_connection():
    conn=oracledb.connect(
        user=get_env_required("ORC_USER"),
        password=get_env_required("ORC_PASSWORD"),
        dsn=get_env_required("ORC_ADDRESS")
    )

    return conn
