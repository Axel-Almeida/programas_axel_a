# weather
def water_column_height(tower_height, tank_height):
    t=float(tower_height)
    w=float(tank_height)
    h=t+((3*w)/4)
    return h

def pressure_gain_from_water_height(water_column_height):
    p=998.2
    g=9.80665
    pasl=(p*g*water_column_height)/1000
    return pasl

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    p=998.2
    pasl=(-1*friction_factor*pipe_length* p*(fluid_velocity*fluid_velocity))/(2000*pipe_diameter)
    return pasl