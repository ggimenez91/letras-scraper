import unittest
from samplesongs import songs
from lyricscraper import LyricScraper

class lyric_test(unittest.TestCase):
    def test_sample_song(self):
        scraper = LyricScraper()
        test_song = songs[0][1]
        scraped_song = scraper.run([songs[0][0]])[0]
        self.assertTrue(test_song == scraped_song)

if __name__ == '__main__':
    unittest.main()
