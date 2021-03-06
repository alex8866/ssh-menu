from . import application

def validate_connection(connection):
    return connection.count('@') == 1 and connection.count(' ') == 0

def add_server(args, config):
    if not validate_connection(args.connection):
        ArgumentParser.exit(1, "Invalid connection string '%s' (must be user@address)" % args.connection)

    (user, address) = args.connection.split('@')
    config.add_server(args.name, user, address)
    config.save()

def remove_server(args, config):
    server = config.get_server(args.name)
    if not server:
        ArgumentParser.exit(1, "No such server '%s'" % args.name)

    config.remove_server(server.name)
    config.save()

def list_servers(args, config):
    for server in config.get_servers():
        print('%s    %s' % (server.name, server.connection_string()))

def run_app(args, config):
    print('running app...')
    print(args)
    choice = application.start(config)
    print('user chose: %s' % choice)

