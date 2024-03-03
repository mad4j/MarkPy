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
        assert head.render_hn("Title", 1) == "# Title\n\n"

        # test level 2 syntax
        assert head.render_hn("Title", 2) == "## Title\n\n"

        # test level 3 syntax
        assert head.render_hn("Title", 3) == "### Title\n\n"

        # test level 4 syntax
        assert head.render_hn("Title", 4) == "#### Title\n\n"

        # test level 5 syntax
        assert head.render_hn("Title", 5) == "##### Title\n\n"

        # test level 6 syntax
        assert head.render_hn("Title", 6) == "###### Title\n\n"


    def test_hn_with_strip(self):
        """
        Test to verify standard heading rendering
        """

        # test level 1 syntax
        assert head.render_hn(" Title ", 1) == "# Title\n\n"

        # test level 2 syntax
        assert head.render_hn(" Title ", 2) == "## Title\n\n"

        # test level 3 syntax
        assert head.render_hn(" Title ", 3) == "### Title\n\n"

        # test level 4 syntax
        assert head.render_hn(" Title ", 4) == "#### Title\n\n"

        # test level 5 syntax
        assert head.render_hn(" Title ", 5) == "##### Title\n\n"

        # test level 6 syntax
        assert head.render_hn(" Title ", 6) == "###### Title\n\n"


    def test_render_uhn(self):
        """
        Test to verify underlined heading rendering
        """

        # test level 1 syntax
        assert head.render_uhn("Title", 1) == "Title\n=====\n\n"

        # test level 1 syntax
        assert head.render_uhn("Title", 2) == "Title\n-----\n\n"


    def test_render_uhn_with_strip(self):
        """
        Test to verify underlined heading rendering
        """

        # test level 1 syntax
        assert head.render_uhn(" Title ", 1) == "Title\n=====\n\n"

        # test level 1 syntax
        assert head.render_uhn(" Title ", 2) == "Title\n-----\n\n"

    def test_render_ruler(self):
        """
        Test to verify horizonal ruler rendering
        """

        assert head.render_ruler(3) == "---\n\n"
        assert head.render_ruler(4) == "----\n\n"
        assert head.render_ruler(5) == "-----\n\n"

        for i in range(6, 21):
            assert head.render_ruler(i) == "-"*i + "\n\n"

        assert head.render_ruler(1) == "---\n\n"
        assert head.render_ruler(2) == "---\n\n"
