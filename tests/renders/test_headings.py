"""
Tests for 'headings' module
"""

import markpy.renders.headings as head


class TestHeadings:
    """
    Tests for 'headings' module
    """

    def test_render_hn(self):
        """
        Test to verify standard heading rendering
        """

        # test level 1 syntax
        assert head.render_hn("Title", 1) == "\n# Title\n\n"

        # test level 2 syntax
        assert head.render_hn("Title", 2) == "\n## Title\n\n"

        # test level 3 syntax
        assert head.render_hn("Title", 3) == "\n### Title\n\n"

        # test level 4 syntax
        assert head.render_hn("Title", 4) == "\n#### Title\n\n"

        # test level 5 syntax
        assert head.render_hn("Title", 5) == "\n##### Title\n\n"

        # test level 6 syntax
        assert head.render_hn("Title", 6) == "\n###### Title\n\n"


    def test_hn_with_strip(self):
        """
        Test to verify standard heading rendering
        """

        # test level 1 syntax
        assert head.render_hn(" Title ", 1) == "\n# Title\n\n"

        # test level 2 syntax
        assert head.render_hn(" Title ", 2) == "\n## Title\n\n"

        # test level 3 syntax
        assert head.render_hn(" Title ", 3) == "\n### Title\n\n"

        # test level 4 syntax
        assert head.render_hn(" Title ", 4) == "\n#### Title\n\n"

        # test level 5 syntax
        assert head.render_hn(" Title ", 5) == "\n##### Title\n\n"

        # test level 6 syntax
        assert head.render_hn(" Title ", 6) == "\n###### Title\n\n"


    def test_render_uhn(self):
        """
        Test to verify underlined heading rendering
        """

        # test level 1 syntax
        assert head.render_uhn("Title", 1) == "\nTitle\n=====\n\n"

        # test level 1 syntax
        assert head.render_uhn("Title", 2) == "\nTitle\n-----\n\n"


    def test_render_uhn_with_strip(self):
        """
        Test to verify underlined heading rendering
        """

        # test level 1 syntax
        assert head.render_uhn(" Title ", 1) == "\nTitle\n=====\n\n"

        # test level 1 syntax
        assert head.render_uhn(" Title ", 2) == "\nTitle\n-----\n\n"

    def test_render_ruler(self):

        assert head.render_ruler(3) == "\n---\n\n"
        assert head.render_ruler(4) == "\n----\n\n"
        assert head.render_ruler(5) == "\n-----\n\n"

        for i in range(6, 21):
            assert head.render_ruler(i) == "\n" + "-"*i + "\n\n"

    def test_render_ruler_with_min_value(self):
        assert head.render_ruler(1) == "\n---\n\n"
        assert head.render_ruler(2) == "\n---\n\n"
