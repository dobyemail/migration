import imaplib
import email
import argparse
import sys

def connect_to_imap(server, port, username, password):
    try:
        connection = imaplib.IMAP4_SSL(server, port)
        connection.login(username, password)
        return connection
    except imaplib.IMAP4.error as e:
        print(f"Unable to connect to server {server}. Error: {e}")
        sys.exit(1)

def migrate_emails(source_connection, destination_connection, folder):
    try:
        source_connection.select(folder)
        typ, data = source_connection.search(None, 'ALL')
        if typ != 'OK':
            print(f"No messages found in {folder}")
            return

        for num in data[0].split():
            typ, msg_data = source_connection.fetch(num, '(RFC822)')
            if typ != 'OK':
                print(f"Error fetching message {num} from {folder}")
                continue

            msg = msg_data[0][1]
            typ, data = destination_connection.append(folder, '', imaplib.Time2Internaldate(None), msg)
            if typ != 'OK':
                print(f"Error appending message {num} to {folder}")

    except Exception as e:
        print(f"Error in migrating emails from folder {folder}: {e}")

def get_folders(connection):
    typ, data = connection.list()
    if typ != 'OK':
        print("Error listing folders")
        sys.exit(1)
    
    folders = []
    for folder in data:
        folders.append(folder.decode().split(' "/" ')[1].strip('"'))
    return folders

def main():
    parser = argparse.ArgumentParser(description='IMAP email migration script')
    parser.add_argument('--host1', required=True, help='Source IMAP server')
    parser.add_argument('--port1', type=int, default=993, help='Source IMAP server port')
    parser.add_argument('--user1', required=True, help='Source IMAP username')
    parser.add_argument('--password1', required=True, help='Source IMAP password')

    parser.add_argument('--host2', required=True, help='Destination IMAP server')
    parser.add_argument('--port2', type=int, default=993, help='Destination IMAP server port')
    parser.add_argument('--user2', required=True, help='Destination IMAP username')
    parser.add_argument('--password2', required=True, help='Destination IMAP password')

    args = parser.parse_args()

    source_connection = connect_to_imap(args.host1, args.port1, args.user1, args.password1)
    destination_connection = connect_to_imap(args.host2, args.port2, args.user2, args.password2)

    source_folders = get_folders(source_connection)

    for folder in source_folders:
        print(f"Migrating folder: {folder}")
        try:
            destination_connection.create(folder)
        except:
            print(f"Folder {folder} might already exist in the destination account")
        
        migrate_emails(source_connection, destination_connection, folder)

    # Logout
    source_connection.logout()
    destination_connection.logout()
    print("Migration completed successfully")

if __name__ == "__main__":
    main()
