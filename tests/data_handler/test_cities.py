from collections import defaultdict

from tests.data_handler.data_handler_tests_utils import DataHandlerTestsUtils
from covid19_il.data_handler.data_handlers.cities import Cities
from covid19_il.data_handler.enums.resource_id import ResourceId


class TestCities(DataHandlerTestsUtils):
    """ Tests for Cities Data Handler Class.

    Methods:
        setUp(self): Announce of starting the class's tests, initialize & verify cities data handler's instance.
        _check_base_step_of_all_methods(self): General base test for all methods.
        test_cities_by_date(self): Tests results of tests cities by specific date and its results as city's tuples.
        test_cases_statistics(self): Tests the test cases statistics data & type.

    """

    def setUp(self) -> None:
        """ Announce of starting the class's tests, initialize & verify Cities data handler's instance """
        print("testing Cities Class...")
        self.data_handler_1 = self._init_mocked_data_handler(json_file_path="json_files/cities_mocked_data.json",
                                                             resource_id_enum=ResourceId.CITIES_POPULATION_RESOURCE_ID)
        self._check_base_step_of_all_methods(data_handler=self.data_handler_1, class_type=Cities)

    def test_cities_by_date(self) -> None:
        """ Tests results of tests cities by specific date and its results as city's tuples """
        # Get Data
        data = self.data_handler_1.cities_by_date("2020-10-03")
        results = defaultdict(None, {"אבו ג'ווייעד (שבט)": Cities.city(City_name="אבו ג'ווייעד (שבט)", City_code='967', Date='2020-10-03', Cumulative_verified_cases='0', Cumulated_recovered='0', Cumulated_deaths='0', Cumulated_number_of_tests='225', Cumulated_number_of_diagnostic_tests='225'),
                                     'אבו גוש': Cities.city(City_name='אבו גוש', City_code='472', Date='2020-10-03', Cumulative_verified_cases='206', Cumulated_recovered='178', Cumulated_deaths='0', Cumulated_number_of_tests='4101', Cumulated_number_of_diagnostic_tests='3993')})
        # Check yield type as a generator
        self.assertIsInstance(data, type(_ for _ in range(0)))

        for _, city in data:
            self.assertIs(type(city), Cities.city)
        # Check for values equality
        for data_value, result_value in zip(data, results.values()):
            self.assertTupleEqual(data_value, result_value)

    def test_top_cases_in_cities(self) -> None:
        """ Tests results data & type of top cases in cities  """
        # Get Data
        results = defaultdict(None,
                              {'Cumulative_verified_cases': defaultdict(int, {'אבו גוש': 211, "אבו ג'ווייעד (שבט)": 14}),
                               'Cumulated_recovered': defaultdict(int, {'אבו גוש': 206, "אבו ג'ווייעד (שבט)": 0}),
                               'Cumulated_deaths': defaultdict(int, {"אבו ג'ווייעד (שבט)": 0, 'אבו גוש': 0}),
                               'Cumulated_number_of_tests': defaultdict(int, {'אבו גוש': 4508, "אבו ג'ווייעד (שבט)": 250}),
                               'Cumulated_number_of_diagnostic_tests': defaultdict(int, {'אבו גוש': 4365, "אבו ג'ווייעד (שבט)": 250})
                               })
        data = self.data_handler_1.top_cases_in_cities()
        # Data Validation
        self._test_two_level_depth_nested_dictionaries(data, results)

    def test_cases_statistics(self) -> None:
        """ Tests the test cases statistics data & type """
        # Get Data
        results = {'Cumulative_verified_cases': {'min': 0, 'max': 212, 'mean': 25.96, 'sum': 12980},
                   'Cumulated_recovered': {'min': 0, 'max': 206, 'mean': 18.502, 'sum': 9251},
                   'Cumulated_deaths': {'min': 0, 'max': 0, 'mean': 0.0, 'sum': 0},
                   'Cumulated_number_of_tests': {'min': 0, 'max': 4584, 'mean': 677.404, 'sum': 338702},
                   'Cumulated_number_of_diagnostic_tests': {'min': 0, 'max': 4439, 'mean': 665.46, 'sum': 332730}}
        data = self.data_handler_1.cases_statistics()
        # Data Validation
        self._test_two_level_depth_nested_dictionaries(data, results)
