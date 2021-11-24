import RPi.GPIO as g

if __name__ != '__main__':
    import sevenseq.config.config as config

g.setmode(g.BCM)
g.setwarnings(False)

led1a = config.led1a
led1b = config.led1b
led1c = config.led1c
led1d = config.led1d
led1e = config.led1e
led1f = config.led1f
led1g = config.led1g
led1dot = config.led1dot

led2a = config.led2a
led2b = config.led2b
led2c = config.led2c
led2d = config.led2d
led2e = config.led2e
led2f = config.led2f
led2g = config.led2g
led2dot = config.led2dot

g.setup(led1a, g.OUT)
g.setup(led1b, g.OUT)
g.setup(led1c, g.OUT)
g.setup(led1d, g.OUT)
g.setup(led1e, g.OUT)
g.setup(led1f, g.OUT)
g.setup(led1g, g.OUT)
g.setup(led1dot, g.OUT)

g.setup(led2a, g.OUT)
g.setup(led2b, g.OUT)
g.setup(led2c, g.OUT)
g.setup(led2d, g.OUT)
g.setup(led2e, g.OUT)
g.setup(led2f, g.OUT)
g.setup(led2g, g.OUT)
g.setup(led2dot, g.OUT)

def setnum(num):
    digit1 = 0
    digit2 = 0
    
    if num > 99:
        return
    if num >= 10:
        a = int(str(num)[0])
        b = int(str(num)[1])
    else:
        a = 0
        b = num
    numa0 = [led1a, led1b, led1c, led1d, led1e, led1f]
    numa1 = [led1b, led1c]
    numa2 = [led1a, led1b, led1g, led1e, led1d]
    numa3 = [led1a, led1b, led1g, led1c, led1d]
    numa4 = [led1f, led1g, led1b, led1c]
    numa5 = [led1a, led1f, led1g, led1c, led1d]
    numa6 = [led1a, led1f, led1e, led1d, led1c, led1g]
    numa7 = [led1a, led1b, led1c]
    numa8 = [led1a, led1b, led1c, led1d, led1e, led1f, led1g]
    numa9 = [led1a, led1f, led1g, led1b, led1c]
    
    numb0 = [led2a, led2b, led2c, led2d, led2e, led2f]
    numb1 = [led2b, led2c]
    numb2 = [led2a, led2b, led2g, led2e, led2d]
    numb3 = [led2a, led2b, led2g, led2c, led2d]
    numb4 = [led2f, led2g, led2b, led2c]
    numb5 = [led2a, led2f, led2g, led2c, led2d]
    numb6 = [led2a, led2f, led2e, led2d, led2c, led2g]
    numb7 = [led2a, led2b, led2c]
    numb8 = [led2a, led2b, led2c, led2d, led2e, led2f, led2g]
    numb9 = [led2a, led2f, led2g, led2b, led2c]
    
    g.output(led1a, g.LOW)
    g.output(led1b, g.LOW)
    g.output(led1c, g.LOW)
    g.output(led1d, g.LOW)
    g.output(led1e, g.LOW)
    g.output(led1f, g.LOW)
    g.output(led1g, g.LOW)
    g.output(led1dot, g.LOW)
    
    g.output(led2a, g.LOW)
    g.output(led2b, g.LOW)
    g.output(led2c, g.LOW)
    g.output(led2d, g.LOW)
    g.output(led2e, g.LOW)
    g.output(led2f, g.LOW)
    g.output(led2g, g.LOW)
    g.output(led2dot, g.LOW)
    
    if a == 0:
        g.output(numa0, g.HIGH)
    if a == 1:
        g.output(numa1, g.HIGH)
    if a == 2:
        g.output(numa2, g.HIGH)
    if a == 3:
        g.output(numa3, g.HIGH)
    if a == 4:
        g.output(numa4, g.HIGH)
    if a == 5:
        g.output(numa5, g.HIGH)
    if a == 6:
        g.output(numa6, g.HIGH)
    if a == 7:
        g.output(numa7, g.HIGH)
    if a == 8:
        g.output(numa8, g.HIGH)
    if a == 9:
        g.output(numa9, g.HIGH)
    if b == 0:
        g.output(numb0, g.HIGH)
    if b == 1:
        g.output(numb1, g.HIGH)
    if b == 2:
        g.output(numb2, g.HIGH)
    if b == 3:
        g.output(numb3, g.HIGH)
    if b == 4:
        g.output(numb4, g.HIGH)
    if b == 5:
        g.output(numb5, g.HIGH)
    if b == 6:
        g.output(numb6, g.HIGH)
    if b == 7:
        g.output(numb7, g.HIGH)
    if b == 8:
        g.output(numb8, g.HIGH)
    if b == 9:
        g.output(numb9, g.HIGH)
