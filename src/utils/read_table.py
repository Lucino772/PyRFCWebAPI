
def get_fields(fields: list):
    listanames = []
    for field in fields: 
        fieldname = field['FIELDNAME']
        listanames.append(fieldname)
    return listanames

def mapv(fields, values):
    listmap = []
    for value in values: 
        valuestr = value['WA'] 
        sep = valuestr.split(',')
        obj = {}
        for index, field in enumerate(fields): 
            obj[field] = sep[index].lstrip().rstrip() 
        listmap.append(obj)
    return listmap

def readtable(conn, table: str, fields, options):
    fields = [{'FIELDNAME': i} for i in fields]
    options = [{'TEXT': i} for i in options]
    result = conn.call(
        '/BODS/RFC_READ_TABLE2', 
        QUERY_TABLE = table,
        DELIMITER = ',',
        FIELDS = fields,
        OPTIONS = options
    )
    # print(result['OUT_TABLE'])
    fieldnames = get_fields(result['FIELDS'])
    values = mapv(fieldnames, result[result['OUT_TABLE']])
    return values
