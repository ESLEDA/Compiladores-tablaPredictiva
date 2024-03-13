import re

class TablaPredictive:
    def __init__(self):
        self.stack = []
        self.input = []
        
        self.table = {
            ('REPET', 'MIENTRAS'): ['MIENTRAS', 'COND',],
            ('COND', 'PARENTESIS_A'): ['PARENTESIS_A', 'EXPRE', 'OPCI', 'PARENTESIS_C'],
            ('EXPRE', 'LETRA'): ['VAL', 'OPER', 'VAL'],
            ('VAL', 'LETRA'): ['LTR', 'RES'],
            ('RES', 'LETRA'): ['LTR', 'RES'],
            ('RES', 'AND'): ['epsilon'],
            ('RES', 'OR'): ['epsilon'],
            ('RES', 'PARENTESIS_C'): ['epsilon'],
            ('RES', 'MENOR_QUE'): ['epsilon'],
            ('RES', 'MAYOR_QUE'): ['epsilon'],
            ('RES', 'COMPARACION'): ['epsilon'],
            ('RES', 'MAYOR_EIGUAL'): ['epsilon'],
            ('RES', 'MENOR_EIGUAL'): ['epsilon'],
            ('LTR', 'LETRA'): ['LETRA'],
            ('OPER', 'MENOR_QUE'): ['MENOR_QUE'],
            ('OPER', 'MAYOR_QUE'): ['MAYOR_QUE'],
            ('OPER', 'COMPARACION'): ['COMPARACION'],
            ('OPER', 'MAYOR_EIGUAL'): ['MAYOR_EIGUAL'],
            ('OPER', 'MENOR_EIGUAL'): ['MENOR_EIGUAL'],
            ('OPCI', 'AND'): ['LOG', 'EXPRE'],
            ('OPCI', 'OR'): ['LOG', 'EXPRE'],
            ('OPCI', 'PARENTESIS_C'): ['epsilon'],
            ('LOG', 'AND'): ['AND'],
            ('LOG', 'OR'): ['OR'],
        }

    def parse(self, tokens):
        self.tokens = tokens
        self.stack = ['$', 'REPET']  
        self.cursor = 0
        output = []
        
        
        while self.stack:
            
            print(f"Pila: {self.stack}, token: {self.tokens[self.cursor] if self.cursor < len(self.tokens) else '$'}")
            output.append("Pila: " + str(self.stack[:]))
            top = self.stack[-1]  
            current_token = self.tokens[self.cursor][0] if self.cursor < len(self.tokens) else '$'
            
            if top == current_token:  # Coincidencia con un terminal
                self.stack.pop()  
                self.cursor += 1
            elif (top, current_token) in self.table:
                self.stack.pop()  
                symbols = self.table[(top, current_token)]
                if symbols != ['epsilon']:  
                    for symbol in reversed(symbols):
                        self.stack.append(symbol)
            else:
                print(f"No se encontró entrada en la tabla: {top}, {current_token}")
                raise Exception("Error de sintaxis")
        
        if self.cursor == len(self.tokens):
            raise Exception("Error de sintaxis - La entrada no ha sido  completamente")
        print("Análisis correcto")
        
        return "\n".join(output)


def lexer(input_string):
    tokens = []
    token_specs = [
        ('MIENTRAS', r'\bmientras\b'),
        ('AND', r'\band\b'),
        ('OR', r'\bor\b'),
        ('LETRA', r'[a-z]+'),
        ('PARENTESIS_A', r'\('),
        ('PARENTESIS_C', r'\)'),
        ('MENOR_QUE', r'\<'),
        ('MAYOR_QUE', r'\>'),
        ('COMPARACION', r'\=\='),
        ('MAYOR_EIGUAL', r'\=\>'),
        ('MENOR_EIGUAL', r'\=\<'),
        ('IGNORAR', r'[ \t\n]+'),
        ('TCH', r'.'),
    ]
    
    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specs)
    for match in re.finditer(token_regex, input_string):
        type = match.lastgroup
        if type == 'IGNORAR':
            continue
        elif type == 'TCH':
            raise RuntimeError(f'legal caracter: {match.group(0)}')
        else:
            tokens.append((type, match.group(0)))
    return tokens


def parse_input(input_string):
    try:
        tokens = lexer(input_string)
        parser = TablaPredictive()
        estado_pila = parser.parse(tokens) 
        return f"Análisis completado .\n final de la pila: {estado_pila}"
        # return estado_pila
    except Exception as e:
        return str(e)


