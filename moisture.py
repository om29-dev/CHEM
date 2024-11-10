from machine import ADC # type: ignore

# Getting the analog data from soil moisture detector
adc = ADC(0)

# Function to Read Soil Moisture
def percent():
    value = adc.read()
    # Convert analog value to percentage
    percent = 100 - ((value / 1023.0) * 100)
    return percent