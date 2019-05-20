def response(filename, params={}):
    try:
        file = open('template/' + filename + '.html', 'r')
        data = file.read()
    except:
        print('Error in Loading/Reading file ' + filename)
        return b'null'
    for key, val in params.items():
        data = data.replace('%' + key + '%', val)
    return str.encode(data)
