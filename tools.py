from src import NormalLyricLine

def qq_lyrics_seperate(ori_path, ori_save_path, trans_save_path): 
    with open(ori_path, "r", encoding="utf-8") as f: 
        ori_lyrics = f.read().split("\n")
    
    for i in range(1, len(ori_lyrics)): 
        current_time = NormalLyricLine(ori_lyrics[i]).play_time
        p_time = NormalLyricLine(ori_lyrics[i-1]).play_time
        if p_time > current_time: 
            ori_lrc = ori_lyrics[:i]
            trans_lrc = ori_lyrics[i:]
            break
    with open(ori_save_path, "w", encoding="utf-8") as f: 
        f.write("\n".join(ori_lrc))
    with open(trans_save_path, "w", encoding="utf-8") as f:
        f.write("\n".join(trans_lrc))

qq_lyrics_seperate(r"d:\ncm\v6.3-green\鹿乃,Lon,hanser - 爱言叶Ⅳ.lrc", r"d:\ncm\v6.3-green\鹿乃,Lon,hanser - 爱言叶Ⅳo.lrc", r"d:\ncm\v6.3-green\鹿乃,Lon,hanser - 爱言叶Ⅳt.lrc")