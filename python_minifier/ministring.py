import re


BACKSLASH = '\\'


class MiniString(object):
    """
    Create a representation of a string object

    :param str string: The string to minify

    """

    def __init__(self, string, quote="'"):
        self._s = string
        self.safe_mode = False
        self.quote = quote

    def __str__(self):
        """
        The smallest python literal representation of a string

        :rtype: str

        """

        if self._s == '':
            return ''

        if len(self.quote) == 1:
            s = self.to_short()
        else:
            s = self.to_long()

        try:
            eval(self.quote + s + self.quote)
        except (UnicodeDecodeError, UnicodeEncodeError):
            if self.safe_mode:
                raise

            self.safe_mode = True
            if len(self.quote) == 1:
                s = self.to_short()
            else:
                s = self.to_long()

        assert eval(self.quote + s + self.quote) == self._s

        return s

    def to_short(self):
        s = ''

        escaped = {
            '\n': BACKSLASH + 'n',
            '\\': BACKSLASH + BACKSLASH,
            '\a': BACKSLASH + 'a',
            '\b': BACKSLASH + 'b',
            '\f': BACKSLASH + 'f',
            '\r': BACKSLASH + 'r',
            '\t': BACKSLASH + 't',
            '\v': BACKSLASH + 'v',
            '\0': BACKSLASH + 'x00',
            self.quote: BACKSLASH + self.quote,
        }

        for c in self._s:
            if c in escaped:
                s += escaped[c]
            else:
                if self.safe_mode:
                    unicode_value = ord(c)
                    if unicode_value <= 0x7F:
                        s += c
                    elif unicode_value <= 0xFFFF:
                        s += BACKSLASH + 'u' + format(unicode_value, '04x')
                    else:
                        s += BACKSLASH + 'U' + format(unicode_value, '08x')
                else:
                    s += c

        return s

    def to_long(self):
        s = ''

        escaped = {
            '\\': BACKSLASH + BACKSLASH,
            '\a': BACKSLASH + 'a',
            '\b': BACKSLASH + 'b',
            '\f': BACKSLASH + 'f',
            '\r': BACKSLASH + 'r',
            '\t': BACKSLASH + 't',
            '\v': BACKSLASH + 'v',
            '\0': BACKSLASH + 'x00',
            self.quote[0]: BACKSLASH + self.quote[0],
        }

        for c in self._s:
            if c in escaped:
                s += escaped[c]
            else:
                if self.safe_mode:
                    unicode_value = ord(c)
                    if unicode_value <= 0x7F:
                        s += c
                    elif unicode_value <= 0xFFFF:
                        s += BACKSLASH + 'u' + format(unicode_value, '04x')
                    else:
                        s += BACKSLASH + 'U' + format(unicode_value, '08x')
                else:
                    s += c

        return s


class MiniBytes(object):
    """
    Create a representation of a bytes object

    :param bytes string: The string to minify

    """

    def __init__(self, string, quote="'"):
        self._b = string
        self.quote = quote

    def __str__(self):
        """
        The smallest python literal representation of a string

        :rtype: str

        """

        if self._b == b'':
            return ''

        if len(self.quote) == 1:
            s = self.to_short()
        else:
            s = self.to_long()

        assert eval('b' + self.quote + s + self.quote) == self._b

        return s

    def to_short(self):
        b = ''

        for c in self._b:
            if c == b'\\':
                b += BACKSLASH
            elif c == b'\n':
                b += BACKSLASH + 'n'
            elif c == self.quote:
                b += BACKSLASH + self.quote
            else:
                if c >= 128:
                    b += BACKSLASH + chr(c)
                else:
                    b += chr(c)

        return b

    def to_long(self):
        b = ''

        for c in self._b:
            if c == b'\\':
                b += BACKSLASH
            elif c == self.quote:
                b += BACKSLASH + self.quote
            else:
                if c >= 128:
                    b += BACKSLASH + chr(c)
                else:
                    b += chr(c)

        return b

should_escapes = [
    b'\\"', b"\\'", b'\\0', b'\\1', b'\\2', b'\\3', b'\\4', b'\\5', b'\\6', b'\\7',
    b'\\N', b'\\U', b'\\a', b'\\b', b'\\f', b'\\n', b'\\r', b'\\t', b'\\u', b'\\v', b'\\x'
]
# TODO: bytesで128以上の文字を使えないのめんどくて対応してない。まあ使うやつが悪い
def get_embed(b: bytes, prefix=b''):
    orig = b

    b = re.sub(br'\\+', lambda m: b'\\' * (2 * len(m.group(0)) - 1), b)

    for should_escape in should_escapes:
        b = b.replace(b"\\" + should_escape, b"\\\\\\" + should_escape)
        b = b.replace(should_escape, b"\\" + should_escape)

    # null byte を \0 に置換したとき、\01 みたいなのが間違って解釈されるのを防ぐ
    for i in range(8):
        b = b.replace(b"\\\x00" + f"{i}".encode(), b"\\\\\\000" + f"{i}".encode())
        b = b.replace(b"\x00" + f"{i}".encode(), b"\\000" + f"{i}".encode())

    b = b.replace(b"\\\x00", b"\\\\\\0").replace(b"\x00", b"\\0")
    # \r はなんかパースされたあとに \n になっちゃうと思ってたんだけどなんないっぽい?よくわかんねえ
    # b = b.replace(b"\\\r", b"\\\\\\r").replace(b"\r", b"\\r")

    if b.endswith(b"\\"): b += b'\\'

    l: list[bytes] = []
    for sep in (b"'", b'"', b"'''", b'"""'):
        if len(sep) == 1:
            t = b.replace(b'\\\n', b'\\\\\\n').replace(b'\n', b'\\n') \
                .replace(b'\\\r', b'\\\\\\r').replace(b'\r', b'\\r') \
                .replace(sep, b'\\'+sep)
            l.append(sep + t + sep)
        else:
            # TODO: 流石にないと思うけど """ とかを消す
            if sep in b: continue
            t = b.replace(b'\\\n', b'\\\\\n').replace(b'\\\r', b'\\\\\r')
            t = t[:-1] + b'\\' + t[-1:] if t.endswith(sep[:1]) else t
            l.append(sep + t + sep)

    if not orig.endswith(b"\\"):
        for sep in (b"'", b'"', b"'''", b'"""'):
            if len(sep) == 1:
                if b"\n" in orig or b"\r" in orig:
                    continue
                t = orig.replace(sep, b'\\'+sep)
                l.append(b"r" + sep + t + sep)
            else:
                if sep in orig: continue
                t = orig[:-1] + b'\\' + b[-1:] if b.endswith(sep[:1]) else orig
                l.append(b"r" + sep + t + sep)

    res = min(l, key=len)
    return prefix + res
