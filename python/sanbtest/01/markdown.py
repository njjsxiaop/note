import re

class Helper(object):
    def __init__(self,input):
        self.__input = input

    def wrap_links(self):
        compile_url = re.compile(r'[^"([]\s*(https*[^\s]*)')
        compile_seg = re.compile(r'([^"([]\s*)https*[^\s]*')

        l_url = re.findall(compile_url, self.__input)
        l_wrap = ['[', '](', ')']
        result = self.__input

        for url in l_url:
            repl = url.join(l_wrap)
            l_seg = re.findall(compile_seg, result)
            repl = l_seg[0] + repl

            result = re.sub(compile_url, repl, result)

        return result

    def extract_images(self):
        compile_url1 = re.compile(r'![[][a-zA-Z0-9_]*[]][(](.*?)[)]')
        compile_url2 = re.compile(r'<img src="(.*?)"></img>')

        l_url = re.findall(compile_url1, self.__input)
        l_url.extend(re.findall(compile_url2, self.__input))

        return l_url
