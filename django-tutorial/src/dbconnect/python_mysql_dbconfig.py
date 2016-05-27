from configparser import ConfigParser
# import os.path
# HERE = os.path.abspath(os.path.dirname(__file__))
# CONFIG_PATH = os.path.join(HERE, 'config.ini')

def read_db_config(filename='config.ini', section='vsource'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)
    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
    return db

print read_db_config()