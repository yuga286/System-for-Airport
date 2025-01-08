# Copyright (c) 2024, yugandhara and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase, UnitTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record depdendencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class UnitTestDemo(UnitTestCase):
	"""
	Unit tests for Demo.
	Use this class for testing individual functions and methods.
	"""
	# def test_get_item(self):
	# 	response = frappe.get_doc("demo", "Test Item")
	# 	self.assertEqual(response.item_name, "Test Item")
	pass


class IntegrationTestDemo(IntegrationTestCase):
	"""
	Integration tests for Demo.
	Use this class for testing interactions between multiple components.
	"""

	pass
