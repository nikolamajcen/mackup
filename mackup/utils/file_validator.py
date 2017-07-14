#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
import json

class FileValidator:

    def file_exists(self, filename):
        return os.path.exists(filename)

    def valid_json(self, filename):
        content = self._get_json_content(filename)
        try:
            json.loads(content)
            return True
        except ValueError:
            return False

    def _get_json_content(self, filename):
        json_file = open(filename)
        content = json_file.read()
        json_file.close()
        return content
