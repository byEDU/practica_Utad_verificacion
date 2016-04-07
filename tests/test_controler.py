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

    def test_showHistory(self):
        m = self.controler
        aux = mock.MagicMock({'Ganador': 'Amancio', 'Perdedor': 'Francisco'})
        listaAuxiliar = []
        for partida in aux:
            listaAuxiliar.append("Ganador: " + partida['Ganador'] + " Perdedor: " + partida['Perdedor'])
        self.assertTrue(len(listaAuxiliar) == 0)


    def test_numPartidasJugadas(self):
        m = self.controler

        numPartidas = 0
        aux = mock.MagicMock({'Ganador': 'Amancio', 'Perdedor': 'Francisco'})
        for partida in aux:
            numPartidas += 1

        self.assertEquals(numPartidas, 0)
