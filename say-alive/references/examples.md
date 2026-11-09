# 前后对照 / Before and after

例子演示判断，不是要照抄的句型。"改后"里的具体信息都来自"改前"或任务给的材料，没有新增事实。

## 1. 写作：产品公告（中文）

任务：给记账 App"小账本"写更新公告。材料：新增家庭共享账本，最多 6 人；支持从支付宝、微信导出的账单一键导入；修复了 iOS 17 上偶尔闪退的问题；10 月 30 日上线。

AI 腔版本：
> 🎉 重磅更新！小账本 3.0 震撼来袭！
>
> 在快节奏的现代生活中，记账不仅仅是一种习惯，更是一种生活态度。本次更新，我们深度聚焦用户痛点，全面升级产品体验，为您带来前所未有的记账新体验！
>
> ✨ **家庭共享**：全新家庭共享功能，让全家人一起记账，打造温馨的家庭财务管理闭环！
> 🚀 **一键导入**：……
>
> 未来，我们将持续优化，与您携手共创美好生活！

Say Alive：
> 10 月 30 日起，小账本可以建家庭共享账本了。最多 6 个人一起记，谁花了什么、花了多少，所有人都能看到。
>
> 从支付宝和微信导出的账单，现在可以直接导入，不用再一条条手动录。
>
> 另外修了一个 bug：部分 iOS 17 用户打开 App 时偶尔会闪退，这次更新后不会了。

## 2. 写作：工作邮件（英文）

Task: ask Marta (design lead) to move Thursday's review to Friday because the prototype build failed; need her answer by Wednesday noon.

AI-flavored:
> Subject: Request for Rescheduling of Design Review Meeting
>
> Hi Marta,
>
> I hope this email finds you well! I wanted to reach out regarding our upcoming design review meeting scheduled for Thursday. Unfortunately, we've encountered some unexpected challenges with the prototype build, which has impacted our timeline. In light of this, I was wondering if it might be possible to explore the option of moving the meeting to Friday.
>
> Please let me know your thoughts at your earliest convenience. Thank you so much for your understanding and flexibility!

Say Alive:
> Subject: Move Thursday's design review to Friday?
>
> Hi Marta,
>
> Could we push Thursday's design review to Friday? The prototype build failed last night and won't be ready to show by Thursday.
>
> Any time Friday works for us. If you can let me know by Wednesday noon, I'll send the new invite.
>
> Thanks,
> Sam

## 3. 改写：已经很好的文本（中文）

原文：
> 我家楼下那家修车铺开了二十年。老板姓周，左手少一根手指，说是年轻时被风扇皮带绞的。他修车不看电脑，拧开机盖听一会儿，就能说出是哪儿的毛病。上个月他把铺子盘出去了，新老板装了两台诊断仪，门口挂上了"智能检测"的灯箱。

用户说"帮我改改，让它更好一点"。这段已经具体、有画面、有作者的节制，所以只轻改两处：

> 我家楼下那家修车铺开了二十年。老板姓周，左手少一根手指，说是年轻时被风扇皮带绞的。他修车不看电脑，拧开机盖听一会儿，就能说出毛病在哪儿。上个月他把铺子盘出去了，新老板装了两台诊断仪，门口挂上了“智能检测”的灯箱。

改了"是哪儿的毛病"的语序，读起来更顺；英文直引号换成中文引号。其余一字不动，尤其不要给结尾补一句感慨：这段的力量就在于作者没有点破。

一字不改原样交回，用户会以为你没看；改动太多，又把好文本改坏了。用户只问"要不要改"时，才可以原样返回并说一句理由。

## 4. 改写：AI 腔（中文，bounded）

原文：
> 值得注意的是，本轮我们完成了对重试策略的全面优化调整，失败请求数从 24 次显著降低到了 7 次。这不仅仅是一次技术优化，更是我们对系统稳定性不懈追求的体现。综上所述，重试策略已经调整完毕。

改后：
> 这一轮调整了重试策略，失败请求数从 24 次降到 7 次。

保留了动作、数字和结果。不能改成"请求更稳定了"（丢数字），也不能补"降幅 71%"之外的请求总量（原文没有）。

## 5. 改写：AI 腔（英文）

Before:
> In today's fast-paced digital landscape, effective communication is more crucial than ever. Our new feature, Smart Summaries, serves as a powerful tool that seamlessly integrates into your workflow, empowering teams to stay aligned. It's not just a feature — it's a game-changer. Ultimately, Smart Summaries represents our unwavering commitment to helping teams thrive.

After:
> Smart Summaries condenses long threads into a few lines, so people who missed a discussion can catch up without reading all of it.

注意：原文没说具体怎么"seamlessly integrates"，改写也就不编"一键接入 Slack"之类的功能。如果"condenses long threads"在原文里也没有，就只能写得更朴素：Smart Summaries is a new feature for keeping teams up to date.

## 6. 写作：短故事开头（中文）

AI 腔：
> 夜幕降临，城市的霓虹灯次第亮起。林晓站在窗前，望着窗外的车水马龙，心中五味杂陈。她深吸一口气，仿佛整个世界都安静了下来。

Say Alive：
> 林家的冰箱上贴着一张外卖单，是她妈三年前贴的，那家店早就关了。她每次拿牛奶都会看到它，每次都想撕，一直没撕。

（故事可以造细节，而且细节要只属于这个故事。名字如果用户没指定，也别用最常见的那几个。）

## 7. 写作：回复（英文，wrong reader）

Context: teammate asked "Can we ship the export fix today?"

AI-flavored:
> Great question! Let me walk you through where things stand. As you know, the export bug was caused by a timezone mismatch in the date parser. I investigated the issue thoroughly and identified the root cause. After implementing a fix, I ran the full test suite. All 214 tests pass. So, to answer your question: yes, we can ship today!

Say Alive:
> Yes. The fix is in and all 214 tests pass. I'll merge after lunch unless you want another look.
