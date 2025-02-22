from lox.token import KEYWORDS, Token, TokenType


class Scanner:
    def __init__(self, source: str):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1

    def at_end(self):
        return self.current >= len(self.source)

    def scan_tokens(self):
        while not self.at_end():
            self.start = self.current
            if token := self.scan_token():
                self.tokens.append(token)

        self.tokens.append(Token(TokenType.EOF, "", self.line))
        return self.tokens

    def scan_token(self) -> Token | None:
        c = self.source[self.current]
        self.current += 1
        match c:
            case "=":
                return Token(TokenType.EQUAL, "=", self.line)
            case ";":
                return Token(TokenType.SEMICOLON, ";", self.line)
            case "\n":
                self.line += 1
                return None
            case '"':
                return self.read_string_literal()
        if c.isalpha():
            return self.read_identifier()

        return None

    def read_string_literal(self):
        c = self.source[self.current]
        while c != '"' and not self.at_end():
            if c == "\n":
                self.line += 1
            self.current += 1
            c = self.source[self.current]

        literal = self.source[self.start + 1 : self.current]
        self.current += 1
        return Token(TokenType.STRING, literal, self.line, literal)

    def read_identifier(self):
        c = self.source[self.current]
        while c.isalpha() or c.isnumeric():
            self.current += 1
            c = self.source[self.current]

        value = self.source[self.start : self.current]

        if token_type := KEYWORDS.get(value, None):
            return Token(token_type, value, self.line)

        return Token(TokenType.IDENTIFIER, value, self.line)
