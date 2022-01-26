import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
	def setUp(self):
		self.varasto = Varasto(10)

	def test_konstruktori_luo_tyhjan_varaston(self):
		# https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
		self.assertAlmostEqual(self.varasto.saldo, 0)

	def test_uudella_varastolla_oikea_tilavuus(self):
		self.assertAlmostEqual(self.varasto.tilavuus, 10)
		
	def test_uuden_varaston_tilavuus_ei_voi_olla_negatiivinen(self):
		self.varasto = Varasto(-10)
		
		self.assertAlmostEqual(self.varasto.tilavuus, 0)
		
	def test_varaston_alkusaldo_ei_voi_olla_negatiivinen(self):
		self.varasto = Varasto(10, alku_saldo = -5)
		
		self.assertAlmostEqual(self.varasto.saldo, 0)

	def test_lisays_lisaa_saldoa(self):
		self.varasto.lisaa_varastoon(8)

		self.assertAlmostEqual(self.varasto.saldo, 8)

	def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
		self.varasto.lisaa_varastoon(8)

		# vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
		self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

	def test_ottaminen_palauttaa_oikean_maaran(self):
		self.varasto.lisaa_varastoon(8)

		saatu_maara = self.varasto.ota_varastosta(2)

		self.assertAlmostEqual(saatu_maara, 2)

	def test_ottaminen_lisaa_tilaa(self):
		self.varasto.lisaa_varastoon(8)

		self.varasto.ota_varastosta(2)

		# varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
		self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
        
	def test_lisays_liikaa_tayttaa_varaston(self):
		self.varasto.lisaa_varastoon(4)
		self.varasto.lisaa_varastoon(15)
		
		# varaston pitäisi olla täynnä eli vapaata tilaa 0
		self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)
		
	def test_ottaminen_liikaa_tyhjentaa_varaston(self):
		self.varasto.lisaa_varastoon(7)
		self.varasto.ota_varastosta(10)
		
		self.assertAlmostEqual(self.varasto.saldo, 0)
		
	def test_negatiivisen_maaran_lisays_ei_muuta_saldoa(self):
		self.varasto.lisaa_varastoon(8)
		self.varasto.lisaa_varastoon(-4)
		
		self.assertAlmostEqual(self.varasto.saldo, 8)
		
	def test_negatiivisen_maaran_ottaminen_ei_mahdollista(self):
		self.varasto.lisaa_varastoon(8)
		saatu_maara = self.varasto.ota_varastosta(-4)
		
		self.assertAlmostEqual(saatu_maara, 0)
		
	def test_varaston_tiedot_tulostuvat_oikein(self):
		self.assertAlmostEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
