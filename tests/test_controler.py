from unittest import TestCase
from src.controler import Controler
from src.dbconnection import DbConnection
import mock
import mongomock

class TestController(TestCase):
    def setUp(self):
        self.controler = Controler()
        self.controler.client = mongomock.MongoClient()
        self.controler.dbs = self.controler.client["baseDatosPalitos"]["Partidos"]

    def test_insertIsNotNoneWinner1(self):
        m = self.controler
        m.player1Name = 'Fermin'
        conex = m.dbs
        conex.client = mongomock.MongoClient()
        winner = 1
        #m.insertResultadoPartido = mock.MagicMock(return_value="insertedID")
        self.assertIsNotNone(m.insertResultadoPartido(winner))

    def test_insertIsNotNoneWinner2(self):
        m = self.controler
        m.player2Name = 'Amancio'
        conex = m.dbs
        conex.client = mongomock.MongoClient()
        winner = 2
        #m.insertResultadoPartido = mock.MagicMock(return_value="insertedID")
        self.assertIsNotNone(m.insertResultadoPartido(winner))

    '''
    def test_insertIsNotNoneWinner2(self):
        m = Controler()
        m.player2Name = 'Juan'
        conex = DbConnection("baseDatosPalitos","Partidos")
        conex.client = mongomock.MongoClient()
        winner = 1
        #m.insertResultadoPartido = mock.MagicMock(return_value="insertedID")
        self.assertIsNotNone(m.insertResultadoPartido(winner))



    def test_showHistory(self):
        m = Controler()
        m.showHistory = mock.MagicMock({'Ganador':'Ermidio','Perdedor' : 'Juanillo'})
        self.assertEquals(m.showHistory(), None)

'''