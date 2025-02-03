import re
from src import NormalLyricLine, EnhancedLyricLine
from src import CombinedLyrics
from src import FullLyrics, FullLyricsWithTranslate
from src import TranslateExportType
import math

class NormalParser: 
    def __init__(self):
        pass

    @staticmethod
    def parse_with_translate(origin_lyrics: str, *trans_lyrics: str, interval=0):
        origin_lyrics_list = origin_lyrics.split("\n")
        trans_lyrics_list = [trans_lyric.split("\n") for trans_lyric in trans_lyrics]

        origin_obj_list = []
        trans_obj_list = []
        full_list = []
        
        for origin in origin_lyrics_list:
            match_result = re.findall(r"\[(\d{2}):(\d{2})\.(\d{1,3})\](.*)", origin)
            try: 
                if len(match_result[0]) == 4:
                    origin_obj_list.append(NormalLyricLine(origin))
            except IndexError: pass
        for trans in trans_lyrics_list:
            for origin in trans:
                match_result = re.findall(r"\[(\d{2}):(\d{2})\.(\d{1,3})\](.*)", origin)
                try: 
                    if len(match_result[0]) == 4:
                        trans_obj_list.append(NormalLyricLine(origin))
                except IndexError: pass

        for origin in origin_obj_list: 
            trans = list(filter(lambda x: abs(origin.play_time - x.play_time) <= interval, trans_obj_list))
            full_list.append(CombinedLyrics(origin, *trans))

        return FullLyricsWithTranslate(full_list)


class EnhancedParser:
    def __init__(self):
        pass

    @staticmethod
    def parse_with_translate(origin_lyrics: str, *trans_lyrics: str, interval=0):
        origin_lyrics_list = origin_lyrics.split("\n")
        trans_lyrics_list = trans_lyrics_list = [trans_lyric.split("\n") for trans_lyric in trans_lyrics]

        origin_obj_list = []
        trans_obj_list = []
        full_list = []
        pattern = r"\[(\d{2}):(\d{2})\.(\d{1,3})\]([^\[\]]*)"
        
        for origin in origin_lyrics_list:
            match_result = re.findall(pattern, origin)
    
            if match_result != []:
                origin_obj_list.append(EnhancedLyricLine(origin))
           
        for trans in trans_lyrics_list:
            for origin in trans:
                match_result = re.findall(r"\[(\d{2}):(\d{2})\.(\d{1,3})\](.*)", origin)
                try: 
                    if len(match_result[0]) == 4:
                        trans_obj_list.append(NormalLyricLine(origin))
                except IndexError: pass

        for origin in origin_obj_list: 
            trans = list(filter(lambda x: abs(origin.play_time - x.play_time) <= interval, trans_obj_list))
            full_list.append(CombinedLyrics(origin, *trans))

        return FullLyricsWithTranslate(full_list)
    # @staticmethod
    # def get_lyric_obj(lyric: str): 
    #     match_result = re.findall(r"\[(\d{2}):(\d{2})\.(\d{1,3})\](.*)", lyric)
    #     if len(match_result[0]) == 4:
    #         return 


if __name__ == "__main__": 
    with open(r"d:\ncm\鹿乃,Lon,hanser - 爱言叶Ⅳo.lrc", "r", encoding="utf-8") as f: 
        ori = f.read()
    with open(r"d:\ncm\鹿乃,Lon,hanser - 爱言叶Ⅳ - 1.lrc", "r", encoding="utf-8") as f: 
        trans = f.read()
    with open(r"d:\ncm\鹿乃,Lon,hanser - 爱言叶Ⅳ - 2.lrc", "r", encoding="utf-8") as f: 
        roma = f.read()
    a = EnhancedParser.parse_with_translate(ori, trans, roma, interval=10)
    a.sort()
    with open(r"d:\ncm\v6.3-green\鹿乃,Lon,hanser - 爱言叶Ⅳ - com.lrc", "w", encoding="utf-8") as f: 

        f.write(a.tostr(lrc_type=TranslateExportType.INTERLACED))