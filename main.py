import imaplib
import email
from email.parser import BytesParser
import sys

# Configuration
source_server = 'imap.source-email.com'
source_port = 993
source_username = 'source_username'
source_password = 'source_password'

destination_server = 'imap.destination-email.com'
destination_port = 993
destination_username = 'destination_username'
destination_password = 'destination_password'

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
    source_connection = connect_to_imap(source_server, source_port, source_username, source_password)
    destination_connection = connect_to_imap(destination_server, destination_port, destination_username, destination_password)

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
