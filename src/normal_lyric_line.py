import re
from .lrc_time import LRCTime

class NormalLyricLine: 
    def __init__(self, lyric_string: str):
        match_result = re.match(r"\[(\d{2}):(\d{2})\.(\d{1,3})\](.*)", lyric_string)
        self.lyric_time = LRCTime(match_result.group(1), match_result.group(2), match_result.group(3))
        self.lyric = match_result.group(4)

    @property
    def play_time(self): 
        return self.lyric_time.play_time
    @play_time.setter
    def play_time(self, time: int):
        self.lyric_time.play_time = time
    
    def tostr(self): 
        return f"{self.lyric_time.tostr()}{self.lyric}"
    
    def forward(self, time: int) -> None:
        """_summary_

        Args:
            time (int): 单位为毫秒, 将这句歌词向前调整的时间,向后则传入负数
        """
        if self.lyric_time.play_time + time < 0:
            self.lyric_time.play_time = 0
        else:   
            self.lyric_time.play_time += time
    
if __name__ == "__main__": 
    lyric_line = NormalLyricLine("[01:12.450]我的世界已坠入爱河")
    print(lyric_line.tostr())
    lyric_line.forward(500)
    print(lyric_line.tostr())