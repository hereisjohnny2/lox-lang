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
            case c if c.isnumeric():
                return self.read_numeric()
            case c if c.isalpha():
                return self.read_identifier()

        return None

    def read_string_literal(self):
        while self.peek() != '"' and not self.at_end():
            if self.peek() == "\n":
                self.line += 1
            self.advance()

        self.advance()

        literal = self.source[self.start + 1 : self.current - 1]
        return Token(TokenType.STRING, literal, self.line, literal)

    def read_numeric(self):
        while self.peek().isnumeric():
            self.advance()

        if self.peek() == "." and self.peek(1).isnumeric():
            self.advance()
            while self.peek().isnumeric():
                self.advance()

        value = self.source[self.start : self.current]
        literal = float(value) if "." in value else int(value)

        return Token(TokenType.NUMERIC, value, self.line, literal)

    def read_identifier(self):
        while self.peek().isalnum():
            self.advance()

        value = self.source[self.start : self.current]

        if token_type := KEYWORDS.get(value, None):
            return Token(token_type, value, self.line)

        return Token(TokenType.IDENTIFIER, value, self.line)

    def advance(self) -> str:
        if self.at_end():
            return None

        c = self.source[self.current]
        self.current += 1
        return c

    def peek(self, next: int = 0) -> str:
        if self.current + next >= len(self.source):
            return "\0"

        return self.source[self.current + next]
