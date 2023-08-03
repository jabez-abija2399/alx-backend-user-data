#!/usr/bin/env python3
""" Regex-ing, Log formatter, Create logger, Connect to secure database,
    Read and filter data """
import re
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')
""" containing the fields from user_data.csv that are considered PII. """


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

if __name__ == "__main__":
    main()