# -*- coding: utf-8 -*-

from ext.server import server
from ext.database import create_db

if __name__ == '__main__':
    create_db()
    server()
