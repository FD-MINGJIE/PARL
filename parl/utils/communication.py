#   Copyright (c) 2018 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pyarrow

__all__ = ['dumps_argument', 'loads_argument', 'dumps_return', 'loads_return']


def dumps_argument(*args, **kwargs):
    """

    Serialize arguments passed to a function.

    args: 
        *args, **kwargs are general a commonly used representation of arguments in python.

    Returns:
        Implementation-dependent object in bytes.
    """
    return pyarrow.serialize([args, kwargs]).to_buffer()


def loads_argument(data):
    """
    Restore bytes data to their initial data formats.

    Args:
        data: the output of `dumps_argument`.

    Returns:
        deserialized arguments [args, kwargs]
        like the input of `dumps_argument`, args is a tuple, and kwargs is a dict 
    """
    return pyarrow.deserialize(data)


def dumps_return(data):
    """
    Serialize the return data of a function.

    Args:
        data: the output of a function.

    Returns:
        Implementation-dependent object in bytes.
    """
    return pyarrow.serialize(data).to_buffer()


def loads_return(data):
    """
    Deserialize the data generated by `dumps_return`.

    Args:
        data: the output of `dumps_return`

    Returns:
        deserialized data
    """
    return pyarrow.deserialize(data)
