from unittest import TestCase
from src.controler import Controler
import mock
import mongomock

class TestController(TestCase):

    def test_insertResultadoPartido(self, winner):
        m = Controler()

        m.insertResultadoPartido = mock.MagicMock(return_value="insertedID")
        self.assertEquals(m.insertResultadoPartido(winner) , "insertedId")

    def test_showHistory(self):
        m = Controler()
        m.showHistory = mock.MagicMock({'Ganador':'Ermidio','Perdedor' : 'Juanillo'})
        self.assertEquals(m.showHistory(), None)

