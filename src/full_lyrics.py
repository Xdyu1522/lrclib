from .normal_lyric_line import NormalLyricLine
from .combined_lyrics import CombinedLyrics
from .translate_export_type import TranslateExportType
from itertools import zip_longest


class FullLyrics: 
    def __init__(self, lyrics: list[NormalLyricLine]): 
        self.lyrics = lyrics
    
    def tostr(self) -> str:
        return '\n'.join([lyric.tostr() for lyric in self.lyrics])
    
    def forward(self, time: int) -> None:
        for lyric in self.lyrics:
            lyric.forward(time)

    def sort(self): 
        self.lyrics = sorted(self.lyrics, key=lambda lyric: lyric.play_time)

class FullLyricsWithTranslate: 
    def __init__(self, lyrics: list[CombinedLyrics]):
        self.lyrics = lyrics

    def forward(self, time: int) -> None: 
        for lyric in self.lyrics:
            lyric.forward(time)

    def sort(self):
        self.lyrics = sorted(self.lyrics, key=lambda lyric: lyric.play_time)

    def tostr(self, lrc_type: TranslateExportType) -> str:

        if lrc_type == TranslateExportType.INTERLACED:
            return '\n'.join([lyric.tostr() for lyric in self.lyrics])

        elif lrc_type == TranslateExportType.INDEPENDENT:
            origin_lyric = []
            translate_lyrics = []
            for lyric in self.lyrics: 
                origin_lyric.append(lyric.origin_lyric_str())
                translate_lyrics.append(lyric.translate_lyrics_str_list())
            
            translate_lyrics = [list(row) for row in zip_longest(*translate_lyrics, fillvalue="")]

            origin_string = "\n".join(origin_lyric)
            translate_string = "\n".join(["\n".join(row) for row in translate_lyrics])
            return f"{origin_string}{translate_string}"




