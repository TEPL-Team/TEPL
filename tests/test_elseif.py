import io
import unittest
from contextlib import redirect_stdout

from src.interpreter import compile_ast
from src.lexer import lexer
from src.nodes import If
from src.parser import parser, semantic_analysis


class ElseIfTests(unittest.TestCase):
    def test_parser_builds_elseif_and_else_branches(self):
        code = """
if 1 == 2 then
    output "first"
elseif 2 == 3 then
    output "second"
else then
    output "third"
end
"""
        tree = parser.parse(code, lexer=lexer)
        self.assertTrue(semantic_analysis(tree))
        self.assertEqual(len(tree), 1)
        self.assertIsInstance(tree[0], If)
        self.assertEqual(len(tree[0].elif_branches), 1)
        self.assertIsNotNone(tree[0].else_body)

    def test_compiler_emits_and_runs_elseif(self):
        code = """
if 1 == 2 then
    output "first"
elseif 2 == 2 then
    output "second"
else then
    output "third"
end
"""
        tree = parser.parse(code, lexer=lexer)
        compiled = compile_ast(tree)
        self.assertIn("elif 2 == 2:", compiled)
        self.assertIn("else:", compiled)

        output = io.StringIO()
        with redirect_stdout(output):
            exec(compiled, {})
        self.assertEqual(output.getvalue().strip(), "second")


if __name__ == "__main__":
    unittest.main()
