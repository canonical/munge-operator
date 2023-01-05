#!/usr/bin/env python3
# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.

import unittest

import ops.testing
from ops.model import ActiveStatus
from ops.testing import Harness

from charm import MungeOperatorCharm


class TestCharm(unittest.TestCase):
    def setUp(self):
        ops.testing.SIMULATE_CAN_CONNECT = True
        self.addCleanup(setattr, ops.testing, "SIMULATE_CAN_CONNECT", False)

        self.harness = Harness(MungeOperatorCharm)
        self.addCleanup(self.harness.cleanup)

    def test_start(self):
        # Simulate the charm starting
        self.harness.begin_with_initial_hooks()

        # Ensure we set an ActiveStatus with no message
        self.assertEqual(self.harness.model.unit.status, ActiveStatus())
