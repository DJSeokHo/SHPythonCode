# _*_ coding: utf-8 _*_
# @Time : 2023/03/23 5:59 PM
# @Author : Coding with cat
# @File : gpt_test
# @Project : SHPythonCode
from requests import Response

from example.gpt_example.tutorial.gpt_constants import API_KET
from framewrok.module.http.http_wrapper import HTTPWrapper
from framewrok.utility.log_utility import ILog

if __name__ == '__main__':

    # content = "Hello!"

    example = """
    判断一下用户的评论情感上是正面的还是负面的
    
    评论：买的银色版真的很好看，一天就到了，晚上就开始拿起来完系统很丝滑流畅，做工扎实，手感细腻，很精致哦苹果一如既往的好品质
    情感：正面
    
    评论：随意降价，不予价保，服务态度差
    情感：负面
    
    以上内容是样例，只需要回答正面或者负面两个字
    """

    content = example + """
    评论：
    外形外观：苹果审美一直很好，金色非常漂亮
    拍照效果：14pro升级的4800万像素真的是没的说，太好了
    运行速度：苹果的反应速度好，用上三五年也不会卡顿的，之前的7P用到现在也不卡
    其他特色：14pro的磨砂金真的太好看了，不太高调，也不至于没有特点，非常耐看，很好的
    情感：
    """

    response = HTTPWrapper() \
        .url("https://api.openai.com/v1/chat/completions") \
        .header({
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KET}"
        }) \
        .body({
            "model": "gpt-3.5-turbo-1106",
            "temperature": 1.0,  # 这个参数的输入范围是 0-2 之间的浮点数，代表输出结果的随机性或者说多样性。在这里，我们选择了
            # 1.0，也就是还是让每次生成的内容都有些不一样。你也可以把这个参数设置为 0，这样，每次输出的结果的随机性就会比较小。我将 temperature 设置为 0，你可以看到两句内容的遣词造句就基本一致了。
            "n": 1,  # 代表你希望 AI 给你生成几条内容供你选择。在这样自动生成客服内容的场景里，我们当然设置成 1。但是如果在一些辅助写作的场景里，你可以设置成 3
            # 或者更多，供用户在多个结果里面自己选择自己想要的。
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": content
                }
            ]
        }) \
        .post()

    ILog.debug(__file__, response)
