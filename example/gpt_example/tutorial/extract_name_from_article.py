from framewrok.module.http.http_wrapper import HTTPWrapper
from framewrok.utility.log_utility import ILog

if __name__ == '__main__':

    # 从文章中提取人名
    response = HTTPWrapper() \
        .url("https://api.openai.com/v1/chat/completions") \
        .header({
            "Content-Type": "application/json",
            "Authorization": "Bearer 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"
        }) \
        .body({
            "model": "gpt-3.5-turbo-1106",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": """
                    Man Utd must win trophies, says Ten Hag ahead of League Cup final
                    
                    请将上面这句话的人名提取出来，并用json的方式展示出来
                    """
                }
            ]
        }) \
        .post()

    ILog.debug(__file__, response)
