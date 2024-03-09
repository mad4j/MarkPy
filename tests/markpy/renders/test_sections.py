"""
Tests for 'sections' module
"""

import markpy.renders.sections as se


class TestEmphasys:
    """
    Tests for 'sections' module
    """

    def test_render_plain(self):
        """
        Test to verify plain sections
        """

         # test plain sections
        assert se.render_plain("text") == "text"


    def test_render_plain_nospaces(self):
        """
        Test to verify plain sections
        """

         # test end-of lines
        assert se.render_plain("text\n") == "text"
        assert se.render_plain("\ntext") == "text"
        assert se.render_plain("\ntext\n") == "text"
        assert se.render_plain("text\n\n") == "text"
        assert se.render_plain("\n\ntext") == "text"

        # test white spaces
        assert se.render_plain("text ") == "text"
        assert se.render_plain(" text") == "text"
        assert se.render_plain(" text ") == "text"
        assert se.render_plain("text  ") == "text"
        assert se.render_plain("  text") == "text"

        # test mix of white spaces and end-of-lines
        assert se.render_plain("text \n") == "text"
        assert se.render_plain("text\n ") == "text"
        assert se.render_plain("\n text") == "text"
        assert se.render_plain(" \ntext") == "text"
        assert se.render_plain("\n text \n") == "text"
        assert se.render_plain(" \ntext\n ") == "text"

    def test_render_code(self):
        """
        Test to verify fenced sections
        """

         # test fenced code section
        assert se.render_code("text") == "```text\ntext\n```\n\n"

