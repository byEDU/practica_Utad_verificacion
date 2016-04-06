from unittest import TestCase
from mock import MagicMock
from controler import Controler
from dbconnection import DbConnection

class TestControler:
    def setUp(self):

        self.connection = Mongomock()