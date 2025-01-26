class LRCTime: 
    def __init__(self, minutes: str, seconds: str, milliseconds: str):
        self.milliseconds = int(milliseconds.ljust(3, "0"))
        self.minutes = int(minutes)
        self.seconds = int(seconds)

    def tostr(self):
        return f"[{str(self.minutes).rjust(2, '0')}:{str(self.seconds).rjust(2, '0')}.{str(self.milliseconds).rjust(3, '0')}]"
    
    @property
    # 返回当前时间，单位为毫秒
    def play_time(self): 
        # 将分钟转换为毫秒
        return self.minutes * 60 * 1000 + self.seconds * 1000 + self.milliseconds
    
    @play_time.setter
    def play_time(self, time: int):
        self.minutes = time // (60 * 1000)
        self.seconds = (time - self.minutes * 60 * 1000) // 1000
        self.milliseconds = time % 1000