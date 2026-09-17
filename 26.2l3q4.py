print("Espaço: a fronteira final. Estas são as viagens da nave estelar Enterprise…")
print(
    "Sua missão de cinco anos: explorar novos mundos, procurar novas vidas e novas civilizações, audaciosamente indo aonde nenhum homem jamais esteve."
)
print(
    "Dr. McCoy: Eu sou um médico, não um matemático. Mas tenho que fazer o que precisa ser feito."
)
print("=====")

sample_size = int(input())
while not (5 <= sample_size <= 12):
    print(
        "Dr. McCoy: Esse número não é ideal, é possível trazer uma amostra de 5 a 12 indivíduos?"
    )
    sample_size = int(input())
print(f"Dr. McCoy: Certo, {sample_size} indivíduos. É um número bom.")
print("=====")

temperature_samples = []
pulse_samples = []
gas_change_samples = []
pressure_samples = []

# coleta de amostras
for _ in range(sample_size):
    vital_signals = input()

    temperature, vital_signals = vital_signals.split(" °C - ")
    pulse, vital_signals = vital_signals.split(" bpm - ")
    gas_change, vital_signals = vital_signals.split(" irpm - ")
    pressure = vital_signals[:-5]

    temperature_samples.append(float(temperature))
    pulse_samples.append(float(pulse))
    gas_change_samples.append(float(gas_change))
    pressure_samples.append(float(pressure))

# cálculo de medianas
mid = sample_size // 2
odd = sample_size % 2

temperature_samples.sort()
median_temperature = round(
    temperature_samples[mid]  # valor central
    if odd  # se ímpar
    else (temperature_samples[mid - 1] + temperature_samples[mid])
    / 2,  # senão média dos valores centrais
    1,
)

pulse_samples.sort()
median_pulse = round(
    pulse_samples[mid] if odd else (pulse_samples[mid - 1] + pulse_samples[mid]) / 2, 1
)

gas_change_samples.sort()
median_gas_change = round(
    gas_change_samples[mid]
    if odd
    else (gas_change_samples[mid - 1] + gas_change_samples[mid]) / 2,
    1,
)

pressure_samples.sort()
median_pressure = round(
    pressure_samples[mid]
    if odd
    else (pressure_samples[mid - 1] + pressure_samples[mid]) / 2,
    1,
)

print("Relatório de dados da amostra:")
print(f"Temperatura: {temperature_samples}")
print(f"Mediana: {median_temperature}")
print(f"Frequência de pulso fluido: {pulse_samples}")
print(f"Mediana: {median_pulse}")
print(f"Frequência de troca gasosa: {gas_change_samples}")
print(f"Mediana: {median_gas_change}")
print(f"Pressão interna de homeostase: {pressure_samples}")
print(f"Mediana: {median_pressure}")
print("=====")

# coleta de sinais do paciente
print("Dr. McCoy: Agora irei medir os sinais do paciente.")
print("=====")

patient_vital_signals = input()

patient_temperature, patient_vital_signals = patient_vital_signals.split(" °C - ")
patient_pulse, patient_vital_signals = patient_vital_signals.split(" bpm - ")
patient_gas_change, patient_vital_signals = patient_vital_signals.split(" irpm - ")
patient_pressure = patient_vital_signals[:-5]

patient_temperature = float(patient_temperature)
patient_pulse = float(patient_pulse)
patient_gas_change = float(patient_gas_change)
patient_pressure = float(patient_pressure)

# verificação de sinais críticos
critic_signals = 0
if not (temperature_samples[0] <= patient_temperature <= temperature_samples[-1]):
    critic_signals += 1
if not (pulse_samples[0] <= patient_pulse <= pulse_samples[-1]):
    critic_signals += 1
if not (gas_change_samples[0] <= patient_gas_change <= gas_change_samples[-1]):
    critic_signals += 1
if not (pressure_samples[0] <= patient_pressure <= pressure_samples[-1]):
    critic_signals += 1

print("Relatório final:")
print(f"Temperatura do paciente: {patient_temperature}")
print(f"Diferença para a mediana: {round(patient_temperature - median_temperature, 1)}")
print(f"Frequência de pulso fluido do paciente: {patient_pulse}")
print(f"Diferença para a mediana: {round(patient_pulse - median_pulse, 1)}")
print(f"Frequência de troca gasosa: {patient_gas_change}")
print(f"Diferença para a mediana: {round(patient_gas_change - median_gas_change, 1)}")
print(f"Pressão interna de homeostase: {patient_pressure}")
print(f"Diferença para a mediana: {round(patient_pressure - median_pressure, 1)}")
print(f"Quantidade de sinais críticos encontrados: {critic_signals}")
print(f"Avaliação final: {'Alerta Crítico' if critic_signals >= 2 else 'Estável'}")
print("=====")
print("Dr. McCoy: Certo, agora sei o que fazer.")
