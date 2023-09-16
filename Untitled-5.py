def emergency_brake(sensor_data):
    if danger_detected(sensor_data):
        apply_brakes()
