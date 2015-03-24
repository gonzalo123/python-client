# coding: utf-8
from coreapi.codecs import JSONCodec
from coreapi.document import Array, Document, Link, Object, required
from coreapi.document import remove, replace, deep_remove, deep_replace
from coreapi.exceptions import ParseError, TransportError
from coreapi.transport import transition


__version__ = '0.2.0'
__all__ = [
    'JSONCodec',
    'Array', 'Document', 'Link', 'Object', 'required',
    'remove', 'replace', 'deep_remove', 'deep_replace',
    'ParseError', 'TransportError',
    'HTTPTransport',
    'load', 'dump', 'get'
]


def load(bytestring):
    codec = JSONCodec()
    return codec.load(bytestring)


def dump(document, verbose=False):
    codec = JSONCodec()
    return codec.dump(document, verbose=verbose)


def get(url):
    return transition(url, 'follow')
