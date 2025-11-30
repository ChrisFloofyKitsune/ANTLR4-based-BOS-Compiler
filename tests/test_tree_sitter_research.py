import unittest
from pathlib import Path
from bos._test_helpers import walk_files, purge_preproc_nodes


class TestWalkFiles(unittest.TestCase):
    def test_walk_files_filters_by_extension(self):
        # create a temporary directory structure
        base = Path('tests/_tmp_walk')
        (base / 'sub').mkdir(parents=True, exist_ok=True)
        file1 = base / 'a.bos'
        file2 = base / 'b.txt'
        file3 = base / 'sub' / 'c.h'
        file1.write_text('x')
        file2.write_text('y')
        file3.write_text('z')

        results = list(walk_files(base, ['.bos', '.h']))
        self.assertIn(file1, results)
        self.assertIn(file3, results)
        self.assertNotIn(file2, results)

        # cleanup
        for p in [file1, file2, file3]:
            if p.exists():
                p.unlink()
        for d in [base / 'sub', base]:
            if d.exists():
                d.rmdir()


class TestPurgePreprocNodes(unittest.TestCase):
    def test_purge_simple(self):
        data = {
            'Name': 'value',
            'PreprocSomething': 'ignore',
            'Nested': {'Keep': 1, 'PreprocX': 2},
            'List': [{'Keep': 'a', 'PreprocY': 'b'}, 'c']
        }
        cleaned = purge_preproc_nodes(data)
        self.assertIn('Name', cleaned)
        self.assertNotIn('PreprocSomething', cleaned)
        self.assertIn('Nested', cleaned)
        self.assertIn('Keep', cleaned['Nested'])
        self.assertNotIn('PreprocX', cleaned['Nested'])
        self.assertIn('List', cleaned)
        self.assertEqual(cleaned['List'], [{'Keep': 'a'}, 'c'])

    def test_purge_all_preproc(self):
        data = {'PreprocA': {'PreprocB': 'x'}, 'PreprocC': []}
        self.assertEqual(purge_preproc_nodes(data), {})


if __name__ == '__main__':
    unittest.main()

