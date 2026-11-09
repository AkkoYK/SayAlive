#!/usr/bin/env python3
"""Count common AI-writing tells in Chinese and English text.

A rough self-check, not a verdict: a hit can be fine in context, and clean
output can still read badly. Stdlib only.

Usage:
    python3 tell_lint.py FILE [FILE ...]
    python3 tell_lint.py --json FILE [FILE ...]
    cat draft.md | python3 tell_lint.py -
"""
import argparse
import json
import re
import sys

# (category, tier, regex). Tier: strong = act on one hit, weak = act on density.
ZH = [
    ("假对比", "strong", r"不(?:仅仅|仅|只)?是[^。！？\n]{1,30}?[，,]\s*(?:而|更)是|与其说[^。！？\n]{1,30}?不如说|不是[^。！？\n]{1,20}?。\s*(?:而)?是"),
    ("时代背景开头", "strong", r"在当今|随着[^。！？\n]{1,20}?(?:不断|快速|飞速|迅速)?(?:发展|普及|演进)|在这个[^。！？\n]{1,12}?的时代|大背景下"),
    ("起跑式铺垫", "strong", r"让我们(?:一起)?(?:来)?(?:看看|深入|探讨|聊聊)|接下来我(?:将|会)为你|话不多说|一句话总结|下面我们(?:来)?深入"),
    ("伪洞见", "strong", r"本质上|归根结底|底层逻辑|说到底|核心在于|关键在于|最后比拼的是"),
    ("意义拔高", "strong", r"标志着|具有(?:重要|深远|里程碑)(?:的)?意义|奠定了?(?:坚实)?(?:的)?基础|彰显|注入新动能|开启新篇章|书写[^。]{0,6}篇章|迈出了?坚实"),
    ("套话收尾", "strong", r"综上所述|总而言之|总的来说|让我们拭目以待|未来可期|共创美好|携手共进|与君共勉"),
    ("聊天残留", "strong", r"好问题|希望(?:这|以上)?(?:对你|对您)有(?:所)?帮助|如果你还有(?:其他|任何)问题|以下是为(?:你|您)|需要我(?:帮你|为你)"),
    ("无源权威", "strong", r"研究表明|数据显示|有专家指出|专家认为|业内人士(?:认为|指出)|众所周知"),
    ("高频大词", "strong", r"赋能|助力|打造|深入探讨|至关重要|不可或缺|无缝|抓手|颗粒度|痛点|心智|链路|触达|降本增效|全方位|多维度"),
    ("小红书腔", "strong", r"姐妹们|绝绝子|谁懂啊|真的会谢|保姆级|干货满满|建议收藏|一文读懂|划重点|yyds"),
    ("咨询式安抚", "strong", r"我就在这里|稳稳(?:地)?接住|你不是(?:敏感|矫情|想太多)|我完全理解你的感受"),
    ("万能连接词", "weak", r"值得注意的是|值得一提的是|需要指出的是|不难发现|不可否认|事实上|与此同时|此外|然而|由此可见|换句话说"),
    ("程度副词", "weak", r"显著(?:提升|提高|改善|降低)|有效(?:解决|推动|提升)|全面(?:提升|推进|升级)|持续(?:优化|推进)|进一步(?:加强|提升|完善)|充分(?:发挥|体现)|切实|深度融合|极致"),
    ("翻译腔", "weak", r"进行(?:了)?(?:全面|深入|有效)?(?:的)?(?:优化|测试|分析|调整|讨论|研究|处理)|对于[^。，]{1,12}?(?:来说|而言)|作为一(?:个|名|位)"),
    ("抒情词", "weak", r"安放|微光|褶皱|丰盈|滚烫|奔赴|星辰大海"),
    ("破折号", "weak", r"——"),
    ("机械递进", "weak", r"首先[，,][^。]*?其次|一方面[^。]*?另一方面"),
]

