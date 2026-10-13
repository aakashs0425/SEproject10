"""Checks that scholarship.py does what the SATS rules say."""

import unittest

import scholarship


class ScholarshipTests(unittest.TestCase):
    # calculate_waiver
    def test_waiver_top_band(self):
        self.assertEqual(scholarship.calculate_waiver(100000, 95), 50000)

    def test_waiver_middle_band(self):
        self.assertEqual(scholarship.calculate_waiver(100000, 80), 25000)

    def test_waiver_none(self):
        self.assertEqual(scholarship.calculate_waiver(100000, 60), 0)

    def test_waiver_boundary_90(self):
        self.assertEqual(scholarship.calculate_waiver(100000, 90), 25000)

    def test_waiver_boundary_75(self):
        self.assertEqual(scholarship.calculate_waiver(100000, 75), 0)

    # calculate_stipend
    def test_stipend_merit_top(self):
        self.assertEqual(scholarship.calculate_stipend(95, "merit"), 20000)

    def test_stipend_merit_middle(self):
        self.assertEqual(scholarship.calculate_stipend(80, "merit"), 15000)

    def test_stipend_merit_low(self):
        self.assertEqual(scholarship.calculate_stipend(70, "merit"), 0)

    def test_stipend_need_based(self):
        self.assertEqual(scholarship.calculate_stipend(60, "need_based"), 10000)

    def test_stipend_need_based_low(self):
        self.assertEqual(scholarship.calculate_stipend(59, "need_based"), 0)

    def test_stipend_invalid_marks(self):
        with self.assertRaises(ValueError):
            scholarship.calculate_stipend(101, "merit")

    def test_stipend_unknown_category(self):
        with self.assertRaises(ValueError):
            scholarship.calculate_stipend(80, "sports")

    # per_capita_income
    def test_per_capita_income(self):
        self.assertEqual(scholarship.per_capita_income(240000, 4), 60000)

    def test_per_capita_income_zero_members(self):
        with self.assertRaises(ValueError):
            scholarship.per_capita_income(240000, 0)

    # is_age_allowed
    def test_age_17_allowed(self):
        self.assertTrue(scholarship.is_age_allowed(17))

    def test_age_16_not_allowed(self):
        self.assertFalse(scholarship.is_age_allowed(16))

    # application_status
    def test_status_documents_incomplete(self):
        self.assertEqual(scholarship.application_status(False, 20, True), "Documents incomplete")

    def test_status_age_not_permitted(self):
        result = scholarship.application_status(True, 16, True)
        self.assertEqual(result, "Applicant age not permitted")

    def test_status_window_closed(self):
        result = scholarship.application_status(True, 20, False)
        self.assertEqual(result, "Application window closed")

    def test_status_submitted(self):
        self.assertEqual(scholarship.application_status(True, 20, True), "Application submitted")


if __name__ == "__main__":
    unittest.main()