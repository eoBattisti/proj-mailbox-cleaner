import imaplib
import email
from email.header import decode_header
import logging

from defaults import USERNAME, PASSWORD, EMAILS_TO_EXCLUDE


class Cleaner:

    def __init__(self) -> None:
        self.imap = imaplib.IMAP4_SSL('imap.gmail.com')
        self.imap.login(user=USERNAME, password=PASSWORD)
        self.imap.select('INBOX')
        self.clean()

    def clean(self) -> None:
        logging.info('Started the cleaning')
        for sender in EMAILS_TO_EXCLUDE:
            status, messages = self.imap.search(None, f'FROM "{sender}"')
            messages = messages[0].split(b' ')
            for mail in messages:
                if not mail:
                    continue
                self.imap.store(mail, "+FLAGS", "\\Deleted")
        self.imap.expunge()
        self.imap.close()
        logging.info('Email cleaned...')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename='cleaner.log', filemode='a',
                        format='%(asctime)s - [%(levelname)s] - %(message)s',datefmt='%d/%m/%Y %H:%M:%S')
    Cleaner()
