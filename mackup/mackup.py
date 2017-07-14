#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
from utils.file_validator import FileValidator

class Mackup:

    @staticmethod
    def start(filename='mackup.json'):
        file_validator = FileValidator()

        if not file_validator.file_exists(filename):
            sys.exit('File "%s" not found.' % filename)

        if not file_validator.valid_json(filename):
            sys.exit('File "%s" not valid JSON file.' % filename)
