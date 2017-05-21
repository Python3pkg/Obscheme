# -*- coding: utf-8 -*-
"""
    obscheme.exceptions
    ~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Thomas Wiebe.
    :license: BSD, see LICENSE for more details.
"""


########################################################################
class ValidationError(Exception):
    pass


########################################################################
class InvariantError(ValidationError):

    #----------------------------------------------------------------------
    def __init__(self, message):
        self.message = message

    #----------------------------------------------------------------------
    def __str__(self):
        return 'Invariant found: {}'.format(self.message)


########################################################################
class FieldInvalidError(ValidationError):

    #----------------------------------------------------------------------
    def __init__(self, name):
        self.name_stack = name.split('.') if name else []

    #----------------------------------------------------------------------
    @property
    def message(self):
        # ABCmeta does not work with exceptions
        raise NotImplementedError('Subclass to implement')

    #----------------------------------------------------------------------
    def __str__(self):
        return 'Field {} invalid: {}'.format('.'.join(self.name_stack), self.message)


########################################################################
class WrongTypeError(FieldInvalidError):

    #----------------------------------------------------------------------
    def __init__(self, name, type_, expected_types):
        FieldInvalidError.__init__(self, name)
        self.type = type_
        self.expected_types = expected_types

    #----------------------------------------------------------------------
    @property
    def message(self):
        return 'Field expects types {}, but got {}'.format(
            ', '.join(self.expected_type),
            self.type)
