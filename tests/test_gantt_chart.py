
import unittest
import tracking_dashboard.gantt_chart as gantt

class TestGanttChart(unittest.TestCase):
    def test_chart_generation(self):
        # Assume a sample file path exists
        self.assertTrue(gantt.generate_gantt_chart("config/project_plan_template.xlsx"))

if __name__ == "__main__":
    unittest.main()
