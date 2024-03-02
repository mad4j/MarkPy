"""
Tests for 'emphasys' module
"""

import markpy.renders.emphasys as em


class TestEmphasys:
    """
    Tests for 'emphasys' module
    """

    def test_render_bold(self):
        """
        Test to verify bold emphasys
        """

         # test bold emphasys
        assert em.bold("text") == "**text**"

    def test_render_italic(self):
        """
        Test to verify italic emphasys
        """

         # test italic emphasys
        assert em.italic("text") == "*text*"

    def test_render_bold_and_italic(self):
        """
        Test to verify bold and italic emphasys
        """

         # test bold and italic emphasys
        assert em.bold(em.italic("text")) == "***text***"

    def test_render_code(self):
        """
        Test to verify code emphasys
        """

         # test code emphasys
        assert em.code("text") == "`text`"
        
    def test_render_highlight(self):
        """
        Test to verify highlight emphasys
        """

         # test highlight emphasys
        assert em.highlight("text") == "==text=="
