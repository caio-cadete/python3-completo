'''

CONSTANTE: "Variáveis" que não vão mudar
Muitas condições no mesmo "if" (ruim)
    <- Contagem de complexidade (ruim) 
    Espaços e/ou afastamento da margem

Na 99% dos casos você está escrevendo código para outras pessoas, 
o mínimo para um bom programador é um código bem organizado e estru-
turado.

'''

# Variável (padrão minúscula)

velocidade = 61 # Velocidade atual do carro
local_carro = 100 # Local em que o carro está na estrada

# Constante (padrão maiúscula)

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância que o radar pega

velocidade_limite_radar = velocidade > RADAR_1
radar_local_carro = local_carro <= (LOCAL_1 + RADAR_RANGE) and local_carro >= (LOCAL_1 - RADAR_RANGE)



print(f'Velocidade: {velocidade} km/h')
print(f'Local carro: {local_carro}')
print(60 * '-')
print(f'Local radar: {LOCAL_1}')
print(f'Range do radar: {LOCAL_1 - RADAR_RANGE} até {LOCAL_1 + RADAR_RANGE}')

try: # Tentar
    if velocidade_limite_radar:
        print(f'Atenção! O carro está acima da velocidade permitida do radar: {velocidade} km/h')
        if radar_local_carro:
            print('O seu carro foi multado pois está no range do radar')
        else:
            print('O seu carro não foi multado, pois está fora do range do radar')
    else:
        print(f'O seu carro não foi multado porque estava na velocidade permitida segundo o radar: {velocidade} km/h')
except: # Capturar exceção
    print("Erro detectado")



# Obs*: Permitido usar "\"" para quebrar linhas sem que o código interrompa a leitura
# Exemplo:
# local_carro <= (LOCAL_1 + RADAR_RANGE) and \
# local_carro >= (LOCAL_1 - RADAR_RANGE)
