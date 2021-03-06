# MIT License
#
# Copyright (c) 2020 vincihb, michaelalbinson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sqlite3
import os.path as path


class SqlExecutor:
    def __init__(self, debug=False, db_name="papers_database.db"):
        self._local_dir = path.dirname(path.abspath(__file__))
        self._db_path = path.join(self._local_dir, '..', 'data', 'sqlite', db_name)
        self.debug = debug

        db_exists = path.isfile(self._db_path)
        self.db = sqlite3.connect(self._db_path)
        # load in the database if one doesn't exist before
        self.db.row_factory = SqlExecutor.dict_factory

        if not db_exists:
            self._exec_core()

        self.is_closed = False

    def _exec_core(self):
        cursor = self.db.cursor()
        with open(path.join(self._local_dir, '..', 'data', 'sqlite', 'sql', 'data_core.sql')) as sql:
            cursor.executescript(sql.read())

    def exec_select(self, sql, with_params=None):
        if self.is_closed:
            return None

        if self.debug:
            print(sql)

        cursor = self.db.cursor()
        if with_params is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, with_params)

        return cursor

    def exec_insert(self, sql, with_params=None):
        if self.debug:
            print(sql)

        cursor = self._exec_sql(sql, with_params)
        return cursor.lastrowid

    def exec_update(self, sql, with_params=None):
        if self.debug:
            print(sql)

        cursor = self._exec_sql(sql, with_params)
        return cursor.lastrowid

    def _exec_sql(self, sql, with_params):
        if self.is_closed:
            return None

        cursor = self.db.cursor()
        with self.db:
            if with_params is None:
                cursor.execute(sql)
            else:
                cursor.execute(sql, with_params)

        return cursor

    def close(self):
        self.db.close()
        self.is_closed = True

    @staticmethod
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
