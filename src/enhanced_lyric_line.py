import re
from .lrc_time import LRCTime

class SingleCharacter: 
    def __init__(self, char: str, miutes: str, seconds: str, milliseconds: str):
        self.char = char
        self.is_end_character = False
        self.char_time = LRCTime(minutes=miutes, seconds=seconds, milliseconds=milliseconds)

    def end_character(self, miutes: str, seconds: str, milliseconds: str): 
        end_time = LRCTime(miutes, seconds, milliseconds)
        if end_time.play_time < self.char_time.play_time: 
            raise ValueError("结束时间不能小于开始时间")
        self.is_end_character = True
        self.end_time = end_time

    def tostr(self): 
        if self.is_end_character:
            return f"{self.char_time.tostr()}{self.char}{self.end_time.tostr()}"
        else: 
            return f"{self.char_time.tostr()}{self.char}"

    def forward(self, time: int) -> None:
        """_summary_

        Args:
            time (int): 单位为毫秒, 将这句歌词向前调整的时间,向后则传入负数
        """
        if not self.is_end_character:
            if self.char_time.play_time + time < 0 and self.char_time.play_time != 0:
                self.char_time.play_time = 0
            elif self.char_time.play_time == 0: 
                pass
            else: 
                self.char_time.play_time += time
        else: 
            if self.char_time.play_time + time < 0 or self.end_time.play_time + time < 0:
                raise ValueError("调整后的时间不能小于0")
            else: 
                self.char_time.play_time += time
                self.end_time.play_time += time

    @property
    def play_time(self):
        return self.char_time.play_time

class EnhancedLyricLine:
    def __init__(self, lyric_string: str):
        self.character_list = []

        self.pattern = r"\[(\d{2}):(\d{2})\.(\d{1,3})\]([^\[\]]*)"
        find_result = re.findall(self.pattern, lyric_string)

        for i in find_result[0:len(find_result)-1]: 
            self.character_list.append(SingleCharacter(i[3], i[0], i[1], i[2]))

        self.character_list[-1].end_character(find_result[-1][0], find_result[-1][1], find_result[-1][2])

    def tostr(self):
        return "".join([i.tostr() for i in self.character_list])

    def forward(self, time: int) -> None:
        for i in self.character_list: 
            i.forward(time)

    @property
    def play_time(self): 
        return self.character_list[0].play_time

if __name__ == "__main__": 
    el = EnhancedLyricLine("[00:55.775]我[00:55.960]随[00:56.137]时[00:56.354]都[00:56.566]愿[00:56.896]意[00:57.458]为[00:57.650]了[00:57.793]你[00:58.000]唱[00:59.523]")
    print(el.tostr())
    el.forward(256)
    print(el.tostr())