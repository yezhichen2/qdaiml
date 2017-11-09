# coding=utf-8
import re


class Utils(object):

    @classmethod
    def get_patterns(cls, category_el):
        pattern_el = category_el.find("./pattern")
        if pattern_el is None: return []

        text = (pattern_el.text or "")
        text = re.sub("\(\s*\{\{\s*(\w+)\s*\}\}", "(?P<\\1>", text)
        lines = filter(lambda line: line, [line.strip() for line in text.splitlines()])
        return list(lines)

    @classmethod
    def get_template(cls, category_el):
        template_el = category_el.find("./template")
        if template_el is None: return ""
        text = (template_el.text or "")
        return text

    @classmethod
    def splitlines_template_output(cls, template_output):
        lines = filter(lambda line: line, [line.strip() for line in template_output.splitlines()])
        return list(lines)

    @classmethod
    def match_categorys(cls, text, aiml_roots):

        categoryies = []
        for aiml_root in aiml_roots:
            categoryies.extend(aiml_root.findall("./category"))

        for category in categoryies:
            patterns = cls.get_patterns(category)

            for pattern in patterns:
                search = re.search(pattern, text)

                if search:
                    groupdict = search.groupdict()
                    yield (category, groupdict)
                    break






