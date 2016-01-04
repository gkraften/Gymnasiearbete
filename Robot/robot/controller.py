class PID:
    def __init__(self, kp, ki, kd, target):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.last_error = 0
        self.integral = 0
        self.max_correction = None
        self.min_correction = None
        self.target = 0

    def set_target(self, target):
        self.target = target

    def set_correction_bounds(self, min_corr, max_corr):
        self.max_correction = max_corr
        self.min_correction = min_corr

    def update(self, value, dt):
        error = self.target - value

        self.integral += error * dt
        derivative = (self.last_error - error)/dt
        self.last_error = error

        correction = self.kp * value + self.ki * self.integral + self.kd * derivative
        if not self.max_correction is None and correction > self.max_correction:
            correction = self.max_correction
        if not self.min_correction is None and correction < self.min_correction:
            correction = self.min_correction

        return correction