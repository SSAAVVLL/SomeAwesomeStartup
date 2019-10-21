import sqlite3


class ValidationError(Exception):
    """Ошибка валидации"""


class SQLModel:
    _DATABASE = None
    _to_sqltype = { str: "text", float: "real", int: "integer"}

    @classmethod
    def _connect(cls):
        return sqlite3.connect(cls._DATABASE)

    @classmethod
    def query(cls, query, vars=None, return_=False):
        conn = cls._connect()
        cur = conn.cursor()
        if vars:
            cur.execute(query, vars)
        else:
            cur.execute(query)

        if return_:
            response = cur.fetchall() 
        conn.commit()
        conn.close()
        return response if return_ else None


class BasicModel(SQLModel):
    _DATABASE = 'app/models/mydb.db'
    _TABLE = ''
    _FIELDS_MAPPING = {}
    _PK = ''


    def __init__(self, *args):
        self._create_table()
        pk = args[0]
        if self.has(pk):
            self._fill_data(self.get(pk))
        else:
            self._fill_data(args)


    def __getattr__(self, attr):
        if attr in self._FIELDS_MAPPING.keys():
            return None
        raise AttributeError()

    def __setattr__(self, attr, val):
        if self._validate(attr, val):
            self.__dict__[attr] = val

    def _validate(self, key, val):
        type_ = self._FIELDS_MAPPING.get(key)
        if not type_:
            return False
        if type_ != type(val):
            raise ValidationError
        return True


    def _hastable(self):
        query = "SELECT name FROM sqlite_master WHERE type = ? AND name = ?"
        result = self.query(query, ('table', self._TABLE), return_=True)
        return True if result else False


    def _attrs_tosql(self):
        return ', '. join([
                    '%s %s' % (attr, self._to_sqltype[type_])
                    for attr, type_ in self._FIELDS_MAPPING.items()
                    ])


    def _create_table(self):
        if not self._hastable():
            self.query(f'CREATE TABLE {self._TABLE} ( {self._attrs_tosql()} )')


    @classmethod
    def get(cls, pk):
        res = cls.query(f'SELECT * FROM {cls._TABLE} WHERE {cls._PK}=?', (str(pk),), return_=True)
        return res[0] if res else None

    @classmethod
    def getall(cls):
        return cls.query(f'SELECT * FROM {cls._TABLE}', return_=True)

    def _get_attrs(self):
        return tuple(str(val) for key, val in self.__dict__.items() if key[0][0] is not '_')


    def has(self, pk):
        result = self.get(pk)
        return True if result else False

    def insert(self):
        pk = self.__dict__[self._PK]
        if self.has(pk):
            msg = f'Object id already registred with {self._PK} = {pk}'
            raise ValueError(msg)
        attrs = self._get_attrs()
        attrs_refs = ', '.join('?' for i in range(len(attrs)))
        query = f'INSERT INTO {self._TABLE} VALUES ({attrs_refs})'
        self.query(query, attrs)


    # def update(self, pk):
    #     self.query(f'UPDATE {self._TABLE} SET (...) WHERE {self._PK}=?', (str(pk),))


    def delete(self, pk):
        self.query(f'DELETE FROM {self._TABLE} WHERE {self._PK}=?', (str(pk),))


    def _fill_data(self, data):
        keys = self._FIELDS_MAPPING.keys()
        for key, val in zip(keys, data):
            self.__setattr__(key, val)


