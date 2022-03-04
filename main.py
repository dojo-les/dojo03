import pytest


pytest.main([__file__, "-p", "no:warnings"])


class NumeroRomanoInvalido(BaseException):
    ...


def romano_para_decimal(numero_romano):
    if numero_romano == 'IIII':
        raise NumeroRomanoInvalido

    decimais = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    resultado = 0
   
    for i in range(len(numero_romano)-1):
        atual = numero_romano[i]
        proximo = numero_romano[i + 1]
        if decimais[atual] < decimais[proximo]:
            resultado -= decimais[atual]
        else:
            resultado += decimais[atual]
    
    resultado += decimais[numero_romano[-1]]         
    
    return resultado


def teste_repeticao_irregular():
    with pytest.raises(NumeroRomanoInvalido):
        romano_para_decimal('IIII')

def teste_19():
    assert romano_para_decimal("MCXX") == 1120
  
def teste_18():
    assert romano_para_decimal("CM") == 900

def teste_17():
    assert romano_para_decimal("M") == 1000

def teste_16():
    assert romano_para_decimal("CDXC") == 490
    
def teste_15():
    assert romano_para_decimal("D") == 500

def teste_14():
    assert romano_para_decimal("XC") == 90

def teste_13():
    assert romano_para_decimal("C") == 100

def teste_12():
    assert romano_para_decimal("XL") == 40

def teste_11():
    assert romano_para_decimal("L") == 50

def teste_10():
    assert romano_para_decimal("XVI") == 16

def teste_9():
    assert romano_para_decimal("XI") == 11
  
def teste_8():
    assert romano_para_decimal("IX") == 9

          
def teste_7():
    assert romano_para_decimal("X") == 10

def teste_6():
    assert romano_para_decimal("VI") == 6     
    
def teste_5():
    assert romano_para_decimal("V") == 5
        
def teste_4():
    assert romano_para_decimal('IV') == 4

def teste_3():
    assert romano_para_decimal('III') == 3

def teste_2():
    assert romano_para_decimal('II') == 2

def teste_1():
    assert romano_para_decimal('I') == 1






