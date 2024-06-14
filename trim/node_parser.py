# from trim import TrimTemplate
import os

SINGLE_TAGS = ["doctype", "img", "br", "hr", "input", "link", "meta"]
BOOLEAN_ATTRIBUTES = [
    'checked', 'selected', 'disabled', 'readonly', 'multiple', 'ismap', 'defer', 'declare', 'noresize', 'nowrap',
]

DOCTYPES = {
    "html":         '<!DOCTYPE html>',
    "basic":        '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML Basic 1.1//EN" "http://www.w3.org/TR/xhtml-basic/xhtml-basic11.dtd">',
    "frameset":     '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd">',
    "mobile":       '<!DOCTYPE html PUBLIC "-//WAPFORUM//DTD XHTML Mobile 1.2//EN" "http://www.openmobilealliance.org/tech/DTD/xhtml-mobile12.dtd">',
    "strict":       '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">',
    "transitional": '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">',
}


class NodeParser:
    def __init__(self, node, engine=None):
        self.node      = node
        self.parsed    = ""
        self.engine    = engine
        self.variables = engine.variables.copy()

    def parse(self):
        match self.node.tag:
            case 'comment':
                return f"<!-- {self.node.text} -->"
            case 'css:':
                return f"\n<style>\n{self.node.text}</style>"
            case "doctype":
                return DOCTYPES.get(self.node.text, "")
            case "else":
                return self.parse_else()
            case "javascript:":
                return f"\n<script type='javascript'>\n{self.node.text}\n</script>"
            case 'javascript:':
                return f"\n<script type='javascript'>\n{self.node.text}</script>"
            case 'if':
                return self.parse_if()
            case "for":
                return self.parse_for()
            case "render":
                dir      = self.engine.dir
                template = dir + '/' + self.node.attributes.get("template")
                renderer = self.engine.clone(template)
                # breakpoint()
                return renderer.render()
            case "root":
                return self.parse_children()

        self.parse_node()

        return self.parsed

    def parse_node(self):
        self.parsed += f"<{self.node.tag}"
        self.parsed += self.parse_attributes()

        if self.node.tag in SINGLE_TAGS:
            self.parsed += self.close_node()
        else:
            self.parsed += ">"
            self.parse_children()

        self.parsed += self.parse_text()

        if self.node.tag not in SINGLE_TAGS:
            self.parsed += self.close_node()

        return self.parsed

    def parse_for(self):
        var   = self.node.attributes.get("var", "")
        array = self.node.attributes.get("array", "")

        for t in self.engine.variables.get(array):
            self.variables[var] = t
            for node in self.node.children:
                self.parsed += NodeParser(node, self).parse()

        return self.parsed

    def parse_if(self):
        condition = self.node.attributes.get("condition", "False")
        result    = eval(condition, self.engine.variables)

        if result:
            return self.parse_children()

        self.node.last_result = result

        return ""

    def parse_else(self):
        if not self.node.prev_sibling.last_result:
            return self.parse_children()

        return ""

    def parse_text(self):
        t = self.node.text

        if t == "":
            return ""

        if self.node.ws_prepend:
            t = " " + t

        if "{" in t:
            t = t.format(**self.engine.variables)

        if self.node.ws_append:
            t += " "

        return t

    def parse_children(self):
        for node in self.node.children:
            self.parsed += NodeParser(node, self.engine).parse()

        return self.parsed

    def close_node(self):
        tag = self.node.tag
        if tag == "":
            return ""
        if tag in SINGLE_TAGS:
            return "/>"
        else:
            return f"</{tag}>"

    def parse_attributes(self):
        p = ""
        if self.node.has_attributes():
            for a, v in self.node.attributes.items():
                if v == "":
                    continue

                if "{" in v:
                    v = v.format(**self.engine.variables)

                if a in BOOLEAN_ATTRIBUTES:
                    v = self.boolean_attribute(a, v)
                    if v is False:
                        continue

                p += f' {a}="{v}"'

        return p

    def boolean_attribute(self, attribute, value):
        if attribute in BOOLEAN_ATTRIBUTES:
            if value == "True":
                return attribute

        if self.engine.variables.get(value, False):
            return attribute

        return False
