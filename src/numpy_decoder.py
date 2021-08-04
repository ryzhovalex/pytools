""" Tools for decoding numpy arrays from compressed bytes.
source: https://stackoverflow.com/a/63451010/14748231
"""
from __future__ import annotations
import io
import zlib
from typing import TYPE_CHECKING, Any

import numpy as np

if TYPE_CHECKING:
    from numpy import ndarray


def encode_ndarray(numpy_array: ndarray) -> bytes:
    # source: https://stackoverflow.com/a/63451010/14748231
    bytestream = io.BytesIO()
    np.save(bytestream, numpy_array)
    uncompressed = bytestream.getvalue()
    compressed = zlib.compress(uncompressed, level=1) 
    return compressed


def decode_ndarray(bytestream: bytes) -> Any:
    return np.load(io.BytesIO(zlib.decompress(bytestream)))