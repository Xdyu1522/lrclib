from .normal_lyric_line import NormalLyricLine
from .enhanced_lyric_line import EnhancedLyricLine

class CombinedLyrics: 
    def __init__(self, origin_lyric: NormalLyricLine | EnhancedLyricLine, *translate_lyrics: NormalLyricLine):
        
        for translate_lyric in translate_lyrics:
            if origin_lyric.play_time != translate_lyric.play_time:
                translate_lyric.play_time = origin_lyric.play_time

        self.origin_lyric = origin_lyric
        self.translate_lyrics = translate_lyrics
        
    def tostr(self) -> str: 
        """返回字符串, 类型默认为交错"""
        translate_str = "\n".join([i.tostr() if i.lyric != r"//" else "" for i in self.translate_lyrics])
        origin_str = self.origin_lyric.tostr()
        if origin_str != translate_str and translate_str != "" and translate_str != r"//": 
            return f"{origin_str}\n{translate_str}"
        else: 
            return origin_str
    
    def origin_lyric_str(self) -> str: 
        return self.origin_lyric.tostr()
    
    def translate_lyrics_str_list(self) -> list[str]:
        return [trans.tostr() for trans in self.translate_lyrics]
    
    def forward(self, time: int) -> None: 
        self.origin_lyric.forward(time)
        for translate_lyric in self.translate_lyrics:
            translate_lyric.forward(time)
    
    @property
    def play_time(self) -> int:
        return self.origin_lyric.play_time