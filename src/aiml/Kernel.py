# coding=utf-8
import random
import os

from jinja2 import Template

from aiml.loader import AimlLoader
from aiml.tmp_ext import TmpExt
from aiml.utils import Utils


class Kernel(object):

    def __init__(self, main_xml):
        self.aiml_roots = [root for root in AimlLoader.load(main_xml)]
        self.ext_ctx = {}

    def _render_template(self, template_text, ctx={}):
        template = Template(template_text)
        template.environment.globals.update(TmpExt.exts(self.ext_ctx))
        ctx.update({"ext": self.ext_ctx})
        template_output = template.render(**ctx)
        return template_output

    def respond(self, text):
        choice = random.choice(list(Utils.match_categorys(text, self.aiml_roots)) or [None])
        if not choice:
            return "嗯..,我不知道说什么了"

        ctg, groupdict = choice

        ctx = {}
        ctx.update(groupdict)

        template_text = Utils.get_template(ctg)
        template_output = self._render_template(template_text, ctx)
        answers = Utils.splitlines_template_output(template_output) or [""]

        answer = random.choice(answers)

        self.ext_ctx["thata"] = answer
        self.ext_ctx["thatq"] = (text or "").strip()
        return answer


def loop_parse():
    start_xml_path = os.path.abspath(os.path.join(__file__, "../../../", "corpus/main.xml"))
    kernel = Kernel(start_xml_path)

    while True:
        text = input(">")
        an = kernel.respond(text)
        print(an)


if __name__ == "__main__":
    loop_parse()