EN = [
    ("fake contrast", "strong", r"\b(?:it'?s|this is|that'?s)\s+not\s+(?:just\s+|merely\s+|only\s+)?[^.?!\n]{1,40}?[,;—–-]+\s*(?:it'?s|but)\b|\bnot\s+(?:just|merely|only)\s+[^.?!\n]{1,40}?,?\s+but\b"),
    ("staged run-up", "strong", r"\blet'?s\s+(?:dive|delve|break\s+(?:this|it)\s+down|explore|unpack)\b|\bhere'?s\s+(?:the\s+thing|what\s+you\s+need)\b|\bwithout\s+further\s+ado\b|^\s*honestly\?|\breal\s+talk\b"),
    ("fake depth", "strong", r"\bat\s+its\s+core\b|\bthe\s+real\s+question\s+is\b|\bwhat\s+really\s+matters\b|\bat\s+the\s+end\s+of\s+the\s+day\b|\bfundamentally\b"),
    ("inflated significance", "strong", r"\btestament\s+to\b|\bpivotal\s+(?:moment|role)\b|\bplays?\s+a\s+(?:key|crucial|vital|pivotal)\s+role\b|\bmarks?\s+a\s+(?:new|pivotal|significant)\b|\bpaving\s+the\s+way\b|\bsetting\s+the\s+stage\b|\bindelible\b|\bthe\s+future\s+looks\s+bright\b|\bexciting\s+times\b|\bever-evolving\b"),
    ("summary ending", "strong", r"\bin\s+conclusion\b|\bin\s+summary\b|\ball\s+in\s+all\b|\bultimately,"),
    ("chatbot residue", "strong", r"\bgreat\s+question\b|\bi\s+hope\s+this\s+(?:helps|email\s+finds\s+you)\b|\blet\s+me\s+know\s+if\s+you'?d\s+like\b|\bfeel\s+free\s+to\b|\bcertainly!|\bof\s+course!"),
    ("borrowed authority", "strong", r"\b(?:studies|research)\s+(?:show|shows|suggest|suggests)\b|\bexperts\s+(?:say|agree|believe|argue)\b|\bobservers\s+(?:note|have)\b"),
    ("AI vocabulary", "strong", r"\bdelv(?:e|es|ing)\b|\btapestry\b|\bmeticulous(?:ly)?\b|\bvibrant\b|\bshowcas(?:e|es|ing)\b|\bunderscor(?:e|es|ing)\b|\bseamless(?:ly)?\b|\blandscape\b|\brealm\b|\bembark(?:s|ing)?\b|\bfoster(?:s|ing)?\b|\bgarner(?:s|ed)?\b|\bbolster(?:s|ed)?\b|\bintricate\b|\bleverag(?:e|es|ing)\b|\bempower(?:s|ing)?\b|\bgame-changer\b|\bcutting-edge\b|\bunlock(?:s|ing)?\b|\belevat(?:e|es|ing)\b|\brobust\b|\bcrucial\b|\bnavigat(?:e|es|ing)\s+the\b"),
    ("-ing rider", "strong", r",\s+(?:highlighting|underscoring|emphasizing|reflecting|symbolizing|showcasing|fostering|ensuring|contributing\s+to)\b"),
    ("copula avoidance", "strong", r"\b(?:serves|stands|functions|acts)\s+as\b|\bboasts\b"),
    ("sales language", "strong", r"\bnestled\b|\bin\s+the\s+heart\s+of\b|\bbreathtaking\b|\bmust-visit\b|\bstunning\b|\bworld-class\b|\bunparalleled\b|\bgroundbreaking\b"),
    ("signpost transition", "weak", r"\b(?:additionally|furthermore|moreover|notably|importantly)\b|\bit'?s\s+worth\s+noting\b"),
    ("rhetorical Q&A", "weak", r"\bthe\s+result\?|\bwhy\s+does\s+this\s+matter\?|\bwhat\s+makes\s+[^.?!]{1,30}\s+(?:unique|special)\s+is\b"),
    ("stacked hedge", "weak", r"\bcould\s+potentially\b|\bmight\s+arguably\b|\bmay\s+potentially\b"),
    ("em dash", "weak", r"—|\s--\s"),
]

FORMAT = [
    ("bold label", "strong", r"^\s*(?:[-*]|\d+\.)\s+\*\*[^*\n]{1,30}\*\*\s*[:：]"),
    ("emoji", "strong", r"[\U0001F300-\U0001FAFF☀-➿]"),
]

CJK = re.compile(r"[一-鿿]")
WORD = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")


def strip_code(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", " ", text)


def lint(text):
    text = strip_code(text)
    cjk = len(CJK.findall(text))
    words = len(WORD.findall(text))
    lang = "zh" if cjk >= words else "en"
    rules = (ZH if lang == "zh" else EN) + FORMAT
    flags = re.I | re.M
    hits = []
    for cat, tier, pat in rules:
        found = [m.group(0) for m in re.finditer(pat, text, flags)]
        if found:
            hits.append({"category": cat, "tier": tier, "count": len(found), "examples": found[:3]})
    size = cjk if lang == "zh" else words
    unit = 1000 if lang == "zh" else 500  # per 1000 字 / per 500 words
    strong = sum(h["count"] for h in hits if h["tier"] == "strong")
    weak = sum(h["count"] for h in hits if h["tier"] == "weak")
    norm = unit / size if size else 0
    return {
        "lang": lang,
        "length": size,
        "strong": strong,
        "weak": weak,
        "strong_per_unit": round(strong * norm, 2),
        "weak_per_unit": round(weak * norm, 2),
        "unit": "1000字" if lang == "zh" else "500 words",
        "hits": hits,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+", help="files to check, or - for stdin")
    ap.add_argument("--json", action="store_true", help="print JSON")
    args = ap.parse_args()
    results = {}
    for f in args.files:
        text = sys.stdin.read() if f == "-" else open(f, encoding="utf-8").read()
        results[f] = lint(text)
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return
    for f, r in results.items():
        print(f"{f}  [{r['lang']}, {r['length']}]  strong={r['strong']} weak={r['weak']}  "
              f"(per {r['unit']}: {r['strong_per_unit']} / {r['weak_per_unit']})")
        for h in r["hits"]:
            print(f"  {h['tier']:6} {h['category']}: {h['count']}  e.g. {' | '.join(h['examples'])}")


if __name__ == "__main__":
    main()
