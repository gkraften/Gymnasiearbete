class PID:
    def __init__(self, kp, ki, kd, min_val, max_val):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.min_val = min_val
        self.max_val = max_val
        self.target = 0

        self.integral = 0
        self.last_error = 0

        self.difference = lambda a, b: a-b

    def set_target(self, target):
        self.target = target

    def update(self, val, dt=1):
        error = self.difference(self.target, val)
        print(error)

        self.integral += error * dt

        derivative = (self.last_error - error)/dt
        self.last_error = error

        result = self.kp*error + self.ki*self.integral + self.kd*derivative
        if result > self.max_val:
            result = self.max_val
        if result < self.min_val:
            result = self.min_val

        return result