import unittest
from testdata import songs
from lyricsscraper import LyricsScraper

class lyric_test(unittest.TestCase):
    def test_sample_song(self):
        scraper = LyricsScraper()
        test_song = songs[0]
        scraped_song = scraper.get_songs([songs[0].link])[0]
        self.assertTrue(test_song == scraped_song)

if __name__ == '__main__':
    unittest.main()
