#!/usr/bin/env python3
""" Regex-ing, Log formatter, Create logger, Connect to secure database,
    Read and filter data """
from typing import List
import re
import logging
import os
import mysql.connector
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')
""" containing the fields from user_data.csv that are considered PII. """


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ constructor """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ filter values in incoming log records """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)




if __name__ == "__main__":
    main()
