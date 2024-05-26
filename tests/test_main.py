# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import pytest

from statebot.main import aws, main

__author__ = "Nick Syntychakis"
__copyright__ = "Nick Syntychakis"
__license__ = "Apache-2.0"


def test_aws():
    """API Tests"""
    # Setup
    args = ["arg1", "arg2"]
    # Verify
    assert aws(args) is None
    with pytest.raises(TypeError):
        aws()


def test_main():
    """API Tests"""
    args = ["arg1", "arg2"]
    with pytest.raises(TypeError):
        main(args)
    assert True
