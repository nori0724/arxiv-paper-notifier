import unittest
from src.arxiv_api import get_papers_from_arxiv

class TestArxivAPI(unittest.TestCase):
    def test_get_papers_from_arxiv(self):
        papers = get_papers_from_arxiv()
        self.assertIsInstance(papers, list)

        for paper in papers:
            self.assertIn('title', paper)
            self.assertIn('link', paper)
            self.assertIn('published', paper)
            self.assertIn('summary', paper)
            self.assertIn('score', paper)
            self.assertIn('hit_keywords', paper)

if __name__ == '__main__':
    unittest.main()