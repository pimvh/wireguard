#!/usr/bin/python3

import itertools

from ansible.errors import AnsibleFilterError

class FilterModule():
    ''' custom filter to check if something is a list '''

    def filters(self):
        return {
            "change_cidr_range_to" : self.change_cidr_range_to,
        }

    def change_cidr_range_to(self, obj, new_range):
        if not isinstance(obj, str):
            raise AnsibleFilterError('Range should be string')

        if not '/' in obj:
            raise AnsibleFilterError('should be cidr range')

        ip, range = obj.split('/')

        return '/'.join([ip, new_range])

