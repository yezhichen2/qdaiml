# coding=utf-8
import os
import xml.etree.ElementTree as ET

class AimlLoader(object):

    @classmethod
    def _load_main_xml(cls, main_xml):
        tree = ET.parse(main_xml)
        root = tree.getroot()

        return root

    @classmethod
    def _load_aiml_xml(cls, aiml_xml):
        tree = ET.parse(aiml_xml)
        root = tree.getroot()
        return root


    @classmethod
    def load(cls, main_xml):

        path1 = os.path.dirname(main_xml)
        main_root = cls._load_main_xml(main_xml)

        aimls = main_root.findall("aiml")

        for aiml in aimls:
            aiml_file_name = (aiml.text or "").strip()
            if not aiml_file_name:
                print("Not aiml file name")
                continue

            aiml_file_name = os.path.join(path1, aiml_file_name)

            try:
                aiml_root = cls._load_aiml_xml(aiml_file_name)
                yield aiml_root

            except Exception as e:
                print(e)


